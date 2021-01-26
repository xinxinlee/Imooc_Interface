from wsgiref.simple_server import make_server

def f1(requ):
    return ["<h1>hello yuan!</h1>".encode('utf8')]

def f2(requ):
    return ["<h1>hello alex!</h1>".encode('utf8')]

def application(environ, start_response):#这个函数也可以重写，这个括号里面的两个参数是固定格式
    print(environ)
    start_response('200 OK', [('Content-Type', 'text/html')])#相应头，告诉浏览器返回的是一个HTML数据
    path = environ['PATH_INFO']
    print(path)
    if path == "/yuan":
        return f1(environ)
    elif path == "/alex":
        return f2(environ)
    else:
        return ["<h1>hello world!</h1>".encode('utf8')]

httpd = make_server('127.0.0.1', 8089, application)

print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()#对象去启动这个访问hhhhghgg