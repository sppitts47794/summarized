import os
import requests, urllib2
from flask import Flask, render_template, url_for, request

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from bs4 import BeautifulSoup

import nltk
from nltk import sent_tokenize

nltk.download('punkt')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/summarized', methods=['POST'])
def summary():
    return render_template(
        'summarized.html',
        summary = summarized(),
        header = get_title(),
    )

def summarized():
    # Requests data in forms
    URL = request.form['url-field']
    SENTENCES_COUNT = request.form['quantity']
    LANGUAGE = "english"

    # Summarization
    parser = HtmlParser.from_url(URL, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    list = []
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        list.append(sentence)

    return list

def get_title():
    # Requests data from url
    URL = request.form['url-field']
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.title.string
