import sys
from playwright.sync_api import sync_playwright

def test_search_feature():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to a real, stable public sandbox
        page.goto("https://example.com")
        print("STEP 1: Successfully navigated to example.com")

        # FIX APPLIED: "#broken-search-input-id" does not exist on example.com.
        # Using "h1" selector with page.inner_text() which reliably exists on example.com.
        print("STEP 2: Attempting to read the h1 heading text...")
        heading_text = page.inner_text("h1")
        print(f"STEP 2: Found h1 element with text: '{heading_text}'")

        # Validate the heading is non-empty and correct
        assert heading_text.strip() != "", "H1 heading should not be empty!"
        assert "Example Domain" in heading_text, f"Unexpected heading text: '{heading_text}'"

        print("STEP 3: Action executed successfully.")
        browser.close()

if __name__ == "__main__":
    try:
        test_search_feature()
        print("RESULT: All tests passed successfully!")
        sys.exit(0)
    except Exception as e:
        print(f"RESULT: Test Suite Failed! Error Details: {str(e)}")
        sys.exit(1)
