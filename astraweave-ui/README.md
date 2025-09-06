# AstraWeave UI

A Rust UI library using egui with wgpu backend.

## Overview

This crate demonstrates the proper way to fix the common import syntax errors when working with egui and related crates.

## Fixed Issues

### 1. Import Syntax Errors

**Problem**: Rust compilation errors due to incorrect import syntax:
```rust
// ❌ WRONG - This causes compilation errors
use egui-wgpu::renderer::{Renderer as EguiRenderer, ScreenDescriptor};
use egui-winit::State as EguiWinitState;
```

**Solution**: Use underscores in import paths (even though dependencies use hyphens):
```rust
// ✅ CORRECT - Use underscores in import paths
use egui_wgpu::{Renderer as EguiRenderer, ScreenDescriptor};
use egui_winit::State as EguiWinitState;
```

### 2. UiData Clone Implementation

**Problem**: Struct with `#[derive(Clone)]` containing mutable references:
```rust
// ❌ WRONG - Cannot clone structs with mutable references
#[derive(Clone, Debug)]
pub struct UiData<'a> {
    pub player_stats: &'a Stats,
    pub player_pos: Vec3,
    pub inventory: &'a mut Inventory,  // Cannot be cloned!
}
```

**Solution 1**: Remove Clone derive (simplest approach):
```rust
// ✅ CORRECT - Remove Clone if not needed
#[derive(Debug)]
pub struct UiData<'a> {
    pub player_stats: &'a Stats,
    pub player_pos: Vec3,
    pub inventory: &'a mut Inventory,
}
```

**Solution 2**: Use interior mutability if Clone is required:
```rust
// ✅ ALTERNATIVE - Use RefCell for interior mutability
#[derive(Clone, Debug)]
pub struct UiDataCloneable<'a> {
    pub player_stats: &'a Stats,
    pub player_pos: Vec3,
    pub inventory: &'a RefCell<Inventory>,
}
```

## Key Points

1. **Dependency Names vs Import Paths**: 
   - In `Cargo.toml`: Use hyphens (`egui-wgpu = "0.28"`)
   - In `use` statements: Use underscores (`use egui_wgpu::...`)

2. **Clone and Mutable References**: 
   - Mutable references (`&mut T`) cannot be cloned
   - Either remove `Clone` derive or use interior mutability patterns

3. **API Changes**: 
   - The egui-wgpu API has evolved; private modules like `renderer` are no longer accessible
   - Use the public API directly: `egui_wgpu::Renderer`

## Dependencies

```toml
[dependencies]
egui = "0.28"
egui-wgpu = "0.28"
egui-winit = "0.28"
wgpu = "0.20"
winit = "0.29"
glam = "0.28"
```

## Features

- `clone-ui-data`: Enables the cloneable UiData variant using RefCell

## Testing

Run tests with:
```bash
cargo test                          # Basic tests
cargo test --features clone-ui-data # Test with cloneable variant
```