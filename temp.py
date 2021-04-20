from tkinter import *
from functools import partial

checkk = 3
def blnk_space(frame_val):
    blnkspace = Label(frame_val,text = "")
    blnkspace.pack(side = TOP)
    return
    
def nextPage(pageNo,crntPage,yesOrNo,val):
    global count
    global checkk
    if yesOrNo == True:
        count.set(count.get() + val)
        checkk = count.get()
        
    crntPage.pack_forget()
    pageNo.pack(side = TOP,fill = "both", expand =True)
    return
    
    




    
  

#defining the words   
dt = {3 : "Android",
     4 : "Apple",
     5 : "AI",
     6 : "web",
     7 : "graphics",
     8 : "metrics",
     9 : "Computer",
     10 : "Internet",
     11 : "FreeSoftware",
     12 :"Steve Jobs"}
#creating the main window
root = Tk()
root.geometry("400x400")
root.title("GuessThePerson")

count = IntVar(root, value = 3)
scndPage = Frame(root)  
thirdPage = Frame(root)
fourthPage =Frame(root)
fifthPage = Frame(root)
sixthPage = Frame(root)
lastPage = Frame(root)
#This portions is the code for mainpage     
mainPage = Frame(root)
mainPage.pack(side = TOP,fill = "both",expand = True)

hd = Label(mainPage,text = "Choose a Word",fg = "black", font= ("Aerial" , 20,"bold")  ).pack()
blnk_space(mainPage)

#Displaying the words
for i in range(3,13):
    val = Label(mainPage,text = dt[i]).pack(side = TOP )

#adding blank space
blnk_space(mainPage)
blnk_space(mainPage)

nxt = Button(mainPage,text = "NEXT",command = partial(nextPage,scndPage,mainPage,False,0),highlightcolor = "RED")
nxt.place(x = 180,y = 300)

#To close the prgrm
close = Button(mainPage,text = "CLOSE" ,command = root.destroy).place(x = 176,y = 330)

#End here

#second page code
hd1 = Label(scndPage,text = "Word is there or not",fg = "black",font = ("Aerial",20,"bold")).pack()

val  = Label(scndPage,text ="Android").pack()
val  = Label(scndPage,text ="Apple").pack()
val  = Label(scndPage,text ="Graphics").pack()
val  = Label(scndPage,text ="Computer").pack()
val  = Label(scndPage,text ="Internet").pack()

btnYes1 = Button(scndPage,text = "YES",height = 2,width = 5,bg = "RED",fg = "WHITE" ,command = partial(nextPage,thirdPage,scndPage,True,1))
btnYes1.place(x = 100,y = 250)
btnNo1 = Button(scndPage,text = "NO",height = 2,width = 5,bg = "RED",fg = "WHITE", command = partial(nextPage,thirdPage,scndPage,False,0))
btnNo1.place(x = 250 , y = 250)
close = Button(scndPage,text = "CLOSE" ,command = root.destroy).place(x = 176,y = 330)
#ends here


#third page code 
hd2 = Label(thirdPage,text = "Word is there or not",fg = "black",font = ("Aerial",20,"bold")).pack()

val  = Label(thirdPage,text ="Android").pack()
val  = Label(thirdPage,text ="AI").pack()
val  = Label(thirdPage,text ="Graphics").pack()
val  = Label(thirdPage,text ="Web").pack()
val  = Label(thirdPage,text ="Free Software").pack()

btnYes2 = Button(thirdPage,text = "YES",height = 2,width = 5,bg = "RED",fg = "WHITE" ,command = partial(nextPage,fourthPage,thirdPage,True,2))
btnYes2.place(x = 100,y = 250)
btnNo2 = Button(thirdPage,text = "NO",height = 2,width = 5,bg = "RED",fg = "WHITE", command = partial(nextPage,fourthPage,thirdPage,False,0))
btnNo2.place(x = 250 , y = 250)
close = Button(thirdPage,text = "CLOSE" ,command = root.destroy).place(x = 176,y = 330)
#ends here

#fourth page code
hd3 = Label(fourthPage,text = "Word is there or not",fg = "black",font = ("Aerial",20,"bold")).pack()

val  = Label(fourthPage,text ="AI").pack()
val  = Label(fourthPage,text ="Metrics").pack()
val  = Label(fourthPage,text ="Apple").pack()
val  = Label(fourthPage,text ="Computer").pack()
val  = Label(fourthPage,text ="Steve Jobs").pack()

btnYes3 = Button(fourthPage,text = "YES",height = 2,width = 5,bg = "RED",fg = "WHITE" ,command = partial(nextPage,fifthPage,fourthPage,True,3))
btnYes3.place(x = 100,y = 250)
btnNo3 = Button(fourthPage,text = "NO",height = 2,width = 5,bg = "RED",fg = "WHITE", command = partial(nextPage,fifthPage,fourthPage,False,0))
btnNo3.place(x = 250 , y = 250)
close = Button(fourthPage,text = "CLOSE" ,command = root.destroy).place(x = 176,y = 330)
#end code Here

#fifth page code
hd4 = Label(fifthPage,text = "Word is there or not",fg = "black",font = ("Aerial",20,"bold")).pack()

val  = Label(fifthPage,text ="Web").pack()
val  = Label(fifthPage,text ="Graphics").pack()
val  = Label(fifthPage,text ="Steve Jobs").pack()
val  = Label(fifthPage,text ="Free Software").pack()
val  = Label(fifthPage,text ="Internet").pack()

btnYes4 = Button(fifthPage,text = "YES",height = 2,width = 5,bg = "RED",fg = "WHITE" ,command = partial(nextPage,sixthPage,fifthPage,True,4))
btnYes4.place(x = 100,y = 250)
btnNo4 = Button(fifthPage,text = "NO",height = 2,width = 5,bg = "RED",fg = "WHITE", command = partial(nextPage,sixthPage,fifthPage,False,0))
btnNo4.place(x = 250 , y = 250)
close = Button(fifthPage,text = "CLOSE" ,command = root.destroy).place(x = 176,y = 330)
#ends here

#sixth page code
hd5 = Label(sixthPage,text = "Word is there or not",fg = "black",font = ("Aerial",20,"bold")).pack()
    


val  = Label(sixthPage,text ="Metrics").pack()
val  = Label(sixthPage,text ="Free Software").pack()
val  = Label(sixthPage,text ="Steve Jobs").pack()
val  = Label(sixthPage,text ="Computer").pack()
val  = Label(sixthPage,text ="Internet").pack()

btnYes5 = Button(sixthPage,text = "YES",height = 2,width = 5,bg = "RED",fg = "WHITE" ,command = partial(nextPage,lastPage,sixthPage,True,5))
btnYes5.place(x = 100,y = 250)
btnNo5 = Button(sixthPage,text = "NO",height = 2,width = 5,bg = "RED",fg = "WHITE", command = partial(nextPage,lastPage,sixthPage,False,0))
btnNo5.place(x = 250 , y = 250)
close = Button(sixthPage,text = "CLOSE" ,command = root.destroy).place(x = 176,y = 330)
#ends here

hd6 = Label(lastPage,text = "The Word In Your Mind",fg = "blue",font = ("Aerial",20,"bold")).pack()
answer = count.get()
ans = Label(lastPage,text = answer)
ans.pack()


root.mainloop()
