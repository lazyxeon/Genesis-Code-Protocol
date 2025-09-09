//! Telemetry system for Genesis Code Protocol
//!
//! Handles metrics collection, performance tracking, and observability

use anyhow::Result;
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::sync::{Arc, Mutex};

use crate::Phase;

/// Telemetry collector for protocol metrics
#[derive(Debug, Clone)]
pub struct TelemetryCollector {
    metrics: Arc<Mutex<Vec<TelemetryMetric>>>,
    events: Arc<Mutex<Vec<TelemetryEvent>>>,
}

/// Individual telemetry metric
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TelemetryMetric {
    pub name: String,
    pub value: f64,
    pub unit: String,
    pub timestamp: DateTime<Utc>,
    pub tags: HashMap<String, String>,
}

/// Telemetry event for tracking discrete occurrences
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TelemetryEvent {
    pub name: String,
    pub timestamp: DateTime<Utc>,
    pub phase: Option<Phase>,
    pub data: HashMap<String, serde_json::Value>,
    pub severity: EventSeverity,
}

/// Severity levels for telemetry events
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum EventSeverity {
    Debug,
    Info,
    Warning,
    Error,
    Critical,
}

/// Performance tracking for specific operations
#[derive(Debug)]
pub struct PerformanceTracker {
    operation_name: String,
    start_time: std::time::Instant,
    collector: TelemetryCollector,
}

/// Aggregated telemetry report
#[derive(Debug, Serialize, Deserialize)]
pub struct TelemetryReport {
    pub generated_at: DateTime<Utc>,
    pub total_metrics: usize,
    pub total_events: usize,
    pub performance_summary: PerformanceSummary,
    pub error_summary: ErrorSummary,
    pub phase_distribution: HashMap<String, usize>,
}

/// Performance metrics summary
#[derive(Debug, Serialize, Deserialize)]
pub struct PerformanceSummary {
    pub average_execution_time_ms: f64,
    pub min_execution_time_ms: f64,
    pub max_execution_time_ms: f64,
    pub total_operations: usize,
}

/// Error and warning summary
#[derive(Debug, Serialize, Deserialize)]
pub struct ErrorSummary {
    pub total_errors: usize,
    pub total_warnings: usize,
    pub error_rate_percent: f64,
    pub most_common_errors: Vec<String>,
}

impl TelemetryCollector {
    /// Creates a new telemetry collector
    pub fn new() -> Self {
        Self {
            metrics: Arc::new(Mutex::new(Vec::new())),
            events: Arc::new(Mutex::new(Vec::new())),
        }
    }

    /// Records a metric
    pub fn record_metric(
        &self,
        name: String,
        value: f64,
        unit: String,
        tags: HashMap<String, String>,
    ) -> Result<()> {
        let metric = TelemetryMetric {
            name,
            value,
            unit,
            timestamp: Utc::now(),
            tags,
        };

        self.metrics
            .lock()
            .map_err(|_| anyhow::anyhow!("Failed to acquire metrics lock"))?
            .push(metric);

        Ok(())
    }

    /// Records an event
    pub fn record_event(
        &self,
        name: String,
        phase: Option<Phase>,
        data: HashMap<String, serde_json::Value>,
        severity: EventSeverity,
    ) -> Result<()> {
        let event = TelemetryEvent {
            name,
            timestamp: Utc::now(),
            phase,
            data,
            severity,
        };

        self.events
            .lock()
            .map_err(|_| anyhow::anyhow!("Failed to acquire events lock"))?
            .push(event);

        Ok(())
    }

    /// Records execution time for an operation
    pub fn record_execution_time(
        &self,
        operation: &str,
        duration_ms: f64,
        phase: Option<Phase>,
    ) -> Result<()> {
        let mut tags = HashMap::new();
        tags.insert("operation".to_string(), operation.to_string());
        if let Some(phase) = &phase {
            tags.insert("phase".to_string(), format!("{:?}", phase));
        }

        self.record_metric(
            "execution_time".to_string(),
            duration_ms,
            "milliseconds".to_string(),
            tags,
        )?;

        // Also record as an event for detailed tracking
        let mut event_data = HashMap::new();
        event_data.insert(
            "operation".to_string(),
            serde_json::Value::String(operation.to_string()),
        );
        event_data.insert(
            "duration_ms".to_string(),
            serde_json::Value::Number(serde_json::Number::from_f64(duration_ms).unwrap()),
        );

        self.record_event(
            "operation_completed".to_string(),
            phase,
            event_data,
            EventSeverity::Info,
        )?;

        Ok(())
    }

