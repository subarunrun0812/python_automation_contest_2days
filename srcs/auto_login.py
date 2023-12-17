from playwright.sync_api import Playwright, sync_playwright


# username = "github_master"
# password = "42tokyo"

def locate(page):
    # フォローを最後までスクロールする
    previous_count = 0
    userNames = []
    while True:
        # フォローページの末尾にいくまでスクロールする
        page.locator('a > div > div > span[dir="auto"]').last.scroll_into_view_if_needed()

        # ユーザー名の取得
        following_locator = page.locator('body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1)')
        followingUsersElements = following_locator.locator('.x1a02dak.x1q0g3np.xdl72j9 a[role="link"]')
        for followingUsersElement in followingUsersElements.all():
            userName = followingUsersElement.inner_text()
            userNames.append(userName)
        page.wait_for_timeout(2000)  # Adjust the timeout as needed

        # 現在までにロードしたフォロー数を数える
        current_count = page.locator('a > div > div > span[dir="auto"]').count()

        # スクロールの前後でカウント数が更新されているか確認、更新がなかったらスクロールをやめる
        if current_count == previous_count:
            break  
    
        previous_count = current_count

    return userNames



def find_user(page, username):
    # フォローしているユーザーのリストを表示
    page.goto(f"https://www.instagram.com/{username}/following/")
    page.wait_for_timeout(5000)  # Adjust the timeout as needed
    return(locate(page))

def find_unique_followers(a_list, b_list, my_list, page):
	# 4. 2次元リスト x_list を作成
	x_list = []

	for account in a_list:
		if account in b_list and account not in my_list:
			x_list.append([account])

	for j in range(len(x_list)):
		followers = find_user(page, x_list[j])
		x_list[j].append(followers)
	print(x_list)
		
	y_list = []
	for _, followers in x_list:
		for follower in followers:
			if follower not in a_list and follower not in b_list and follower not in my_list:
				y_list.append(follower)

	#順序を保持する
	unique_list = []
	for item in y_list:
		if item not in unique_list:
			unique_list.append(item)

	y_list = unique_list
	return y_list


def run(playwright: Playwright, username, password, user1, user2) -> None:
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
    page.goto(f"https://www.instagram.com/{username}/following/")

    # ユーザーA、ユーザーBの情報を得る
    user_self = find_user(page, username)
    user_a = find_user(page, user1)
    user_b = find_user(page, user2)
    print(user_self)
    print(user_a)
    print(user_b)

    unique_followers = find_unique_followers(user_a, user_b, user_self,page)
    print(unique_followers)
    # ブラウザを閉じる
    browser.close()

def run_playwright(username, password, insta1, insta2):
    with sync_playwright() as pw:
        run(pw, username, password, insta1, insta2)
