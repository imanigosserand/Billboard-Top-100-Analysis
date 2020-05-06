S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Michael Jackson",
    "prop": "pageimages",
    "pithumbsize": 5000
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

num = list(DATA['query']['pages'].keys())[0]

img = DATA['query']['pages'][num]['thumbnail']['source']
print(DATA)
# PAGES = DATA['query']['pages']

# for k, v in PAGES.items():
#     for img in v['images']:
#         print(img["title"])
#         print(v)

input = img
algo = client.algo('opencv/SkinColorDetection/0.1.19')
algo.set_options(timeout=300) # optional
result = algo.pipe(input).result[0]
print(result)
# red_min, red_max, green_min, green_max, blue_min, blue_max

plt.imshow([[(result[0]/255.0, result[2]/255.0, result[4]/255.0)]])
plt.imshow([[((result[0] + result[1])/2/255.0, (result[2] + result[3])/2/255.0, (result[4] + result[5])/2/255.0)]])