# 181221 수업정리

## 1. 수업내용

* 사이트 만들기

  ```python
  from flask import Flask, jsonify, render_template, request, redirect
  import random
  import requests
  from lotto_functions import am_i_lucky,get_lotto,pick_lotto,pick_lotto2
  from bs4 import BeautifulSoup
  from realtime import realtime_check, boring
  
  
  app = Flask(__name__)
  
  @app.route("/ide/<string:username>/<string:workplace>/")
  def username_workspace(username,workplace):
      return render_template('ide.html', name=username, space=workplace)
  
  @app.route("/")
  def index():
      lunch = random.choice(['20층', 'piet'])
      return render_template('index.html', select=lunch)
      
  @app.route("/hi")
  def hi():
      return 'Hello SSAFY'
  
  @app.route("/pick_lotto")
  def pick():
      return render_template('lucky_number.html', lucky= pick_lotto())
  
  @app.route("/get_lotto")
  def get():
      turn = request.args.get('turn')
      return render_template('get_lotto.html', turn=turn, result=get_lotto(turn))
  
  @app.route("/am_I_lucky")
  def lucky():
      turn = request.args.get('turn')
      return render_template('am_I_lucky.html', num = turn, result = am_i_lucky(pick_lotto(), get_lotto(turn)))
      
  @app.route("/am_I_lucky2")
  def lucky2():
      return render_template('am_I_lucky2.html', result = am_i_lucky(pick_lotto(), pick_lotto2()))
  
  
  @app.route("/want_to_say")
  def say():
      return render_template('want_to_say.html')
      
  @app.route("/to_admin")
  def toadmin():
      say = request.args.get('say')
      MY_CHAT_ID = '706691859'
      BOT_TOKEN = '745206985:AAHT_i_bBPtC5zJsxmV6Wm8-LNP85VgqgXg'
      
      url = "https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, say)
  
      response = requests.get(url)
  
  
      return render_template('to_admin.html', say=say)
  
  # @app.route("/ping")
  # def ping():
  #     return render_template('ping.html')
  
  # @app.route("/pong")
  # def pong():
  #     ssum = request.args.get('ssum')
  #     match_point = random.choice(range(1,101))
      
  #     MY_CHAT_ID = '706691859'
  #     BOT_TOKEN = '745206985:AAHT_i_bBPtC5zJsxmV6Wm8-LNP85VgqgXg'
      
  #     url = "https://api.hphk.io/telegram/bot{}/sendMessage?chat_id={}&text={}".format(BOT_TOKEN, MY_CHAT_ID, ssum)
  
      # response = requests.get(url)
  
      # c9에서는 response = requests.get(url)
  
      # return render_template('pong.html', ssum=ssum, match_point=match_point)
  
  @app.route("/realtime")
  def realtime():
      return render_template('realtime.html', data1=realtime_check()['1위'], data2=realtime_check()['2위'],
      data3=realtime_check()['3위'],data4=realtime_check()['4위'],
      data5=realtime_check()['5위'],data6=realtime_check()['6위'],
      data7=realtime_check()['7위'],data8=realtime_check()['8위'],
      data9=realtime_check()['9위'],data10=realtime_check()['10위'])
  
  
  @app.route("/boring")
  def iamboring():
      return redirect(boring())
  
  
      
  # @app.route('/test')
  # def test():
  #     return jsonify()
  
  
  if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0',port=8080
  ```

## 2. 기억해야할 것

* `http:// ide.c9.io/leesangju92/startcamp`에서 ` http:// ide.c9.io/` 는 도메인,  `leesangju92/startcamp`는 라우터

* HTML에서 `! + tab`을 누르면 기본 서식 자동으로 작성된다.

* 링크걸때는 헷갈리지 않게 왠만하면 같은 단어로 하는 것이 추천된다. 

* convention of HTML

* ```
  1. 식은 = 양옆 띄우지 않는다
  2. 따움표는 큰따움표사용
  3. default는 type="text"
  4. input type="number"
  5. 대문자로 표시한 변수는 상수, 다신 바꾸지 않는다는 약속
  
  ```

* `if __name__ == '__main__':
  ​    app.run(debug=True, host='0.0.0.0',port=8080)` : debug빼고 로컬에선 쓰지 않는다!