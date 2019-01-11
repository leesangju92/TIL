from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/")   # @app.route = 데코레이터 , 조건부실행?, 도메인 뒤에 아무것도 없을때 인덱스 페이지라고 한다.
def index():
    return "Hi"

@app.route("/ssafy")     #보통 주소와 함수 이름 같게
def ssafy():
    return "sssssssafy"

@app.route("/hi/<string:name>") #variable routing
def hi(name):
    return (f"hi {name}!")

@app.route("/lotto") # route로 들어오면 밑에 정의되어 있는 함수를 실행하라는 의미.
def lotto():
    i = random.sample(range(1,46), 6)
    return jsonify(i)

@app.route("/dictionary/<string:word>")
def dictionary(word):
    my_dictionary = { "apple": "사과", "banana": "바나나", "melon": "멜론", "pear" : "배" }
    if word in my_dictionary:
        return f"{word}은(는) {my_dictionary[word]}!"
    else:
        return f"{word}은(는) 나만의 단어장에 없는 단어입니다!"

if __name__ == "__main__":
    app.run(debug = True)   #debug모드 실행
