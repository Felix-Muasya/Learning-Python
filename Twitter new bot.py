# My first attempt at creating a bot that reads breaking news, summarizes it n saves it as a word doc :)

#imports

import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize