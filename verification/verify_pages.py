from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Verify index page
        cwd = os.getcwd()
        index_path = f"file://{cwd}/dam.html"
        print(f"Navigating to {index_path}")
        page.goto(index_path)
        page.screenshot(path="verification/dam_index.png", full_page=True)
        print("Screenshot saved: verification/dam_index.png")

        # Verify module page (dam_si.html)
        si_path = f"file://{cwd}/dam_si.html"
        print(f"Navigating to {si_path}")
        page.goto(si_path)

        # Expand details to see content
        page.eval_on_selector_all("details", "elements => elements.forEach(e => e.open = true)")

        page.screenshot(path="verification/dam_si.png", full_page=True)
        print("Screenshot saved: verification/dam_si.png")

        # Verify DI page specifically for Hours/Weeks
        di_path = f"file://{cwd}/dam_di.html"
        print(f"Navigating to {di_path}")
        page.goto(di_path)
        page.screenshot(path="verification/dam_di.png", full_page=True)
        print("Screenshot saved: verification/dam_di.png")

        browser.close()

if __name__ == "__main__":
    run()
