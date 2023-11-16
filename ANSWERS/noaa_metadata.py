from pprint import pprint
import requests

URLS = {
    'stations': (
        'https://www.ncdc.noaa.gov/cdo-web/api/v2/stations',
        {'locationid': "FIPS:51"}
    ),
}

TOKEN = 'RZvAuJvzafAimtwbJFmORyXQbOpEoVId'

session = requests.Session()
session.headers.update({'token': TOKEN})

for url_name, (url, params) in URLS.items():
    print(f"**** {url_name.upper()} ****")
    response = session.get(
        url,
        params=params,
        verify=False,
    )

    pprint(response.json())
    print('-' * 60)
