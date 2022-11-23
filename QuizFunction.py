import random

class Quiz(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary
    def quiz_handler(self):
        template = "*"*30 + '\n英単語 : {}\n日本語を入力してください\n'+ '↓'*15

        print("英単語クイズを開始します。")
        switch = input("クイズを開始しますか？ y/[N] : ")

        while switch == "y":
            word = random.choice(list(self.dictionary.keys()))
            print(template.format(word))
            answer = input("入力してください : ")
            if answer == "Quit":
                return "プログラムを終了します。"
            elif answer == self.dictionary[word]:
                print("正解です。")
            elif answer!= self.dictionary[word]:
                print("不正解です。")
                print(f'正解は[{self.dictionary[word]}]です。')
        else:
            return "プログラムを終了します。"
