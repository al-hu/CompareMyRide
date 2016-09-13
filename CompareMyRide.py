import requests
import json
import sys


uber_client_id = "YQIgetGmABtkErAUcgQ2-po207TvJg8c"
uber_client_secret = "of9PtO1hfHIo-L2pw80lr3amblltOSU6ZS2FJI3s"
uber_server_token = "Gok6o1f9mdRYJR78A9WW3fAmdpAKAC5e_WyPp5S9"

lyft_client_id = "JpWPeznr4Y4Y"
lyft_client_token = "gAAAAABX1vxNONlyqn0Id7Rv-WyZPvNAq_u-z5lhSghC0dAZnCUv-_snT1br8mSXlH0DpAx-JFCg6ijp4XAd9Q8Atw_ZFSQHnhEaV-rdHx3C3N2FaLeCl_-02ZM8f2jrEfgMAZ0io9daVt-oVIIHopHG1W3FGs9as2mUm6NaiIPr5UjKWJ3qqfs="
lyft_client_secret = "3BP5tUBf8N3IWdfltvgdWWLSpKorn6JM"


uber_price_url = "https://api.uber.com/v1/estimates/price"
lyft_price_url = "https://api.lyft.com/v1/cost"
lyft_auth_url = "https://api.lyft.com/oauth/token"

     
args = sys.argv[1:]

if len(args) != 4:
    print("You must enter four arguments: the start longitude, start lattitude, end longitude, and end lattitude")
    quit()
else:
    start_lat = float(args[0])
    start_lon = float(args[1])
    end_lat = float(args[2])
    end_lon = float(args[3])

def get_uber_estimates(start_lat, start_lon, end_lat, end_lon):
    uber_parameters = {
        'server_token': uber_server_token,
        'start_latitude': start_lat,
        'start_longitude': start_lon,
        'end_latitude': end_lat,
        'end_longitude': end_lon,
    }
    uber_response = requests.get(uber_price_url, params=uber_parameters)

    if uber_response.status_code == 422:
        print("Your distance exceeds 100 miles.  Please choose locations that are less than 100 miles apart.")
        quit()
    else:
        uber_estimates = uber_response.json()
        return uber_estimates


def get_lyft_access_token():

    headers = {'Content-Type': 'application/json'}
    data = '{"grant_type": "client_credentials", "scope": "public"}'
    lyft_auth_response = requests.post(lyft_auth_url, headers=headers, data=data,
        auth = (lyft_client_id, lyft_client_secret))

    if lyft_auth_response.status_code != 200:
        print("Error: " + str(lyft_auth_response.status_code) + " on line 53")
        quit()
    else:
        lyft_auth_token = lyft_auth_response.json()['access_token']
        return lyft_auth_token


def get_lyft_estimates(auth_token):
    headers = {'Content-Type': 'application/json', 'Authorization': 'bearer ' + auth_token}
    lyft_parameters = {
        'start_lat': start_lat,
        'start_lng': start_lon,
        'end_lat': end_lat,
        'end_lng': end_lon,
    }
    lyft_response = requests.get(lyft_price_url, params = lyft_parameters, headers = headers)

    if lyft_response.status_code != 200:
        print("Error: " + str(lyft_response.status_code) + " on line 72")
        quit()
    else:
        lyft_estimates = lyft_response.json()
        return lyft_estimates

def print_results(uber_estimates = None, lyft_estimates = None):
    if uber_estimates == None and lyft_estimates == None:
        print("There are no available rides, sorry.")
        quit()
    else:
        number_results_uber = len(uber_estimates['prices'])
        number_results_lyft = len(lyft_estimates['cost_estimates'])

        print("Estimates for Uber:")
        for x in range(0, number_results_uber):
            curr = uber_estimates['prices'][x]
            travel_time = curr['duration'] / 60

            print("Product: " + curr['display_name'])
            print("Estimated Cost: " + curr['estimate'])
            print("Estimated Travel Time: " + str(travel_time) + " minutes")
            print("\n")

        print("-------------------------------")

        for x in range(0, number_results_lyft):
            curr = lyft_estimates['cost_estimates'][x]
            min_cost = curr['estimated_cost_cents_min'] / 60
            max_cost = curr['estimated_cost_cents_max'] / 60
            travel_time = curr['estimated_duration_seconds'] / 60
            estimate_range = "$" + str(min_cost) + "-" + str(max_cost)
            if min_cost == max_cost:
                estimate_range = "$" + str(min_cost)
            print("Product: " + curr['ride_type'])
            print("Estimated Cost: " + estimate_range)
            print("Estimated Travel Time: " + str(travel_time) + " minutes")
            print("\n")

if __name__ == "__main__":
    uber_estimates = get_uber_estimates(start_lat, start_lon, end_lat, end_lon)
    access_token = get_lyft_access_token()
    lyft_estimates = get_lyft_estimates(access_token)
    print_results(uber_estimates, lyft_estimates)
