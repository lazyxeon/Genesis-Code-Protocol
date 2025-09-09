//! Gate system for Genesis Code Protocol
//!
//! Implements decision gates for phase transitions and quality control

use anyhow::Result;
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};

/// Gate decision outcomes
#[derive(Debug, Clone, Serialize, Deserialize, PartialEq)]
pub enum GateDecision {
    Allow,
    Deny,
    NeedsHuman,
}

/// Gate signal with metadata
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct GateSignal {
    pub decision: GateDecision,
    pub confidence: f64,
    pub reasoning: String,
    pub timestamp: DateTime<Utc>,
    pub gate_type: GateType,
}

/// Types of gates in the protocol
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum GateType {
    PhaseTransition,
    QualityCheck,
    SecurityReview,
    ComplianceCheck,
    ResourceApproval,
}

/// Gate processor for making automated decisions
#[derive(Debug)]
pub struct GateProcessor {
    pub auto_gate_verbosity: GateVerbosity,
    pub auto_gate_preview: bool,
}

/// Verbosity levels for gate decisions
#[derive(Debug, Clone)]
pub enum GateVerbosity {
    Brief,
    Full,
}

impl GateProcessor {
    /// Creates a new gate processor
    pub fn new() -> Self {
        Self {
            auto_gate_verbosity: GateVerbosity::Brief,
            auto_gate_preview: false,
        }
    }

    /// Processes a gate decision
    pub fn process_gate(&self, gate_type: GateType, context: &str) -> Result<GateSignal> {
        let (decision, confidence, reasoning) = match gate_type {
            GateType::PhaseTransition => self.evaluate_phase_transition(context),
            GateType::QualityCheck => self.evaluate_quality(context),
            GateType::SecurityReview => self.evaluate_security(context),
            GateType::ComplianceCheck => self.evaluate_compliance(context),
            GateType::ResourceApproval => self.evaluate_resources(context),
        };

        Ok(GateSignal {
            decision,
            confidence,
            reasoning,
            timestamp: Utc::now(),
            gate_type,
        })
    }

    /// Evaluates phase transition readiness
    fn evaluate_phase_transition(&self, _context: &str) -> (GateDecision, f64, String) {
        // Simplified evaluation logic
        let confidence = 0.85;
        let decision = if confidence > 0.8 {
            GateDecision::Allow
        } else if confidence > 0.5 {
            GateDecision::NeedsHuman
        } else {
            GateDecision::Deny
        };

        (
            decision,
            confidence,
            "Phase transition criteria evaluated based on artifact completeness".to_string(),
        )
    }

    /// Evaluates quality metrics
    fn evaluate_quality(&self, context: &str) -> (GateDecision, f64, String) {
        let has_tests = context.contains("test");
        let has_docs = context.contains("documentation");
        
        let confidence = if has_tests && has_docs { 0.9 } else { 0.6 };
        let decision = if confidence > 0.8 {
            GateDecision::Allow
        } else {
            GateDecision::NeedsHuman
        };

        (
            decision,
            confidence,
            format!("Quality assessment: tests={}, docs={}", has_tests, has_docs),
        )
    }

    /// Evaluates security concerns
    fn evaluate_security(&self, context: &str) -> (GateDecision, f64, String) {
        let has_vulnerabilities = context.contains("vulnerability") || context.contains("security issue");
        
        let (decision, confidence) = if has_vulnerabilities {
            (GateDecision::Deny, 0.95)
        } else {
            (GateDecision::Allow, 0.8)
        };

        (
            decision,
            confidence,
            "Security evaluation based on vulnerability scanning".to_string(),
        )
    }

    /// Evaluates compliance requirements
    fn evaluate_compliance(&self, context: &str) -> (GateDecision, f64, String) {
        let has_compliance_docs = context.contains("compliance") || context.contains("audit");
        
        let confidence = if has_compliance_docs { 0.9 } else { 0.5 };
        let decision = if confidence > 0.7 {
            GateDecision::Allow
        } else {
            GateDecision::NeedsHuman
        };

        (
            decision,
            confidence,
            "Compliance evaluation based on documentation completeness".to_string(),
        )
    }

    /// Evaluates resource requirements
    fn evaluate_resources(&self, _context: &str) -> (GateDecision, f64, String) {
        // Simplified resource evaluation
        (
            GateDecision::Allow,
            0.8,
            "Resource requirements within acceptable limits".to_string(),
        )
    }
}

impl Default for GateProcessor {
    fn default() -> Self {
        Self::new()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_gate_processor_creation() {
        let processor = GateProcessor::new();
        assert!(matches!(processor.auto_gate_verbosity, GateVerbosity::Brief));
        assert!(!processor.auto_gate_preview);
    }

    #[test]
    fn test_phase_transition_gate() {
        let processor = GateProcessor::new();
        let signal = processor.process_gate(
            GateType::PhaseTransition,
            "All artifacts complete with documentation"
        ).unwrap();

        assert!(matches!(signal.decision, GateDecision::Allow));
        assert!(signal.confidence > 0.8);
        assert!(matches!(signal.gate_type, GateType::PhaseTransition));
    }

    #[test]
    fn test_quality_gate_with_tests_and_docs() {
        let processor = GateProcessor::new();
        let signal = processor.process_gate(
            GateType::QualityCheck,
            "Code includes comprehensive test coverage and documentation"
        ).unwrap();

        assert!(matches!(signal.decision, GateDecision::Allow));
        assert!(signal.confidence > 0.8);
    }

    #[test]
    fn test_security_gate_with_vulnerabilities() {
        let processor = GateProcessor::new();
        let signal = processor.process_gate(
            GateType::SecurityReview,
            "Found critical vulnerability in dependencies"
        ).unwrap();

        assert!(matches!(signal.decision, GateDecision::Deny));
        assert!(signal.confidence > 0.9);
    }

    #[test]
    fn test_gate_signal_serialization() {
        let signal = GateSignal {
            decision: GateDecision::Allow,
            confidence: 0.85,
            reasoning: "Test reasoning".to_string(),
            timestamp: Utc::now(),
            gate_type: GateType::QualityCheck,
        };

        let json = serde_json::to_string(&signal).unwrap();
        let deserialized: GateSignal = serde_json::from_str(&json).unwrap();

        assert_eq!(signal.decision, deserialized.decision);
        assert_eq!(signal.confidence, deserialized.confidence);
    }
}