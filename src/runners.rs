//! Runner system for Genesis Code Protocol
//!
//! Implements deterministic modules for protocol execution

use anyhow::Result;
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

use crate::Phase;

/// Represents a protocol runner
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Runner {
    pub name: String,
    pub version: String,
    pub description: String,
    pub supported_phases: Vec<Phase>,
    pub inputs: Vec<RunnerInput>,
    pub outputs: Vec<RunnerOutput>,
    pub metadata: HashMap<String, String>,
}

/// Input specification for a runner
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RunnerInput {
    pub name: String,
    pub input_type: InputType,
    pub required: bool,
    pub description: String,
}

/// Output specification for a runner
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RunnerOutput {
    pub name: String,
    pub output_type: OutputType,
    pub description: String,
}

/// Types of runner inputs
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum InputType {
    Text,
    Json,
    File,
    Binary,
    Configuration,
}

/// Types of runner outputs
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum OutputType {
    Artifact,
    Report,
    Metrics,
    Log,
    Configuration,
}

/// Execution context for runner
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RunnerContext {
    pub run_id: String,
    pub phase: Phase,
    pub inputs: HashMap<String, String>,
    pub started_at: DateTime<Utc>,
}

/// Result of runner execution
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct RunnerResult {
    pub success: bool,
    pub outputs: HashMap<String, String>,
    pub metrics: HashMap<String, f64>,
    pub execution_time_ms: u64,
    pub error_message: Option<String>,
}

/// Runner registry for managing available runners
#[derive(Debug, Default)]
pub struct RunnerRegistry {
    runners: HashMap<String, Runner>,
}

impl RunnerRegistry {
    /// Creates a new runner registry
    pub fn new() -> Self {
        Self {
            runners: HashMap::new(),
        }
    }

    /// Registers a new runner
    pub fn register_runner(&mut self, runner: Runner) -> Result<()> {
        if self.runners.contains_key(&runner.name) {
            anyhow::bail!("Runner '{}' is already registered", runner.name);
        }
        self.runners.insert(runner.name.clone(), runner);
        Ok(())
    }

    /// Gets a runner by name
    pub fn get_runner(&self, name: &str) -> Option<&Runner> {
        self.runners.get(name)
    }

    /// Lists all registered runners
    pub fn list_runners(&self) -> Vec<&Runner> {
        self.runners.values().collect()
    }

    /// Finds runners that support a specific phase
    pub fn find_runners_for_phase(&self, phase: &Phase) -> Vec<&Runner> {
        self.runners
            .values()
            .filter(|runner| runner.supported_phases.contains(phase))
            .collect()
    }
}

/// Executor for running protocol runners
pub struct RunnerExecutor {
    registry: RunnerRegistry,
}

impl RunnerExecutor {
    /// Creates a new runner executor
    pub fn new(registry: RunnerRegistry) -> Self {
        Self { registry }
    }

    /// Executes a runner with the given context
    pub async fn execute_runner(
        &self,
        runner_name: &str,
        context: RunnerContext,
    ) -> Result<RunnerResult> {
        let runner = self
            .registry
            .get_runner(runner_name)
            .ok_or_else(|| anyhow::anyhow!("Runner '{}' not found", runner_name))?;

        // Validate inputs
        self.validate_inputs(runner, &context.inputs)?;

        let start_time = std::time::Instant::now();

        // Execute the runner logic (simplified simulation)
        let result = self.execute_runner_logic(runner, &context).await?;

        let execution_time = start_time.elapsed().as_millis() as u64;

        Ok(RunnerResult {
            success: result.success,
            outputs: result.outputs,
            metrics: result.metrics,
            execution_time_ms: execution_time,
            error_message: result.error_message,
        })
    }

    /// Validates runner inputs
    fn validate_inputs(&self, runner: &Runner, inputs: &HashMap<String, String>) -> Result<()> {
        for input_spec in &runner.inputs {
            if input_spec.required && !inputs.contains_key(&input_spec.name) {
                anyhow::bail!(
                    "Required input '{}' missing for runner '{}'",
                    input_spec.name,
                    runner.name
                );
            }
        }
        Ok(())
    }

    /// Executes the actual runner logic (simplified simulation)
    async fn execute_runner_logic(
        &self,
        runner: &Runner,
        context: &RunnerContext,
    ) -> Result<RunnerResult> {
        // Simulate different runner behaviors based on name
        match runner.name.as_str() {
            "code_generator" => self.execute_code_generator(context).await,
            "quality_checker" => self.execute_quality_checker(context).await,
            "security_scanner" => self.execute_security_scanner(context).await,
            "documentation_generator" => self.execute_documentation_generator(context).await,
            _ => self.execute_generic_runner(context).await,
        }
    }

