from QuizFunction import Quiz
import random
import requests
import re
from bs4 import BeautifulSoup

url = 'https://toiguru.jp/toeic-vocabulary-list#smoothplay1'

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
        english.append(re.findall('[a-z]+', word))
        japanese.append(re.sub("[a-zA-Z]", "", word))
    
    if len(english) == len(japanese):
        print("単語を取得しました。")
    else:
        print("単語の取得に失敗しました。")

#test

    
#englishリストが、二重リストになっていて、[be], [interested], [in]という状態を解消する。

# questions = dict(zip(english, japanese))
# for s, t in enumerate(questions):
#     print(f'{s} : {t}')

# quiz = Quiz(questions)
# result = quiz.quiz_handler()
# print(result)









    