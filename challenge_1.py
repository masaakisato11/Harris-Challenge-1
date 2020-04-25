# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020
# to analyze supply and demand for bikes in the system.

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
from numpy import mean, median
import json

# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('divvy_stations.txt').read())

# PROBLEM 1
# find average number of empty docks (num_docks_available) and
# available bikes (num_bikes_available) at all stations in the system

divvy_num_docks_available = [divvy_stations[i]['num_docks_available'] for i in range(0,len(divvy_stations))]
print(mean(divvy_num_docks_available))

divvy_num_bikes_available = [divvy_stations[i]['num_bikes_available'] for i in range(0,len(divvy_stations))]
print(mean(divvy_num_bikes_available))

# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)

a = sum(divvy_num_docks_available)
b = sum(divvy_num_bikes_available) + sum(divvy_num_docks_available)
print(a/b)

# PROBLEM 3
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows
# the percentage of bikes available at each individual station (again ignore ebikes).
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%

for i in range(0,len(divvy_stations)):
    a = divvy_num_bikes_available[i]
    b = divvy_num_docks_available[i]
    divvy_stations[i]['percent_bikes_remaining'] = round(a/(a+b)*100,2)
divvy_stations