    /// Simulates code generation runner
    async fn execute_code_generator(&self, _context: &RunnerContext) -> Result<RunnerResult> {
        // Simulate async work
        tokio::time::sleep(tokio::time::Duration::from_millis(100)).await;

        let mut outputs = HashMap::new();
        outputs.insert(
            "generated_code".to_string(),
            "fn main() { println!(\"Hello, world!\"); }".to_string(),
        );
        outputs.insert("build_script".to_string(), "cargo build".to_string());

        let mut metrics = HashMap::new();
        metrics.insert("lines_of_code".to_string(), 42.0);
        metrics.insert("complexity_score".to_string(), 3.5);

        Ok(RunnerResult {
            success: true,
            outputs,
            metrics,
            execution_time_ms: 100,
            error_message: None,
        })
    }

    /// Simulates quality checking runner
    async fn execute_quality_checker(&self, context: &RunnerContext) -> Result<RunnerResult> {
        tokio::time::sleep(tokio::time::Duration::from_millis(200)).await;

        let has_code = context.inputs.contains_key("source_code");
        let has_tests = context
            .inputs
            .get("source_code")
            .map(|code| code.contains("test"))
            .unwrap_or(false);

        let mut outputs = HashMap::new();
        outputs.insert(
            "quality_report".to_string(),
            format!("Quality analysis: code={}, tests={}", has_code, has_tests),
        );

        let mut metrics = HashMap::new();
        metrics.insert(
            "quality_score".to_string(),
            if has_tests { 8.5 } else { 6.0 },
        );
        metrics.insert(
            "test_coverage".to_string(),
            if has_tests { 85.0 } else { 0.0 },
        );

        Ok(RunnerResult {
            success: true,
            outputs,
            metrics,
            execution_time_ms: 200,
            error_message: None,
        })
    }

    /// Simulates security scanning runner
    async fn execute_security_scanner(&self, context: &RunnerContext) -> Result<RunnerResult> {
        tokio::time::sleep(tokio::time::Duration::from_millis(300)).await;

        let has_vulnerabilities = context
            .inputs
            .get("source_code")
            .map(|code| code.contains("unsafe") || code.contains("vulnerability"))
            .unwrap_or(false);

        let mut outputs = HashMap::new();
        outputs.insert(
            "security_report".to_string(),
            if has_vulnerabilities {
                "Security issues found".to_string()
            } else {
                "No security issues detected".to_string()
            },
        );

        let mut metrics = HashMap::new();
        metrics.insert(
            "vulnerability_count".to_string(),
            if has_vulnerabilities { 3.0 } else { 0.0 },
        );
        metrics.insert(
            "security_score".to_string(),
            if has_vulnerabilities { 4.0 } else { 9.5 },
        );

        Ok(RunnerResult {
            success: !has_vulnerabilities,
            outputs,
            metrics,
            execution_time_ms: 300,
            error_message: if has_vulnerabilities {
                Some("Security vulnerabilities detected".to_string())
            } else {
                None
            },
        })
    }

    /// Simulates documentation generation runner
    async fn execute_documentation_generator(
        &self,
        _context: &RunnerContext,
    ) -> Result<RunnerResult> {
        tokio::time::sleep(tokio::time::Duration::from_millis(150)).await;

        let mut outputs = HashMap::new();
        outputs.insert(
            "readme".to_string(),
            "# Project Documentation\n\nThis is auto-generated documentation.".to_string(),
        );
        outputs.insert(
            "api_docs".to_string(),
            "API documentation generated.".to_string(),
        );

        let mut metrics = HashMap::new();
        metrics.insert("doc_coverage".to_string(), 92.0);
        metrics.insert("doc_quality".to_string(), 8.7);

        Ok(RunnerResult {
            success: true,
            outputs,
            metrics,
            execution_time_ms: 150,
            error_message: None,
        })
    }

    /// Generic runner execution
    async fn execute_generic_runner(&self, _context: &RunnerContext) -> Result<RunnerResult> {
        tokio::time::sleep(tokio::time::Duration::from_millis(50)).await;

        let mut outputs = HashMap::new();
        outputs.insert(
            "result".to_string(),
            "Generic runner executed successfully".to_string(),
        );

        let mut metrics = HashMap::new();
        metrics.insert("execution_score".to_string(), 7.5);

        Ok(RunnerResult {
            success: true,
            outputs,
            metrics,
            execution_time_ms: 50,
            error_message: None,
        })
    }
}

