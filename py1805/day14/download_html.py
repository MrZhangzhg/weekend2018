from urllib import request
import os
import re

def download_file(url, dest_dir):
    dst_fname = url.split('/')[-1]
    dst_fname = os.path.join(dest_dir, dst_fname)
    html = request.urlopen(url)
    with open(dst_fname, 'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

def get_patt(fname, patt):
    patt_list = []
    cpatt = re.compile(patt)
    with open(fname, 'rb') as fobj:
        while True:
            try:
                line = fobj.readline().decode('utf8')
            except:
                continue
            if not line:
                break
            m = cpatt.search(line)
            if m:
                patt_list.append(m.group())
    return patt_list

if __name__ == '__main__':
    if not os._exists('/tmp/netease'):
        os.makedirs('/tmp/netease')
    download_file('http://sports.163.com/index.html', '/tmp/netease')
    url_patt = 'http://[^\s;)(:]+\.(png|jpeg|jpg)'
    url_list = get_patt('/tmp/netease/index.html', url_patt)
    for img_url in url_list:
        download_file(img_url, '/tmp/netease')
