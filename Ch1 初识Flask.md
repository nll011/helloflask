## 1.2 Hello, Flask!

### 1.2.1 创建程序实例

```python
from flask import Flask
app=Flask(__name__)
```

### 1.2.2 注册路由

在一个Web应用里，客户端和服务器上的Flask程序的交互可以简单概况为以下几步：

1. 用户在浏览器输入URL访问某个资源
2. Flask接收用户请求并分析请求的URL
3. 为这个URL找到对应的处理函数
4. 执行函数并生成响应，返回给浏览器
5. 浏览器接收并解析响应，将信息显示在页面中

我们要做的是：

* 建立处理请求的函数
* 为其定义对应的URL规则
* 只需为函数附加`app.route()`装饰器，并传入URL规则作为参数

以上过程称为注册路由(route), 这个函数被称为视图函数(view function)



```python
@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'
```

* `route()`装饰器的第一参数是URL规则，用字符串表示
* 必须以`/`开始
* 这里的URL是相对URL



#### 1.2.2.1 为视图绑定多个URL

```python
@app.route('/')
@app.route('/hello')
def index():
    return '<h1>Hello Flask!</h1>'
```

#### 1.2.2.2 动态URL

```python
@app.route('/greet/<name>')
def index():
    return '<h1>Hello %s</h1>' % name
```

* 当URL规则中包含变量时候，如果用户访问的URL中没有添加变量，那么在匹配失败后返回一个404错误响应
* 常见行为在`app.route()`使用defaults参数设置URL变量的默认值，这个参数接收字典作为输入，存储URL变量和默认值的映射

```python
@app.route('/greet',defaults={'name':'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello %s</h1>' % name
```

* 也可以这么写

```python
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name='Programmer'):
    return '<h1>Hello %s</h1>' % name
```



## 1.3 启动开发服务器



