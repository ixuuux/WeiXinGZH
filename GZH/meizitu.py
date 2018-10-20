# -*- coding: utf-8 -*-
from lxml import etree
import random
from requests_get import get
def meizi():
    try:
        headers = [{
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }, {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5'}]
        r = get(url='http://mzitu.com/zipai/', headers=random.choice(headers), timeout=3, try_max_num=5).text
        html = etree.HTML(r)
        img_urls = html.xpath('//p/img/@src')
        # return '<a href="{}">点击查看</a>'.format(random.choice(img_urls))
        return '\n'.join(['<a href="{i}">点击查看</a>'.format(i=i) for i in img_urls])
    except:
        return '程序似乎出现了一些问题 -_-\n请稍后重试'

if __name__ == '__main__':
    a = meizi()
    print(a)
