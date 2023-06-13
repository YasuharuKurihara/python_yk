class Character:

    def __init__(self, name):
        self.name = name

    def speak(self, comment):
        print(self.name + ':' + comment)


# class クラス名(継承元):
class Healer(Character):

    def speak(self, commnet):
        print(f"{self.name}(Healer):{commnet}")
    # 継承すると、Charcterのメソッド等が暗黙のうちに受け継がれる
    # つぎのようなメソッド定義がされているのと、同じ状態
    # def __init__(self, name):
    #     self.name = name
    #
    # def speak(self, comment):
    #     print(self.name + ':' + comment)


taro = Healer('tarou')  # インスタンス化
taro.speak(comment='ハロー')


class Character:

    def __init__(self, name, age, item):
        self.name = name
        self.age = age
        self.item = item

    def speak(self, comment):
        print(self.name + ':' + comment)


# class クラス名(継承元):
class Healer(Character):

    # __init__も上書きできます
    def __init__(self, name, age, item, heal_power):
        # 親クラスのメソッドを呼ぶ
        # super().親クラスのメソッド名(親で必要な引数...)
        # super()関数の引数は、今は空でよいです
        super().__init__(name, age, item)
        self.heal_power = heal_power

    # オーバーライド
    # 親クラスのspeakは呼ばれなくなる
    def speak(self, comment):
        # 親のspeakも読んでみる
        super().speak(comment)
        print('私はヒーラーです')

    # 新規追加のメソッド
    def healing(self):
        print(f'{self.name}は回復した！')


taro = Healer('tarou')  # インスタンスか
taro.speak(comment='ハロー')


# 定義だけしたい場合にpass文を使う(エラーにならなくなる)
# def hello():
#     pass