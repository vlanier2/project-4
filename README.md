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

Control location (km)	Minimum Speed (km/hr)	Maximum Speed (km/hr)
0 - 200	15	34
200 - 400	15	32
400 - 600	15	30
600 - 1000	11.428	28
1000 - 1300	13.333	26

The calculator converts all inputs expressed in units of miles to kilometers and rounds (April 2021) truncates the result to the nearest kilometer before being used in calculations. Times are rounded to the nearest minute.

## Setup

### Supplying a Credentials File

credentials-skel.ini should be replaced by a credentials.ini file specifying the port and debug mode. If no credentials file is provided, it defaults to port 5000 and debug=True. *Note: The credentials.ini file should be placed in the /vocab directory so it can be accessed within the container.

credentials.ini should also provide three additional variables related to the anagram game.

"secret_key" - should be replaced by a random string

"success_at_count" - decides how many words must be guessed to win the game

"vocab" - path to the vocab list used in the game. Three vocab lists are provided in /data and any custom vocab list can be used in this format

### Building a Container

Move to /vocab and build the simple flask app image using

```
docker build -t <some-image-name> .
```

Run the container using

```
docker run -d -p desired-port:5000 some-image-name
```

## Usage

Use the letters provided in bold to determine which of the words shown make up the anagram. When you have a guess, type in the field labeled word. 
The page will dynamically update and let you know one of three cases: 

1) The typed characters are not in the list of words

2) The typed word can't be made from the letters in the anagram

3) You already found the word

Once a word is correctly guessed, it will appear on screen under "You found". Once the required number of words are guessed you are redirected to a success page and given the option to return and start again.

## Testing

## Shutting Down

Simply shut down the flask app with ctrl-c in your terminal, and/or stop the docker container.