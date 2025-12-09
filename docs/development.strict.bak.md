# Development Guidelines

## Test-Driven Development (MANDATORY)

This project strictly follows TDD principles:

1. **Write tests first** - All features must have failing tests before implementation
2. **Real integrations only** - No mocks for integration tests
3. **Commit tests before code** - Tests are committed separately from implementation
4. **Minimal implementation** - Write only enough code to pass tests
5. **Refactor with confidence** - Use passing tests to guide refactoring

## Test Structure

- `tests/unit/` - Fast, isolated unit tests
- `tests/integration/` - Tests with real external dependencies
- Coverage minimum: 80%

## Forbidden Patterns

- Mock data generation for integration tests
- Simulated API responses
- Dummy database connections
- Placeholder implementations
- Tests that pass without real integration

## MVP Definition

Each feature must have:
1. Clear, testable goal
2. Integration test with real connections
3. Error handling for actual failure modes
4. No feature is complete until integration test passes

## Running Tests

```bash
# Run all tests
pytest

# Run only unit tests
pytest -m unit

# Run only integration tests
pytest -m integration

# Generate coverage report
pytest --cov=lit_agent --cov-report=html
```

## Documentation

Documentation is auto-generated from docstrings. Use Google-style docstrings:

```python
def extract_references(text: str) -> list[str]:
    """Extract academic references from text.

    Args:
        text: Input text containing references

    Returns:
        List of extracted reference strings

    Raises:
        ValueError: If text is empty or invalid
    """
```