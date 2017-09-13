"""
My Weather App
Team of:Rajdeep Singh(SKNSITS-SE-B), Sankalp Khawade(SKNSITS-SE-B), Omkar Kandale(SKNSITS-SE-A)

Weather provider openweathermap.org
message service twilio.com
(Since the api key is free and testing version, the sms notification only goes to registered mobile number ie. +919004107960 , hence the Phone number input option isnt added)

things used:-

openweather api and twilio api
gi and Gtk for gui
userlib and json libraries to process the url

"""
import gi
import urllib.request
import json

# from twilio.rest import TwilioRestClient

from gi.repository import Gtk

"""Keys for openweather and twilio respectively"""
# key_ow = '6985a5fb6a438fcd9d4c80b9c2dfac8c'
# ACCOUNT_SID = "ACf28b3c25bdb550c5c10a46cf2de66a0c"
# AUTH_TOKEN = "74c9042f051ec170e055186a12c5342d"

"""Function To reprocess and Send SMS"""


def sms(self):
    city = input1.get_text()
    url1 = ('http://api.openweathermap.org/data/2.5/weather?q=' + city + ',in&appid=' + key_ow)
    f = urllib.request.urlopen(url1)
    json_var1 = f.read()
    obj1_json = json.loads(json_var1.decode())
    temper = (obj1_json['main']['temp'])
    wind = (obj1_json['wind']['speed'])
    status = (obj1_json['weather'][0]['main'])
    sky = (obj1_json['weather'][0]['description'])
    pres = (obj1_json['main']['pressure'])
    humi = (obj1_json['main']['humidity'])

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    """SMS notification of weather report to registered number, since its trial api its only for destination number +919004107960"""
    client.messages.create(
        to="+919004107960",
        from_="+1 865-512-7377",
        body=('Temperature of ' + city + ' will be:' + str(temper - 273) + ' Degrees Celcius' + '\nWind Speed:' + str(
            wind) + ' kmph' + '\nWeather status:' + status + '\nDescription: ' + sky + '\nPressure ' + str(
            pres) + 'hPa' + '\nHumidity: ' + str(humi) + '%\nHave a Good Day')
    )

    newwin2 = Gtk.Window(title="Note!")
    newwin2.set_border_width(20)
    newwin2.set_size_request(200, 40)

    label4 = Gtk.Label()
    label4.set_label("Message Sent!")
    label4.set_halign(Gtk.Align.CENTER)

    newwin2.add(label4)

    newwin2.connect("delete-event", Gtk.main_quit)
    newwin2.show_all()
    Gtk.main()


"""Function to find and display weather a popup"""


def findw(self):
    """finding the status according to location added in """
    city = input1.get_text()
    url1 = ('http://api.openweathermap.org/data/2.5/weather?q=' + city + ',in&appid=' + key_ow)
    f = urllib.request.urlopen(url1)
    json_var1 = f.read()
    obj1_json = json.loads(json_var1.decode())

    """accessing the elements of the json result file"""
    temper = (obj1_json['main']['temp'])
    wind = (obj1_json['wind']['speed'])
    status = (obj1_json['weather'][0]['main'])
    sky = (obj1_json['weather'][0]['description'])
    pres = (obj1_json['main']['pressure'])
    humi = (obj1_json['main']['humidity'])

    """New window that shows the result and has option to send sms"""
    newwin = Gtk.Window(title="Weather Report")
    newwin.set_border_width(20)
    newwin.set_size_request(200, 40)
    label1 = Gtk.Label()
    label1.set_label(
        'Temperature of ' + city + ' will be:' + str(temper - 273) + ' Degrees Celcius' + '\nWind Speed:' + str(
            wind) + ' kmph' + '\nWeather status:' + status + '\nDescription: ' + sky + '\nPressure ' + str(
            pres) + 'hPa' + '\nHumidity: ' + str(humi))
    label1.set_halign(Gtk.Align.CENTER)

    """Clicking this will call the sms function that will reprocess the data and send the result status via sms"""
    button3 = Gtk.Button(label="Notify Me!")
    button3.connect("clicked", sms)

    grid2 = Gtk.Grid()
    newwin.add(grid2)

    grid2.add(label1)
    grid2.attach_next_to(button3, label1, Gtk.PositionType.BOTTOM, 2, 1)

    newwin.connect("delete-event", Gtk.main_quit)
    newwin.show_all()
    Gtk.main()


"""Codes for the main window GUI"""

window = Gtk.Window(title="My Weather App")
window.set_border_width(20)
window.set_size_request(200, 40)
label = Gtk.Label()
grid = Gtk.Grid()
window.add(grid)

vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

input1 = Gtk.Entry()
input1.set_text("Enter Here")

label.set_label("Enter City: ")
label.set_halign(Gtk.Align.CENTER)

button1 = Gtk.Button(label='Quit')
button1.connect("clicked", Gtk.main_quit)

button2 = Gtk.Button(label='Find')
button2.connect("clicked", findw)

grid.add(label)
grid.attach_next_to(input1, label, Gtk.PositionType.RIGHT, 8, 1)
grid.attach_next_to(button1, label, Gtk.PositionType.BOTTOM, 5, 1)
grid.attach_next_to(button2, button1, Gtk.PositionType.RIGHT, 5, 1)

window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
