from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
# Imports flask modules
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/summarized', methods=['POST'])
def summarized():
    # Requests data in forms
    URL = request.form['url-field']
    SENTENCES_COUNT = request.form['quantity']
    LANGUAGE = "english"

    parser = HtmlParser.from_url(URL, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    bullets = []
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        bullets.append(sentence)

    return render_template('summarized.html', summary = bullets)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
