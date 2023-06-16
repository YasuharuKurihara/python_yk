num1 = 3
num2 = 5
num3 = 2

print("-------演算子-------")
print(num2/num1)    #「/」では小数点も表示
print(num2//num1)   #「//」では整数部分のみ表示
print(num3**num1)   #「**」べき乗

flist2 = ["orange", "apple", "maron"]
flist4 = ["orange", "apple", "maron"]
flist3 = flist2
# flist2.sort()
print(f"{flist2}\n{flist3}")
print(f"{flist2 == flist4}\n{flist2 is flist4}")
print(f"{flist2 == flist3}\n{flist2 is flist3}")
