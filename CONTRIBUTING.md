# Contributing to InsightfulPy

Guidelines for contributing to InsightfulPy.

## Getting Started

### Prerequisites

- Python 3.8+
- Git
- pip

### Fork and Clone

```bash
# Fork on GitHub, then clone
git clone https://github.com/YOUR_USERNAME/insightfulpy.git
cd insightfulpy

# Add upstream remote
git remote add upstream https://github.com/dhaneshbb/insightfulpy.git
```

## Development Setup

```bash
# Install with development dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

Pre-commit hooks run Black, isort, mypy, Flake8, and file checks automatically.

See [Developer Guide](docs/developer-guide.md#development-setup) for detailed instructions.

## Contributing Workflow

### Reporting Bugs

Check existing issues first, then use [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md).

### Suggesting Features

Use [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md).

### Code Contributions

```bash
# Create feature branch
git checkout -b feature/description

# Make changes and add tests
# Run quality checks
pre-commit run --all-files

# Run tests
pytest

# Commit with conventional format
git commit -m "feat: add new function"

# Push and create pull request
git push origin feature/description
```

## Code Standards

### Quality Checks

```bash
pre-commit run --all-files
```

### Testing

All contributions require tests with minimum 80% coverage:

```bash
pytest
```

### Commit Message Format

Use conventional commit format: `<type>: <description>`

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation
- `style` - Code formatting
- `refactor` - Code refactoring
- `test` - Tests
- `chore` - Build/tooling

**Examples:**
```
feat: add median absolute deviation function
fix: handle empty DataFrames in detect_outliers
docs: update API reference for batch functions
```

See [Developer Guide](docs/developer-guide.md) for architecture patterns, testing guidelines, and code quality details.

## Pull Request Checklist

Use [Pull Request Template](.github/pull_request_template.md) and ensure:

- [ ] Tests pass with 80% coverage
- [ ] Pre-commit hooks pass
- [ ] Documentation updated
- [ ] Commit messages follow convention

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
