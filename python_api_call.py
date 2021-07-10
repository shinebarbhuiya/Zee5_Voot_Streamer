import requests

link = input("Enter the movie link:")

url = f"https://zee5api.herokuapp.com/z5api.php?q={link}"

r = requests.get(url, headers= {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"})


json_data = r.json()


title = json_data['title']
desc = json_data['description']
thumbnail = json_data['thumbnail']
main_link = json_data['video_url']

