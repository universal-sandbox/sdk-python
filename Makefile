.PHONY: build publish release

# Build distribution packages
build:
	@echo "Cleaning build artifacts..."
	@rm -rf build/ dist/ *.egg-info/
	@echo "Building distribution packages..."
	python -m build
	@echo "✓ Built packages:"
	@ls -lh dist/

# Publish to PyPI
publish: build
	@echo "Publishing to PyPI..."
	twine upload dist/*

# Alias for publish (for consistency across projects)
release: publish