/// Creates a default runner registry with common runners
pub fn create_default_registry() -> RunnerRegistry {
    let mut registry = RunnerRegistry::new();

    // Code generation runner
    let code_runner = Runner {
        name: "code_generator".to_string(),
        version: "1.0.0".to_string(),
        description: "Generates code based on specifications".to_string(),
        supported_phases: vec![Phase::C3Implementation],
        inputs: vec![RunnerInput {
            name: "specification".to_string(),
            input_type: InputType::Text,
            required: true,
            description: "Code specification and requirements".to_string(),
        }],
        outputs: vec![RunnerOutput {
            name: "generated_code".to_string(),
            output_type: OutputType::Artifact,
            description: "Generated source code".to_string(),
        }],
        metadata: HashMap::new(),
    };

    // Quality checker runner
    let quality_runner = Runner {
        name: "quality_checker".to_string(),
        version: "1.0.0".to_string(),
        description: "Analyzes code quality metrics".to_string(),
        supported_phases: vec![Phase::C4Validation],
        inputs: vec![RunnerInput {
            name: "source_code".to_string(),
            input_type: InputType::Text,
            required: true,
            description: "Source code to analyze".to_string(),
        }],
        outputs: vec![RunnerOutput {
            name: "quality_report".to_string(),
            output_type: OutputType::Report,
            description: "Quality analysis report".to_string(),
        }],
        metadata: HashMap::new(),
    };

    registry.register_runner(code_runner).unwrap();
    registry.register_runner(quality_runner).unwrap();

    registry
}

#[cfg(test)]
mod tests {
    use super::*;
    use uuid::Uuid;

    #[test]
    fn test_runner_registry() {
        let mut registry = RunnerRegistry::new();
        let runner = Runner {
            name: "test_runner".to_string(),
            version: "1.0.0".to_string(),
            description: "Test runner".to_string(),
            supported_phases: vec![Phase::C3Implementation],
            inputs: vec![],
            outputs: vec![],
            metadata: HashMap::new(),
        };

        registry.register_runner(runner).unwrap();
        assert!(registry.get_runner("test_runner").is_some());
        assert_eq!(registry.list_runners().len(), 1);
    }

    #[test]
    fn test_find_runners_for_phase() {
        let registry = create_default_registry();
        let runners = registry.find_runners_for_phase(&Phase::C3Implementation);

        assert_eq!(runners.len(), 1);
        assert_eq!(runners[0].name, "code_generator");
    }

    #[tokio::test]
    async fn test_runner_execution() {
        let registry = create_default_registry();
        let executor = RunnerExecutor::new(registry);

        let context = RunnerContext {
            run_id: Uuid::new_v4().to_string(),
            phase: Phase::C3Implementation,
            inputs: HashMap::from([(
                "specification".to_string(),
                "Generate a hello world function".to_string(),
            )]),
            started_at: Utc::now(),
        };

        let result = executor
            .execute_runner("code_generator", context)
            .await
            .unwrap();

        assert!(result.success);
        assert!(result.outputs.contains_key("generated_code"));
        assert!(result.execution_time_ms > 0);
    }

    #[tokio::test]
    async fn test_security_scanner_with_vulnerabilities() {
        let registry = create_default_registry();
        let mut executor = RunnerExecutor::new(registry);

        // Add security scanner to registry
        let security_runner = Runner {
            name: "security_scanner".to_string(),
            version: "1.0.0".to_string(),
            description: "Scans for security vulnerabilities".to_string(),
            supported_phases: vec![Phase::C4Validation],
            inputs: vec![RunnerInput {
                name: "source_code".to_string(),
                input_type: InputType::Text,
                required: true,
                description: "Source code to scan".to_string(),
            }],
            outputs: vec![RunnerOutput {
                name: "security_report".to_string(),
                output_type: OutputType::Report,
                description: "Security scan report".to_string(),
            }],
            metadata: HashMap::new(),
        };

        executor.registry.register_runner(security_runner).unwrap();

        let context = RunnerContext {
            run_id: Uuid::new_v4().to_string(),
            phase: Phase::C4Validation,
            inputs: HashMap::from([(
                "source_code".to_string(),
                "unsafe { vulnerability_code() }".to_string(),
            )]),
            started_at: Utc::now(),
        };

        let result = executor
            .execute_runner("security_scanner", context)
            .await
            .unwrap();

        assert!(!result.success);
        assert!(result.error_message.is_some());
        assert!(result.metrics.get("vulnerability_count").unwrap() > &0.0);
    }
}
