# Dependency Review Workflow Fix

## Issues Identified

After analyzing the workflow logs, I found several issues with the dependency review configuration:

1. **Inconsistent parameter naming**: The configuration was using underscores (`_`) in parameter names instead of hyphens (`-`), which is required by the GitHub action.

2. **Invalid `deny_packages` format**: The configuration was using an object structure for `deny_packages` when a string array was expected.

3. **Incorrect `allow_packages` format**: The configuration for allowing specific packages was not in the format expected by the action.

## Changes Made

### 1. Fixed Parameter Naming

Changed all parameter names to use hyphens instead of underscores:
- `fail_on_severity` → `fail-on-severity`
- `deny_licenses` → `deny-licenses`
- `allow_licenses` → `allow-licenses`
- `vulnerability_check` → `vulnerability-check`
- `license_check` → `license-check`
- `comment_summary_in_pr` → `comment-summary-in-pr`
- `warn_only` → `warn-only`

### 2. Fixed `deny-packages` Format

Changed from:
```yaml
deny_packages:
  - scope: "*"
    name: "malicious-package-*"
```

To:
```yaml
deny-packages:
  - "malicious-package-*"
```

### 3. Fixed Package Allowlist Format

Changed from:
```yaml
allow_packages:
  - scope: "python"
    name: "setuptools"
  - scope: "python"
    name: "pip"
  - scope: "python"
    name: "wheel"
```

To:
```yaml
allow-dependencies-licenses:
  - package: setuptools
    license: MIT
  - package: pip
    license: MIT
  - package: wheel
    license: MIT
```

### 4. Fixed Python Configuration Keys

Changed Python configuration keys to use hyphens:
- `ignore_dev_dependencies` → `ignore-dev-dependencies`
- `check_requirements_files` → `check-requirements-files`

## Expected Outcome

These changes should resolve the workflow failures by ensuring:

1. All parameter names match the expected format for the GitHub action
2. The `deny-packages` configuration uses the correct format
3. The package allowlist uses the correct parameter name and structure
4. All configuration keys follow a consistent naming convention with hyphens

The workflow should now run successfully without the previous errors.