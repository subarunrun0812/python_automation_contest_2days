from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Your login code here

    # Navigate to the following list
    following_page = f"https://www.instagram.com/{username}/following/"
    page.goto(following_page)

    # Wait for the page to load and for the followers list to be visible
    page.wait_for_selector("selector_for_following_list_container")  # Replace with actual selector

    # Selecting the elements containing the usernames
    following_users_elements = page.query_selector_all("css_selector_for_usernames")  # Replace with actual CSS selector

    following_user_names = []
    for element in following_users_elements:
        user_name = element.inner_text()
        following_user_names.append(user_name)

    print(following_user_names)

    browser.close()

if __name__ == "__main__":
    with sync_playwright() as pw:
        run(pw)
