#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import threading
import os
import asyncio
import argparse
import time

pathTextFile = ''
proxyType = ''
headers_mobile = { 'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'}

class LoadStopWatch:
    def __enter__(self):
        self.start = time.process_time()
        return self
    def __exit__(self, *args):
        self.end = time.process_time()
        self.delta = self.end - self.start

# From proxyscrape.com 
def proxyscrapeScraper(proxytype, timeout, country):
    response = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=" + proxytype + "&timeout=" + timeout + "&country=" + country)
    proxies = response.text
    with open(pathTextFile, "a") as txt_file:
        txt_file.write(proxies)


# From proxy-list.download
def proxyListDownloadScraper(url, type, anon):
    session = requests.session()
    url = url + '?type=' + type + '&anon=' + anon 
    html = session.get(url).text
    with open(pathTextFile, "a") as txt_file:
        for line in html.split('\n'):
            if len(line) > 0:
                txt_file.write(line)
                
# From sslproxies.org, free-proxy-list.net, us-proxy.org, socks-proxy.net
def makesoup(url):
    page=requests.get(url)
    return BeautifulSoup(page.text,"html.parser")

def proxyscrape(table):
    proxies = set()
    for row in table.findAll('tr'):
        fields = row.findAll('td')
        count = 0
        proxy = ""
        for cell in row.findAll('td'):
            if count == 1:
                proxy += ":" + cell.text.replace('&nbsp;', '')
                proxies.add(proxy)
                break
            proxy += cell.text.replace('&nbsp;', '')
            count += 1
    return proxies

def scrapeproxies(url):
    soup=makesoup(url)
    result = proxyscrape(table = soup.find('table', attrs={'id': 'proxylisttable'}))
    proxies = set()
    proxies.update(result)
    with open(pathTextFile, "a") as txt_file:
        for line in proxies:
	        txt_file.write("".join(line) + "\n")


# output watcher
def output():
    if os.path.exists(pathTextFile):
        os.remove(pathTextFile)
    elif not os.path.exists(pathTextFile):
        with open(pathTextFile, 'w'): pass

def check_connect(data):
    try:
        with LoadStopWatch() as ya_ping:
            yandex = requests.get('https://yandex.ru/', proxies = { 'https' : 
            data['proxyType'] + "://" + data['ip']+":"+data['port'] }, headers = headers_mobile, timeout = 2)
        data['ping_to_yandex'] = round(ya_ping.delta, 3)
    except:
        data['ping_to_yandex'] = 99999
    try:
        with LoadStopWatch() as go_ping:
            google = requests.get('https://www.google.com/humans.txt', proxies = { 'https' : 
            data['proxyType'] + "://" + data['ip']+":"+data['port'] }, headers = headers_mobile, timeout = 2)

        data['ping_to_google'] = round(go_ping.delta, 3)
    except:
        # print('Google -> BAD', data)
        data['ping_to_google'] = 99999 
        
    if data['ping_to_yandex'] == 99999 and data['ping_to_google'] == 99999:
        print('bad', data)
    else:
        print('GOOD', data)
        country = requests.get('https://ipwhois.app/json/'+data['ip'],headers = headers_mobile, timeout = 10)
        data['country'] = country.json()['country']
        response = requests.post('http://nginx/api/get_proxy/', data = data)

def start_checker(type_p,filename):
    with open(filename, 'r') as proxy_list:
        ip_port = proxy_list.readlines()
        threads_count = 0
        for elem in ip_port:
            if threads_count == 20:
                time.sleep(2)
                threads_count = 0
            data = {'ip': elem.split(":")[0], 'port': elem.split(":")[1].rstrip(), 'proxyType': type_p, 'country': 'NONE', 'ping_to_google': 0 , 'ping_to_yandex': 0}
            threading.Thread(target=check_connect, args=(data,)).start()
            threads_count += 1


if __name__ == "__main__":

        response = requests.get('http://nginx/api/get_proxy/delete_all/')

        print(response.text)
        if 'Success' in response.text:
            response = requests.get('http://nginx/api/update_time/update_time/')
            pathTextFile = "socks5.txt"
            output()
            threading.Thread(target=proxyscrapeScraper, args=('socks5','1000','All',)).start()
            threading.Thread(target=proxyListDownloadScraper, args=('https://www.proxy-list.download/api/v1/get', 'socks5', 'elite',)).start()
            time.sleep(5)
            start_checker("socks5",pathTextFile)
                
            pathTextFile = "socks4.txt"
            output()
            threading.Thread(target=proxyscrapeScraper, args=('socks4','1000','All',)).start()
            threading.Thread(target=proxyListDownloadScraper, args=('https://www.proxy-list.download/api/v1/get', 'socks4', 'elite',)).start()
            time.sleep(5)
            start_checker("socks4",pathTextFile)
       
