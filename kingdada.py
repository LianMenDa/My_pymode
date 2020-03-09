import os, datetime, urllib.request, time, requests


# 创建文件夹
def make_dirs(dirsname):
    # 移除空格
    path = dirsname.strip()  # 首尾空格
    isdone = os.path.exists(path)
    if not isdone:
        os.makedirs(dirsname)
        print('创建了目录');  # 信号发送
        print(dirsname);  # 信号发送
    else:
        print('目录已经存在');  # 信号发送


# 创建文件
def make_file(filename):
    # 移除空格
    path = filename.strip()  # 首尾空格
    isdone = os.path.exists(path)
    if not isdone:
        fh = open(filename, 'a')
        fh.close()
        print('创建了文件');  # 信号发送
        print(filename);  # 信号发送
    else:
        print('文件已存在')


# 计算运行时间
def get_runtime(starttime, endtime):
    i = int(endtime - starttime)
    time = datetime.timedelta(seconds=i)
    print('程序总运行时间为:', time)


# 获取网页源码
def get_urldata(url, code='utf-8'):
    headers = ("User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode(code)
    return data


# 获取文件大小
def get_bytes(number):
    symbols = ('KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    prefix = dict()
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if int(number) >= prefix[s]:
            value = float(number) / prefix[s]
            return '%.2f%s' % (value, s)
    return "%sB" % number


# 下载文件显示速度，大小
def downloadFile(name, url):
    r = requests.get(url, stream=True)
    length = float(r.headers['content-length'])
    size = get_bytes(length)
    print('此文件大小为' + size)
    f = open(name, 'wb')
    count = 0
    count_tmp = 0
    time1 = time.time()
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)
            count += len(chunk)
            if time.time() - time1 > 2:
                p = count / length * 100
                speed = (count - count_tmp) / 1024 / 1024 / 2
                count_tmp = count
                print(name + ': ' + formatFloat(p) + '%' + ' Speed: ' + formatFloat(speed) + 'M/S')
                time1 = time.time()
    f.close()


def formatFloat(num):
    return '{:.2f}'.format(num)
