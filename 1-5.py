list = [2, 55.6, "栗原", 3]
print(list, list[1:3], list[3])
list[0] = "orange"
print(list)

print(len(list))    #文字列の長さを取得

text = ""   #空文字列、白紙のノート的な

list2 = [   #listの中にlistを書ける
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(list2[0][2], list2[1][0], list2[2][1])

flist = ["orange", "apple", "lemon"]
flist.append("susi")    #末尾に追加
print(flist)
flist.insert(0, "gohan")    #指定したインデックスに追加
print(flist)
del flist[2]
print(flist)
flist.pop()
print(list)

num_list = [3,5,1,34,67,2]
print(sorted(num_list))
print(sorted(num_list, reverse=True))
print(max(num_list), min(num_list), sum(num_list), len(num_list), int(sum(num_list)/len(num_list)))

text = 'apple,banana,orange'
food_list = text.split(',')
print(food_list)

food_text = ','.join(food_list)
print(food_text)

empty_tuple = ()
empty_tuple2 = ("niku",)
print(empty_tuple2)

