#this file is unused

# run: pip install zuora-swagger-client
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure the API key given when signed up
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'db0e47ce3f844d46a91200336242804'

# Create an instance of the API Class
api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
q = '51.11,9.851' 
# This is the parameter that the API uses for location data, currently using 'lat,lon' notation
lang = 'de'
# This parameter is optional, but if included would currently give 
# the weather data in the german language

try:
    # Realtime Weather
    api_response = api_instance.realtime_weather(q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->realtime_weather: %s\n" % e)