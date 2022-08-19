import requests
import json
import turtle


def move_iss(latitude, longitude):
    global iss

    iss.penup()
    iss.goto(long, lat)
    iss.pendown()


screen = turtle.Screen()
screen.setup(1000, 500)
screen.bgpic('earth.png')
screen.setworldcoordinates(-180, -90, 180, 90)

iss = turtle.Turtle()
turtle.register_shape("iss.gif")
iss.shape("iss.gif")

url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)

if response.status_code == 200:
    response_dict = json.loads(response.text)
    position = response_dict['iss_position']
    print('International Space Station at ' + position['latitude'] + ', ' + position['longitude'])
    lat = float(position['latitude'])
    long = float(position['longitude'])
    move_iss(lat, long)
else:
    print("Houston, we've got a problem: ", response.status_code)


turtle.mainloop()
