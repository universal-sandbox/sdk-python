from universal_sandbox import Sandbox
import os

# Initialize client
# Get Sandbox API Token from https://ai-infra.org/
sandbox = Sandbox(token=os.getenv("SANDBOX_API_TOKEN"))

# ---------- Volcengine Code Interpreter sandbox -------------- #
# Create a code interpreter sandbox
box = sandbox.code_interpreter.create(provider="volcengine")
print(f"Sandbox ID: {box.id}")
print(f"Provider: {box.provider}")
print()

# Execute code
result = sandbox.sandboxes.execute(box.id, command="echo 'Hello from Volcengine!'")
print(result.stdout)
print()

# Get sandbox info
info = sandbox.sandboxes.get(box.id)
print(f"Status: {info.status}")
print()

# List all sandboxes
sandbox_list = sandbox.sandboxes.list()
print(f"Total: {sandbox_list.total}")
print()

# Delete sandbox
resp = sandbox.sandboxes.delete(box.id)
print(resp)
print()
