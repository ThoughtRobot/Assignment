#!/usr/bin/env python
# coding: utf-8

# In[2]:


# install necessary packages to run this
# -pip install flask
# -pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def count_words(url='https://coder.today/tech/2018-10-27_10-examples-of-how-to-use-static-html-websites/'):
    
    #fetch html content
    response = requests.get(url)     
    
    #parse html using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')   
    
    #extarct text from HTMl
    text = soup.get_text()                                           

    # remove special characters and convert to lowercase
    text = ''.join(c for c in text if c.isalnum() or c.isspace())    
    text = text.lower()

    # split the text into words
    words = text.split()

    # count word occurrences
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    
    #get url from the request
    url = data.get('url')

    # if url not provied error is thrown
    if not url:
        return jsonify({'error': 'URL not provided'}), 400
    
    #count the words and return in json format
    word_count = count_words(url)
    return jsonify(word_count)

if __name__ == '__main__':
    app.run()


# In[ ]:




