from tkinter import *
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup


root= Tk()

root.geometry("360x200")
root.maxsize(360, 200)
root.minsize(360, 200)
root.title("WEATHER APP")

url='https://weather.com/en-IN/weather/today/l/28.65,77.34?par=google'


site= requests.get(url)
soup= BeautifulSoup(site.content, "html.parser")

def check():
    location= soup.find('h1').text
    temperature= soup.find('span', class_="CurrentConditions--tempValue--3a50n").text
    climate= soup.find('div', class_="CurrentConditions--phraseValue--2Z18W").text
    location_label = Label(root, text=location, font=("Lucida", 15, "bold")).grid(row=0, column=0, padx= 60)
    temperature_label = Label(root, text=temperature, font=("Lucida", 30, "bold")).grid(row=1, sticky="w", padx="50")
    climate_label = Label(root, text=climate, font=("Lucida", 30, "bold")).grid(row=2, pady=10)


photo= Image.open("C:\\Users\Shashank-dt\Desktop\weather.png")
photo= photo.resize((80, 80))
photo= ImageTk.PhotoImage(photo)

img = Label(image=photo).grid(row=1, sticky="e", padx=40, pady=10)

check()
root.mainloop()