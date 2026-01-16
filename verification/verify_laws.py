
import os
from playwright.sync_api import sync_playwright

def verify_laws():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to the file
        cwd = os.getcwd()
        file_path = f"file://{cwd}/infografia01c.html"

        print(f"Navigating to {file_path}")
        page.goto(file_path)

        # Locate the details element in the Superior section
        # The details element has text "Normativa Reguladora (ASIR, DAM, DAW)"
        details_summary = page.get_by_text("Normativa Reguladora (ASIR, DAM, DAW)")

        # Scroll into view
        details_summary.scroll_into_view_if_needed()

        # Click to open
        details_summary.click()

        # Wait for animation (transition-all duration-300)
        page.wait_for_timeout(500)

        # Take a screenshot of the opened details content
        # We can locate the parent details element
        details_element = page.locator("details.group.bg-orange-50")

        output_path = f"{cwd}/verification/laws_verification.png"
        details_element.screenshot(path=output_path)
        print(f"Screenshot saved to {output_path}")

        browser.close()

if __name__ == "__main__":
    verify_laws()
