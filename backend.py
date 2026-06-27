import requests

API_KEY = 'c9d83d125dcfcfe04341301f58cd9d5d'
def get_data(place,forecast_days=None):

        url =f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            filtered_data = data['list']
            nr_values = 8 * forecast_days
            filtered_data = filtered_data[:nr_values]
            return filtered_data
        else:
            return 'please enter a valid place'






if __name__=='__main__':
    print(get_data('London',2))