import requests,random
import re

def get_article():

    # list1 = ["Pac-Man Celebrates 40th Anniversary With Gorgeous New Arcade Cabinet","Prince Of Persia: The Sands Of Time Remake Officially Announced During Ubisoft Forward"]
    # list2 = ["Discord To Offer Limited Game Streaming Functionality","Confirmed Game Release Dates 2020: Xbox Series X, Xbox One, PS5, PS4, Switch, PC"]
    # list3 = ["Fall Guys Never Really Die; They Achieve Serenity And Then Respawn","Pokemon Developer's Other RPG Is Coming To Steam"]
    # list4 = ["Game Of The Year 2019 -- Sekiro: Shadows Die Twice","Super Mario 3D All-Stars Features Three Fantastic Platformers"]

    l=["Pac-Man Celebrates 40th Anniversary With Gorgeous New Arcade Cabinet",
    "Discord To Offer Limited Game Streaming Functionality",
    "Confirmed Game Release Dates 2020: Xbox Series X, Xbox One, PS5, PS4, Switch, PC",
    "Fall Guys Never Really Die; They Achieve Serenity And Then Respawn","Pokemon Developer's Other RPG Is Coming To Steam",
    "Game Of The Year 2019 -- Sekiro: Shadows Die Twice","Super Mario 3D All-Stars Features Three Fantastic Platformers"]


    def url(name):
        url_s = "http://www.gamespot.com/api/articles/?api_key="
        api_key = "fcfc08ce9023a7d999d9c5f4e8af5f531de829c7"
        queries = "&filter=title:"+name+"&field_list=title,authors,deck,lede,image,site_detail_url&format=json&limit=1"
        # queries = "&filter=title:"+name+"&field_list=image,site_detail_url&format=json&limit=1"
        return url_s+api_key+queries


    # urls = []
    # i = random.randint(0,1)
    # urls.append(url(list1[i]))
    # i = random.randint(0,1)
    # urls.append(url(list2[i]))
    # i = random.randint(0,1)
    # urls.append(url(list3[i]))
    # i = random.randint(0,1)
    # urls.append(url(list4[i]))

    urls=[]
    j=0
    for i in range(4):
        z=random.randint(0,7)
        if(j==z):
            i-=1
        j=z
        urls.append(url(l[i]))


    headers = {'user-agent': 'my-app/0.0.1'}
    # r1 = requests.get(urls[0], headers=headers)
    # r2 = requests.get(urls[1], headers=headers)
    # r3 = requests.get(urls[2], headers=headers)
    # r4 = requests.get(urls[3], headers=headers)
    x={}

    for j in range(4):
        r= requests.get(urls[j], headers=headers)
        data=eval(r.text)
        img=data['results'][0]['image']['square_small']
        i=img.replace('/',"")
        url_address=data['results'][0]['site_detail_url']
        u=url_address.replace('/',"")
        d={'author': data['results'][0]['authors'],
        'title':data['results'][0]['title'],
        'info':data['results'][0]['deck'],
        'img':i,'url':u}
        x[j]=d
    
    print(x)
    
    return x


# get_article()