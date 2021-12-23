import requests as requests

category_list = ['top']
# category_list = ['top', 'sports', 'business', 'entertainment', 'health', 'politics', 'technology']

url = "https://newsdata.io/api/1/news"
curPage = 0
for category in category_list:
    params = {'apikey': 'pub_2967e2652fda502b2fc1fae5062eac00ce50', 'domain': 'ctvnews, cbc,globalnews,cp24',
              'category': {category}, 'page': {curPage}}
    response = requests.get(url, params)
    json = response.json()
    print(json)

    while json["nextPage"] is not None:
        curPage = curPage + 1
        params = {'apikey': 'pub_2967e2652fda502b2fc1fae5062eac00ce50', 'domain': 'ctvnews, cbc,globalnews,cp24',
                  'category': {category}, 'page': {curPage}}
        response = requests.get(url, params)
        json = response.json()
        json.append(json)
        print(json)

    print(json)
