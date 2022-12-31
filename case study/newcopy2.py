#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

urls = []
for iter in range(2, 75):
    txt = "https://www.webmd.com/drugs/drugreview-9690-ambien-oral?conditionid=&sortval=1&page={numb}&next_page=true"
    dut = txt.format(numb=iter)

    response = requests.get(dut, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')


    numb = soup.find('div', class_='auto-tabs-container')
    cont = numb.find('span').text

    pgenum = soup.find_all('div', class_='pagination-holder')

    for pg in pgenum:
        sl = pg.find('li', class_='page-item pagination-item--active').text
        print(sl)


    bad_chars = '()'
    translator = str.maketrans('', '', bad_chars)
    clean_digits = cont.translate(translator).strip()
    print(clean_digits)
    lnt = min(20, int(clean_digits)-20*iter)
    print(lnt)


    commentlist = []

    cs = soup.find('div', class_='reviews-page')
    content = cs.find_all('p')

    for i in range(7, (7 + lnt)):
        commentlist.append(content[i].text)

    len(commentlist)

    for i in range(len(commentlist)):
        print(i)
        print(commentlist[i])

    datelist = []

    ds = soup.find_all('div', class_='date')
    print(ds)

    for i in range(0, lnt):
        datelist.append(ds[i].text)

    ns = soup.find_all('div', class_='details')
    print(ns)

    namelist = []


    for i in range(0, lnt):
        j = ns[i].text
        splword = '|'
        namelist.append(j.partition(splword)[0])

    titles_list = []

    count = 1
    for i in range(0, lnt):
        d = {}
        d['Author name'] = namelist[i].strip()
        d['Date of review'] = datelist[i]
        d['Comment'] = commentlist[i].replace("Read More Read Less", "")
        count += 1
        titles_list.append(d)

    filename = 'healthdata2.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, ['Author name', 'Date of review', 'Comment'])
        w.writeheader()

        w.writerows(titles_list)





