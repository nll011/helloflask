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

### 1.3.1 Run, Flask, Run!

* http:127.0.0.1 即 localhost, 是指向本机的IP地址，一般用来测试
* Flask默认使用5000端口

1. 自动发现程序实例

   * 从当前目录找app.py和wsgi.py模块，并从中寻找名为app或者application的程序实例

   * 从环境变量FLASK_APP对应的模块名/导入路径寻找名为app或者application的程序实例

   * 如果程序主模块是其他名称，设置环境变量FLASK_APP

     ```shell
     set FLASK_APP=hellp
     ```

2. 管理环境变量
   * 如果安装了python-dotenv, 在使用`flask run`或者其他命令时会自动从.flaskenv文件和.env文件加载环境变量
     优先级： 手动设置的环境变量>.env中设置的环境变量>.flaskenv设置的环境变量
3. 使用PyCharm运行服务器



### 1.3.2 更多的启动选项

1. 使服务器外部可见（默认不可见）

   ```shell
   flask run--host=0.0.0.0
   ```

   这会让服务器监听所有外部请求

2. 改变默认端口

   ```shell
   flask run--port=8000
   ```



### 1.3.3 设置运行环境

* 开发环境 -- development enivronment

* 生产环境 -- production enivronment

* Flask提供了一个FLASK_ENV环境变量来设置环境，默认为production

  * 在开发是，我们将环境变量的值写入.flaskenv文件中

    ```shell
    FLASK_ENV=development
    ```

* 在生产环境中部署程序时，绝不能开启调试模式，会带来巨大的安全隐患

1. 调试器
2. 重载器



* 当在一个新电脑创建运行环境时，使用pipenv install 命令时需要添加额外的--dev选项才会安装dec-packages部分定义的开发依赖包



## 1.4 Python Shell

```shell
flask shell
```

* `exit()`或`quit()`退出



## 1.5 Flask扩展



## 1.6 项目配置

Flask提供了很多种方式来加载配置:

* 字典中添加键值, 配置的名称必须全大写

  ```python
  app.config['ADMIN_NAME']='Peter'
  ```

* 使用update()方法

  ```python
  app.config.update(
      TESTING=True,
      SECRET_KSY='_5#yF4Q8z\n\xec]/'
  )
  ```

* 还可以把配置变量存储在单独的Python脚本，JSON格式的文件或者是Python类中

* 尽量在加载配置的操作提前，最好在程序实例app创建后就加载配置



## 1.7 URL与端点

* 用Flask提供的`url_for()`函数获取url

* `url_for()`:

  * 第一个参数endpoint, 端点

  ```python
  @app.route('/hello/<name>')
  def greet(name):
      return '<h1>Hello %s</h1>' % name
  ```

  * 这时用`url_for('greek',name='Jack'),得到的URL为"/hello/Jack"`

* `url_for()`生成的是相对URL，如果想要生成绝对URL，_external参数设为True



## 1.8 Flask 命令

* 通过创建任意一个函数，并为其添加`app.cli.command()`装饰器，就可以注册一个flask命令

  ```python
  @app.cli.command()
  def hello():
      """Just say hello"""
      click.echo('Hello, Human!')
  # 打印一行问候
  ```

* 在shell里输入`flask hello`就会出现 Hello, Human!
* 在shell里输入`flask --help`会出现命令帮助文档



### 1.9 模板与静态文件

* 模板 -- template
  * 包含程序页面的HTML文件
  * 默认存放在template文件夹中
* 静态文件 -- static file
  * 需要在HTML中加载的CSS和JavaScript文件
  * 以及图片、字体文件等资源
  * 默认存放在static文件夹
* 建议在开发环境下使用本地资源



## 1.10 Flask 与 MVC架构

MVC架构中，程序被分为三个组件：

* 数据处理（Model）
* 用户界面（View）
* 交互逻辑（Controller）