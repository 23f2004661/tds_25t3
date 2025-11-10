import os
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Get the absolute path to the index.html file
    index_path = os.path.abspath("index.html")

    # Navigate to the local index.html file
    page.goto(f"file://{index_path}")

    # Find the link to login.html and click it
    login_link = page.get_by_role("link", name="Login")
    login_link.click()

    # Wait for the login page to load and assert the title
    expect(page).to_have_title("Login")

    # Assert that the login form is visible
    expect(page.get_by_role("heading", name="Login Form")).to_be_visible()

    # Take a screenshot of the login page
    page.screenshot(path="jules-scratch/verification/verification.png")

    browser.close()

print("Screenshot created at jules-scratch/verification/verification.png")