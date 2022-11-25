import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_blog():
    url = ' https://www.hibob.com/blog/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    links = []
    for link in soup.find("div", id="main").find_all("a"):
        data_blog = link.get('href')
        links.append(data_blog)
        
    return links

get_blog()

def get_info(urls):
    res = []
    for url in urls:
        data = {}
        blog = requests.get(url)
        soup = BeautifulSoup(blog.text, 'html.parser')
        for title in soup.find_all('title'):
            data['title'] = title.text
            data['link'] = url
            for date in soup.find('div', class_='info').find_all('time'):
                data['date'] = date.text
            data['description'] = soup.find('meta', attrs={'name': 'description'}).get('content')
            res.append(data)
    return res

results = get_info(get_blog())

df = pd.DataFrame(results)

df.to_csv('blog_data.csv', index=False)

