from flask import Flask, render_template, jsonify, request, make_response, Markup
from nnw import parse_words, parse_word, mappings

import conf

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/words")
def words():
    words = request.args.get("words")
    if not words:
        return jsonify({"message":"words param cannot be null"})
    word_list = words.split(",")

    bad_words = parse_words(word_list)

    bad_words = [Markup.escape(word) for word in bad_words]

    return jsonify({"badwords": bad_words})

@app.route("/download")
def download():
    words = request.args.get("words", [])
    word_list = words.split(",")
    word_list = [word.strip() for word in word_list]
    bad_words = parse_words(word_list)

    resp_text = "\n".join(bad_words)

    response = make_response(resp_text)
    response.headers["Content-Type"] = 'text/plain'

    return response

@app.route("/masterlist")
def masterlist():
    #TODO: Compile this as a static file
    word_list = [
        "shit",
        "fuck",
    ]
    bad_words = parse_words(word_list)

    resp_text = ",".join(bad_words)
    return resp_text


if __name__ == "__main__":
    app.run(debug=conf.APP_DEBUG,
            port=conf.APP_PORT)
