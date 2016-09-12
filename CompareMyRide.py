import requests
import json
import sys

uber_client_id = "YQIgetGmABtkErAUcgQ2-po207TvJg8c"
uber_client_secret = "of9PtO1hfHIo-L2pw80lr3amblltOSU6ZS2FJI3s"
uber_server_token = "Gok6o1f9mdRYJR78A9WW3fAmdpAKAC5e_WyPp5S9"

lyft_client_token = "gAAAAABX1QfwJ2O6soRfPPcIZm6IKV-_jVtII5W7EFpDVjclRwObue4mAsmUZKaIa0LAzYNy0hj37s65T-aofFclzXJbMKiZCfR_Q8lmE5m5nDj4t3S1JiQAjCaleqMjpS3Z_7lsWzTyI3Lky3HfoJpfPHHacVZxxJHXbn_U37KwuNciwWRnyxg="
lyft_client_secret = "xxmulseLmBjJU79x82K9E4mgfqvJhRaZ"

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

    parameters = {
        'server_token': uber_server_token,
        'start_latitude': start_lat,
        'start_longitude': start_lon,
        'end_latitude': end_lat,
        'end_longitude': end_lon,
    }

    response = requests.get(uber_url, params=parameters)

    if response.status_code == 422:
        print("Your distance exceeds 100 miles.  Please choose locations that are less than 100 miles apart.")
        quit()
    else:
        uber_estimates = response.json()
        uber_price_estimate = uber_estimates['prices'][0]['estimate']
        uber_time_estimate = uber_estimates['prices'][0]['duration'] / 60

        lyft_price_estimate = 15
        lyft_time_estimate = 15




print("Calculating estimates for Uber and Lyft from " + str(start_lat) + ", " + str(start_lon) + " to " + str(end_lat) + ", " +str(end_lon) + ":")
print("Uber: Estimated Cost is " + str(uber_price_estimate) + ".")
print("Uber: Estimated Time is " + str(uber_time_estimate) + " minutes.")
print("Lyft: Estimated Cost is " + str(lyft_price_estimate) + ".")
print("Lyft: Estimated Cost is " + str(lyft_time_estimate) + " minutes.")

