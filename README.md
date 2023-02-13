# UOCIS322 - Project 4 

NOTE: This time, you should outline the application, the algorithm, and how to use start (docker instructions, web app instructions). Make sure you're thorough, otherwise you may not get all the points.

NAME: Vincent Lanier

CONTACT: vlanier@uoregon.edu

## Project Description

This project consists of a web application that is based on RUSA's online calculator. The algorithm for calculating control times is described here https://rusa.org/pages/acp-brevet-control-times-calculator. Additional background information is given here https://rusa.org/pages/rulesForRiders.

The webpage contains a spreadsheet for calculating start and end times for control points in a given brevet. After a control point distance is given, the spreadsheet automatically updates without refresh. The project makes use of AJAX, JQuery, and bootstrap for a dynamic webpage. A flask server supplies the page template and responds to AJAX queries to update control point times. 

## Algorithm

A control's opening time is found by dividing its kilometer placement by the maximum speed given by the table below.
A control's closing time is found by dividing its kilometer placement by the minimum speed given by the table below.

This calculation produces a time in hours. To convert into hours and minutes we multiply the fractional part by 60 minutes.

The table below gives the minimum and maximum speeds for ACP brevets.

Control location (km)	  Minimum Speed (km/hr)	  Maximum Speed (km/hr)

0 - 200	                        15	                    34

200 - 400	                      15	                    32

400 - 600	                      15	                    30

600 - 1000	                    11.428	                28

1000 - 1300	                    13.333	                26

The calculator converts all inputs expressed in units of miles to kilometers and truncates the result to the nearest kilometer before being used in calculations. Kilometer values are rounded to the nearest kilometer before being used in calculations. Times are rounded to the nearest minute after all calculations are complete.

### Calculating Times Across Multiple Speed Ranges

Calculation of control times that fall beyond 200km is more complex. The following example comes from https://rusa.org/pages/acp-brevet-control-times-calculator.

"Consider a control at 350km. We have 200/34 + 150/32 = 5H53 + 4H41 = 10H34. The 200/34 gives us the minimum time to complete the first 200km while the 150/32 gives us the minimum time to complete the next 150km. The sum gives us the control's opening time."

### Special Exceptions

The closing time for the starting point (at 0km) is one hour after the official start.

Overall time limits vary for each brevet are: (in hours and minutes, HH:MM) 13:30 for 200 KM, 20:00 for 300 KM, 27:00 for 400 KM, 40:00 for 600 KM, and 75:00 for 1000 KM. These are used as closing times for the final control point regardless if the final control is located beyond the total brevet distance. Final control points are allowed by rule to be 20% further than the total brevet distance.

The closing time for a control within the first 60km is based on 20 km/hr, plus 1 hour. This is to ensure points within 60km do not close during the open period of the start at 0km.

## Setup

### Supplying a Credentials File

credentials-skel.ini should be replaced by a credentials.ini file specifying the port and debug mode. If no credentials file is provided, it defaults to port 5000 and debug=True. *Note: The credentials.ini file should be placed in the /brevets directory so it can be accessed within the container.

### Building a Container

Move to /brevets and build the simple flask app image using

```
docker build -t <some-image-name> .
```

Run the container using

```
docker run -d -p <desired-port>:<port-set-in-credentials> <some-image-name>
```

To run the flask server without docker simply navidate to /brevets and run

```
python3 flast_brevets.py
```

## Usage

With the container running, navigate to localhost:<port> to oepn the brevet checkpoint spreadsheet. Select a total brevet distance and a start date and time at the top of the page. Then enter checkpoint distances in miles or kilometers. The times for each checkpoint will fill in response to a new kilometer distance being entered.

## Testing

### Testing Without Container

A series of nosetests are included for the control time calculation logic. Run these tests by navigating to /brevets and running

```
nosetests
```

or run the added bash test script with

```
./run_tests.sh
```

### Testing in Container

the nosetests script can be run in the container with

```
docker run -it --entrypoint /bin/bash -p 5000:5000 testimg -c nosetests
```

or 

```
docker run -it --entrypoint /bin/bash -p 5000:5000 testimg -c ./run_tests.sh
```


## Shutting Down

Simply shut down the flask app with ctrl-c in your terminal, and/or stop the running docker container.
