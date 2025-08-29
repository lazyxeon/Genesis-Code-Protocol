#!/bin/bash
# LYRA/GCP Rehydration Script
# Regenerates the development environment from this bundle

set -euo pipefail

echo "=== LYRA/GCP Rehydration ==="
echo "Reconstructing development environment..."

# Install Python dependencies if requirements exist
if [ -f "source/requirements.txt" ]; then
    echo "📦 Installing Python dependencies..."
    pip install -r source/requirements.txt
fi

if [ -f "source/requirements-dev.txt" ]; then
    echo "📦 Installing development dependencies..."
    pip install -r source/requirements-dev.txt
fi

# Make scripts executable
if [ -d "source/scripts" ]; then
    echo "🔧 Making scripts executable..."
    chmod +x source/scripts/*.py source/scripts/*.sh 2>/dev/null || true
fi

# Run basic validation if available
if [ -f "source/scripts/validate_workflows.py" ]; then
    echo "✅ Running validation..."
    python source/scripts/validate_workflows.py
fi

echo "✅ Rehydration complete!"
echo "💡 Next steps:"
echo "   - Review docs/ for documentation"
echo "   - Check source/cli_bundle/ for CLI tools"
echo "   - Run source/scripts/ for available utilities"
