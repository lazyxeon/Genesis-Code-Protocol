# .github/workflows/ghcr-build.yml
name: Build & Push (GHCR)

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

permissions:
  contents: read
  packages: write   # <— needed for ghcr push (with GITHUB_TOKEN) 
  id-token: write   # (optional) enables attestations/provenance

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      # QEMU only if you build multi-arch (arm64 + amd64)
      - name: Set up QEMU
        uses: docker/setup-qemu-action@v3

      - name: Set up Buildx
        uses: docker/setup-buildx-action@v3
        # Creates a builder usable by build-push-action. 0

      - name: Login to GHCR
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
        # GHCR supports GITHUB_TOKEN; no PAT needed. 1

      - name: Compute image name (lowercase)
        id: vars
        shell: bash
        run: |
          IMAGE="ghcr.io/${GITHUB_REPOSITORY,,}"
          echo "image=$IMAGE" >> "$GITHUB_OUTPUT"

      - name: Build & Push
        uses: docker/build-push-action@v6
        with:
          context: .
          # If your Dockerfile lives elsewhere, set: file: docker/Dockerfile
          push: true
          # For multi-arch builds (requires QEMU step):
          platforms: linux/amd64,linux/arm64
          tags: |
            ${{ steps.vars.outputs.image }}:latest
            ${{ steps.vars.outputs.image }}:${{ github.sha }}
          # Supply-chain goodies (optional but nice):
          provenance: mode=max        # SLSA provenance attestation
          attests: type=sbom          # SBOM attestation
          # Simple cache to speed up subsequent builds:
          cache-from: type=gha
          cache-to: type=gha,mode=max
        # build-push-action inputs/provenance/attests are documented here. 2