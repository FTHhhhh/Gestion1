import requests

r = requests.get('https://v2.jokeapi.dev/joke/Any?lang=fr')

json_blague = r.json()

if "setup" in json_blague:
    print("Question: " + json_blague["setup"])
    print("Reponse: " + json_blague["delivery"])
