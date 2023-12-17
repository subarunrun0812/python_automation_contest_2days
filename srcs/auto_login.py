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
        following_locator = page.locator('#mount_0_0_vu > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div._aano > div > div')
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



def find_my_user(page, username):
    # フォローしているユーザーのリストを表示
    page.goto(f"https://www.instagram.com/{username}/following/")
    page.wait_for_timeout(5000)  # Adjust the timeout as needed
    return(locate(page))

def find_other_user(page, username):
    # フォローしているユーザーのリストを表示
    # 「following」ボタンをクリック
    page.wait_for_load_state('networkidle')
    following_button = page.get_by_text("following", exact=True)
    # following_button = page.locator('#mount_0_0_44 > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > ul > li:nth-child(3) > a > span')
    following_button.click()
    page.wait_for_load_state('networkidle')
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

    # デバイスを指定
    iphone_13 = playwright.devices['iPhone 13']
    context = browser.new_context(**iphone_13,)
	
    # 新しいページを開く
    page = context.new_page()
    
    # https://www.instagram.com/に飛ぶ
    page.goto("https://www.instagram.com/")
	
	
    # 「Log in」ボタンをクリック
    page.get_by_role("button", name="Log in", exact=True).click()
	 
    # 時間を置く
    page.wait_for_timeout(2000)  

    # ユーザーネームを入力
    page.get_by_label("Phone number, username, or email").click()
    page.get_by_label("Phone number, username, or email").fill(username)

    # パスワードを入力
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(password)

    # 時間を置く
    page.wait_for_timeout(2000)  
	
    # Log inをクリック
    page.get_by_role("button", name="Log in", exact=True).click()
    page.wait_for_url("https://www.instagram.com/accounts/onetap/?next=%2F")

    page.goto("https://www.instagram.com/")

    # 通知表示で「Not Now」を入力
    # page.get_by_role("button", name="Not Now").click()
    # page.wait_for_url("https://www.instagram.com/") 今消した

    # 時間を置く
    page.wait_for_load_state('networkidle')
	
    # フォローしているユーザーのリストを表示
    # page.goto(f"https://www.instagram.com/{username}/following/")
    page.goto(f"https://www.instagram.com/{username}/")

    # page.get_by_role("button", name="Not Now").click()
	
    # 時間を置く
    page.wait_for_load_state('networkidle')
	 
    # ユーザーA、ユーザーBの情報を得る
    user_self = find_my_user(page, username)
    page.wait_for_load_state('networkidle')
    print(user_self)
    page.goto(f"https://www.instagram.com/{user1}/")
    page.wait_for_load_state('networkidle')
    user_a = find_other_user(page, user1)
    page.wait_for_load_state('networkidle')
    page.goto(f"https://www.instagram.com/{user2}/")
    page.wait_for_load_state('networkidle')
    user_b = find_other_user(page, user2)
    print(user_a)
    print(user_b)

    unique_followers = find_unique_followers(user_a, user_b, user_self,page)
    print(unique_followers)
    # ブラウザを閉じる
    browser.close()

def run_playwright(username, password, insta1, insta2):
    with sync_playwright() as pw:
        run(pw, username, password, insta1, insta2)
