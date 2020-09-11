import random,sys,requests

def facts():
    # for _ in range(4):
    i = random.randint(0,4)

    games= ["Super Mario Bros.","Contra","Pong","Tetris","Return of Arcade"]

    url_s = "http://www.gamespot.com/api/games/?api_key="
    api_key = "fcfc08ce9023a7d999d9c5f4e8af5f531de829c7"
    name=games[i]
    queries = "&field_list=name,release_date,themes,franchises&format=json&limit=1&filter=name:"+name

    url = url_s+api_key+queries
    headers = {'user-agent': 'my-app/0.0.1'}

    data = requests.get(url, headers=headers)

    game_data = eval(data.text)
    name=game_data['results'][0]['name']
    release_date=game_data['results'][0]['release_date']
    franchise=game_data['results'][0]['franchises'][0]['name']
    return [name,release_date,franchise]

facts()