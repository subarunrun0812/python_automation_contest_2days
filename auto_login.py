from playwright.sync_api import Playwright, sync_playwright

username = "yuendo42"
password = "42tokyo"

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # 新しいページを開く
    page = context.new_page()

    # https://www.instagram.com/に飛ぶ
    page.goto("https://www.instagram.com/")

    # ユーザーネームを入力
    page.get_by_label("Phone number, username, or email").click()
    page.get_by_label("Phone number, username, or email").fill(username)

    # パスワードを入力
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(password)

    # Log inをクリック
    page.get_by_role("button", name="Log in", exact=True).click()
    page.wait_for_url("https://www.instagram.com/accounts/onetap/?next=%2F")

    page.goto("https://www.instagram.com/")

    # 通知表示で「Not Now」を入力
    page.get_by_role("button", name="Not Now").click()
    page.wait_for_url("https://www.instagram.com/")

    # フォローしているユーザーのリストを表示
    page_to_go = "https://www.instagram.com/" + username + "/following/"
    page.goto(page_to_go)

    previous_count = 0
    while True:
        # フォローページの末尾にいくまでスクロールする
        page.locator('a > div > div > span[dir="auto"]').last.scroll_into_view_if_needed()
        page.wait_for_timeout(2000)  # Adjust the timeout as needed

        # 現在までにロードしたフォロー数を数える
        current_count = page.locator('a > div > div > span[dir="auto"]').count()

        # スクロールの前後でカウント数が更新されているか確認、更新がなかったらスクロールをやめる
        if current_count == previous_count:
            break  # Exit the loop if no new elements are loaded

        previous_count = current_count

    # ブラウザを閉じる
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as pw:
        run(pw)