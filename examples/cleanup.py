from universal_sandbox import Sandbox
import os

# Initialize client
# Get Sandbox API Token from https://ai-infra.org/
sandbox = Sandbox(token=os.getenv("SANDBOX_API_TOKEN"))

print("=" * 70)
print("Cleaning up all sandboxes")
print("=" * 70)
print()

# List all sandboxes
sandbox_list = sandbox.sandboxes.list()
print(f"Total sandboxes: {sandbox_list.total}")
print()

if sandbox_list.total == 0:
    print("No sandboxes to delete.")
else:
    print(f"Deleting {sandbox_list.total} sandbox(es)...")
    print()

    # Delete all sandboxes
    for s in sandbox_list.sandboxes:
        print(f"Deleting sandbox: {s.id}")
        print(f"  Provider: {s.provider}")
        print(f"  Type: {s.type}")
        resp = sandbox.sandboxes.delete(s.id)
        print(f"  Response: {resp}")
        print()

    print("=" * 70)
    print("Cleanup completed!")
    print("=" * 70)
