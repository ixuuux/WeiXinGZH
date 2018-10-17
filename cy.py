import random
import requests

def cy(key):
    # key须为一个汉字
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28204&&format=json&query=成语接龙 {}'.format(key)
        data = requests.get(url, headers=headers, timeout=3).json()
        # print(data)
        if data.get('data')[0]:
            results = data.get('data')[0].get('result')
            # 从结果中随机选择一个成语
            result = random.choice(results)
            # return random.choice(results).get('ename')
            return '<a href="{}">{}</a>'.format(result.get('jumplink'), result.get('ename'))  # 带有释义链接
        else:
            return '恭喜，你赢了百度！ ☺'
    except:
        return '程序似乎出现了问题 -_- '

if __name__ == '__main__':
    test = cy('百')
    print(test)
