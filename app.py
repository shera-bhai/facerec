import os
import subprocess
from tkinter import *
from tkinter import ttk
from CTkTable import *
import customtkinter as ctk
from PIL import Image, ImageTk, ImageFilter
from CTkMessagebox import CTkMessagebox as mb

class Second_Screen(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1920x1080")
        self.resizable(False, True)
        self.title("Face Recognition Attendance System")
        self.after(0, lambda:self.state('zoomed'))
        self.font = ctk.CTkFont('arial', 30, weight="bold")
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.open = ctk.CTkImage(dark_image=Image.open(self.path + "/assets/bkg2.jpg"), size=(1550, 900))
        self.bkg = ctk.CTkLabel(self, image=self.open, text='').pack(padx=1, pady=1)
        self.btn_1 = ctk.CTkButton(self, text="Train Model", anchor=ctk.CENTER, compound="top", width=250, height=230, command=self.train_model, font=self.font, border_color="white", border_width=2, corner_radius=10, bg_color="#002949")
        self.btn_1.place(x=120, y=445)
        self.btn_2 = ctk.CTkButton(self, text="Mark Attendance", anchor=ctk.CENTER, compound="top", width=250, height=230, command=self.track_faces, font=self.font, border_color="white", border_width=2, corner_radius=10, bg_color="#002949")
        self.btn_2.place(x=635, y=445)
        self.btn_3 = ctk.CTkButton(self, text="Check Attendance", anchor=ctk.CENTER, compound="top", width=250, height=230, command=self.train_model, font=self.font, border_color="white", border_width=2, corner_radius=10, bg_color="#002949")
        self.btn_3.place(x=1130, y=445)

    def train_model(self):
        subprocess.Popen(["python", "train_model.py"])

    def track_faces(self):
        subprocess.Popen(["python", "track_faces.py"])

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1920x1080")
        self.resizable(False, True)
        self.after(0, lambda:self.state('zoomed'))
        self.title("Face Recognition Attendance System")
        self.font = ctk.CTkFont('arial', 30, weight="bold")
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.open = ctk.CTkImage(dark_image=Image.open(self.path + "/assets/bkg.jpg"), size=(1550, 900))
        self.bkg = ctk.CTkLabel(self, image=self.open, text='').pack(padx=1, pady=1)
        self.btn_1 = ctk.CTkButton(self, text="Get Started", anchor=ctk.CENTER, compound="top", width=220, height=50, command=self.second_scrn, font=self.font, border_color="white", border_width=2, corner_radius=10, bg_color="#002949")
        self.btn_1.place(x=80, y=565)
        self.protocol('WM_DELETE_WINDOW', self.close_window)
        self.second_win = None

    def second_scrn(self):
        if self.second_win is None or not self.second_win.winfo_exists():
            self.second_win = Second_Screen(self)
            self.second_win.focus()
        else:
            self.second_win.focus()

    def close_window(self):
        res = mb(title="Exit?", message="Are you sure you want to close the program?", icon="question", option_1="Cancel", option_2="Yes")
        if res.get() == "Yes":
            print(">>> Program Exited!")
            self.destroy()

if __name__ == "__main__":
    app = App()
    # app.after(0, lambda:app.state('zoomed'))
    app.mainloop()