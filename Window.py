import customtkinter
window = ["800", "600"]

app = customtkinter.CTk()
app.geometry(window[0] + "x" + window[1])
app.title("EQ Tester")

tabview = customtkinter.CTkTabview(master=app, width=(int(window[0]) - 20), height=(int(window[0]) - 10))
tabview.pack(padx=0, pady=0)
tabview.add("Basic")  # add tab at the end
tabview.add("Advanced")  # add tab at the end
tabview.set("Basic")  # set currently visible tab

# mainframe = customtkinter.CTkFrame(tabview.tab("Basic"))
# mainframe.grid(column=0,row=0)
# mainframe.columnconfigure(0, weight = 1)
# mainframe.rowconfigure(0, weight = 1)
# mainframe.pack(pady = 100, padx = 400)

app.grid_columnconfigure(0, weight=1)

label1 = customtkinter.CTkLabel(master=tabview.tab("Basic"), text="Please select a value from 1-10 corresponding to your assesment of your own qualities as mentioned.", padx=100)
label1.pack()

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

optionmenu = customtkinter.CTkComboBox(master=tabview.tab("Basic"), values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], command=optionmenu_callback)
optionmenu.set("Select a value...")
optionmenu.pack()

app.mainloop()