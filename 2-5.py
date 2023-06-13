class Character:
    def __init__(self, name, level):
        self._level = level     #「_変数名」でカプセル化になる(しかし、強制的に外からはアクセスできる)
        self.__name = name      #「__変数名」で絶対外からアクセスできなくなる

        #先頭に「__」を付けると他言語でprivate
        #先頭に「_」を付けると他言語でprodected

    def _speak(self):
        print()

taro = Character("tarou", 2)
print(taro._level)

