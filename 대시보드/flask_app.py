# 필요한 패키지 import 하는것 
from flask import Flask, render_template
import flask
from flask import Flask, request, render_template
import os

# 여기서 flask 로컬호스트를 여는 부분
import numpy as np
app = Flask(__name__)

# 웹 시작했을때 첫화면에 나오는 html 정의한것
@app.route("/")
@app.route("/index.html")
def template_test():
    return render_template(
                'index.html',
                # 웹 메인이름 지정                      
                title="전주시 빅데이터 CAN WIN",     
            )
@app.route("/전라북도사고횟수.html")
def a1():
    return render_template('전라북도사고횟수.html')

@app.route("/전라북도주변사고횟수.html")
def a2():
    return render_template('전라북도주변사고횟수.html')

@app.route("/자전거도로.html")
def a3():
    return render_template('자전거도로.html')

@app.route("/열지도.html")
def a4():
    return render_template('열지도.html')

@app.route("/마커클러스터.html")
def a5():
    return render_template('마커클러스터.html')

@app.route("/마커.html")
def a6():
    return render_template('마커.html')

@app.route("/최종.html")
def a7():
    return render_template('최종.html')

@app.route("/도로만.html")
def a8():
    return render_template('도로만.html')



# flask 실행 자동화 하는 부분
if __name__ == '__main__':
    app.run(debug=True)
