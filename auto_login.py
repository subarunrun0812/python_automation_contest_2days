from playwright.sync_api import Playwright, sync_playwright

username = "yuendo42"
password = "42tokyo"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.instagram.com/
    page.goto("https://www.instagram.com/")

    # Fill with username
    page.get_by_label("Phone number, username, or email").click()
    page.get_by_label("Phone number, username, or email").fill(username)

    # Fill with password
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(password)

    # Click Log In
    page.get_by_role("button", name="Log in", exact=True).click()
    page.wait_for_url("https://www.instagram.com/accounts/onetap/?next=%2F")

    page.goto("https://www.instagram.com/")

    # Click text=Not Now
    page.get_by_role("button", name="Not Now").click()
    page.wait_for_url("https://www.instagram.com/")

    # put the link of the profile from which you want to get followers
    # page.goto("https://www.instagram.com/desired_profile/followers/")
    page_to_go = "https://www.instagram.com/" + username + "/followers/"
    page.goto(page_to_go)

    # Use the while loop where you compare the number of profiles in the DOM
    # with the number of followers indicated in the profile header
    # because this example will only scroll 5 times
    for _ in range(5):
        page.locator('a > div > div > span[dir="auto"]').last.scroll_into_view_if_needed()
        page.wait_for_timeout(5 * 1000)
    page.pause()

if __name__ == "__main__":
    with sync_playwright() as pw:
        run(pw)