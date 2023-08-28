import requests


APIkey="4ba6709e93de561c36c921d955ce9eff"
def get_data(place,forcast_days=None,kind=None):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response=requests.get(url)

    data = response.json()
    return data

if __name__=="__main__":
    print(get_data(place="Tokyo"))