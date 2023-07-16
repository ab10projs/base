import requests
from bs4 import BeautifulSoup
#---------------------------------------------------------------------
"""
1) This is the code to connect to a site and get the text to a file
"""

website ='https://subslikescript.com/movie/Titanic-120338'
result= requests.get(website)

content = (result.text)
soup = BeautifulSoup(content, 'lxml')

#print(soup.prettify())
box= soup.find('article',class_ ='main-article')

# print(box.h1.text)
title= soup.find('h1').get_text(strip=True, separator=' ')
transcript = soup.find('div', class_ ='full-script').get_text(strip=True, separator=' ')
#print(transcript)

with open(f'{title}.txt','w', encoding="utf-8") as output:
    output.write(transcript)
print('done')

#---------------------------------------------------------------------
"""
2
This is the code to get text of multiple movies 

# https://subslikescript.com/movies  
this is the site of multiple movies in a list
"""
root= 'https://subslikescript.com'
website =f'{root}/movies'
result= requests.get(website)

content = (result.text)
soup = BeautifulSoup(content, 'lxml')

box = soup.find('article', class_ = 'main-article')

lists = []
for i in box.find_all('a',href=True):
    lists.append( i['href'])

print(lists)
for i in lists:
    print(root+"/"+i)
    website = root+"/"+i
    result = requests.get(website)
    content = (result.text)
    soup = BeautifulSoup(content, 'lxml')
    transcript = soup.find('div', class_ = 'full-script').get_text(separator=' ', strip=True)

    with open(f'{i}.txt', 'a', encoding="utf-8") as output:
        output.write(transcript)
print('done')


