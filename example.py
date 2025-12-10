from universal_sandbox import Sandbox
import os

# Initialize client
# Get Sandbox API Token from https://ai-infra.org/
sandbox = Sandbox(token=os.getenv("SANDBOX_API_TOKEN"))

# ---------- General sandbox -------------- #

# create a code interpreter sandbox
box = sandbox.code_interpreter.create()
print(f"Sandbox ID: {box.id}")
print(f"Provider: {box.provider}")
print()

# execute code
result = sandbox.code_interpreter.execute(box.id, command="print('Hello, World!')")
print(result.stdout)
print()

# get sandbox info
info = sandbox.sandboxes.get(box.id)
print(f"Status: {info.status}")
print()

# list all sandboxes
sandbox_list = sandbox.sandboxes.list()
print(f"Total: {sandbox_list.total}")
print()

# delete sandbox
for s in sandbox_list.sandboxes:
    resp = sandbox.sandboxes.delete(s.id)
    print(resp)
    print()

# ---------- Basic information -------------- #

# Check API health
health = sandbox.check_health()
print(health.status)
print()

# List regions
regions = sandbox.list_regions()
print(f"Regions: {regions}")
print()

# Get limits
limits = sandbox.get_limits()
print(f"Limits: {limits}")
print()

# ---------- E2B sandbox -------------- #
# Create a code interpreter sandbox
sb = sandbox.code_interpreter.create(provider="e2b", timeout_minutes=1)
print(f"Sandbox ID: {sb.id}")

# Execute code
result = sandbox.sandboxes.execute(sb.id, command="print('Hello, World!')")
print(result.stdout)

# List all sandboxes
sanboxes = sandbox.sandboxes.list()
print(f"Total: {sanboxes.total}")
print()

# Delete sandbox
resp = sandbox.sandboxes.delete(sb.id)
print(resp)
print()


# ---------- Volcengine All-in-One sandbox -------------- #
# Create an all-in-one sandbox (only Volcengine supported)
aio = sandbox.aio.create(provider="volcengine")
print(f"Sandbox ID: {aio.id}")
print(f"Status: {aio.status}")
print(f"vnc url: {aio.urls.vnc_url}")
print(f"mcp url: {aio.urls.mcp_url}")
print(f"api url: {aio.urls.api_url}")
print(f"wss url: {aio.urls.wss_url}")

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

# ---------- AWS: Browser/code-interpreter sandbox -------------- #
# Create a browser sandbox
browser = sandbox.code_interpreter.create(provider="aws")
print(f"Sandbox ID: {browser.id}")
print(f"Status: {browser.status}")

resp = sandbox.code_interpreter.execute(browser.id, command="print('Hello, World!')")
print(resp.stdout)
print()

# Get sandbox info
info = sandbox.sandboxes.get(browser.id)
print(f"Status: {info.status}")

# List all sandboxes
sandbox_list = sandbox.sandboxes.list()
print(f"Total: {sandbox_list.total}")

# Delete sandbox
resp = sandbox.sandboxes.delete(browser.id)
print(resp)