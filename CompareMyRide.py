import requests
import json
import sys

uber_client_id = "YQIgetGmABtkErAUcgQ2-po207TvJg8c"
uber_client_secret = "of9PtO1hfHIo-L2pw80lr3amblltOSU6ZS2FJI3s"
uber_server_token = "Gok6o1f9mdRYJR78A9WW3fAmdpAKAC5e_WyPp5S9"

args = sys.argv[1:]

if len(args) != 4:
	print("You must enter four arguments: the start longitude, start lattitude, end longitude, and end lattitude")
	quit()

start_lon = float(args[0])
start_lat = float(args[1])
end_lon = float(args[2])
end_lat = float(args[3])

url = "https://api.uber.com/v1/estimates/price"

parameters = {
    'server_token': uber_server_token,
    'start_latitude': 37.775818,
    'start_longitude': -122.418028,
    'end_latitude': 37.774231,
    'end_longitude': -122.41293,
}

response = requests.get(url, params=parameters)
estimates = response

uber_estimate_cost = 14
uber_estimate_time = 14
lyft_estimate_cost = 15
lyft_estimate_time = 15



if __name__ == '__main__':
    for x in [start_lon, start_lat, end_lon, end_lat]:
    	print(x)
    print("Calculating estimates for Uber and Lyft from" + str(start_lat) + ", " + str(start_lon) + " to " + str(end_lat) + ", " +str(end_lon) + ":")
    print("Please wait")
    print("Uber: Estimated Cost is " + str(uber_estimate_cost) + " dollars.")
    print("Uber: Estimated Time is " + str(uber_estimate_time) + " minutes.")
    print("Lyft: Estimated Cost is " + str(lyft_estimate_cost) + " dollars.")
    print("Lyft: Estimated Cost is " + str(lyft_estimate_time) + " minutes.")
    print(estimates)

