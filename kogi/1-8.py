name_list = ["satou", "kurihara","misaki", "suzuki"]

for name in name_list:
    print(name, end="覚醒しました\n")

for i in range(10):
    print(i)

for i in range(0, 20, 2):
    print(i)

dic = {"商品A":3, "商品B":4, "商品C":10, "商品D":5}
print("商品一覧")
for key in dic.keys():
    print(key)

for key in dic:     #同じようにkeyを習得できる（こちらの書き方が主流）
    print(key)

print("\n商品と在庫数の一覧")
for key, value in dic.items():
    print(f"商品名：{key}、在庫数：{value}")

numlist = []
for i in range(5):
    numlist.append(i+1)     #numlist = [1,2,3,4,5]となる
print(numlist)

numlist2 = [i+1 for i in range(5)]  #list内包表記
print(numlist2)