import requests

reaction_id = "R00200"  # Remplace par ton ID de réaction KEGG
url = f"https://rest.kegg.jp/get/{reaction_id}"

response = requests.get(url)
print(response.text)

### multiple possibilities to be tested 
## Either ModelSeed, MetaNetX, or BiGG database

## In this script i will try to use ...


