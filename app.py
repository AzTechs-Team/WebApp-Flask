from flask import Flask,render_template,url_for
import requests


app=Flask(__name__)

@app.route('/')
def index():
    games=['pong','donkeykong']
    return render_template('index.html',games=games)

@app.route('/game/pong')
def pingpong():
    data={
        'name':'Ping Pong',
        'desc':'Pong is a table tennis-themed arcade video game featuring simple two-dimensional graphics, manufactured by Atari and originally released in 1972.'
    }
    return render_template('game.html',data=data)

if __name__=='__main__':
    app.run(debug=True)