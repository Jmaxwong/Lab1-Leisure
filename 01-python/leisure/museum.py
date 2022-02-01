
from PIL import Image, ImageDraw
import PySimpleGUI as sg
from PIL import Image
import os
import tkinter
import io

def draw_museum():
    #print("market not found")
    img = Image.open("/Users/abdelazimlokma/Desktop/mus.jpg")
    #img.show()
    img.thumbnail((1200,800))
    bio = io.BytesIO()
    img.save(bio, format="PNG")

    #GUI implement
    layout = [[[sg.Text("Museum:", font= ("Arial", 25)),],
    [sg.Image(data=bio.getvalue())]],
    [sg.Button("Don't Show Me Anymore")]]

    #closing window con
    window = sg.Window("Image", layout, size=(1200, 800))
    while True:
        event, values = window.read()
        if event == "Don't Show Me Anymore" or event == sg.WIN_CLOSED:
            break
    
    window.close()

    return

draw_museum();