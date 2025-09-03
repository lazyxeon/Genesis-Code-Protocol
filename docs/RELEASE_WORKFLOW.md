# Release Workflow Documentation

## Overview

The Genesis Code Protocol repository includes a comprehensive release workflow that automates the creation, signing, and verification of release artifacts following security best practices and the Exit Wizard pattern.

## Workflows

### 1. `release-complete.yml` (Recommended)

This is the primary workflow that handles the complete release process in two coordinated jobs:

#### Features
- **Bundle Creation**: Creates release bundles with SBOM generation
- **Cryptographic Signing**: Signs all artifacts using Sigstore (keyless signing)
- **Transparency Log**: Automatically registers signatures in Sigstore Rekor
- **RFC 3161 Timestamps**: Generates timestamps for temporal verification
- **Exit Wizard Integration**: Creates manifest following GCP Exit Wizard pattern
- **Comprehensive Verification**: Verifies all signatures before upload

#### Triggers
- Automatically on release publication
- Manual trigger via `workflow_dispatch`

### 2. `release-bundle.yml` (Legacy)

Creates and uploads release bundles with SBOMs.

### 3. `release-sign.yml` (Legacy)

Signs existing release artifacts. Enhanced with better coordination and verification.

## Security Features

### Sigstore Integration
- **Keyless Signing**: No need to manage private keys
- **Transparency Log**: All signatures are publicly verifiable
- **Certificate Transparency**: Uses OIDC identity for signing

### SBOM Generation
- **SPDX Format**: Industry standard Software Bill of Materials
- **CycloneDX Format**: Alternative SBOM format for compatibility
- **Comprehensive Coverage**: Covers all bundled components

### Verification
- **Signature Verification**: All signatures verified before upload
- **Integrity Checking**: SHA-256 checksums for all artifacts
- **Transparency Verification**: Rekor inclusion proof validation

## Usage

### Automatic Release
1. Create a new release in GitHub
2. Publish the release
3. The workflow automatically triggers and processes all artifacts

### Manual Trigger
1. Go to Actions → "Complete Release Process"
2. Click "Run workflow"
3. Select the branch/tag
4. Run the workflow

## Artifacts Generated

### Release Bundle
- `GCP_{TAG}_Field_Kit.zip` - Main release bundle
- `sbom.spdx.json` - SPDX Software Bill of Materials
- `sbom.cdx.json` - CycloneDX Software Bill of Materials
- `SHA256SUMS.txt` - Checksums for all artifacts

### Signatures
- `{artifact}.sigstore` - Sigstore signature bundles
- `{artifact}.sig` - Traditional signature files

### Timestamps (when available)
- `{artifact}.tsr` - RFC 3161 timestamp responses

### Manifests
- `EXIT_WIZARD_MANIFEST.json` - Exit Wizard pattern manifest
- `SIGNING_SUMMARY.md` - Human-readable signing summary

## Verification Instructions

### Using Cosign (Recommended)

```bash
# Install cosign
curl -O -L "https://github.com/sigstore/cosign/releases/latest/download/cosign-linux-amd64"
sudo mv cosign-linux-amd64 /usr/local/bin/cosign
sudo chmod +x /usr/local/bin/cosign

# Verify an artifact
cosign verify-blob --bundle <artifact>.sigstore <artifact>
```

### Using Traditional Tools

```bash
# Verify with openssl (if traditional signatures are used)
openssl dgst -sha256 -verify pubkey.pem -signature <artifact>.sig <artifact>
```

## Exit Wizard Integration

This workflow implements the Genesis Code Protocol Exit Wizard pattern:

- ✅ **Reproducible**: All artifacts include SBOMs and provenance
- ✅ **Verifiable**: Cryptographic signatures with transparency log
- ✅ **Timestamped**: RFC 3161 timestamps for temporal verification  
- ✅ **Transparent**: Public transparency log via Sigstore Rekor
- ✅ **Auditable**: Comprehensive manifest and signing summary

## Troubleshooting

### Common Issues

1. **Workflow fails on artifact download**
   - Check if release exists and is published
   - Verify workflow permissions
   - Check for race conditions between workflows

2. **Signing fails**
   - Verify Cosign installation step
   - Check OIDC token permissions
   - Ensure artifacts exist and are accessible

3. **Timestamp creation fails**
   - This is non-fatal; workflow continues without timestamps
   - May be due to TSA service availability
   - Check network connectivity to timestamp authorities

### Manual Recovery

If the workflow fails, you can:

1. Re-run the failed workflow
2. Use the individual workflows (`release-bundle.yml`, `release-sign.yml`)
3. Manually sign artifacts using the provided scripts

## Security Considerations

- All signing is keyless using OIDC identity
- Signatures are publicly verifiable via transparency log
- No secret keys stored in repository
- All artifacts include integrity checks
- Timestamps provide temporal proof of signing

## Dependencies

- GitHub Actions environment
- Cosign (automatically installed)
- Anchore SBOM Action
- OpenSSL (for timestamps)
- Python 3 (for manifest generation)