    /// Records an error
    pub fn record_error(
        &self,
        error_message: String,
        phase: Option<Phase>,
        context: HashMap<String, String>,
    ) -> Result<()> {
        let mut event_data = HashMap::new();
        event_data.insert(
            "error_message".to_string(),
            serde_json::Value::String(error_message.clone()),
        );
        for (key, value) in context {
            event_data.insert(key, serde_json::Value::String(value));
        }

        self.record_event(
            "error_occurred".to_string(),
            phase,
            event_data,
            EventSeverity::Error,
        )?;

        // Also increment error counter metric
        self.record_metric(
            "error_count".to_string(),
            1.0,
            "count".to_string(),
            HashMap::from([("error_type".to_string(), "general".to_string())]),
        )?;

        Ok(())
    }

    /// Starts performance tracking for an operation
    pub fn start_performance_tracking(&self, operation_name: String) -> PerformanceTracker {
        PerformanceTracker {
            operation_name,
            start_time: std::time::Instant::now(),
            collector: self.clone(),
        }
    }

    /// Generates a comprehensive telemetry report
    pub fn generate_report(&self) -> Result<TelemetryReport> {
        let metrics = self
            .metrics
            .lock()
            .map_err(|_| anyhow::anyhow!("Failed to acquire metrics lock"))?
            .clone();

        let events = self
            .events
            .lock()
            .map_err(|_| anyhow::anyhow!("Failed to acquire events lock"))?
            .clone();

        // Calculate performance summary
        let execution_times: Vec<f64> = metrics
            .iter()
            .filter(|m| m.name == "execution_time")
            .map(|m| m.value)
            .collect();

        let performance_summary = if execution_times.is_empty() {
            PerformanceSummary {
                average_execution_time_ms: 0.0,
                min_execution_time_ms: 0.0,
                max_execution_time_ms: 0.0,
                total_operations: 0,
            }
        } else {
            PerformanceSummary {
                average_execution_time_ms: execution_times.iter().sum::<f64>()
                    / execution_times.len() as f64,
                min_execution_time_ms: execution_times.iter().fold(f64::INFINITY, |a, &b| a.min(b)),
                max_execution_time_ms: execution_times
                    .iter()
                    .fold(f64::NEG_INFINITY, |a, &b| a.max(b)),
                total_operations: execution_times.len(),
            }
        };

        // Calculate error summary
        let error_events: Vec<&TelemetryEvent> = events
            .iter()
            .filter(|e| matches!(e.severity, EventSeverity::Error | EventSeverity::Critical))
            .collect();

        let warning_events: Vec<&TelemetryEvent> = events
            .iter()
            .filter(|e| matches!(e.severity, EventSeverity::Warning))
            .collect();

        let error_rate = if !events.is_empty() {
            (error_events.len() as f64 / events.len() as f64) * 100.0
        } else {
            0.0
        };

        let error_summary = ErrorSummary {
            total_errors: error_events.len(),
            total_warnings: warning_events.len(),
            error_rate_percent: error_rate,
            most_common_errors: vec![], // Simplified for now
        };

        // Calculate phase distribution
        let mut phase_distribution = HashMap::new();
        for event in &events {
            if let Some(phase) = &event.phase {
                let phase_name = format!("{:?}", phase);
                *phase_distribution.entry(phase_name).or_insert(0) += 1;
            }
        }

        Ok(TelemetryReport {
            generated_at: Utc::now(),
            total_metrics: metrics.len(),
            total_events: events.len(),
            performance_summary,
            error_summary,
            phase_distribution,
        })
    }

    /// Exports telemetry data to JSON
    pub fn export_to_json(&self) -> Result<String> {
        let report = self.generate_report()?;
        serde_json::to_string_pretty(&report)
            .map_err(|e| anyhow::anyhow!("Failed to serialize telemetry report: {}", e))
    }

    /// Clears all collected telemetry data
    pub fn clear(&self) -> Result<()> {
        self.metrics
            .lock()
            .map_err(|_| anyhow::anyhow!("Failed to acquire metrics lock"))?
            .clear();

        self.events
            .lock()
            .map_err(|_| anyhow::anyhow!("Failed to acquire events lock"))?
            .clear();

        Ok(())
    }
}

impl PerformanceTracker {
    /// Stops tracking and records the performance metric
    pub fn stop(self, phase: Option<Phase>) -> Result<f64> {
        let duration = self.start_time.elapsed();
        let duration_ms = duration.as_millis() as f64;

        self.collector
            .record_execution_time(&self.operation_name, duration_ms, phase)?;

        Ok(duration_ms)
    }

