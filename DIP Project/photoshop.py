from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk, Image, ImageOps
from PIL import ImageFilter


window = Tk()
window.geometry("1270x550")
window.title("Photoshop App")


f_types = [('Jpg Files', '.jpg'),("all files",".*")]
filename = filedialog.askopenfilename(filetypes=f_types)
main_img = Image.open(filename)
main_img = main_img.resize((250,250))



img1=ImageTk.PhotoImage(main_img)



img2 = ImageOps.grayscale(main_img)
img2=ImageTk.PhotoImage(img2)

img3 = Image.open(filename)
img3= img3.resize((250,250))

w,h = img3.size
for i in range(w):

    for j in range(h):

        r,g,b = img3.getpixel((i,j))

        r   = 255 - r

        g  = 255 - g

        b   = 255 - b


        img3.putpixel((i,j),(r,g,b))

img33 = ImageTk.PhotoImage(img3)


img4 = main_img.filter(ImageFilter.BLUR)
img4 = ImageTk.PhotoImage(img4)

img5 = main_img.filter(ImageFilter.SHARPEN)
img5 = ImageTk.PhotoImage(img5)


img6 = main_img.filter(ImageFilter.SMOOTH)
img6 = ImageTk.PhotoImage(img6)

img7 = main_img.filter(ImageFilter.CONTOUR)
img7 = ImageTk.PhotoImage(img7)

img8 = main_img.filter(ImageFilter.FIND_EDGES)
img8 = ImageTk.PhotoImage(img8)

img9 = main_img.rotate(180)
img9 = ImageTk.PhotoImage(img9)

img10 = main_img.transpose(Image.FLIP_LEFT_RIGHT)
img10 = ImageTk.PhotoImage(img10)


labelOriginalText = Label(window, text ="ORIGINAL")
labelOriginalText.grid(row =3, column = 0)

labelOriginalImage =Label(window,image=img1) 
labelOriginalImage.grid(row=4,column=0)

labelBWText = Label(window, text ="GRAYSCALED")
labelBWText.grid(row =3, column = 1)

labelBWImage = Label(window,image=img2) 
labelBWImage.grid(row=4,column=1)

labelNegativeText = Label(window, text ="NEGATIVE")
labelNegativeText.grid(row =3, column = 2)

labelNegativeImage=Label(window, image=img33)
labelNegativeImage.grid(row=4, column=2)

labelBlurText = Label(window, text ="BLURRED")
labelBlurText.grid(row =3, column = 3)

labelBlurImage =Label(window,image=img4)
labelBlurImage.grid(row=4,column=3)

labelSharpenText = Label(window, text ="SHARPENED")
labelSharpenText.grid(row =3, column = 4)

labelSharpenImage =Label(window,image=img5) 
labelSharpenImage.grid(row=4,column=4)

labelSmoothText = Label(window, text="SMOOTHENED")
labelSmoothText.grid(row = 5,column=0)

labelSmoothImage =Label(window,image=img6)
labelSmoothImage.grid(row=6,column=0)

labelContourText = Label(window, text="CONTOURED")
labelContourText.grid(row = 5,column=1)

labelContourImage =Label(window,image=img7) 
labelContourImage.grid(row=6,column=1)

labelEdgeText = Label(window, text="EDGES FOUND")
labelEdgeText.grid(row = 5,column=2)

labelEdgeImage =Label(window,image=img8) 
labelEdgeImage.grid(row=6,column=2)

labelEdgeTexta = Label(window, text="ROTATED")
labelEdgeTexta.grid(row = 5,column=3)

labelEdgeImagea =Label(window,image=img9) 
labelEdgeImagea.grid(row=6,column=3)

labelEdgeTexta = Label(window, text="FLIPPED")
labelEdgeTexta.grid(row = 5,column=4)

labelEdgeImagea =Label(window,image=img10)
labelEdgeImagea.grid(row=6,column=4)



window.mainloop()