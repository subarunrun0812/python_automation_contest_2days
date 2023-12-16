from playwright.sync_api import Playwright, sync_playwright

username = "yuendo42"
password = "42tokyo"

def locate(page):
    # ユーザー名の取得
    following_locator = page.locator('body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1)')
    followingUsersElements = following_locator.locator('.x1a02dak.x1q0g3np.xdl72j9 a[role="link"]')
    
    userNames = []
    for followingUsersElement in followingUsersElements.all():
        userName = followingUsersElement.inner_text()
        userNames.append(userName)

    return userNames



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
    page_to_go = f"https://www.instagram.com/{username}/following/"
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
            break  
    
        previous_count = current_count

    # ユーザーのフォローを配列で取得
    user_follows = locate(page)
    print(user_follows)
    
    # for friend in user_follows:

    
    # ブラウザを閉じる
    browser.close()

if __name__ == "__main__":
    with sync_playwright() as pw:
        run(pw)