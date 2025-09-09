use criterion::{black_box, criterion_group, criterion_main, BenchmarkId, Criterion};
use genesis_code_protocol_rs::performance::*;
use genesis_code_protocol_rs::*;
use std::collections::HashMap;

fn benchmark_gcp_run_creation(c: &mut Criterion) {
    c.bench_function("gcp_run_creation", |b| {
        b.iter(|| {
            GcpRun::new(
                black_box(RunMode::Auto),
                black_box(StartupMode::SparkProvided),
                black_box(RiskTier::R1),
            )
        })
    });
}

fn benchmark_artifact_processing(c: &mut Criterion) {
    let mut group = c.benchmark_group("artifact_processing");

    for size in [100, 1000, 10000].iter() {
        let data: Vec<u8> = (0..*size).map(|i| (i % 256) as u8).collect();

        group.bench_with_input(
            BenchmarkId::new("single_artifact", size),
            &data,
            |b, data| b.iter(|| process_large_artifact(black_box(data))),
        );
    }

    group.finish();
}

fn benchmark_batch_processing(c: &mut Criterion) {
    let mut group = c.benchmark_group("batch_processing");

    for batch_size in [1, 5, 10, 20].iter() {
        let artifacts: Vec<Vec<u8>> = (0..*batch_size)
            .map(|i| (0..1000).map(|j| ((i * 1000 + j) % 256) as u8).collect())
            .collect();

        let artifact_refs: Vec<&[u8]> = artifacts.iter().map(|v| v.as_slice()).collect();

        group.bench_with_input(
            BenchmarkId::new("batch_size", batch_size),
            &artifact_refs,
            |b, artifacts| b.iter(|| batch_process_artifacts(black_box(artifacts))),
        );
    }

    group.finish();
}

fn benchmark_json_serialization(c: &mut Criterion) {
    let mut run = GcpRun::new(RunMode::Full, StartupMode::Autonomous, RiskTier::R2);

    // Add some data to make serialization more realistic
    for i in 0..10 {
        run.add_artifact(format!("artifact_{}", i), format!("content_{}", i))
            .unwrap();
    }

    let mut group = c.benchmark_group("json_operations");

    group.bench_function("serialize", |b| b.iter(|| run.to_json().unwrap()));

    let json = run.to_json().unwrap();
    group.bench_function("deserialize", |b| {
        b.iter(|| GcpRun::from_json(black_box(&json)).unwrap())
    });

    group.finish();
}

fn benchmark_phase_transitions(c: &mut Criterion) {
    use genesis_code_protocol_rs::phases::PhaseManager;

    c.bench_function("phase_transition", |b| {
        b.iter(|| {
            let mut manager = PhaseManager::new(Phase::C0AmbiguityToBrief);
            manager
                .transition_to_phase(
                    black_box(Phase::C1RequirementsAnalysis),
                    black_box("Test transition with complete documentation and artifacts"),
                )
                .unwrap()
        })
    });
}

fn benchmark_telemetry_operations(c: &mut Criterion) {
    use genesis_code_protocol_rs::telemetry::{EventSeverity, TelemetryCollector};

    let collector = TelemetryCollector::new();
    let mut group = c.benchmark_group("telemetry");

    group.bench_function("record_metric", |b| {
        b.iter(|| {
            collector
                .record_metric(
                    black_box("test_metric".to_string()),
                    black_box(42.0),
                    black_box("units".to_string()),
                    black_box(HashMap::new()),
                )
                .unwrap()
        })
    });

    group.bench_function("record_event", |b| {
        b.iter(|| {
            collector
                .record_event(
                    black_box("test_event".to_string()),
                    black_box(Some(Phase::C3Implementation)),
                    black_box(HashMap::new()),
                    black_box(EventSeverity::Info),
                )
                .unwrap()
        })
    });

    // Add just a few data points for report generation
    for i in 0..10 {
        collector
            .record_metric(
                format!("metric_{}", i),
                i as f64,
                "units".to_string(),
                HashMap::new(),
            )
            .unwrap();
    }

    group.bench_function("generate_report", |b| {
        b.iter(|| collector.generate_report().unwrap())
    });

    group.finish();
}

fn benchmark_runner_execution(c: &mut Criterion) {
    use chrono::Utc;
    use genesis_code_protocol_rs::runners::{
        create_default_registry, RunnerContext, RunnerExecutor,
    };
    use uuid::Uuid;

    let registry = create_default_registry();
    let executor = RunnerExecutor::new(registry);

    let context = RunnerContext {
        run_id: Uuid::new_v4().to_string(),
        phase: Phase::C3Implementation,
        inputs: HashMap::from([(
            "specification".to_string(),
            "Generate a complex application".to_string(),
        )]),
        started_at: Utc::now(),
    };

    // Create async runtime for benchmarking
    let rt = tokio::runtime::Runtime::new().unwrap();

    c.bench_function("runner_execution", |b| {
        b.iter(|| {
            rt.block_on(async {
                executor
                    .execute_runner(black_box("code_generator"), black_box(context.clone()))
                    .await
                    .unwrap()
            })
        })
    });
}

fn benchmark_artifact_validation(c: &mut Criterion) {
    use genesis_code_protocol_rs::artifacts::{Artifact, ArtifactManager, ArtifactType};

    let mut group = c.benchmark_group("artifact_validation");

    // Single artifact validation
    let artifact = Artifact::new(
        "test_artifact".to_string(),
        "test content for validation".to_string(),
        ArtifactType::Documentation,
    );

    group.bench_function("single_validation", |b| {
        b.iter(|| artifact.validate().unwrap())
    });

    // Multiple artifacts validation
    let mut manager = ArtifactManager::new();
    for i in 0..50 {
        let artifact = Artifact::new(
            format!("artifact_{}", i),
            format!("content for artifact {}", i),
            ArtifactType::Documentation,
        );
        manager.add_artifact(artifact).unwrap();
    }

    group.bench_function("batch_validation", |b| {
        b.iter(|| manager.validate_all().unwrap())
    });

    group.finish();
}

fn benchmark_gate_processing(c: &mut Criterion) {
    use genesis_code_protocol_rs::gates::{GateProcessor, GateType};

    let processor = GateProcessor::new();
    let contexts = [
        "Simple context with basic requirements",
        "Complex context with comprehensive test coverage and extensive documentation including security analysis",
        "Context with vulnerability detection and security issues requiring immediate attention",
        "Compliance context with full audit trail and regulatory documentation",
    ];

    let mut group = c.benchmark_group("gate_processing");

    for (i, context) in contexts.iter().enumerate() {
        group.bench_with_input(BenchmarkId::new("gate_type", i), context, |b, context| {
            b.iter(|| {
                processor
                    .process_gate(black_box(GateType::QualityCheck), black_box(context))
                    .unwrap()
            })
        });
    }

    group.finish();
}

criterion_group!(
    benches,
    benchmark_gcp_run_creation,
    benchmark_artifact_processing,
    benchmark_batch_processing,
    benchmark_json_serialization,
    benchmark_phase_transitions,
    benchmark_telemetry_operations,
    benchmark_runner_execution,
    benchmark_artifact_validation,
    benchmark_gate_processing
);

criterion_main!(benches);
