import requests

try:
    web = input("Enter the website. : ")
    website = "https://"+web
    r = requests.get(website)
    if r.status_code == 200:
        print(f"The website '{website}' is up and running.")

except ConnectionError:
    print(f"The website '{website}' is down.")