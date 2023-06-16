user_name = input("名前を入力してください：")
# user_name = "こんにちは" + user_name
# もうちょい古い書き方。formatで、変数を埋め込める
# 'こんにちは{}'.format(user_input_name)
user_name = f"こんにちは、{user_name}"
print(user_name)

