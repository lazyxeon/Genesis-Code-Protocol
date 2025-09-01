#!/bin/bash
# Exit Wizard Bundle Generation Script
# Creates a comprehensive source bundle for LYRA/GCP releases
# Aligned with documentation in Notebooks/Full Runs/Flagship Full Runs/LYRA.md

set -euo pipefail

# Configuration
SEMVER_TAG="${GITHUB_REF_NAME:-v0.0.0}"
# Sanitize tag name for filename
SAFE_TAG=$(echo "$SEMVER_TAG" | sed 's/[^a-zA-Z0-9._-]/_/g')
OUT="lyra-exit-bundle-${SAFE_TAG}.zip"
STAGING_DIR="dist/lyra-exit-bundle"

echo "=== LYRA Exit Wizard Bundle Generation ==="
echo "Version: $SEMVER_TAG"
echo "Output: $OUT"

# Clean and prepare staging
rm -rf dist
mkdir -p "$STAGING_DIR"
mkdir -p "$STAGING_DIR"/{SBOM,provenance,rehydration,docs,source}

echo "📁 Preparing source bundle structure..."

# 1) Copy core source and documentation
echo "📋 Copying core project files..."
cp -r cli_bundle "$STAGING_DIR/source/"
cp -r Documents "$STAGING_DIR/docs/"
cp -r scripts "$STAGING_DIR/source/"
cp -r src "$STAGING_DIR/source/" 2>/dev/null || echo "No src directory found, skipping"

# Copy key project files
cp README.md "$STAGING_DIR/"
cp LICENSE.md "$STAGING_DIR/" 2>/dev/null || echo "No LICENSE.md found"
cp CHANGELOG.md "$STAGING_DIR/" 2>/dev/null || echo "No CHANGELOG.md found"
cp requirements*.txt "$STAGING_DIR/source/" 2>/dev/null || echo "No requirements files found"
cp setup.py "$STAGING_DIR/source/" 2>/dev/null || echo "No setup.py found"

# 2) Generate rehydration script
echo "🔄 Creating rehydration script..."
cat > "$STAGING_DIR/rehydrate.sh" << 'EOF'
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
EOF

chmod +x "$STAGING_DIR/rehydrate.sh"

# 3) Generate basic SBOMs (using built-in tools if available)
echo "📊 Generating Software Bill of Materials..."
if command -v syft >/dev/null 2>&1; then
    syft dir:. -o spdx-json > "$STAGING_DIR/SBOM/sbom.spdx.json" 2>/dev/null || echo "SBOM generation failed, creating placeholder"
else
    # Create a basic SBOM placeholder
    cat > "$STAGING_DIR/SBOM/sbom.spdx.json" << EOF
{
  "spdxVersion": "SPDX-2.3",
  "dataLicense": "CC0-1.0",
  "SPDXID": "SPDXRef-DOCUMENT",
  "name": "LYRA-Exit-Bundle-${SEMVER_TAG}",
  "documentNamespace": "https://github.com/lazyxeon/Genesis-Code-Protocol/bundle/${SEMVER_TAG}",
  "creationInfo": {
    "created": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
    "creators": ["Tool: make_exit_bundle.sh"]
  },
  "packages": [
    {
      "SPDXID": "SPDXRef-Package",
      "name": "LYRA-Exit-Bundle",
      "downloadLocation": "NOASSERTION",
      "filesAnalyzed": false,
      "copyrightText": "NOASSERTION"
    }
  ]
}
EOF
fi

# 4) Generate basic SLSA provenance
echo "🔐 Generating SLSA provenance..."
cat > "$STAGING_DIR/provenance/slsa_provenance.json" << EOF
{
  "_type": "https://in-toto.io/Statement/v0.1",
  "predicateType": "https://slsa.dev/provenance/v0.2",
  "subject": [
    {
      "name": "$OUT",
      "digest": {
        "sha256": "placeholder-will-be-calculated-after-zip"
      }
    }
  ],
  "predicate": {
    "builder": {
      "id": "https://github.com/lazyxeon/Genesis-Code-Protocol/.github/workflows/release-bundle.yml"
    },
    "buildType": "https://github.com/Attestations/GitHubActionsWorkflow@v1",
    "invocation": {
      "configSource": {
        "uri": "git+https://github.com/lazyxeon/Genesis-Code-Protocol.git",
        "digest": {
          "sha1": "$(git rev-parse HEAD 2>/dev/null || echo 'unknown')"
        }
      }
    },
    "metadata": {
      "buildInvocationId": "${GITHUB_RUN_ID:-unknown}",
      "buildStartedOn": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
      "completeness": {
        "parameters": true,
        "environment": false,
        "materials": false
      },
      "reproducible": false
    },
    "materials": [
      {
        "uri": "git+https://github.com/lazyxeon/Genesis-Code-Protocol.git",
        "digest": {
          "sha1": "$(git rev-parse HEAD 2>/dev/null || echo 'unknown')"
        }
      }
    ]
  }
}
EOF

# 5) Create manifest with metadata
echo "📋 Creating bundle manifest..."
cat > "$STAGING_DIR/MANIFEST.json" << EOF
{
  "bundle_version": "$SEMVER_TAG",
  "created": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "creator": "LYRA Exit Wizard",
  "description": "Comprehensive source bundle for LYRA/Genesis Code Protocol",
  "contents": {
    "source/": "Core source code and CLI tools",
    "docs/": "Project documentation",
    "SBOM/": "Software Bill of Materials",
    "provenance/": "Supply chain provenance attestations",
    "rehydration/": "Scripts for environment reconstruction",
    "rehydrate.sh": "Main rehydration script"
  },
  "usage": "Run ./rehydrate.sh to reconstruct development environment",
  "repository": "https://github.com/lazyxeon/Genesis-Code-Protocol",
  "commit": "$(git rev-parse HEAD 2>/dev/null || echo 'unknown')",
  "standards": [
    "SLSA Build Provenance v0.2",
    "SPDX-2.3",
    "SemVer 2.0.0"
  ]
}
EOF

# 6) Create comprehensive ZIP bundle
echo "📦 Creating final bundle..."
( cd dist && zip -r "../$OUT" "lyra-exit-bundle" -x "*.git*" "*.DS_Store" "*/__pycache__/*" )

# 7) Generate checksums
echo "🔍 Generating checksums..."
mkdir -p dist/checksums
sha256sum "$OUT" > "dist/checksums/SHA256SUMS.txt"
echo "Bundle created: $OUT"
echo "Size: $(du -h "$OUT" | cut -f1)"
echo "SHA256: $(cat dist/checksums/SHA256SUMS.txt)"

echo "✅ Exit Wizard bundle generation complete!"
