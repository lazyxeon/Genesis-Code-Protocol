//! Phase management for Genesis Code Protocol
//!
//! Handles phase definitions, transitions, and lifecycle management

use anyhow::Result;
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};

use crate::{
    gates::{GateDecision, GateProcessor, GateType},
    Phase,
};

/// Phase manager for handling protocol execution flow
#[derive(Debug)]
pub struct PhaseManager {
    pub current_phase: Phase,
    pub phase_history: Vec<PhaseTransition>,
    pub gate_processor: GateProcessor,
}

/// Records a phase transition with metadata
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct PhaseTransition {
    pub from_phase: Phase,
    pub to_phase: Phase,
    pub timestamp: DateTime<Utc>,
    pub gate_decision: GateDecision,
    pub metadata: String,
}

impl PhaseManager {
    /// Creates a new phase manager
    pub fn new(initial_phase: Phase) -> Self {
        Self {
            current_phase: initial_phase,
            phase_history: Vec::new(),
            gate_processor: GateProcessor::new(),
        }
    }

    /// Attempts to transition to the next phase
    pub fn transition_to_phase(&mut self, target_phase: Phase, context: &str) -> Result<bool> {
        // Validate transition is allowed
        if !self.is_valid_transition(&self.current_phase, &target_phase) {
            anyhow::bail!(
                "Invalid phase transition from {:?} to {:?}",
                self.current_phase,
                target_phase
            );
        }

        // Process gate decision
        let gate_signal = self
            .gate_processor
            .process_gate(GateType::PhaseTransition, context)?;

        match gate_signal.decision {
            GateDecision::Allow => {
                // Record transition
                let transition = PhaseTransition {
                    from_phase: self.current_phase.clone(),
                    to_phase: target_phase.clone(),
                    timestamp: Utc::now(),
                    gate_decision: gate_signal.decision,
                    metadata: gate_signal.reasoning,
                };

                self.phase_history.push(transition);
                self.current_phase = target_phase;
                Ok(true)
            }
            GateDecision::Deny => {
                anyhow::bail!("Gate denied phase transition: {}", gate_signal.reasoning);
            }
            GateDecision::NeedsHuman => {
                // Log that human intervention is needed
                tracing::warn!(
                    "Phase transition requires human approval: {}",
                    gate_signal.reasoning
                );
                Ok(false)
            }
        }
    }

    /// Gets the next logical phase in the sequence
    pub fn get_next_phase(&self) -> Option<Phase> {
        match &self.current_phase {
            Phase::I1AutonomousSparkGeneration => Some(Phase::C0AmbiguityToBrief),
            Phase::C0AmbiguityToBrief => Some(Phase::C1RequirementsAnalysis),
            Phase::C1RequirementsAnalysis => Some(Phase::C2DesignPhase),
            Phase::C2DesignPhase => Some(Phase::C3Implementation),
            Phase::C3Implementation => Some(Phase::C4Validation),
            Phase::C4Validation => Some(Phase::C5Documentation),
            Phase::C5Documentation => Some(Phase::C6Deployment),
            Phase::C6Deployment => Some(Phase::C7Monitoring),
            Phase::C7Monitoring => Some(Phase::C8Maintenance),
            Phase::C8Maintenance => Some(Phase::C9Evolution),
            Phase::C9Evolution => Some(Phase::C10Archival),
            Phase::C10Archival => None, // Final phase
        }
    }

    /// Validates if a phase transition is allowed
    pub fn is_valid_transition(&self, from: &Phase, to: &Phase) -> bool {
        // Allow sequential progression
        if let Some(next_phase) = self.get_next_phase_for(from) {
            if std::mem::discriminant(&next_phase) == std::mem::discriminant(to) {
                return true;
            }
        }

        // Allow branching to certain phases
        matches!(
            (from, to),
            (Phase::C2DesignPhase, Phase::C1RequirementsAnalysis) |  // Iteration back
            (Phase::C4Validation, Phase::C3Implementation) |         // Bug fixes
            (Phase::C3Implementation, Phase::C2DesignPhase) |        // Design revision
            (_, Phase::C10Archival) // Emergency archival
        )
    }

    /// Helper to get next phase for any given phase
    fn get_next_phase_for(&self, phase: &Phase) -> Option<Phase> {
        match phase {
            Phase::I1AutonomousSparkGeneration => Some(Phase::C0AmbiguityToBrief),
            Phase::C0AmbiguityToBrief => Some(Phase::C1RequirementsAnalysis),
            Phase::C1RequirementsAnalysis => Some(Phase::C2DesignPhase),
            Phase::C2DesignPhase => Some(Phase::C3Implementation),
            Phase::C3Implementation => Some(Phase::C4Validation),
            Phase::C4Validation => Some(Phase::C5Documentation),
            Phase::C5Documentation => Some(Phase::C6Deployment),
            Phase::C6Deployment => Some(Phase::C7Monitoring),
            Phase::C7Monitoring => Some(Phase::C8Maintenance),
            Phase::C8Maintenance => Some(Phase::C9Evolution),
            Phase::C9Evolution => Some(Phase::C10Archival),
            Phase::C10Archival => None,
        }
    }

