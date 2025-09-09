//! Genesis Code Protocol Rust Implementation
//!
//! This crate provides a Rust implementation of core Genesis Code Protocol (GCP) functionality,
//! designed to complement the existing Python framework with high-performance components.

use anyhow::{Context, Result};
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use uuid::Uuid;

pub mod artifacts;
pub mod gates;
pub mod phases;
pub mod runners;
pub mod telemetry;

/// Represents a GCP run instance with associated metadata and state
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GcpRun {
    pub run_id: Uuid,
    pub mode: RunMode,
    pub startup_mode: StartupMode,
    pub risk_tier: RiskTier,
    pub created_at: DateTime<Utc>,
    pub updated_at: DateTime<Utc>,
    pub current_phase: Phase,
    pub artifacts: HashMap<String, String>,
    pub telemetry: Vec<TelemetryEvent>,
}

/// Execution modes for GCP runs
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub enum RunMode {
    Auto,
    Full,
    Manual,
}

/// Startup modes for GCP initialization
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub enum StartupMode {
    SparkProvided,
    Autonomous,
}

/// Risk assessment tiers
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub enum RiskTier {
    R1, // Low risk
    R2, // Medium risk
    R3, // High risk
}

/// GCP protocol phases
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub enum Phase {
    I1AutonomousSparkGeneration,
    C0AmbiguityToBrief,
    C1RequirementsAnalysis,
    C2DesignPhase,
    C3Implementation,
    C4Validation,
    C5Documentation,
    C6Deployment,
    C7Monitoring,
    C8Maintenance,
    C9Evolution,
    C10Archival,
}

/// Telemetry events for tracking GCP execution
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TelemetryEvent {
    pub timestamp: DateTime<Utc>,
    pub event_type: String,
    pub phase: Phase,
    pub data: serde_json::Value,
}

impl GcpRun {
    /// Creates a new GCP run instance
    pub fn new(mode: RunMode, startup_mode: StartupMode, risk_tier: RiskTier) -> Self {
        let now = Utc::now();
        let current_phase = match startup_mode {
            StartupMode::Autonomous => Phase::I1AutonomousSparkGeneration,
            StartupMode::SparkProvided => Phase::C0AmbiguityToBrief,
        };

        Self {
            run_id: Uuid::new_v4(),
            mode,
            startup_mode,
            risk_tier,
            created_at: now,
            updated_at: now,
            current_phase,
            artifacts: HashMap::new(),
            telemetry: Vec::new(),
        }
    }

    /// Advances the run to the next phase
    pub fn advance_phase(&mut self, next_phase: Phase) -> Result<()> {
        let previous_phase = self.current_phase.clone();
        self.current_phase = next_phase.clone();
        self.updated_at = Utc::now();

        // Record telemetry
        self.add_telemetry_event(
            "phase_advance".to_string(),
            serde_json::json!({
                "previous_phase": previous_phase,
                "new_phase": next_phase
            }),
        );

        Ok(())
    }

    /// Adds an artifact to the run
    pub fn add_artifact(&mut self, name: String, content: String) -> Result<()> {
        let content_size = content.len();
        self.artifacts.insert(name.clone(), content);
        self.updated_at = Utc::now();

        self.add_telemetry_event(
            "artifact_added".to_string(),
            serde_json::json!({
                "artifact_name": name,
                "size": content_size
            }),
        );

        Ok(())
    }

    /// Adds a telemetry event
    pub fn add_telemetry_event(&mut self, event_type: String, data: serde_json::Value) {
        let event = TelemetryEvent {
            timestamp: Utc::now(),
            event_type,
            phase: self.current_phase.clone(),
            data,
        };
        self.telemetry.push(event);
        self.updated_at = Utc::now();
    }

    /// Serializes the run to JSON
    pub fn to_json(&self) -> Result<String> {
        serde_json::to_string_pretty(self).context("Failed to serialize GCP run to JSON")
    }

    /// Deserializes a run from JSON
    pub fn from_json(json: &str) -> Result<Self> {
        serde_json::from_str(json).context("Failed to deserialize GCP run from JSON")
    }

    /// Validates the current state of the run
    pub fn validate(&self) -> Result<()> {
        // Basic validation rules
        if self.artifacts.is_empty()
            && matches!(
                self.current_phase,
                Phase::C5Documentation | Phase::C6Deployment
            )
        {
            anyhow::bail!("No artifacts found for phase requiring outputs");
        }

        // Risk tier specific validations
        match self.risk_tier {
            RiskTier::R2 | RiskTier::R3 => {
                if !self.artifacts.contains_key("SBOM") {
                    anyhow::bail!("SBOM is mandatory for R2+ risk tiers");
                }
            }
            _ => {}
        }

        Ok(())
    }
}

