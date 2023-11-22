import customtkinter
window = ["600", "600"]

app = customtkinter.CTk()
app.geometry(window[0] + "x" + window[1])
app.title("EQ Tester")

tabview = customtkinter.CTkTabview(master=app, width=(int(window[0]) - 20), height=(int(window[0]) - 10))
tabview.pack(padx=0, pady=0)

tabview.add("Basic")  # add tab at the end
tabview.add("Advanced")  # add tab at the end
tabview.set("Basic")  # set currently visible tab

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

optionmenu = customtkinter.CTkOptionMenu(master=tabview.tab("Basic"), values=["option 1", "option 2"], command=optionmenu_callback)
optionmenu.set("option 2")

app.mainloop()