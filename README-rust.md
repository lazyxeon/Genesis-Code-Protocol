# Genesis Code Protocol - Rust Implementation

This directory contains the Rust implementation of core Genesis Code Protocol (GCP) functionality, designed to complement the existing Python framework with high-performance components.

## Features

- **Core GCP Types**: Rust implementations of GCP runs, phases, and execution modes
- **Artifact Management**: High-performance artifact creation, validation, and management
- **Gate System**: Automated decision gates for phase transitions and quality control
- **Phase Management**: Lifecycle management for protocol execution flow
- **Runner System**: Deterministic modules for protocol execution
- **Telemetry**: Comprehensive metrics collection and performance tracking
- **Async Support**: Full async/await support for concurrent operations

## Quick Start

Add this to your `Cargo.toml`:

```toml
[dependencies]
genesis-code-protocol-rs = "0.1.0"
```

Basic usage:

```rust
use genesis_code_protocol_rs::{GcpRun, RunMode, StartupMode, RiskTier};

// Create a new GCP run
let mut run = GcpRun::new(
    RunMode::Auto,
    StartupMode::SparkProvided,
    RiskTier::R1,
);

// Add an artifact
run.add_artifact(
    "requirements.md".to_string(),
    "# Requirements\n\nProject requirements...".to_string()
)?;

// Serialize to JSON
let json = run.to_json()?;
println!("GCP Run: {}", json);
```

## Performance Components

The Rust implementation provides high-performance components for:

- Large artifact processing
- Batch operations on multiple artifacts
- Concurrent runner execution
- Real-time telemetry collection

Example of performance-critical operations:

```rust
use genesis_code_protocol_rs::performance;

// Process a large artifact efficiently
let data = vec![1, 3, 2, 5, 4];
let processed = performance::process_large_artifact(&data);

// Batch process multiple artifacts
let artifacts = vec![&data[..], &[9, 7, 8][..]];
let results = performance::batch_process_artifacts(&artifacts);
```

## Building

```bash
# Build the library
cargo build

# Run tests
cargo test

# Run benchmarks
cargo bench

# Build documentation
cargo doc --open
```

## Features

- `default`: Includes async support
- `async`: Enables async/await functionality (requires tokio)

## Architecture

The Rust implementation is organized into several modules:

- `artifacts`: Artifact management and validation
- `gates`: Decision gates and quality control
- `phases`: Phase lifecycle management
- `runners`: Execution modules and registry
- `telemetry`: Performance monitoring and metrics
- `performance`: High-performance operations

## Integration

This Rust library is designed to integrate seamlessly with the Python-based GCP framework, providing:

- JSON serialization compatibility
- Consistent data models
- Performance-critical operations
- Concurrent processing capabilities

## Benchmarks

The library includes comprehensive benchmarks for all major operations:

```bash
# Run all benchmarks
cargo bench

# Run specific benchmark
cargo bench artifact_processing
```

Benchmark results are available in the `target/criterion` directory.

## Contributing

1. Ensure code follows Rust best practices
2. Add tests for new functionality
3. Update benchmarks for performance-critical code
4. Run `cargo clippy` and `cargo fmt` before submitting

## License

MIT License - see the main project LICENSE.md file.