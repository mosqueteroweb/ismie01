from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Verify dam.html
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/dam.html")
        page.screenshot(path="verification/dam_index_screenshot.png", full_page=True)
        print("Screenshot of dam.html saved to verification/dam_index_screenshot.png")

        # Verify back link on dam_si.html
        page.goto(f"file://{cwd}/dam_si.html")
        # Click the back button (the SVG link in header)
        # It's the first 'a' tag in the header usually.
        # Selector: header a[href='dam.html']
        if page.locator("header a[href='dam.html']").is_visible():
            print("Back link to dam.html found in dam_si.html")
        else:
            print("ERROR: Back link to dam.html NOT found in dam_si.html")

        page.screenshot(path="verification/dam_si_backlink_screenshot.png")

        browser.close()

if __name__ == "__main__":
    run()
