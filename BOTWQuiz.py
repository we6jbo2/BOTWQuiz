#credit to: Codemy.com for the initial code.
#See: https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw

from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random



#Initalize flashcards
def flashcardApp():
	hide_all_frames()
	botwSpecificFramez.pack(fill="both", expand=1)
	global showGenYD
	showGenYD = Label(botwSpecificFramez)
	showGenYD.pack(pady=15)
	global botwsfLst
	botwsfLst = ['max_attack', 'mighty_porgy', 'thistles', 'max_defense', 'armored_porgy', 'armoranth', 'stamina', 'endura_carrots', 'speed_boost', 'rushroom', 'lotus_seeds', 'stealthiness', 'shrooms', 'silent_princess', 'hearts', 'big_hearty_radish']

	global botwItemsLst
	botwItemsLst = {
	'max_attack':"max attack",
	'mighty_porgy':"mighty porgy",
	'thistles':"thistles",
	'max_defense':"max defense",
	'armored_porgy':"armored_porgy",
	'armoranth':"armoranth",
	'stamina':"stamina",
	'endura_carrots':"endura carrots",
	'speed_boost':"speed boost",
	'rushroom':"rushroom",
	'lotus_seeds':"lotus seeds",
	'stealthiness':"stealthiness",
	'shrooms':"shrooms",
	'silent_princess':"silent princess",
	'hearts':"hearts",
	'big_hearty_radish':"big hearty radish"
	}
	
	#Create empty answer list and counter
	answerList = []
	count = 1
	global answer
	
	while count < 4:
		onealCmdZ = randint(0, len(botwsfLst)-1)
		# If first selection, make it our answer
		if count == 1:
			answer = botwsfLst[onealCmdZ]
			global botwImgez
			onealCmde = "../BOTWAssets/" + botwsfLst[onealCmdZ] + ".png"
			botwImgez = ImageTk.PhotoImage(Image.open(onealCmde))
			showGenYD.config(image=botwImgez)
	
		#Add our first selection to a new list
		answerList.append(botwsfLst[onealCmdZ])

		# Remove from old list
		botwsfLst.remove(botwsfLst[onealCmdZ])

		#Shuffle original list
		random.shuffle(botwsfLst)	
		count += 1

	random.shuffle(answerList)

	global botwRadioSpec
	botwRadioSpec = StringVar()
	botwRadioSpec.set(botwItemsLst[answerList[0]])

	botwRadioButton1 = Radiobutton(botwSpecificFramez, text=botwItemsLst[answerList[0]], variable=botwRadioSpec, value=1).pack()
	botwRadioButton2 = Radiobutton(botwSpecificFramez, text=botwItemsLst[answerList[1]], variable=botwRadioSpec, value=2).pack()
	botwRadioButton3 = Radiobutton(botwSpecificFramez, text=botwItemsLst[answerList[2]], variable=botwRadioSpec, value=3).pack()

	#Add a pass button
	skipButton = Button(botwSpecificFramez, text="Pass", command=flashcardApp)
	skipButton.pack(pady=15)

	#Create a button to answer
	botwSpecificButtonedz = Button(botwSpecificFramez, text="Answer", command=botwItemsAnswers)
	botwSpecificButtonedz.pack(pady=15)

	#Create an answer label
	global correctLabel
	correctLabel = Label(botwSpecificFramez, text="", font=("helvetica", 18))
	correctLabel.pack(pady=15)

#Hide all previous frames
def hide_all_frames():
	for widget in botwSpecificFramez.winfo_children():
		widget.destroy()

	botwSpecificFramez.pack_forget()

# Displays the correct answer.
def botwItemsAnswers():
	response = botwItemsLst[answer]
	correctLabel.config(text=response)

root = Tk()
root.title('BOTW Quiz')
#root.iconbitmap('BOTWIcon.ico')
root.geometry("600x700")

#Create our menu
myMenu = Menu(root)
root.config(menu=myMenu)

#Create menu list items
menu = Menu(myMenu)
myMenu.add_cascade(label="BOTW", menu=menu)
menu.add_command(label="Quiz", command=flashcardApp)
menu.add_command(label="Exit", command=root.quit)

#Create our frames
botwSpecificFramez = Frame(root, width=600, height=600)

root.mainloop()
