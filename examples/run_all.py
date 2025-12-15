#!/usr/bin/env python
"""Run all example scripts in sequence."""

import os
import subprocess
import sys
from pathlib import Path

# Get the examples directory
examples_dir = Path(__file__).parent

# List of example files to run (in order)
examples = [
    "code_interpreter_e2b.py",
    "code_interpreter_aws.py",
    "code_interpreter_alibaba.py",
    "code_interpreter_volcengine.py",
    "browser_alibaba.py",
    "browser_volcengine.py",
    "aio_alibaba.py",
    "aio_volcengine.py",
    "cleanup.py",  # Clean up all sandboxes at the end
]

print("=" * 80)
print("Running all Universal Sandbox examples")
print("=" * 80)
print()

failed_examples = []
successful_examples = []

for example in examples:
    example_path = examples_dir / example

    if not example_path.exists():
        print(f"⚠️  Skipping {example} (file not found)")
        continue

    print(f"\n{'=' * 80}")
    print(f"Running: {example}")
    print(f"{'=' * 80}\n")

    try:
        result = subprocess.run(
            [sys.executable, str(example_path)],
            cwd=examples_dir,
            capture_output=False,
            text=True,
            timeout=60  # 60 second timeout per example
        )

        if result.returncode == 0:
            successful_examples.append(example)
            print(f"\n✓ {example} completed successfully")
        else:
            failed_examples.append(example)
            print(f"\n✗ {example} failed with exit code {result.returncode}")

    except subprocess.TimeoutExpired:
        failed_examples.append(example)
        print(f"\n✗ {example} timed out (>60s)")

    except KeyboardInterrupt:
        print(f"\n\n⚠️  Interrupted by user")
        sys.exit(1)

    except Exception as e:
        failed_examples.append(example)
        print(f"\n✗ {example} failed with error: {e}")

# Summary
print(f"\n\n{'=' * 80}")
print("Summary")
print(f"{'=' * 80}")
print(f"Successful: {len(successful_examples)}/{len(examples)}")
print(f"Failed: {len(failed_examples)}/{len(examples)}")

if successful_examples:
    print(f"\n✓ Successful examples:")
    for example in successful_examples:
        print(f"  - {example}")

if failed_examples:
    print(f"\n✗ Failed examples:")
    for example in failed_examples:
        print(f"  - {example}")

print(f"\n{'=' * 80}")

# Exit with error code if any failed
sys.exit(1 if failed_examples else 0)