    /// Gets phase requirements and deliverables
    pub fn get_phase_requirements(&self, phase: &Phase) -> Vec<String> {
        match phase {
            Phase::I1AutonomousSparkGeneration => vec![
                "Problem domain identification".to_string(),
                "Initial spark generation".to_string(),
            ],
            Phase::C0AmbiguityToBrief => vec![
                "Problem statement clarification".to_string(),
                "Scope definition".to_string(),
                "Success criteria".to_string(),
            ],
            Phase::C1RequirementsAnalysis => vec![
                "Functional requirements".to_string(),
                "Non-functional requirements".to_string(),
                "Constraints documentation".to_string(),
            ],
            Phase::C2DesignPhase => vec![
                "Architecture design".to_string(),
                "Component specifications".to_string(),
                "Interface definitions".to_string(),
            ],
            Phase::C3Implementation => vec![
                "Code implementation".to_string(),
                "Unit tests".to_string(),
                "Integration points".to_string(),
            ],
            Phase::C4Validation => vec![
                "Test execution".to_string(),
                "Validation reports".to_string(),
                "Bug fixes".to_string(),
            ],
            Phase::C5Documentation => vec![
                "User documentation".to_string(),
                "API documentation".to_string(),
                "Deployment guides".to_string(),
            ],
            Phase::C6Deployment => vec![
                "Production deployment".to_string(),
                "Configuration management".to_string(),
                "Monitoring setup".to_string(),
            ],
            Phase::C7Monitoring => vec![
                "Performance monitoring".to_string(),
                "Error tracking".to_string(),
                "Usage analytics".to_string(),
            ],
            Phase::C8Maintenance => vec![
                "Bug fixes".to_string(),
                "Security updates".to_string(),
                "Performance optimization".to_string(),
            ],
            Phase::C9Evolution => vec![
                "Feature enhancements".to_string(),
                "Architecture evolution".to_string(),
                "Legacy migration".to_string(),
            ],
            Phase::C10Archival => vec![
                "Data archival".to_string(),
                "Documentation preservation".to_string(),
                "Knowledge transfer".to_string(),
            ],
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_phase_manager_creation() {
        let manager = PhaseManager::new(Phase::C0AmbiguityToBrief);
        assert!(matches!(manager.current_phase, Phase::C0AmbiguityToBrief));
        assert!(manager.phase_history.is_empty());
    }

    #[test]
    fn test_valid_sequential_transition() {
        let mut manager = PhaseManager::new(Phase::C0AmbiguityToBrief);

        let result = manager.transition_to_phase(
            Phase::C1RequirementsAnalysis,
            "Requirements analysis ready with complete documentation",
        );

        assert!(result.is_ok());
        assert!(result.unwrap()); // Should return true for allowed transition
        assert!(matches!(
            manager.current_phase,
            Phase::C1RequirementsAnalysis
        ));
        assert_eq!(manager.phase_history.len(), 1);
    }

    #[test]
    fn test_invalid_transition() {
        let mut manager = PhaseManager::new(Phase::C0AmbiguityToBrief);

        let result = manager.transition_to_phase(Phase::C4Validation, "Skipping to validation");

        assert!(result.is_err());
        assert!(matches!(manager.current_phase, Phase::C0AmbiguityToBrief));
    }

    #[test]
    fn test_get_next_phase() {
        let manager = PhaseManager::new(Phase::C2DesignPhase);
        let next = manager.get_next_phase();

        assert!(next.is_some());
        assert!(matches!(next.unwrap(), Phase::C3Implementation));
    }

    #[test]
    fn test_final_phase_has_no_next() {
        let manager = PhaseManager::new(Phase::C10Archival);
        let next = manager.get_next_phase();

        assert!(next.is_none());
    }

    #[test]
    fn test_valid_iteration_back() {
        let manager = PhaseManager::new(Phase::C4Validation);

        assert!(manager.is_valid_transition(&Phase::C4Validation, &Phase::C3Implementation));
        assert!(manager.is_valid_transition(&Phase::C2DesignPhase, &Phase::C1RequirementsAnalysis));
    }

    #[test]
    fn test_phase_requirements() {
        let manager = PhaseManager::new(Phase::C1RequirementsAnalysis);
        let requirements = manager.get_phase_requirements(&Phase::C1RequirementsAnalysis);

        assert!(!requirements.is_empty());
        assert!(requirements.iter().any(|r| r.contains("requirements")));
    }
}
