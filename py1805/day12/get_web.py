from urllib import request

request = request.urlopen('http://www.baidu.com')
with open('/tmp/b.html', 'wb') as fobj:
    fobj.write(request.read())
