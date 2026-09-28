import tkinter as tk
from tkinter import messagebox
import os
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

def show_chart():
    data = pd.read_csv("Personal_Analyst_Data.csv")

    categories = ["Sleep", "Study", "Coding", "Screen"]
    averages = [
        data["Sleep"].mean(),
        data["Study"].mean(),
        data["Coding"].mean(),
        data["Screen"].mean()
    ]

    plt.bar(categories, averages)
    plt.ylabel("Hours")
    plt.title("Average Daily Activity")
    plt.show()

def save_data():
    try:
        sleep = float(sleep_entry.get())
        study = float(study_entry.get())
        coding = float(coding_entry.get())
        screen = float(screen_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numbers only.")
        return
    if not (0 <= sleep <= 24 and
        0 <= study <= 24 and
        0 <= coding <= 24 and
        0 <= screen <= 24 and (sleep+coding+study+screen)<=24):
        messagebox.showerror("Invalid Input", "Hours must be between 0 and 24.")
        return

    with open("Personal_Analyst_Data.csv","a") as file:
        file.write(f"{today},{sleep},{study},{coding},{screen}\n")
    messagebox.showinfo("Success", "Data Saved Successfully!")
    sleep_entry.delete(0,tk.END)
    study_entry.delete(0,tk.END)
    coding_entry.delete(0,tk.END)
    screen_entry.delete(0,tk.END)
    data = pd.read_csv("Personal_Analyst_Data.csv")
    avg_sleep.config(text=f"Average Sleep: {data['Sleep'].mean():.2f} hrs")
    avg_study.config(text=f"Average Study: {data['Study'].mean():.2f} hrs")
    avg_coding.config(text=f"Average Coding: {data['Coding'].mean():.2f} hrs")
    avg_screen.config(text=f"Average Screen: {data['Screen'].mean():.2f} hrs")

today = date.today()

if not os.path.exists("Personal_Analyst_Data.csv"):
    with open("Personal_Analyst_Data.csv","w") as file:
        file.write(f"Date,Sleep,Study,Coding,Screen\n")

window  = tk.Tk()
window.title("Personal Analyst")
window.geometry("800x500")
window.configure(bg="lightblue")
title = tk.Label(window,text="Personal Analyst", font=("Arial",30,"bold"), bg="Lightblue" ,fg="black")
title.pack()

form = tk.Frame(window, bg="lightblue")
form.pack(side=tk.LEFT, fill=tk.BOTH, expand=True,padx=30,pady=30)

tk.Label(form, text="Sleep Hours",bg="lightblue",fg="black").grid(row=0,column=0,padx=10,pady=8)
sleep_entry = tk.Entry(form,bg="lightblue",fg="black")
sleep_entry.grid(row=0,column=1)

tk.Label(form, text="Study Hours",bg="lightblue",fg="black").grid(row=1,column=0,padx=10,pady=8)
study_entry = tk.Entry(form,bg="lightblue",fg="black")
study_entry.grid(row=1,column=1)

tk.Label(form, text="Coding Hours",bg="lightblue",fg="black").grid(row=2,column=0,padx=10,pady=8)
coding_entry = tk.Entry(form,bg="lightblue",fg="black")
coding_entry.grid(row=2,column=1)

tk.Label(form, text="Screen time",bg="lightblue",fg="black").grid(row=3,column=0,padx=10,pady=8)
screen_entry = tk.Entry(form,bg="lightblue",fg="black")
screen_entry.grid(row=3,column=1)

save_button = tk.Button(form,text="Save", command=save_data,bg="white",fg="black")
save_button.grid(row=4,column=1, padx=10, pady=15)

data = pd.read_csv("Personal_Analyst_Data.csv")
print(data)

data_analysis = tk.Frame(window,bg="lightblue")
data_analysis.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True,padx=30,pady=30)

avg_sleep = tk.Label(data_analysis,text=f"Average Sleep: {data['Sleep'].mean():.2f} hrs",bg="lightblue",fg="black")
avg_sleep.grid(row=0,column=0,padx=10,pady=8)
avg_study = tk.Label(data_analysis,text=f"Average Study: {data['Study'].mean():.2f} hrs",bg="lightblue",fg="black")
avg_study.grid(row=1,column=0,padx=10,pady=8)
avg_coding = tk.Label(data_analysis,text=f"Average Coding: {data['Coding'].mean():.2f} hrs",bg="lightblue",fg="black")
avg_coding.grid(row=2,column=0,padx=10,pady=8)
avg_screen = tk.Label(data_analysis,text=f"Average Screen: {data['Screen'].mean():.2f} hrs",bg="lightblue",fg="black")
avg_screen.grid(row=3,column=0,padx=10,pady=8)

chart_button = tk.Button(data_analysis,text="Show Chart",command=show_chart)
chart_button.grid(row=4, column=0, padx=10, pady=15)

window.mainloop()
