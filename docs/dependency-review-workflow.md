# Dependency Review Workflow Documentation

## Overview
The Dependency Review workflow automatically scans pull requests for dependency changes and security vulnerabilities. It helps maintain security and license compliance by reviewing all dependency modifications.

## Features
- **Vulnerability Scanning**: Detects known security vulnerabilities in dependencies
- **License Compliance**: Enforces allowed/denied license policies
- **Dependency Validation**: Validates syntax and format of dependency files
- **PR Comments**: Automatically posts summary comments on pull requests
- **Multiple Formats**: Supports requirements.txt, setup.py, pyproject.toml, and more

## Configuration

### Workflow File
Located at `.github/workflows/dependency-review.yml`

### Configuration File
Located at `.github/dependency-review-config.yml`

Key settings:
- `fail_on_severity`: Minimum severity level to fail the workflow (default: high)
- `deny_licenses`: List of prohibited licenses
- `allow_licenses`: List of explicitly allowed licenses
- `vulnerability_check`: Enable/disable vulnerability scanning
- `comment_summary_in_pr`: Post summary comments in PRs

## Supported File Types
- `requirements*.txt` - Python requirements files
- `setup.py` - Python setup files
- `pyproject.toml` - Modern Python project configuration
- `setup.cfg` - Python setup configuration
- `Pipfile*` - Pipenv files

## Troubleshooting

### Common Issues

#### 1. Workflow Not Running
- Check if the workflow file has correct YAML syntax
- Verify permissions in repository settings
- Ensure the workflow is enabled in Actions tab

#### 2. "Action Required" Status
- Usually indicates a configuration issue
- Check the workflow logs for specific error messages
- Verify action versions are up to date

#### 3. Permission Errors
- Ensure the workflow has necessary permissions:
  - `contents: read`
  - `pull-requests: read`
  - `security-events: write`

#### 4. License Violations
- Review the deny/allow license lists
- Add exceptions for specific packages if needed
- Update license policy in configuration file

#### 5. Vulnerability Alerts
- Review the specific vulnerabilities found
- Update dependencies to patched versions
- Add temporary exceptions if immediate fixes aren't available

### Debugging Steps

1. **Check Workflow Logs**
   - Go to Actions tab in GitHub
   - Find the failing workflow run
   - Review step-by-step logs

2. **Validate Local Files**

   ```bash
   # Check YAML syntax
   python -c "import yaml; yaml.safe_load(open('.github/workflows/dependency-review.yml'))"
   
   # Validate dependency files
   python -c "
   with open('requirements.txt') as f:
       lines = [l.strip() for l in f if l.strip() and not l.startswith('#')]
   print(f'Found {len(lines)} dependencies')
   "
   ```

3. **Test Configuration**

   ```bash
   # Validate configuration file
   python -c "import yaml; yaml.safe_load(open('.github/dependency-review-config.yml'))"
   ```

## Maintenance

### Updating Action Versions
1. Check for new releases of `actions/dependency-review-action`
2. Update version in workflow file
3. Test with a sample PR

### Updating License Policy
1. Edit `.github/dependency-review-config.yml`
2. Add/remove licenses from allow/deny lists
3. Test changes with a PR that includes dependencies

### Monitoring
- Review workflow runs regularly for failures
- Check for new vulnerability alerts
- Update dependency policies as needed

## Best Practices

1. **Pin Dependency Versions**: Use exact version pins (==) for production dependencies
2. **Regular Updates**: Keep dependencies updated to latest secure versions  
3. **License Audits**: Regularly review license compliance
4. **Security Monitoring**: Monitor for new vulnerability disclosures
5. **Documentation**: Keep dependency changes well documented in PRs

## Contact
For issues with this workflow, check the repository's issue tracker or contact the maintainers.
