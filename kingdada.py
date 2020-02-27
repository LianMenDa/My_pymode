import os, datetime, urllib.request


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
def runtime(starttime, endtime):
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
