//! Artifact management for Genesis Code Protocol
//!
//! Handles creation, validation, and management of protocol artifacts

use anyhow::Result;
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

/// Represents a protocol artifact with metadata
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Artifact {
    pub name: String,
    pub content: String,
    pub artifact_type: ArtifactType,
    pub created_at: DateTime<Utc>,
    pub checksum: String,
    pub metadata: HashMap<String, String>,
}

/// Types of artifacts in the protocol
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum ArtifactType {
    Evidence,
    Documentation,
    Code,
    Configuration,
    Report,
    Manifest,
    Index,
    Ledger,
}

impl Artifact {
    /// Creates a new artifact
    pub fn new(name: String, content: String, artifact_type: ArtifactType) -> Self {
        let checksum = format!("{:x}", md5::compute(&content));
        
        Self {
            name,
            content,
            artifact_type,
            created_at: Utc::now(),
            checksum,
            metadata: HashMap::new(),
        }
    }

    /// Validates the artifact integrity
    pub fn validate(&self) -> Result<()> {
        let current_checksum = format!("{:x}", md5::compute(&self.content));
        if current_checksum != self.checksum {
            anyhow::bail!("Artifact checksum mismatch: expected {}, got {}", 
                         self.checksum, current_checksum);
        }
        Ok(())
    }

    /// Adds metadata to the artifact
    pub fn add_metadata(&mut self, key: String, value: String) {
        self.metadata.insert(key, value);
    }
}

/// Artifact manager for handling collections of artifacts
#[derive(Debug, Default)]
pub struct ArtifactManager {
    artifacts: HashMap<String, Artifact>,
}

impl ArtifactManager {
    /// Creates a new artifact manager
    pub fn new() -> Self {
        Self {
            artifacts: HashMap::new(),
        }
    }

    /// Adds an artifact to the manager
    pub fn add_artifact(&mut self, artifact: Artifact) -> Result<()> {
        artifact.validate()?;
        self.artifacts.insert(artifact.name.clone(), artifact);
        Ok(())
    }

    /// Retrieves an artifact by name
    pub fn get_artifact(&self, name: &str) -> Option<&Artifact> {
        self.artifacts.get(name)
    }

    /// Lists all artifact names
    pub fn list_artifacts(&self) -> Vec<&String> {
        self.artifacts.keys().collect()
    }

    /// Validates all artifacts
    pub fn validate_all(&self) -> Result<()> {
        for artifact in self.artifacts.values() {
            artifact.validate()?;
        }
        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_artifact_creation() {
        let artifact = Artifact::new(
            "test.md".to_string(),
            "# Test Content".to_string(),
            ArtifactType::Documentation,
        );

        assert_eq!(artifact.name, "test.md");
        assert_eq!(artifact.content, "# Test Content");
        assert!(matches!(artifact.artifact_type, ArtifactType::Documentation));
    }

    #[test]
    fn test_artifact_validation() {
        let artifact = Artifact::new(
            "test.md".to_string(),
            "content".to_string(),
            ArtifactType::Documentation,
        );

        assert!(artifact.validate().is_ok());
    }

    #[test]
    fn test_artifact_manager() {
        let mut manager = ArtifactManager::new();
        let artifact = Artifact::new(
            "test.md".to_string(),
            "content".to_string(),
            ArtifactType::Documentation,
        );

        manager.add_artifact(artifact).unwrap();
        assert!(manager.get_artifact("test.md").is_some());
        assert_eq!(manager.list_artifacts().len(), 1);
    }
}