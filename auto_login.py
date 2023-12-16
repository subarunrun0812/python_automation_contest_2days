import instaloader

username = "yuendo42"
password = "42tokyo"

loader = instaloader.Instaloader() # instaloaderのインスタンス作成

loader.login(username, password)

profile = instaloader.Profile.from_username(loader.context, username)

profile = instaloader.Profile.from_username(loader.context, username)

followees = profile.get_followees()

for followee in followees: print(followee.username)