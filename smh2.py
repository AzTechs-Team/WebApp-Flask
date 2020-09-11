import random,sys,requests

for _ in range(4):
	value = random.randint(1,2)
	print(value)

list1 = ["Pac Man", "Super Mario Bros."]
list2 = ["Contra", "Pong"]
list3 = ["tetris","Return of Arcade"]
list4 = ["Tetris", "Tetris"]

url_s = "http://www.gamespot.com/api/games/?api_key="
api_key = "fcfc08ce9023a7d999d9c5f4e8af5f531de829c7"
name = list1[1]
queries = "&field_list=name,release_date,themes,franchises&format=json&limit=1&filter=name:"+name

url = url_s+api_key+queries

headers = {'user-agent': 'my-app/0.0.1'}
r1 = requests.get(url, headers=headers)
game_data = eval(r1.text)
# game_data = eval("{'error': 'OK', 'limit': 1, 'offset': 0, 'number_of_page_results': 1, 'number_of_total_results': 23, 'status_code': 1, 'results': [{'release_date': '2006-05-15 12:00:00', 'name': 'New Super Mario Bros.', 'themes': [], 'franchises': [{'name': 'New Super Mario Bros.'}]}], 'version': '1.0'}")
# print("Release Date : ",game_data["results"][0]["release_date"],"\n","This shit is working :)")
sys.exit()
