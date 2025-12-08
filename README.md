# Universal Sandbox Python SDK

Python SDK for Universal Sandbox API.

## Installation

```bash
pip install universal-sandbox
```

## Usage

```python
from universal_sandbox import SandboxClient

# Initialize client
client = SandboxClient(
    base_url="https://api.sandbox.ai-infra.org",
    token="your-token",  # optional if auth is disabled
)

# Create a code interpreter sandbox
sandbox = client.create_code_interpreter(
    provider="e2b",
    timeout_minutes=10,
)

# Execute code
result = client.execute(sandbox.id, "print('Hello, World!')")
print(result.stdout)

# Delete sandbox
client.delete_sandbox(sandbox.id)
```

## API Reference

### SandboxClient

- `create_code_interpreter(provider, region, timeout_minutes, metadata)` - Create a code interpreter sandbox
- `create_browser(provider, region, timeout_minutes, metadata)` - Create a browser sandbox
- `create_aio(provider, region, timeout_minutes, metadata)` - Create an all-in-one sandbox
- `get_sandbox(sandbox_id)` - Get sandbox by ID
- `list_sandboxes()` - List all sandboxes
- `delete_sandbox(sandbox_id)` - Delete a sandbox
- `execute(sandbox_id, command, timeout)` - Execute command in sandbox
- `health()` - Check API health
- `get_regions()` - Get available regions
- `get_limits()` - Get resource limits
