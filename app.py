from flask import Flask, render_template, url_for, request
import requests, unicodedata
from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer #We're choosing Lexrank, other algorithms are also built in


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/summarized', methods=['POST'])
def summarized():
    content = request.form['text-field']
    content_to_str = unicodedata.normalize('NFKD', content).encode('ascii','ignore')
    parser = PlaintextParser.from_string(content_to_str, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, 5)

    return render_template('summarized.html', summary = summary)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
