# -*- coding: utf-8 -*-
# 给一个名字，返回签名图片
import requests, random
from lxml import etree

def qm(name, try_num=0):
	# 给定名字，返回签名图片链接
	if try_num < 2:
		try:
			style = ['haku.ttf',  # 合文签
					'haku.ttf',  # 合文签
					'jfcs.ttf',  # 个性签
					'qmt.ttf',  # 连笔签
					'zql.ttf',  # 商务签
					'zql.ttf',  # 商务签
					]
			s = random.choice(style)
			data = {
				'word': name,
				'sizes': '60',
				'fonts': s,
				'fontcolor': '#000000'
				}
			USER_AGENTS = [
				    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
				    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
				    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
				    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
				    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
				    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
				    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
				    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
				    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
				    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
				    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"]
			r = requests.post('http://www.uustv.com/', data=data, headers={'User-Agent': random.choice(USER_AGENTS)}, timeout=3)
			html = r.content.decode()
			img = etree.HTML(html)
			i = 'http://www.uustv.com/'+img.xpath('//div[@class="tu"]/img/@src')[0]
			if len(i) > 40:
				# 有时会得到虚假链接，加以判断
				# return '<img src="http://img.zcool.cn/community/0117e2571b8b246ac72538120dd8a4.jpg@1280w_1l_2o_100sh.jpg" alt="Alt text" title="Title text">'
				# img_name = i.split('/')
				# with open('./qianming_img/{}'.format(img_name[-1]), 'wb') as f:
				# 	f.write(requests.get(i).content)
				# return img_name[-1]
				return '<a href="{}">{}</a>'.format(i, s)
			else:
				return qm(name, try_num+1)
		except:
			return qm(name, try_num+1)
	else:
		return None

if __name__ == '__main__':
	info = qm('q霜')
	print(len(info))
	print(info)
