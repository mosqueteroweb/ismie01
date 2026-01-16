from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        file_path = f"file://{os.path.abspath('dam_si.html')}"
        print(f"Navigating to {file_path}")
        page.goto(file_path)

        # Verify title
        if "Sistemas Informáticos" not in page.title():
            print(f"Title mismatch: {page.title()}")
            exit(1)

        # Verify content
        # Check for a specific known new content string
        locator = page.get_by_text("Explotación de sistemas microinformáticos")
        if locator.count() > 0:
             print("Found 'Explotación de sistemas microinformáticos'")
        else:
             print("Content 'Explotación de sistemas microinformáticos' NOT found")

        # Take screenshot
        page.screenshot(path="verification/dam_si_screenshot.png", full_page=True)
        print("Screenshot taken.")
        browser.close()

if __name__ == "__main__":
    run()
