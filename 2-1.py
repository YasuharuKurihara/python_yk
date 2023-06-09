def hello():
    print("Hello World!!")

hello()

def input_hello(s):
    print(f"入力された文字列は「{s}」になります。")

list = [1,2,3]
input_hello(list)

def is_prime(num):
    for i in range(2,num):
        if num%i ==0:
            return False
    return True

print(f"{is_prime(100)}")

def message(s=None):
    if s is None:
        print("文字列が入力されていません")
    else:
        print(f"入力された文字列は{s}です！")

message("hello world")
message()

# # sは、仮引数とも呼ぶ
# def message(s=None):
#     if s is None:  # s == Noneと書きたくなったら、isを使う
#         print('文字列が未入力です')
#     else:
#         print('入力文字列は「' + s + '」です')
#
#
# # 'Hello World'は実引数とも呼ぶ
# # 関数呼び出しの際に、引数名=値のように渡すことができる
# message(s='Hello World')
# message()

def cleaning(date, *args):
    staff = ""
    for person in args:
        staff = staff + "「" + person + "」"
    print(f"{date}の掃除担当は{staff}になります")
cleaning("12/3", "栗原","山本","長谷部")
cleaning("3/7", "藤山","瓜田","川本","井口")

a = 7
def sample():
    a =1
sample()
print(a)

b = 7
def sample():
    global b    #global変数だと関数内で外の変数の値を書き換えれる
    b =1
sample()
print(b)
