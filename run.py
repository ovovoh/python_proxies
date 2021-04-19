'''
构建简易的代理池
'''
import requests
#
# url='https://www.proxy-list.download/api/v1/get?type=http'

# resp=requests.get(url)

# print(resp.text)
# with open('proxies/'+"ip.txt",mode='wb') as f:
#     f.write(resp.content)
with open("proxies/"+'ip.txt') as lines:
    for line in  lines:

        proxies={
            "http":f'http://{line}',
            "https":f'http://{line}'
        }
        url = 'http://www.trackip.net/i'
        try:
            resp = requests.get(url,proxies=proxies,timeout=5)
            print('能使用',line)
        except Exception as e:
            print('不能使用',line)


