print("-----演習１-----")

# for i in range(1,101):
#         if i%15==0:
#             print("FizzBuzz")
#         elif i%5==0:
#             print("Buzz")
#         elif i%3==0:
#             print("Fizz")
#         else:
#             print(i)

# for i in range(1,101):
#     if i>1 and i>2 and i<=10:
#         if i%2!=0:
#             print(i)
#     else:
#         if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
#             print(i)

for i in range(1,101):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)


# for i in range(2, 101):
#     is_prime = True  # 素数かどうかのフラグ
#     # i = 10
#     # 2~9までで、割ってみて
#     # 割れきれたら素数じゃない
#     # print(f'i={i}')
#     for j in range(2, i):
#         # print(f'  j={j}')
#         if i % j == 0:
#             is_prime = False
#
#     if is_prime:
#         print(i)




