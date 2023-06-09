dict = {"水":"water", "火":"fire", "風":"wind", "土":"soil"}
print(dict["火"])
print(dict)

print(dict.get("光", "そんな属性は存在しない！！"))   #存在しないキーを指定された時の値を変更できる

numlist = [1,1,1,1,3,43,23,4,5,65]
number_set = set(numlist)   #重複した数字を消す
print(number_set)