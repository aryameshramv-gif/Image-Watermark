from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path

#-------------------- INPUT THE IMAGES TO USE IN CONVERSION --------------------#
MAIN_IMAGE_PATH = "main image file path"
WATERMARK_PATH = "watermark file path"

#COLORS
WHITE = "#fefae0"
GREEN_1 = "#ecf39e"
GREEN_2 = "#90a955"
GREEN_3 = "#4f772d"
GREEN_4 = "#31572c"
GREEN_5 = "#132a13"
font =  'Helvetica'

#-------------------- FUNCTIONS --------------------#
#here, 'output' is the directory in which the result image is going to be saved in.
def file_name():
    for sequence in range(1,1000):
        file_path = Path(f"output/image{sequence}.png")
        if not file_path.is_file():
            return file_path

def download():
    main.save(f"{file_name()}")
    title_text.config(text="₊✩‧₊˚౨ image downloaded! ৎ˚₊✩‧₊")

#-------------------- UI SETUP --------------------#
window =  Tk()
window.title("Image Watermarker")
window.config(padx=20,pady=20, bg=GREEN_2)

#-------------------- CONVERSION MECHANISM --------------------#
aspect_ratio_main = (400,400)
aspect_ratio_mark = (300,300)

main = Image.open(MAIN_IMAGE_PATH).convert("RGBA")
main.thumbnail(aspect_ratio_main)

watermark = Image.open(WATERMARK_PATH).convert("RGBA")
watermark.thumbnail(aspect_ratio_mark)

#for transparency
opacity = 125
alpha = watermark.getchannel('A')
new_alpha = alpha.point(lambda i: opacity if i > 0 else 0)
watermark.putalpha(new_alpha)
#overlaying image
main.paste(watermark,(30,30),watermark)
image = ImageTk.PhotoImage(image=main)


#-------------------- UI CONT --------------------#
canvas = Canvas(width=500,height=500,bg=GREEN_3,highlightthickness=1,highlightbackground=GREEN_5)
canvas.create_image(250,250, image=image)
canvas.grid(row=3,column=2)

#TITLE TEXT
title_text = Label(text="₊✩‧₊˚౨ Download your image? ৎ˚₊✩‧₊", font=(font,20,'bold'),bg=GREEN_2,fg=WHITE)
title_text.grid(row=1,column=2)

#BUTTON
download_button = Button(text='Download',font=(font,20),command=download,bg=GREEN_5,fg=GREEN_1)
download_button.grid(row=4,column=2)

window.mainloop()