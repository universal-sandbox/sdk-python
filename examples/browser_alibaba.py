from universal_sandbox import Sandbox
import os

# Initialize client
# Get Sandbox API Token from https://ai-infra.org/
sandbox = Sandbox(token=os.getenv("SANDBOX_API_TOKEN"))

# ---------- Alibaba Browser sandbox -------------- #
# Create a browser sandbox
browser = sandbox.browser.create(provider="alibaba", region="cn-hangzhou")
print(f"Sandbox ID: {browser.id}")
print(f"Status: {browser.status}")
print()

# Execute command
result = sandbox.sandboxes.execute(browser.id, command="echo 'Hello from Alibaba Browser!'")
print(result.stdout)
print()

# Get sandbox info
info = sandbox.sandboxes.get(browser.id)
print(f"Status: {info.status}")
print()

# List all sandboxes
sandbox_list = sandbox.sandboxes.list()
print(f"Total: {sandbox_list.total}")
print()

# Delete sandbox
resp = sandbox.sandboxes.delete(browser.id)
print(resp)
print()
