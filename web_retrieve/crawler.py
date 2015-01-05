#coding: utf-8
import urllib as ulib
from time import strftime, localtime
import re
import os

#使用方法在文件末尾。
REG_LIST = (
            ('css', re.compile("""<link.*?href=["'](.*?css)['"].*?>""", re.I)),
            ('js', re.compile("""<script.*?src=["'](.*?js)["'].*?""", re.I)),
            ('img', re.compile("<img.*?\ssrc=[\'\"](.*?)[\'\"].*?>", re.I)),
            ('lazyload img', re.compile("""<img.*?(data-src|original)=['"](.*?)['"].*?>""", re.I)),
            ('swf', re.compile("[\'\"](http.*?\.swf)[\'\"]", re.I)),
           )

def crawl(url, date_trunk):
    rsp = ulib.urlopen(url)
    web_dir = os.path.join(date_trunk, gen_name(url))
    content = rsp.read()
    for craw_type, reg in REG_LIST:
        print 'Crawling %s...' % craw_type
        content = rsc_crawl(content, web_dir, reg, url)
    gen_html(web_dir, content)

def gen_name(url=None):
    time_now = strftime("%Y%m%d", localtime())
    if url:
        name = '_'.join((url, time_now))
    return name

def init_trunk(trunk):
    if not os.path.exists(trunk):
        os.mkdir(trunk)

def gen_html(name, content):
    file_name = ''.join((name, ".html"))
    with open(file_name, 'w') as f:
        f.write(content)

def rsc_crawl(content, trunk, reg, base_url):
    rsc_sum = 0
    bad_rsc = 0
    downloaded = []
    base_url = base_url.rstrip('/')
    rsc_urls = reg.findall(content)
    web_dir = trunk[trunk.index(os.path.sep)+1:]
    init_trunk(trunk)

    for url in rsc_urls:
        if isinstance(url, tuple):
            url = url[-1]
        try:
            rsc_name = url[url.rindex("/")+1:] if '&' not in url else url[url.rindex("/")+1:].split('&')[0]
        except ValueError:
            continue

        if url.startswith("//"): #workaround for baidu
            req_url = ''.join(("http:", url))

        if url.startswith("/"):
            req_url = ''.join((base_url, url))

        if url.startswith("http://"):
            req_url = url
            try:
                if rsc_name not in downloaded:
                    ulib.urlretrieve(req_url, os.path.join(trunk, rsc_name))
                    rsc_sum += 1
                    downloaded.append(rsc_name)
                    print "%s OK" % rsc_name
                content = content.replace(url, os.path.join(web_dir, rsc_name))
            except Exception as e:
                print "cannot download this: %s" % rsc_name

        else:
            print 'invalid %s' % url
            print reg.pattern
            bad_rsc += 1
    print "Success: %d, Failed: %d" % (rsc_sum, bad_rsc)
    print '#'*50
    return content

if __name__ == "__main__":
    """使用方法
将想要爬取的网站完整url（带http前缀）放入下方url_list中，多个用逗号隔开。
运行，在命令行输入: python crawler.py
会在此目录下获取网页：每个网页包括一个html和素材目录。文件名称为url关键字＋时间（年月日小时分秒)。
    """
    url_list = ["http://www.appgame.com/","http://www.gamelook.com.cn/","http://www.mofang.com/","http://www.18183.com/","http://www.18touch.com/","http://www.youxiduo.com/","http://www.ptbus.com/","http://www.9game.cn/","http://games.qq.com/mobile/","http://bbs.9game.cn/","http://www.mgamer.cn/","http://www.youxituoluo.com/","http://www.youxiputao.com/","http://www.17173.com/"]

    date_trunk = strftime("%Y%m%d", localtime())
    init_trunk(date_trunk)
    for url in url_list:
        crawl(url, date_trunk)


"""
LOG 1.1
--
已处理：
1.异步图片lazyload
2.swf,待完善
3.重构

待整理：
1、正则问题，不需要分js，cs之类，直接匹配["'].*?\.(js|css|jpg|jpeg|png|gif|swf)["']
2、非并发，效率低，但考虑到使用环境安装grequests较麻烦，未调用并发。
3. swf
"""
"""
lazyload img:
Invalid: lazyloadplaceholder, spacer, 18touch-lazy-img, common-558-icon
load_tag: data-src, data-original,
"""
