import requests 
from bs4 import BeautifulSoup 
  
url = 'https://www.postimees.ee/'
response = requests.get(url) 
  
soup = BeautifulSoup(response.text, 'html.parser') 
headlines = soup.find('body').find_all('h2') 
unwanted = ['BBC World News TV', 'BBC World Service Radio', 
            'News daily newsletter', 'Mobile app', 'Get in touch'] 
i = 0
print(list(dict.fromkeys(headlines)))
for x in list(dict.fromkeys(headlines))[:3]: 
    if x.text.strip() not in unwanted:
        print(x.text.strip()) 