from universal_sandbox import Sandbox
import os

# Initialize client
# Get Sandbox API Token from https://ai-infra.org/
sandbox = Sandbox(token=os.getenv("SANDBOX_API_TOKEN"))

# ---------- AWS Code Interpreter sandbox -------------- #
# Create a code interpreter sandbox
box = sandbox.code_interpreter.create(provider="aws")
print(f"Sandbox ID: {box.id}")
print(f"Provider: {box.provider}")
print(f"Status: {box.status}")
print()

# Execute code
result = sandbox.code_interpreter.execute(box.id, command="print('Hello from AWS!')")
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
