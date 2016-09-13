CompareMyRide is a simple Python script that compares estimates for a ride from a start point to an end point between Lyft and Uber, using their API.  Note that the distances between the start and end points has to be less than 100 miles.

In order to run the script, open terminal to where the script is and run python CompareMyRide.py start_lat start_lon end_lat end_lon

For example: python CompareMyRide.py 37.775818 -122.418028 37.774231 -122.41293

This outputs:

Estimates for Uber:
Product: POOL
Estimated Cost: $5.75
Estimated Travel Time: 6 minutes


Product: uberX
Estimated Cost: $13-14
Estimated Travel Time: 6 minutes


Product: uberXL
Estimated Cost: $17-18
Estimated Travel Time: 6 minutes


Product: SELECT
Estimated Cost: $10-13
Estimated Travel Time: 6 minutes


Product: BLACK
Estimated Cost: $15-16
Estimated Travel Time: 6 minutes


Product: SUV
Estimated Cost: $25
Estimated Travel Time: 6 minutes


Product: ASSIST
Estimated Cost: $13-14
Estimated Travel Time: 6 minutes


Product: WAV
Estimated Cost: $21-25
Estimated Travel Time: 6 minutes


Product: TAXI
Estimated Cost: Metered
Estimated Travel Time: 6 minutes


-------------------------------
Estimates for Lyft:
Product: lyft_plus
Estimated Cost: $17-22
Estimated Travel Time: 3 minutes


Product: lyft_line
Estimated Cost: $7
Estimated Travel Time: 3 minutes


Product: lyft
Estimated Cost: $12-17
Estimated Travel Time: 3 minutes

