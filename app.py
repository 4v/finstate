from bottle import route, run, view
from bottle import template,static_file
import os

images_path = './files/image' #定义图片路径

def eachbook(fname):
    efnames = []
    for root, dirs, files in os.walk(fname):
        for efname in files:
            fullname = os.path.join(root, efname)
            efnames.append(fullname)
    return sorted(efnames) # , reverse=True

def getbase(images_path):
    books = []
    for root, dirs, files in os.walk(images_path):
        for name in dirs:
            # fname = os.path.join(root, name)
            books.append(name)
    return books

@route('/images/<filename:re:.*\.png>')
def server_static(filename):
    print(filename)
    return static_file(filename, root=images_path)

@route('/book/<book>')
@view('book')
def book(book):
    images_path = '/files/image'
    fname = os.path.join(images_path, book)
    books = eachbook(fname)
    info = {'title':book, 'books':books}
    return info

@route('/')
@view('index')
def index():
    images_path = './files/image'
    books = getbase(images_path)
    info = {'title':'目录', 'books':books}
    return info

@route('/hello')
@view('hello')
def hello():
    name="昝道广"
    blog="xzan.ngrok.cc"
    myfriend=['小昝','小道','小广']
    myinfodir={'age':20,'weight':130}
    info={'name':name,'age':myinfodir,'weight':myinfodir,'blog':blog,'SNS':myfriend}
    return info

run(host='0.0.0.0', port=8080, debug=True)

