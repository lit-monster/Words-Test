from QuizFunction import Quiz
import random
import requests
import re
from bs4 import BeautifulSoup

url = 'https://toiguru.jp/toeic-vocabulary-list#smoothplay1'

english_words = []
japanese = []

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    words = soup.findAll('td')
except requests.exceptions.ConnectionError as e:
    print("※URLが正しくありません。")
    print(e)
else:
    print("requests Succefull")

    for word in words:
        word = str(word).replace('<td>', '').replace('</td>', '').replace('<br/>', '')
        english_words.append(re.findall('[a-z]+', word))
        japanese.append(re.sub("[a-zA-Z]", "", word))
    
    if len(english_words) == len(japanese):
        print("単語を取得しました。")
    else:
        print("単語の取得に失敗しました。")

    # print(english_words[15][0] + " " + english_words[15][1])

    for words in english_words:
        for word in words:
            print(word + " ", end="")
            print("\n")

# questions = dict(zip(english_words, japanese))
# for s, t in enumerate(questions):
#     print(f'{s} : {t}')

# quiz = Quiz(questions)
# result = quiz.quiz_handler()
# print(result)









    