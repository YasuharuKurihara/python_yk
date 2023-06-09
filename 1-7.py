number = int(input("数字を入力してください："))

if number == 123:
    print(f"{number}は０よりも大きい数字です")
elif number%2 == 0:
    print(f"{number}は偶数らしいですよ。知らんけど・・・")
else:
    print(f"{number}はよくわかりません")


namelist = ["kuiahra", "syouiti", "hikaru"]
name1 = "yasuharu"
if name1 not in namelist:
    print("yasuharはいませんでした")
else:
    print("yasuharuはいました")

number = [1,2,3,4,5,6,7,8,9]
for num in number:
    if num<5 and num%2==0:
        print(f"{num}は５より小さく偶数である")
    else:
        print(f"{num}は５以上か奇数である")

