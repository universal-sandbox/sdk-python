from universal_sandbox import Sandbox
import os

# Initialize client
# Get Sandbox API Token from https://ai-infra.org/
sandbox = Sandbox(token=os.getenv("SANDBOX_API_TOKEN"))

# ---------- Volcengine All-in-One sandbox -------------- #
# Create an all-in-one sandbox (Volcengine supported)
aio = sandbox.aio.create(provider="volcengine")
print(f"Sandbox ID: {aio.id}")
print(f"Status: {aio.status}")
print(f"VNC URL: {aio.urls.vnc_url}")
print(f"MCP URL: {aio.urls.mcp_url}")
print(f"API URL: {aio.urls.api_url}")
print(f"WSS URL: {aio.urls.wss_url}")
print()

# Execute code
result = sandbox.sandboxes.execute(aio.id, command="print('Hello from Volcengine AIO!')")
print(result.stdout)
print()

# Get sandbox info
info = sandbox.sandboxes.get(aio.id)
print(f"Status: {info.status}")
print()

# List all sandboxes
sandbox_list = sandbox.sandboxes.list()
print(f"Total: {sandbox_list.total}")
print()

# Delete sandbox
resp = sandbox.sandboxes.delete(aio.id)
print(resp)
print()
