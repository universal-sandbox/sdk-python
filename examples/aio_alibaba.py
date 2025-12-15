"""Example of using Alibaba Cloud all-in-one (AIO) sandbox.

This example demonstrates how to use the Alibaba Cloud AIO sandbox
which combines code interpretation, browser automation, and file operations.

Environment Variables Required:
    SANDBOX_API_TOKEN: Get from https://ai-infra.org/

Supported Regions:
    - cn-hangzhou (Hangzhou, China) - default
    - cn-shenzhen (Shenzhen, China)
    - cn-beijing (Beijing, China)
    - cn-shanghai (Shanghai, China)
    - ap-southeast-1 (Singapore)
"""

from universal_sandbox import Sandbox
import os

# Initialize client
# Get Sandbox API Token from https://ai-infra.org/
sandbox = Sandbox(token=os.getenv("SANDBOX_API_TOKEN"))


# Example 1: AIO - Create and Execute
print("=" * 70)
print("Example 1: AIO - Create and Execute Code")
print("=" * 70)

# Create an AIO sandbox
aio = sandbox.aio.create(provider="alibaba", region="cn-hangzhou", timeout=10)
print(f"Sandbox ID: {aio.id}")
print(f"Provider: {aio.provider}")
print(f"Status: {aio.status}")
print()

# Display access URLs
print("Access URLs:")
print(f"  VNC URL: {aio.urls.vnc_url}")
print(f"  MCP URL: {aio.urls.mcp_url}")
print(f"  API URL: {aio.urls.api_url}")
print(f"  WSS URL: {aio.urls.wss_url}")
print()

# Execute Python code
result = sandbox.sandboxes.execute(aio.id, command="print('Hello from Alibaba Cloud AIO!')")
print(result.stdout)
print()

# Get sandbox info
info = sandbox.sandboxes.get(aio.id)
print(f"Sandbox Status: {info.status}")
print()

# Delete sandbox
sandbox.sandboxes.delete(aio.id)
print("Sandbox deleted")
print()


# Example 2: AIO - List and Check Health
print("=" * 70)
print("Example 2: List Sandboxes and Check Health")
print("=" * 70)

# Check API health
health = sandbox.check_health()
print(f"API Status: {health.status}")
print()

# List all sandboxes
sandbox_list = sandbox.sandboxes.list()
print(f"Total sandboxes: {sandbox_list.total}")
print()


# Example 3: List Regions
print("=" * 70)
print("Example 3: List Available Regions")
print("=" * 70)

regions = sandbox.list_regions()
print(f"Regions: {regions}")
print()

# Example 4: Get Limits
print("=" * 70)
print("Example 4: Get Account Limits")
print("=" * 70)

limits = sandbox.get_limits()
print(f"Limits: {limits}")
print()
