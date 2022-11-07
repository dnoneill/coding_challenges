import requests, json 

url = requests.get("https://annonatatencsu.github.io/hon202_fall2022/manifests/iiif/chapter2/manifest.json")

text = url.text
print(type(text))

data = json.loads(text)

for canvas_item in data['items']:
	for annotation_dict in canvas_item['annotations']:
		print(annotation_dict)
