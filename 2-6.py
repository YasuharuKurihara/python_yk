class Character:
    def __init__(self, name, level, exp, itembox):
        self.name = name
        self.__level = level
        self.__stamina = level * 20
        self.exp = exp
        self.itembox = itembox

    # ゲッターメソッド
    @property
    def stamina(self):
        return self.__stamina

    # セッターメソッド
    @stamina.setter
    def stamina(self, new_stamina):
        # 体力の最小値は0、最大値はレベル×20
        if new_stamina > self.__level * 20:
            self.__stamina = self.__level * 20
        elif new_stamina <= 0:
            self.__stamina = 0
            print(self.name + 'は力尽きた')
        else:
            self.__stamina = new_stamina


taro = Character('タロー', 1, 0, {'かいふくやく': 2})
taro.stamina = 200
print(taro.stamina)
taro.stamina = -10
print(taro.stamina)