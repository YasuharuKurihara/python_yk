class Character:

    def __init__(self, name):
        self.name = name

    # デバッグなど、人間が見やすいクラスの文字列表現を返そう
    def __str__(self):
        return f'Charcter({self.name})'


taro = Character('tarou')
print(taro)

# もともとの表示は
# <__main__.Character object at 0x10b6fada0>

# __str__ メソッドを定義すると、もっとわかりやすい内容に変更できる