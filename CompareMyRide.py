import requests
import json
import sys


uber_client_id = "YQIgetGmABtkErAUcgQ2-po207TvJg8c"
uber_client_secret = "of9PtO1hfHIo-L2pw80lr3amblltOSU6ZS2FJI3s"
uber_server_token = "Gok6o1f9mdRYJR78A9WW3fAmdpAKAC5e_WyPp5S9"

lyft_client_id = "JpWPeznr4Y4Y"
lyft_client_token = "gAAAAABX1vxNONlyqn0Id7Rv-WyZPvNAq_u-z5lhSghC0dAZnCUv-_snT1br8mSXlH0DpAx-JFCg6ijp4XAd9Q8Atw_ZFSQHnhEaV-rdHx3C3N2FaLeCl_-02ZM8f2jrEfgMAZ0io9daVt-oVIIHopHG1W3FGs9as2mUm6NaiIPr5UjKWJ3qqfs="
lyft_client_secret = "3BP5tUBf8N3IWdfltvgdWWLSpKorn6JM"


uber_url = "https://api.uber.com/v1/estimates/price"
lyft_url = "https://api.lyft.com/v1/cost"
lyft_auth_url = "https://api.lyft.com/oauth/token"


# curl -X POST -H "Content-Type: application/json" \
#      --user "JpWPeznr4Y4Y":"3BP5tUBf8N3IWdfltvgdWWLSpKorn6JM" \
#      -d '{"grant_type": "client_credentials", "scope": "public"}' \
#      'https://api.lyft.com/oauth/token'
     
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

def get_uber_estimates(start_lat, start_lon, end_lat, end_lon):
    uber_parameters = {
        'server_token': uber_server_token,
        'start_latitude': start_lat,
        'start_longitude': start_lon,
        'end_latitude': end_lat,
        'end_longitude': end_lon,
    }
    uber_response = requests.get(uber_url, params=uber_parameters)

    if uber_response.status_code == 422:
        print("Your distance exceeds 100 miles.  Please choose locations that are less than 100 miles apart.")
        quit()
    else:
        uber_estimates = uber_response.json()
        uber_price_estimate = uber_estimates['prices'][0]['estimate']
        uber_time_estimate = uber_estimates['prices'][0]['duration'] / 60
        return [uber_price_estimate, uber_time_estimate]

def get_lyft_access_token():

    headers = {'Content-Type': 'application/json'}
    data = '{"grant_type": "client_credentials", "scope": "public"}'
    lyft_auth_response = requests.post(lyft_auth_url, headers=headers, data=data,
        auth = (lyft_client_id, lyft_client_secret))

    if lyft_auth_response.status_code != 200:
        print("Error: " + str(response.status_code))
        quit()
    else:
        lyft_auth_token = lyft_auth_response.json()['access_token']
        return lyft_auth_token


    lyft_parameters = {
        'start_latitude': start_lat,
        'start_longitude': start_lon,
        'end_latitude': end_lat,
        'end_longitude': end_lon,
    }





if __name__ == "__main__":
    uber_response = get_uber_estimates(start_lat, start_lon, end_lat, end_lon)
    access_token = get_lyft_access_token()

    print("Calculating estimates for Uber and Lyft from " + str(start_lat) + ", " + str(start_lon) + " to " + str(end_lat) + ", " +str(end_lon) + ":")
    print("Uber: Estimated Cost is " + str(uber_response[0]) + ".")
    print("Uber: Estimated Time is " + str(uber_response[1]) + " minutes.")
    print("Lyft: Estimated Cost is " + str(lyft_price_estimate) + ".")
    print("Lyft: Estimated Cost is " + str(lyft_time_estimate) + " minutes.")
