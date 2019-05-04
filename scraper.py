import requests
import bs4
import pandas as pd
import json


def basicSoup(url):
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, 'lxml')
    return soup


data = {}
myUrl = "https://www.onlinekhabar.com/content/business/technology"

for i in range(1, 207):
    print("Doing page ", i)
    url = myUrl+'/page'+str(i)
    soup = basicSoup(url)

    allNews = soup.find(name='div', attrs={'class': 'list_child_wrp'})
    urls = list(set([a['href']
                     for a in allNews.findAll(name='a', href=True)]))

    for url in urls:
        soup = basicSoup(url)
        heading = soup.find(name='h2', attrs={'class': 'mb-0'})

        paragraphs = soup.find(name='div', attrs={
            'class': 'col colspan3 main__read--content ok18-single-post-content-wrap'})

        paragraph = [paragraph.get_text(strip=True)
                     for paragraph in paragraphs.findAll('p')]

        data[heading] = paragraphs

json.dumps(data)
