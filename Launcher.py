import customtkinter
import LauncherFunctions
import webbrowser
import subprocess
from tkinter import PhotoImage


togglecounter = 1
MainMenuCunter=0
GuessCounter = 0

def close_window(event=None):
    app.destroy()

app = customtkinter.CTk()
app.title("Launcher")
app.geometry("600x500")
app.iconbitmap("C:\\Users\\jacob\\Downloads\\Python\\icon.ico")
app.grid_columnconfigure((0), weight=5)
app.grid_rowconfigure((0), weight=5)
app._windows_set_titlebar_color("#FFFFFF")
app.bind("<Escape>", close_window)
customtkinter.set_appearance_mode("dark")

"""Launching Stuff"""




with open("Username.txt", "r") as UsernameFile:
    UsernameTXT = UsernameFile.read()
    print(UsernameTXT)

with open("Password.txt", "r") as PasswordFile:
    PasswordTXT = PasswordFile.read()
    print(PasswordTXT)


def UsernameLogin():
    global MainMenuCunter
    Username = UsernameEntry.get()
    Password = PasswordEntry.get()
    if Username == UsernameTXT:
        if Password == PasswordTXT:
            UsernamePassword.destroy()
            LoginButton.destroy()
            LoginLabel.destroy()
            UsernameEntry.destroy()
            MainMenuCunter=1
            OptionMenuPlace()
    else:
        LoginButton.configure(text="Incorrect" ,font=("Arial Black", 15))


def GuessCheckYes():
    GuessFrame.destroy()
    UsernamePassword.place(x=140, y=100)

def GuessCheckNo():
    global UsernameEditEntry
    global PasswordEditEntry
    UsernameEditEntry = customtkinter.CTkEntry(master=GuessFrame, placeholder_text='Username', width=140, height=28)
    PasswordEditEntry = customtkinter.CTkEntry(master=GuessFrame, placeholder_text='Password', width=140, height=28)
    SignUpButton = customtkinter.CTkButton(master=GuessFrame, text='Sign Up', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=SignUpCommand)
    GuessNoButton.destroy()
    GuessYesButton.destroy()
    UsernameEditEntry.place(x=85, y=90)
    PasswordEditEntry.place(x=85, y=130)
    SignUpButton.place(x=85, y=170)
    
def SignUpCommand():
    with open("Username.txt", "w") as UsernameEditFile:
        UsernameEditEntryString = UsernameEditEntry.get()
        UsernameEditFile.write(UsernameEditEntryString)
        print(UsernameEditEntryString)

    with open("Password.txt", "w") as PasswordEditFile:
        PasswordEditEntryString = PasswordEditEntry.get()
        PasswordEditFile.write(PasswordEditEntryString)
        print(PasswordEditEntryString)



GuessFrame = customtkinter.CTkFrame(app, width=300, height=250)
GuessFrame.place(x=140, y=100)
GuessLabel = customtkinter.CTkLabel(master=GuessFrame, text='Jacob`s Launcher', width=40, height=28, fg_color='transparent',font=("Arial Black", 20), text_color='#ADD8E6')
GuessLabel.place(x=60, y=45)
GuessYesButton = customtkinter.CTkButton(master=GuessFrame, text='Yes', width=90, height=28, command=GuessCheckYes)
GuessYesButton.place(x=180, y=120)
GuessNoButton = customtkinter.CTkButton(master=GuessFrame, text='No', width=90, height=28,command=GuessCheckNo)
GuessNoButton.place(x=40, y=120)
UsernamePassword = customtkinter.CTkFrame(app, width=300, height=250)
LoginLabel = customtkinter.CTkLabel(master=UsernamePassword, text='Jacob`s Launcher', width=40, height=28, fg_color='transparent',font=("Arial Black", 20), text_color='#ADD8E6')
LoginLabel.place(x=70, y=45)
UsernameEntry = customtkinter.CTkEntry(master=UsernamePassword, placeholder_text='Username', width=140, height=28)
UsernameEntry.place(x=85, y=90)
PasswordEntry = customtkinter.CTkEntry(master=UsernamePassword, placeholder_text='Password', width=140, height=28)
PasswordEntry.place(x=85, y=130)
LoginButton = customtkinter.CTkButton(master=UsernamePassword, text='Log In', width=140, height=28, corner_radius=32, command=UsernameLogin, fg_color='#A020F0')
LoginButton.place(x=85, y=170)
StartUpFrame = customtkinter.CTkFrame(app, width=300, height=330)





