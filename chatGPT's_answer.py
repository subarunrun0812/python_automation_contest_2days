from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # Set headless=False for debugging
    context = browser.new_context()
    page = context.new_page()

    # Your login code here

    # Navigate to the following list
    following_page = f"https://www.instagram.com/{username}/following/"
    page.goto(following_page)

    followed_profiles_urls = set()
    previous_count = 0
    while True:
        # Scroll to load more profiles
        page.locator('article > div:nth-child(3)').last.scroll_into_view_if_needed()
        page.wait_for_timeout(2000)

        # Collect profile URLs
        profile_links = page.query_selector_all('article > div:nth-child(3) > ul > div > li > div > div > div > span > a')
        for link in profile_links:
            profile_url = link.get_attribute('href')
            if profile_url:
                followed_profiles_urls.add(profile_url)

        # Check if new profiles were loaded
        current_count = len(followed_profiles_urls)
        if current_count == previous_count:
            break  # Exit the loop if no new elements are loaded
        previous_count = current_count

    # Visit each profile
    for profile_url in followed_profiles_urls:
        page.goto(profile_url)
        page.wait_for_load_state('networkidle')
        # Add any actions you want to perform on each profile page

    browser.close()

if __name__ == "__main__":
    with sync_playwright() as pw:
        run(pw)
