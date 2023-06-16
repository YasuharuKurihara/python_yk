user_file_text = """
hoge
fuga
taro
ziro
saburo
"""
list = user_file_text.split()
print(list)
list.sort()
print(list)
user_file_text2 = " ".join(list)
print(user_file_text2)
user_file_text3 = "\n".join(list)
print(user_file_text3)