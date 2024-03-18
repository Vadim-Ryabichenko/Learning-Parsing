import requests



with open('proxy_list.txt') as file:
    proxys = ''.join(file.readlines()).strip().split('\n')
    
for proxy in proxys:
    proxies = {
        'http': f'http://{proxy}',
        'https': f'https//{proxy}'
    }

    try:
        link = 'http://icanhazip.com/'
        responce = requests.get(link, proxies=proxies, timeout=5).text
        print(f'IP: {responce}')
    except:
        print('Proxy error')