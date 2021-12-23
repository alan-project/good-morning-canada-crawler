import requests as requests
import json

category_list = ['technology']
# category_list = ['top', 'sports', 'business', 'entertainment', 'health', 'politics', 'technology']

url = "https://newsdata.io/api/1/news"
curPage = 0
curCategory = 0
for category in category_list:
    params = {'apikey': 'pub_2967e2652fda502b2fc1fae5062eac00ce50', 'domain': 'ctvnews, cbc,globalnews,cp24',
              'category': {category}, 'page': {curPage}}
    response = requests.get(url, params)
    json_data = response.json()
    print(json_data)
    article_list = json.dumps(json_data["results"])
    print(article_list)

    while json_object["nextPage"] is not None:
        curPage = curPage + 1
        params = {'apikey': 'pub_2967e2652fda502b2fc1fae5062eac00ce50', 'domain': 'ctvnews, cbc,globalnews,cp24',
                  'category': {category}, 'page': {curPage}}
        response = requests.get(url, params)
        json_data = json.dumps(response.json())
        json_object = json.loads(json_data)
        article_list = article_list + json_object["results"]

    print(category)
    print(article_list)

    curCategory = curCategory + 1
