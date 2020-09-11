from flask import Flask,render_template,url_for,send_file,flash,request
from facts import facts
from articles import get_article


app=Flask(__name__)

app.secret_key="hello"
article_data=get_article()

@app.route('/')
def index():
    # if(request.method == 'POST'):
    #     # game_facts=facts()
    #     return flash("hello")
    # else:
    games=['pong','space invaders']
    game_facts=facts()
    return render_template('index.html',data=[games,game_facts])

@app.route('/game/pong')
def pingpong():
    data={
        'name':'Ping Pong',
        'desc':'Pong is a table tennis-themed arcade video game featuring simple two-dimensional graphics, manufactured by Atari and originally released in 1972.'
    }
    return render_template('game.html',data=data)


@app.route('/download')
def download():
    return send_file('.\static\games\pong.zip', as_attachment=True)


@app.route('/articles')
def articles():
    return render_template('article.html',data=article_data)


if __name__=='__main__':
    app.run(debug=True)