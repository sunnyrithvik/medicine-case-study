#!/usr/bin/env python
# coding: utf-8

# # Importing required libraries

# In[1]:


import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


# # Reading link from a csv file

# In[2]:


datfr = pd.read_csv('datawebsite.csv')


# In[3]:


datfr


# In[4]:


url = datfr['website'][0]


# In[5]:


url


# # Web Scraping using BeautifulSoup

# In[6]:



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')


# In[7]:


soup


# In[8]:


print(soup.prettify())


# In[9]:


numb = soup.find('div',class_='auto-tabs-container')
cont = numb.find('span').text
print(cont)
print(type(cont))


# In[10]:


bad_chars = '()'
translator = str.maketrans('', '', bad_chars)
clean_digits = cont.translate(translator).strip()
print(clean_digits)


# In[11]:


cd = int(clean_digits)
if cd >= 20:
    lnt = 20
elif cd<20:
    lnt = cd


# In[12]:


commentlist=[]


# In[13]:


cs = soup.find('div', class_='reviews-page')
content = cs.find_all('p')


# In[14]:


for i in range(7,(7+lnt)):
    commentlist.append(content[i].text)


# In[15]:


len(commentlist)


# In[16]:


for i in range(len(commentlist)):
    print(i)
    print(commentlist[i])


# In[17]:


datelist=[]


# In[18]:


ds = soup.find_all('div',class_='date')
print(ds)


# In[19]:


for i in range(0,lnt):
    datelist.append(ds[i].text)


# In[20]:


datelist


# In[21]:


ns = soup.find_all('div',class_='details')
print(ns)


# In[22]:


namelist=[]


# In[23]:


'''
for i in range(0,13):
    j = ns[i].text
    namelist.append(j.split(' ', 2)[1])
'''
for i in range(0,lnt):
    j = ns[i].text
    splword = '|'
    namelist.append(j.partition(splword)[0])


# In[24]:


namelist


# # Converting Obtained data into csv file

# In[25]:


urls=[]
titles_list = []
 
count = 1

for i in range(0,lnt):
    d = {}
    d['Author name'] = namelist[i].strip()
    d['Date of review'] =  datelist[i]
    d['Comment'] = commentlist[i].replace("Read More Read Less","")
    #d['Url'] = urls[i].append(url)
    count += 1
    titles_list.append(d)
d['Url'] = url


# In[26]:


filename = 'healthdata.csv'
with open(filename, 'w', newline='',encoding='utf-8') as f:
    w = csv.DictWriter(f,['Author name','Date of review','Comment','Url'])
    w.writeheader()
    
    w.writerows(titles_list)


# In[ ]:




