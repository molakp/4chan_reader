from flask import Flask, render_template
from helpers.scraper import *

app = Flask(__name__)
from flask_cors import CORS
CORS(app)


@app.route('/')
def index():
    board_name='pol'
    board_url = 'https://boards.4chan.org/' + board_name
    threads = get_threads(board_url)
    #print(threads)  # Stampa la lista dei thread per debug
    return render_template('index.html', threads=threads)


@app.route('/thread/<thread_id>')
def thread(thread_id):
    # Code to retrieve thread details from thread_id
    # Assume the thread is represented as a Python object with attributes like title, posts, etc.
    thread = get_thread_details('pol',thread_id)
    return render_template('thread.html', thread=thread)


if __name__ == '__main__':
    app.run(debug=True)
