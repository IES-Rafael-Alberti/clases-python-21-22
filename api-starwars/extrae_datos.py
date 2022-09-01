import requests
import json

base_url = "https://swapi.dev/api/"

resources = ["people", "films", "planets", "starships", "species"]

def download_data(url):
	api_url = url
	result = []
	while True:
		response = requests.get(api_url, verify=False)
		data = response.json()
		for item in data["results"]:
			result.append(item)
		if data["next"] is None:
			break
		api_url = data["next"]
	return result

if __name__ == "__main__":
	for resource in resources:
		data = download_data(base_url+resource+"/")
		manf = open(resource+".py", "w")
		json.dump(data, manf, indent=4)
		manf.close()
