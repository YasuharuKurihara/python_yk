class Character:

    def __init__(self, name):
        self.name = name

    def speak(self, commnet):
        print(f"{self.name}：{commnet}")
# kurihara = Character()
# kurihara.name = "くりはら"
# print(kurihara.name)
# kurihara.speak("hello")

taro = Character("たろー")
taro.speak("おはようなぎ")
print(taro.name)

