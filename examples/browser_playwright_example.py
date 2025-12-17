from universal_sandbox import Sandbox
import os

# Initialize client
# Get Sandbox API Token from https://ai-infra.org/
sandbox = Sandbox(token=os.getenv("SANDBOX_API_TOKEN"))

print("=" * 70)
print("Browser Sandbox with Playwright Example")
print("=" * 70)
print()

# Create a browser sandbox
print("Creating browser sandbox...")
sbx = sandbox.browser.create(provider="alibaba", region="cn-hangzhou")
print(f"Sandbox ID: {sbx.id}")
print(f"Provider: {sbx.provider}")
print(f"Type: {sbx.type}")
print(f"WSS URL: {sbx.urls.wss_url if sbx.urls else 'N/A'}")
print()

# Use the new get_playwright() method
print("Connecting to browser via Playwright...")
try:
    browser = sbx.get_playwright()
    print("Successfully connected to browser!")
    print()

    # Create a new page
    print("Opening new page...")
    page = browser.new_page()

    # Navigate to a website
    print("Navigating to example.com...")
    page.goto("https://example.com")

    # Get the page title
    title = page.title()
    print(f"Page title: {title}")
    print()

    # Take a screenshot (optional)
    # page.screenshot(path="example.png")
    # print("Screenshot saved to example.png")

    # Close the browser
    browser.close()
    print("Browser closed")
    print()

except Exception as e:
    print(f"Error: {e}")
    print()

# Use the new delete() method (no client parameter needed!)
print("Deleting sandbox using sbx.delete()...")
try:
    resp = sbx.delete()
    print(f"Delete response: {resp}")
except Exception as e:
    print(f"Error during deletion: {e}")

print()
print("=" * 70)
print("Example completed!")
print("=" * 70)
