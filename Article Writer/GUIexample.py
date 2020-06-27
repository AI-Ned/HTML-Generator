from tkinter import *
from tkinter.ttk import *


## This is an example of how I currently Envision the UI. This is subject to change ##

tk = Tk()

frame1 = Frame(tk, borderwidth = 2 )
frame1.pack(fill = BOTH)
frame2 = Frame(tk)
frame2.pack(fill = X)
frame3 = Frame(tk)
frame3.pack(fill = X)
frame4 = Frame(tk)
frame4.pack(fill= X)

tk.title("GUI Example")

  
# Top frame #
## There could be a settings button here that will allow the user to select which template they want and what the image upload directory should be. ## 
mainTitle = Label(frame1, text="Article Editor Tool", font=50)
mainTitle.pack(side = LEFT, padx = 5, pady = 5)


#Header Frame #
headerLabel = Label(frame2, text="Article Header")
headerLabel.pack(side = LEFT, padx = 5, pady = 5)

headerName = Entry(frame2)
headerName.pack(fill = X, padx = 5)


# Article Frame #
articleLabel = Label(frame3, text="Article Content")
articleLabel.pack(side = LEFT, padx = 3, pady = 5)

articleField = Text(frame3)
articleField.pack(fill = X, padx = 5, expand = True)


# Buttons Frame #
## Each button should run a required function, potentially add a save button ##
### Upload Image should upload an image to the required location ###
uploadImage = Button(frame4, text="Upload Image")
uploadImage.pack(side = LEFT, padx = 5, pady = 8 )

### Cancel Button will just quit ### 
cancelButton = Button(frame4, text="Cancel")
cancelButton.pack(side = RIGHT, padx = 5, pady = 8)

### Export button should generate the HTML file, Maybe it should launch a 2nd window with the option to select the HTML file. ###
exportButton = Button(frame4, text="Export")
exportButton.pack(side = RIGHT, padx = 5, pady = 8)




tk.mainloop()



   




