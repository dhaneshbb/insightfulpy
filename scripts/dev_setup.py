#!/usr/bin/env python3
"""
Development setup script for InsightfulPy.
This script helps set up the development environment.
"""

import os
import sys
import subprocess
import argparse


def run_command(command, description=""):
    """Run a command and print the result."""
    if description:
        print(f"\n{description}")
        print("-" * len(description))
    
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✓ Success")
        if result.stdout:
            print(result.stdout)
    else:
        print("✗ Failed")
        if result.stderr:
            print(result.stderr)
        return False
    return True


def install_dev_dependencies():
    """Install development dependencies."""
    return run_command(
        "pip install -e .[dev]",
        "Installing development dependencies"
    )


def run_tests():
    """Run the test suite."""
    return run_command(
        "pytest tests/ -v --cov=insightfulpy",
        "Running test suite"
    )


def format_code():
    """Format code with Black."""
    return run_command(
        "black src/insightfulpy/",
        "Formatting code with Black"
    )


def lint_code():
    """Lint code with flake8."""
    return run_command(
        "flake8 src/insightfulpy --max-line-length=88 --extend-ignore=E203,W503",
        "Linting code with flake8"
    )


def build_package():
    """Build the package."""
    return run_command(
        "python -m build",
        "Building package"
    )


def check_package():
    """Check package with twine."""
    return run_command(
        "twine check dist/*",
        "Checking package with twine"
    )


def clean_build():
    """Clean build artifacts."""
    commands = [
        "rm -rf build/",
        "rm -rf dist/", 
        "rm -rf *.egg-info/",
        "find . -name __pycache__ -type d -exec rm -rf {} +",
        "find . -name '*.pyc' -delete"
    ]
    
    for cmd in commands:
        run_command(cmd)
    
    print("✓ Build artifacts cleaned")


def setup_pre_commit():
    """Set up pre-commit hooks."""
    commands = [
        "pip install pre-commit",
        "pre-commit install"
    ]
    
    for cmd in commands:
        if not run_command(cmd):
            return False
    return True


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="InsightfulPy development setup")
    parser.add_argument(
        'action',
        choices=[
            'install', 'test', 'format', 'lint', 'build', 
            'check', 'clean', 'precommit', 'all'
        ],
        help="Action to perform"
    )
    
    args = parser.parse_args()
    
    print("InsightfulPy Development Setup")
    print("=" * 30)
    
    if args.action == 'install':
        install_dev_dependencies()
    elif args.action == 'test':
        run_tests()
    elif args.action == 'format':
        format_code()
    elif args.action == 'lint':
        lint_code()
    elif args.action == 'build':
        build_package()
    elif args.action == 'check':
        check_package()
    elif args.action == 'clean':
        clean_build()
    elif args.action == 'precommit':
        setup_pre_commit()
    elif args.action == 'all':
        print("Running complete development workflow...")
        success = True
        success &= install_dev_dependencies()
        success &= format_code()
        success &= lint_code()
        success &= run_tests()
        success &= build_package()
        success &= check_package()
        
        if success:
            print("\n✓ All checks passed! Package is ready for release.")
        else:
            print("\n✗ Some checks failed. Please review the output above.")
            sys.exit(1)


if __name__ == "__main__":
    main()