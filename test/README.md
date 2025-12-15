# Universal Sandbox Python SDK Tests

This directory contains pytest-based test cases for the Universal Sandbox Python SDK.

## Prerequisites

1. **Install pytest**:
   ```bash
   pip install pytest pytest-timeout pytest-cov
   ```

2. **Set environment variable**:
   ```bash
   export SANDBOX_API_TOKEN="your-token-here"
   ```
   Get your token from: https://ai-infra.org/

## Running Tests

### Run all tests
```bash
cd /Users/zzxwill/Programming/go/src/ai-infra/sdk-python
pytest test/
```

### Run specific test file
```bash
pytest test/test_code_interpreter_e2b.py
pytest test/test_aio_alibaba.py
```

### Run tests by provider
```bash
# E2B tests
pytest test/test_code_interpreter_e2b.py

# AWS tests
pytest test/test_code_interpreter_aws.py

# Alibaba tests
pytest test/test_code_interpreter_alibaba.py test/test_browser_alibaba.py test/test_aio_alibaba.py

# Volcengine tests
pytest test/test_code_interpreter_volcengine.py test/test_browser_volcengine.py test/test_aio_volcengine.py
```

### Run tests by category using markers
```bash
# Code interpreter tests
pytest -m code_interpreter

# Browser tests
pytest -m browser

# AIO tests
pytest -m aio

# API tests
pytest -m api
```

### Run with verbose output
```bash
pytest -v test/
```

### Run with coverage report
```bash
pytest --cov=universal_sandbox --cov-report=html --cov-report=term test/
```

### Run specific test function
```bash
pytest test/test_code_interpreter_e2b.py::test_e2b_code_interpreter_create_and_execute
```

## Test Structure

- **conftest.py**: Shared fixtures and test configuration
  - `sandbox_client`: Session-scoped Sandbox client
  - `cleanup_sandboxes`: Function-scoped fixture for automatic cleanup

- **test_code_interpreter_*.py**: Code interpreter sandbox tests
- **test_browser_*.py**: Browser sandbox tests
- **test_aio_*.py**: All-in-one sandbox tests
- **test_api_basic.py**: Basic API functionality tests
- **test_cleanup.py**: Cleanup functionality tests

## Test Fixtures

### `sandbox_client`
Session-scoped fixture that creates a Sandbox client using `SANDBOX_API_TOKEN`.

### `cleanup_sandboxes`
Function-scoped fixture that automatically deletes sandboxes created during tests.

Usage:
```python
def test_example(sandbox_client, cleanup_sandboxes):
    box = sandbox_client.code_interpreter.create(provider="e2b")
    cleanup_sandboxes(box.id)  # Will be deleted after test
    # ... test code ...
```

## Cleanup

After running all tests, you can clean up any remaining sandboxes:
```bash
pytest test/test_cleanup.py::test_cleanup_all_sandboxes
```

Or run the cleanup example:
```bash
python examples/cleanup.py
```

## Notes

- Tests automatically clean up created sandboxes using the `cleanup_sandboxes` fixture
- Tests require valid `SANDBOX_API_TOKEN` environment variable
- Some tests may take longer depending on provider response times
- Failed sandbox deletions are logged but don't fail the test cleanup
