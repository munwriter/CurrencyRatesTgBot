from os import getenv

import requests
from dotenv import load_dotenv

load_dotenv()
url = "https://api.apilayer.com/currency_data/change?start_date=2018-01-02&end_date=2018-01-01"
headers = {
    'apikey': getenv('API_KEY')
}
response = requests.request('GET', url, headers=headers)
print(response.text, response.status_code)