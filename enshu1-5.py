print("-----演習１-----")
data_dict = {}

key = input("Keyを入力して下さい＞")
value = input("valueを入力してください＞")

data_dict[key] = int(value)

print(data_dict)

print("-----演習２-----")
print(data_dict[key])

print("-----演習３-----")
print(data_dict.get(key))