def optionmenu_callback(choice):
    global LordsofFallenButton
    global FNAF2Button
    global SubNauticaButton
    global RE4RButton
    global RE7Button
    global CyberPunk
    global SteamButton
    global RainMeterButton
    global HydraButton
    global AssassinsCreedUnityButton

    if choice == 'StartUp':
        StartUpFrame.place(x=140, y=100)
        AssassinsCreedUnityButton.destroy()
        FNAF2Button.destroy()
        CyberPunk.destroy()
        RE7Button.destroy()
        RE4RButton.destroy()
        SubNauticaButton.destroy()
        LordsofFallenButton.destroy()
        SteamButton = customtkinter.CTkButton(master=StartUpFrame, text='Steam', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.Steam_Launch)
        RainMeterButton = customtkinter.CTkButton(master=StartUpFrame, text='Rainmeter', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.RainMeter_Launch)
        HydraButton = customtkinter.CTkButton(master=StartUpFrame, text='Hydra', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.Hydra_Launch)
        SteamButton.place(x=80, y=20)
        RainMeterButton.place(x=80, y=60)
        HydraButton.place(x=80, y=100)
    if choice == 'Games':
        if togglecounter == 1:
            StartUpFrame.place(x=140, y=100)
            SteamButton.destroy()
            RainMeterButton.destroy()
            HydraButton.destroy()
            AssassinsCreedUnityButton = customtkinter.CTkButton(master=StartUpFrame, text='ACU', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.ACULaunch)
            CyberPunk = customtkinter.CTkButton(master=StartUpFrame, text='Cyberpunk', width=140, height=28, corner_radius=32, fg_color='#A020F0',command=LauncherFunctions.CyberPunkLaunch)
            RE7Button = customtkinter.CTkButton(master=StartUpFrame, text='RE7', width=140, height=28, corner_radius=32 , fg_color='#A020F0', command=LauncherFunctions.RE7Launch)
            RE4RButton = customtkinter.CTkButton(master=StartUpFrame, text='RE4R', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.RE4RLaunch)
            SubNauticaButton = customtkinter.CTkButton(master=StartUpFrame, text='Subnautica', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.SubNauticaLaunch)
            FNAF2Button = customtkinter.CTkButton(master=StartUpFrame, text='Fnaf 2', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.FNAF2Launch)
            LordsofFallenButton = customtkinter.CTkButton(master=StartUpFrame, text='Lords of Fallen', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.LordsofFallenLaunch)
            AssassinsCreedUnityButton.place(x=80, y=20)
            CyberPunk.place(x=80, y=60)
            RE7Button.place(x=80, y=100)
            RE4RButton.place(x=80, y=140)
            SubNauticaButton.place(x=80, y=180)
            FNAF2Button.place(x=80, y=220)
            LordsofFallenButton.place(x=80, y=260)








"""Start Up Buttons"""

SteamButton = customtkinter.CTkButton(master=StartUpFrame, text='Steam', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.Steam_Launch)
RainMeterButton = customtkinter.CTkButton(master=StartUpFrame, text='Rainmeter', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.RainMeter_Launch)
HydraButton = customtkinter.CTkButton(master=StartUpFrame, text='Hydra', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.Hydra_Launch)







"""Game Screen"""
AssassinsCreedUnityButton = customtkinter.CTkButton(app, text='ACU', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.ACULaunch)
CyberPunk = customtkinter.CTkButton(master=StartUpFrame, text='Cyberpunk', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.CyberPunkLaunch)
RE7Button = customtkinter.CTkButton(master=StartUpFrame, text='RE7', width=140, height=28, corner_radius=32 , fg_color='#A020F0', command=LauncherFunctions.RE7Launch)
RE4RButton = customtkinter.CTkButton(master=StartUpFrame, text='RE4R', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.RE4RLaunch)
SubNauticaButton = customtkinter.CTkButton(master=StartUpFrame, text='Subnautica', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.SubNauticaLaunch)
FNAF2Button = customtkinter.CTkButton(master=StartUpFrame, text='Fnaf 2', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.FNAF2Launch)
LordsofFallenButton = customtkinter.CTkButton(master=StartUpFrame, text='Lords of Fallen', width=140, height=28, corner_radius=32, fg_color='#A020F0', command=LauncherFunctions.LordsofFallenLaunch)





optionmenu_var = customtkinter.StringVar(value='Main Menu')
optionmenu = customtkinter.CTkOptionMenu(app,values=['StartUp', 'Games'],
                                         width=140, height=28,
                                         command=optionmenu_callback,
                                         variable=optionmenu_var)

def OptionMenuPlace():
    if MainMenuCunter==1:
        optionmenu.place(x=10, y=10)

app.mainloop()