from tkinter import Tk, Frame, Button, filedialog, Label, Canvas, messagebox
from PIL import Image, ImageTk
from dog_classifier_v2 import *

window = Tk()
window.title("Provide Picture For Classification") # self explanatory!
window.geometry("400x400") # size of the window when it opens
window.minsize(width=200, height=200) # you can define the minimum size of the window like this
window.resizable(width="true", height="true") # change to false if you want to prevent resizing

def select_pic():
	global file_path,cv_img, img 
	global photo
	
	file_path = filedialog.askopenfilename()
	img = Image.open(file_path).resize((224,224),Image.ANTIALIAS)
	photo = ImageTk.PhotoImage(img)
	breed = provide_output(file_path)
	return photo, breed

continue_execution = True

while continue_execution == True:

	top_frame = Frame(window,borderwidth=2,pady=2)
	center_frame = Frame(window,borderwidth=2,pady=2)
	bottom_frame = Frame(window,borderwidth=2,pady=2)

	top_frame.grid(row=0, column=0)
	center_frame.grid(row=1, column=0)
	bottom_frame.grid(row=2, column=0)
	photo, breed = select_pic()
	print(breed)
	can = Canvas(top_frame, width=300, height = 300 )
	can.pack()
	can.create_image(0, 0, image=photo, anchor='nw')
	output = Label(center_frame, text='Most Probably a {}'.format(breed))
	output.pack(side='left')
	exit = Button(bottom_frame, text='Exit Program', command=window.destroy)
	exit.pack(side='left')
	
	continue_execution = messagebox.askyesno("Command", "Continue Execution")

window.mainloop()