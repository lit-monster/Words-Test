from QuizFunction import Quiz
import random
import requests
import re
from bs4 import BeautifulSoup

url = 'https://toiguru.jp/toeic-vocabulary-list#smoothplay1'

encord_english = []
english = []
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
        encord_english.append(re.findall('[a-z]+', word))
        japanese.append(re.sub("[a-zA-Z]", "", word))

    for words in encord_english:
        english.append(' '.join(words))

    if len(english) == len(japanese):
        print("単語を取得しました。")
    else:
        print("単語の取得に失敗しました。")

questions = dict(zip(english, japanese))

quiz = Quiz(questions)
result = quiz.quiz_handler()
print(result)