    /// Stops tracking with additional context
    pub fn stop_with_context(
        self,
        phase: Option<Phase>,
        context: HashMap<String, String>,
    ) -> Result<f64> {
        let phase_clone = phase.clone();
        let collector = self.collector.clone();
        let operation_name = self.operation_name.clone();
        let duration_ms = self.stop(phase)?;

        // Record additional context as an event
        let mut event_data: HashMap<String, serde_json::Value> = context
            .into_iter()
            .map(|(k, v)| (k, serde_json::Value::String(v)))
            .collect();

        event_data.insert(
            "operation".to_string(),
            serde_json::Value::String(operation_name),
        );
        event_data.insert(
            "duration_ms".to_string(),
            serde_json::Value::Number(serde_json::Number::from_f64(duration_ms).unwrap()),
        );

        collector.record_event(
            "operation_completed_with_context".to_string(),
            phase_clone,
            event_data,
            EventSeverity::Info,
        )?;

        Ok(duration_ms)
    }
}

impl Default for TelemetryCollector {
    fn default() -> Self {
        Self::new()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_telemetry_collector_creation() {
        let collector = TelemetryCollector::new();
        let report = collector.generate_report().unwrap();

        assert_eq!(report.total_metrics, 0);
        assert_eq!(report.total_events, 0);
    }

    #[test]
    fn test_record_metric() {
        let collector = TelemetryCollector::new();
        let mut tags = HashMap::new();
        tags.insert("test".to_string(), "value".to_string());

        collector
            .record_metric("test_metric".to_string(), 42.0, "units".to_string(), tags)
            .unwrap();

        let report = collector.generate_report().unwrap();
        assert_eq!(report.total_metrics, 1);
    }

    #[test]
    fn test_record_event() {
        let collector = TelemetryCollector::new();
        let mut data = HashMap::new();
        data.insert(
            "test_key".to_string(),
            serde_json::Value::String("test_value".to_string()),
        );

        collector
            .record_event(
                "test_event".to_string(),
                Some(Phase::C1RequirementsAnalysis),
                data,
                EventSeverity::Info,
            )
            .unwrap();

        let report = collector.generate_report().unwrap();
        assert_eq!(report.total_events, 1);
        assert_eq!(
            report.phase_distribution.get("C1RequirementsAnalysis"),
            Some(&1)
        );
    }

    #[test]
    fn test_performance_tracking() {
        let collector = TelemetryCollector::new();
        let tracker = collector.start_performance_tracking("test_operation".to_string());

        // Simulate some work
        std::thread::sleep(std::time::Duration::from_millis(10));

        let duration = tracker.stop(Some(Phase::C3Implementation)).unwrap();

        assert!(duration >= 10.0);

        let report = collector.generate_report().unwrap();
        assert!(report.total_metrics > 0);
        assert!(report.total_events > 0);
        assert!(report.performance_summary.total_operations > 0);
    }

    #[test]
    fn test_error_recording() {
        let collector = TelemetryCollector::new();
        let mut context = HashMap::new();
        context.insert("context_key".to_string(), "context_value".to_string());

        collector
            .record_error(
                "Test error message".to_string(),
                Some(Phase::C4Validation),
                context,
            )
            .unwrap();

        let report = collector.generate_report().unwrap();
        assert_eq!(report.error_summary.total_errors, 1);
        assert!(report.error_summary.error_rate_percent > 0.0);
    }

    #[test]
    fn test_telemetry_export() {
        let collector = TelemetryCollector::new();

        // Add some test data
        collector
            .record_metric(
                "test_metric".to_string(),
                123.45,
                "units".to_string(),
                HashMap::new(),
            )
            .unwrap();

        let json = collector.export_to_json().unwrap();
        assert!(json.contains("generated_at"));
        assert!(json.contains("total_metrics"));
        assert!(json.contains("performance_summary"));
    }

    #[test]
    fn test_clear_telemetry() {
        let collector = TelemetryCollector::new();

        // Add some data
        collector
            .record_metric("test".to_string(), 1.0, "unit".to_string(), HashMap::new())
            .unwrap();
        collector
            .record_event(
                "test".to_string(),
                None,
                HashMap::new(),
                EventSeverity::Info,
            )
            .unwrap();

        let report_before = collector.generate_report().unwrap();
        assert!(report_before.total_metrics > 0);
        assert!(report_before.total_events > 0);

        // Clear data
        collector.clear().unwrap();

        let report_after = collector.generate_report().unwrap();
        assert_eq!(report_after.total_metrics, 0);
        assert_eq!(report_after.total_events, 0);
    }
}
