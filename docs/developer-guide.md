# Developer Guide

Development guide for contributing to InsightfulPy v0.2.0.

## Development Setup

See [CONTRIBUTING.md](../CONTRIBUTING.md#development-setup) for setup instructions including prerequisites, installation, and pre-commit hooks.

## Architecture Overview

### Module Structure

```
src/insightfulpy/
   __init__.py           # Public API and help functions
   core.py               # Core utilities and imports
   constants.py          # Configuration constants
   eda.py                # Backward compatibility layer
   summary.py            # Summary statistics
   statistics.py         # Statistical calculations
   data_quality.py       # Data quality checks
   visualization.py      # Basic visualizations
   advanced_viz.py       # Pair-wise visualizations
   analysis.py           # Individual column analysis
   comparison.py         # Multi-dataset comparison
```

### Layer Responsibilities

**Core Infrastructure:**

- `core.py`: Environment detection, dependency imports, warning suppression
- `constants.py`: Centralized configuration values
- `__init__.py`: Public API definition, function categorization, help system

**Function Modules:**

- `summary.py`: DataFrame summaries and grouping
- `statistics.py`: Statistical calculations
- `data_quality.py`: Missing values, outliers, data types
- `visualization.py`: Single-variable visualizations
- `advanced_viz.py`: Multi-variable visualizations
- `analysis.py`: Individual column analysis
- `comparison.py`: Multi-dataset operations

**Compatibility Layer:**

- `eda.py`: Import hub for backward compatibility (no implementations)

## Code Organization

### Import Pattern

All function modules follow this pattern:

```python
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union
from .core import *
```

### Type Hints

All functions use type hints:

```python
def detect_outliers(
    data: pd.DataFrame,
    max_display: int = constants.DEFAULT_MAX_DISPLAY_OUTLIERS
) -> pd.DataFrame:
    """Detects outliers using the IQR method."""
    # Implementation
```

### Docstrings

Use concise docstrings:

```python
def mad(data: pd.Series) -> float:
    """Calculate Median Absolute Deviation."""
    result = np.mean(np.abs(data - data.mean()))
    return float(result)
```

## Design Patterns

### 1. Constants-Driven Design

Use constants from `constants.py` instead of magic numbers:

```python
# Good
if data[col].nunique() > constants.DEFAULT_HIGH_CARDINALITY_THRESHOLD:
    print("High cardinality")
```

### 2. Environment Detection

Use `_safe_display()` for DataFrame output (works in Jupyter and terminal):

```python
from .core import _safe_display
_safe_display(df)
```

### 3. Backward Compatibility

Never implement functions in `eda.py`. Only import and re-export from specialized modules.

## Adding New Functions

Three-step pattern for backward compatibility:

1. **Implement** in specialized module (e.g., `statistics.py`)
2. **Import** in `eda.py` and add to `__all__`
3. **Re-export** in `__init__.py` and add to category list

## Testing

Minimum coverage: 80%. Fixtures in `conftest.py`.

```bash
pytest  # All tests
pytest tests/test_statistics.py::test_calc_stats  # Specific test
pytest -n auto  # Parallel
pytest --cov=src/insightfulpy  # Coverage
```

## Code Quality

```bash
black src/ tests/  # Format
isort --profile=black src/ tests/  # Sort imports
flake8 src/ tests/  # Lint
mypy src/  # Type check
pre-commit run --all-files  # Run all checks
```

## Git Workflow

### Commit Message Format

See [CONTRIBUTING.md](../CONTRIBUTING.md#commit-message-format) for commit message conventions.

### Branch Strategy

1. Create feature branch from main
2. Implement changes
3. Run tests and code quality checks
4. Commit with conventional format
5. Push and create pull request

**Branch naming:**

- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring

### Pre-commit Checks

See [CONTRIBUTING.md](../CONTRIBUTING.md#pre-commit-hooks) for pre-commit hook details.

### Pull Request Checklist

Before submitting:

- [ ] All tests pass (`pytest`)
- [ ] Coverage meets 80% threshold
- [ ] Code formatted with Black
- [ ] Imports sorted with isort
- [ ] No linting errors (Flake8)
- [ ] Type hints added (mypy passes)
- [ ] Documentation updated
- [ ] Commit messages follow convention
- [ ] Pre-commit hooks pass

## See Also

- [CONTRIBUTING.md](../CONTRIBUTING.md) - Contribution workflow
- [Configuration](configuration.md) - Constants reference

---

Version: 0.2.0 | Status: Beta | Python: 3.8-3.12

Copyright 2025 dhaneshbb | License: MIT | Homepage: https://github.com/dhaneshbb/insightfulpy
