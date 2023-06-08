print("-----演習問題1-----")
data_list = [1, 2, [3, 4, 5], [6, 7], 8, 9, [10, 11]]
print(data_list[3][1])

print("\n-----演習問題2-----")
data_list2 = []
for i in range(3):
    data_list2.insert(i,int(input("数字を入力してください：")))
data_list2.sort()
print(data_list2)

print("\n-----演習問題3-----")
data_list3 = []
for i in range(3):
    data_list3.append(int(input("数字を入力してください：")))
print(sorted(data_list3, reverse=True))
