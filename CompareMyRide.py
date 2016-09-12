import requests
import json
import sys


uber_client_id = "YQIgetGmABtkErAUcgQ2-po207TvJg8c"
uber_client_secret = "of9PtO1hfHIo-L2pw80lr3amblltOSU6ZS2FJI3s"
uber_server_token = "Gok6o1f9mdRYJR78A9WW3fAmdpAKAC5e_WyPp5S9"

lyft_client_id = "JpWPeznr4Y4Y"
lyft_client_token = "gAAAAABX1vxNONlyqn0Id7Rv-WyZPvNAq_u-z5lhSghC0dAZnCUv-_snT1br8mSXlH0DpAx-JFCg6ijp4XAd9Q8Atw_ZFSQHnhEaV-rdHx3C3N2FaLeCl_-02ZM8f2jrEfgMAZ0io9daVt-oVIIHopHG1W3FGs9as2mUm6NaiIPr5UjKWJ3qqfs="
lyft_client_secret = "3BP5tUBf8N3IWdfltvgdWWLSpKorn6JM"

curl -X POST -H "Content-Type: application/json" \
     --user "JpWPeznr4Y4Y":"xxmulseLmBjJU79x82K9E4mgfqvJhRaZ" \
     -d '{"grant_type": "client_credentials", "scope": "public"}' \
     'https://api.lyft.com/oauth/token'
     
args = sys.argv[1:]

if len(args) != 4:
    print("You must enter four arguments: the start longitude, start lattitude, end longitude, and end lattitude")
    quit()
else:
    start_lat = float(args[0])
    start_lon = float(args[1])
    end_lat = float(args[2])
    end_lon = float(args[3])

# these are just placeholders for now
    start_lat = 37.775818
    start_lon = -122.418028
    end_lat = 37.774231
    end_lon = -122.41293

    uber_url = "https://api.uber.com/v1/estimates/price"

    lyft_url = "https://api.lyft.com/v1/cost"

    uber_parameters = {
        'server_token': uber_server_token,
        'start_latitude': start_lat,
        'start_longitude': start_lon,
        'end_latitude': end_lat,
        'end_longitude': end_lon,
    }
    uber_response = requests.get(uber_url, params=uber_parameters)


    lyft_parameters = {
        'start_latitude': start_lat,
        'start_longitude': start_lon,
        'end_latitude': end_lat,
        'end_longitude': end_lon,
    }

    lyft_response = requests.get(lyft_url, params = lyft_parameters, auth = (lyft_client_id, lyft_client_secret))
    print(lyft_response.json())







    if uber_response.status_code == 422:
        print("Your distance exceeds 100 miles.  Please choose locations that are less than 100 miles apart.")
        quit()
    else:
        uber_estimates = uber_response.json()
        uber_price_estimate = uber_estimates['prices'][0]['estimate']
        uber_time_estimate = uber_estimates['prices'][0]['duration'] / 60

        lyft_price_estimate = 15
        lyft_time_estimate = 15




print("Calculating estimates for Uber and Lyft from " + str(start_lat) + ", " + str(start_lon) + " to " + str(end_lat) + ", " +str(end_lon) + ":")
print("Uber: Estimated Cost is " + str(uber_price_estimate) + ".")
print("Uber: Estimated Time is " + str(uber_time_estimate) + " minutes.")
print("Lyft: Estimated Cost is " + str(lyft_price_estimate) + ".")
print("Lyft: Estimated Cost is " + str(lyft_time_estimate) + " minutes.")



    # uri = 'https://api.lyft.com/oauth/token'

    # headers = {
    #     'Content-Type': 'application/json',
    # }

    # data = {"grant_type": "client_credentials", "scope": "public"}

    # # user_auth = (lyft_client_token, lyft_client_secret)
    # # lyft_auth = requests.post(uri, header = headers, data=data, auth = user_auth)

    # r = requests.post('https://api.github.com', auth=(lyft_client_id, lyft_client_token))
    # print(r.json())