def find_unique_followers(a_list, b_list, my_list):
	# 4. 2次元リスト x_list を作成
	x_list = []

	# 5. a_list と b_list に含まれ、かつ my_list に含まれないアカウント名を x_list の要素1に格納する
	for account in a_list:
		if account in b_list and account not in my_list:
			x_list.append([account])
	# ここでは、x_list の要素2に追加するデータは仮のデータとします
	# 6. x_list の要素1が follow しているアカウント名を x_list の要素2に格納する
	print(x_list)
	for j in range(len(x_list)):
		followers = []
		# 仮のフォロワーデータを設定（実際にはSNSから取得する）
		for i in range(5):
			followers.append(f"follower{i}")
		x_list[j].append(followers)
	print(x_list)
		
	# 7. x_list の要素2で not a_list かつ not b_list かつ not my_list に該当するアカウントを探す
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

# サンプルリスト
my_list = ["friend1", "friend2", "friend3"]
a_list = ["accountA1", "accountA2", "friend1", "follower2"]
b_list = ["accountA1", "accountA2", "friend3", "follower1"]

# 関数を呼び出し、結果を表示
unique_followers = find_unique_followers(a_list, b_list, my_list)
print('\033[32m')
print(unique_followers)
print('\033[0m')
