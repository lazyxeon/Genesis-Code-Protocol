#!/usr/bin/env python3
"""Test script for release bundle workflow."""

import os
import subprocess
import tempfile
import zipfile
import json
from pathlib import Path

def test_bundle_script():
    """Test the make_exit_bundle.sh script."""
    print("🧪 Testing make_exit_bundle.sh script...")
    
    # Run the script
    result = subprocess.run(['./scripts/make_exit_bundle.sh'], 
                          capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ Script failed: {result.stderr}")
        return False
    
    # Check if bundle was created
    bundle_files = list(Path('.').glob('lyra-exit-bundle-*.zip'))
    if not bundle_files:
        print("❌ No bundle file created")
        return False
    
    bundle_file = bundle_files[0]
    print(f"✅ Bundle created: {bundle_file}")
    
    # Test bundle contents
    with zipfile.ZipFile(bundle_file, 'r') as zip_ref:
        contents = zip_ref.namelist()
        
        required_files = [
            'lyra-exit-bundle/rehydrate.sh',
            'lyra-exit-bundle/MANIFEST.json', 
            'lyra-exit-bundle/SBOM/sbom.spdx.json',
            'lyra-exit-bundle/provenance/slsa_provenance.json'
        ]
        
        for req_file in required_files:
            if req_file not in contents:
                print(f"❌ Missing required file in bundle: {req_file}")
                return False
            print(f"✅ Found: {req_file}")
        
        # Test MANIFEST.json structure
        try:
            with zip_ref.open('lyra-exit-bundle/MANIFEST.json') as f:
                manifest = json.load(f)
                required_keys = ['bundle_version', 'created', 'creator', 'contents']
                for key in required_keys:
                    if key not in manifest:
                        print(f"❌ Missing key in manifest: {key}")
                        return False
                print(f"✅ Valid manifest structure")
        except Exception as e:
            print(f"❌ Invalid manifest JSON: {e}")
            return False
    
    print("✅ Bundle script test passed!")
    return True

def test_rehydration():
    """Test the rehydration process."""
    print("🧪 Testing rehydration process...")
    
    bundle_files = list(Path('.').glob('lyra-exit-bundle-*.zip'))
    if not bundle_files:
        print("❌ No bundle file found for rehydration test")
        return False
    
    bundle_file = bundle_files[0]
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract bundle
        with zipfile.ZipFile(bundle_file, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        bundle_dir = Path(temp_dir) / 'lyra-exit-bundle'
        if not bundle_dir.exists():
            print("❌ Bundle directory not found after extraction")
            return False
        
        # Test rehydrate script exists and is executable
        rehydrate_script = bundle_dir / 'rehydrate.sh'
        if not rehydrate_script.exists():
            print("❌ rehydrate.sh not found")
            return False
        
        # Make executable (zip might not preserve permissions)
        os.chmod(rehydrate_script, 0o755)
        
        if not os.access(rehydrate_script, os.X_OK):
            print("❌ rehydrate.sh not executable after chmod")
            return False
        
        print("✅ Rehydration script found and executable")
        
        # Test script syntax (dry run)
        result = subprocess.run(['bash', '-n', str(rehydrate_script)], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Rehydration script has syntax errors: {result.stderr}")
            return False
        
        print("✅ Rehydration script syntax valid")
    
    print("✅ Rehydration test passed!")
    return True

def test_workflow_syntax():
    """Test workflow file syntax."""
    print("🧪 Testing workflow file syntax...")
    
    workflow_file = Path('.github/workflows/release-bundle.yml')
    if not workflow_file.exists():
        print("❌ release-bundle.yml workflow not found")
        return False
    
    # Test YAML syntax
    try:
        import yaml
        with open(workflow_file, 'r') as f:
            content = f.read()
            workflow_data = yaml.safe_load(content)
        
        if workflow_data is None:
            print("❌ Failed to parse workflow YAML")
            return False
        
        # Check basic structure (handle YAML boolean parsing quirk for 'on')
        required_keys = ['name', 'jobs']
        on_key = 'on' if 'on' in workflow_data else True  # YAML may parse 'on' as boolean True
        
        for key in required_keys:
            if key not in workflow_data:
                print(f"❌ Missing key in workflow: {key}")
                return False
        
        if on_key not in workflow_data:
            print("❌ Missing 'on' trigger in workflow")
            return False
        
        if 'bundle' not in workflow_data['jobs']:
            print("❌ Missing 'bundle' job in workflow")
            return False
        
        print("✅ Workflow syntax valid")
        
    except ImportError:
        print("⚠️ PyYAML not available, checking basic YAML structure...")
        with open(workflow_file, 'r') as f:
            content = f.read()
            if 'name:' not in content or 'on:' not in content or 'jobs:' not in content:
                print("❌ Basic workflow structure missing")
                return False
        print("✅ Basic workflow structure present")
    except Exception as e:
        print(f"❌ Workflow syntax error: {e}")
        return False
    
    print("✅ Workflow test passed!")
    return True

def main():
    """Run all tests."""
    print("🚀 Starting release bundle workflow tests...\n")
    
    tests = [
        test_bundle_script,
        test_rehydration, 
        test_workflow_syntax
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()  # Blank line between tests
        except Exception as e:
            print(f"❌ Test failed with exception: {e}\n")
    
    print(f"📊 Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("💥 Some tests failed!")
        return 1

if __name__ == '__main__':
    exit(main())