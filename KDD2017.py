# -*- coding: utf-8 -*-
"""
Crawl all KDD papers by years
Get their citations number by crawling Google Scholar （still has some problems when querying citations of some papers）
Sort papers by their citations number (TODO...)

Author: Qiuchen Zhang
"""

import requests
import scholarly
from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = "http://www.kdd.org/kdd2017/accepted-papers"
    cur_page = requests.get(url)
    soup = BeautifulSoup(cur_page.text, 'html.parser')
    p_list = soup.find_all('a')

    paper_dict = {}
    for p in p_list:
        if 'papers/view' in str(p.attrs['href']):
            print "*******************************"
            print p.attrs['href']
            print p.text
            paper_title = p.text.replace(u'\xa0', u' ')
            search_query = scholarly.search_pubs_query(paper_title)
            paper = next(search_query).fill()
            try:
                paper_dict[p.text] = paper.citedby
            except AttributeError:
                paper_dict[p.text] = 0


