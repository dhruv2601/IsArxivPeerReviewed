import json
import re
import random
import pickle
import time
from tqdm import tqdm
import random
import urllib
from kora.selenium import wd

arxiv_base_url = 'https://arxiv.org/abs/'
semantic_base_url = 'https://www.semanticscholar.org/search?q='
semantic_suffix = '&sort=relevance'

article_id = ''

# generate arxiv url
arxiv_url = arxiv_base_url + article_id
print(arxiv_url)

# to remove extra id appended to title
clean_id = '['+article_id+'] '
clean_len = len(clean_id)


# load page via selenium
wd.get(arxiv_url)
time.sleep(1)

# get title from selenium
title_element = wd.title

# clean the title
title = title_element[clean_len:]
print('\n'+title)

# convert title to query - url encode
query_title = urllib.parse.quote(title, safe='')

# construct URL for semantic scholar
query = semantic_base_url + query_title + semantic_suffix
print('\n'+query)

# load semantic scholar - sorted results
wd.get(query)
time.sleep(1)

# get list of papers
element_papers_links = wd.find_elements_by_xpath('//a[@class="flex-row cl-paper-view-paper"]')
print(len(element_papers_links))

# get the first result
element_papers_first = element_papers_links[0]

# get conference/arxiv paper URL 
paper_link = element_papers_first.get_attribute('href')

# get link button class 
paper_class = element_papers_first.find_element_by_class_name('cl-button__label')

# get publishing details text
paper_publish_text = paper_class.text

print('Results: \n')
print(paper_link)
print('\n')    
print(paper_publish_text)


# Handle the results according to your use-case
if 'arxiv' in paper_link:
  print('Arxiv Paper')
else:
  print('Peer-reviewed paper')