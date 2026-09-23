import tkinter as tk
import os
from datetime import date
import pandas as pd

def save_data():
    sleep = float(sleep_entry.get())
    study = float(study_entry.get())
    coding = float(coding_entry.get())
    screen = float(screen_entry.get())
    print("Sleep : ",sleep)
    print("Study : ",study)
    print("Coding: ",coding)
    print("Screen: ",screen)
    with open("Personal_Analyst_Data.csv","a") as file:
        file.write(f"{today},{sleep},{study},{coding},{screen}\n")
    status.config(text="Data saved!")
    sleep_entry.delete(0,tk.END)
    study_entry.delete(0,tk.END)
    coding_entry.delete(0,tk.END)
    screen_entry.delete(0,tk.END)

today = date.today()


if not os.path.exists("Personal_Analyst_Data.csv"):
    with open("Personal_Analyst_Data.csv","w") as file:
        file.write(f"Date,Sleep,Study,Coding,Screen\n")

window  = tk.Tk()
window.title("Personal Analyst")
window.geometry("800x500")
title = tk.Label(window,text="Personal Analyst", font=("Arial",30))
title.pack()

form = tk.Frame(window)
form.pack(pady=30)

tk.Label(form, text="Sleep Hours").grid(row=0,column=0)
sleep_entry = tk.Entry(form)
sleep_entry.grid(row=0,column=1)

tk.Label(form, text="Study Hours").grid(row=1,column=0)
study_entry = tk.Entry(form)
study_entry.grid(row=1,column=1)

tk.Label(form, text="Coding Hours").grid(row=2,column=0)
coding_entry = tk.Entry(form)
coding_entry.grid(row=2,column=1)

tk.Label(form, text="Screen time").grid(row=3,column=0)
screen_entry = tk.Entry(form)
screen_entry.grid(row=3,column=1)

status = tk.Label(form,text="")
status.grid(row=4,column=3)

save_button = tk.Button(form,text="Save", command=save_data)
save_button.grid(row=0,column=3)

data = pd.read_csv("Personal_Analyst_Data.csv")
print(data)

window.mainloop()