from flask import Flask, jsonify, render_template, request, flash
import requests
import json
import os
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.secret_key = "NImit2801"


@app.route('/smh')
def new_api():
    # url = 'http://www.gamespot.com/api/videos/?api_key=fcfc08ce9023a7d999d9c5f4e8af5f531de829c7&limit=1&field_list=title&format=json'
    url2 = 'http://www.gamespot.com/api/games/?api_key=fcfc08ce9023a7d999d9c5f4e8af5f531de829c7&filter=name:mario&limit=2&format=json'
    headers = {'user-agent': 'my-app/0.0.1'}
    r1 = requests.get(url2, headers=headers)
    # x = json.loads(r1.text)
    # print(x["results"][0]["title"])
    y = eval(r1.text)
    print(type(y))
    return y


@app.route('/audio', methods=['GET', 'POST'])
def audio():
    if(request.method == 'POST'):
        result = eval(request.form['expression'])
        flash(result)
        return flash(result)
    return render_template('audio.html')


if __name__ == '__main__':
    app.run(debug=True)
