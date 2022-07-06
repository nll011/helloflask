from flask import Flask,request

app=Flask(__name__)

@app.route('/hello',methods=['GET','POST'])
def hello():
    name=request.args.get('name','Flask') # 获取查询参数name的值
    return '<h1>Hello %s!</h1>' % name # 插入到返回值中

@app.route('/goback/<int:year>')
def go_back(year):
    return '<p>Welcome to %d!</p>' %(2022-year)

@app.route('/colors/<any(blue,white,red):color>')
def three_colors(color):
    return '<p>Love is patient and kind. Love is not jeaous or boastful or proun or rude.</p>'