/// Utility function for generating run IDs with specific prefixes
pub fn generate_run_id_with_prefix(prefix: &str) -> String {
    format!("{}-{}", prefix, Uuid::new_v4())
}

/// Performance-critical protocol operations
pub mod performance {
    use std::time::Instant;

    /// High-performance artifact processing
    pub fn process_large_artifact(content: &[u8]) -> Vec<u8> {
        // Simulate high-performance processing
        let start = Instant::now();
        let mut result = content.to_vec();

        // Perform some processing operations
        result.sort_unstable();
        result.dedup();

        // Log processing time for benchmarking
        let duration = start.elapsed();
        tracing::info!("Processed {} bytes in {:?}", content.len(), duration);

        result
    }

    /// Batch processing for multiple artifacts
    pub fn batch_process_artifacts(artifacts: &[&[u8]]) -> Vec<Vec<u8>> {
        artifacts
            .iter()
            .map(|artifact| process_large_artifact(artifact))
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq;

    #[test]
    fn test_gcp_run_creation() {
        let run = GcpRun::new(RunMode::Auto, StartupMode::SparkProvided, RiskTier::R1);

        assert_eq!(run.mode, RunMode::Auto);
        assert_eq!(run.startup_mode, StartupMode::SparkProvided);
        assert_eq!(run.risk_tier, RiskTier::R1);
        assert!(matches!(run.current_phase, Phase::C0AmbiguityToBrief));
        assert!(run.artifacts.is_empty());
    }

    #[test]
    fn test_artifact_addition() {
        let mut run = GcpRun::new(RunMode::Full, StartupMode::Autonomous, RiskTier::R2);

        run.add_artifact("test_artifact".to_string(), "test content".to_string())
            .unwrap();

        assert_eq!(
            run.artifacts.get("test_artifact"),
            Some(&"test content".to_string())
        );
        assert_eq!(run.telemetry.len(), 1);
        assert_eq!(run.telemetry[0].event_type, "artifact_added");
    }

    #[test]
    fn test_phase_advancement() {
        let mut run = GcpRun::new(RunMode::Manual, StartupMode::SparkProvided, RiskTier::R1);

        run.advance_phase(Phase::C1RequirementsAnalysis).unwrap();

        assert!(matches!(run.current_phase, Phase::C1RequirementsAnalysis));
        assert_eq!(run.telemetry.len(), 1);
        assert_eq!(run.telemetry[0].event_type, "phase_advance");
    }

    #[test]
    fn test_json_serialization() {
        let run = GcpRun::new(RunMode::Auto, StartupMode::Autonomous, RiskTier::R3);

        let json = run.to_json().unwrap();
        let deserialized = GcpRun::from_json(&json).unwrap();

        assert_eq!(run.run_id, deserialized.run_id);
        assert_eq!(run.mode, deserialized.mode);
        assert_eq!(run.startup_mode, deserialized.startup_mode);
        assert_eq!(run.risk_tier, deserialized.risk_tier);
    }

    #[test]
    fn test_validation_r2_requires_sbom() {
        let mut run = GcpRun::new(RunMode::Auto, StartupMode::SparkProvided, RiskTier::R2);
        run.current_phase = Phase::C5Documentation;

        // Should fail without SBOM
        assert!(run.validate().is_err());

        // Should pass with SBOM
        run.add_artifact("SBOM".to_string(), "sbom content".to_string())
            .unwrap();
        assert!(run.validate().is_ok());
    }

    #[test]
    fn test_performance_artifact_processing() {
        let test_data = vec![3u8, 1, 4, 1, 5, 9, 2, 6];
        let result = performance::process_large_artifact(&test_data);

        // Should be sorted and deduplicated
        assert_eq!(result, vec![1, 2, 3, 4, 5, 6, 9]);
    }

    #[test]
    fn test_batch_processing() {
        let artifact1 = vec![3u8, 1, 4];
        let artifact2 = vec![2u8, 7, 1];
        let artifacts = vec![artifact1.as_slice(), artifact2.as_slice()];

        let results = performance::batch_process_artifacts(&artifacts);

        assert_eq!(results.len(), 2);
        assert_eq!(results[0], vec![1, 3, 4]);
        assert_eq!(results[1], vec![1, 2, 7]);
    }
}
