import random
import tkinter as tk
import customtkinter

rock = 1
paper = 2
scissors = 3

def cpu_choice():
    global CPU
    CPU = random.randint(1, 3)

root = tk.Tk()
root.config(bg="#2e2e2e")


lbl = tk.Label(root, text="Rock, Paper, Or Scissors?", font=("Bebas Neue", 40, "bold"), bg="#2e2e2e", fg="#D3D3D3")
lbl.grid(row=0, column=1, padx=50, pady=50)

def on_click_rock():
    cpu_choice()
    if CPU == rock:
        lbl_output.config(text="Tie!")
    elif CPU == paper:
        lbl_output.config(text="You Lose!")
    elif CPU == scissors:
        lbl_output.config(text="You win!")

def on_click_paper():
    cpu_choice()
    if CPU == paper:
        lbl_output.config(text="Tie!")
    elif CPU == rock:
        lbl_output.config(text="You win!")
    elif CPU == scissors:
        lbl_output.config(text="You Lose!")

def on_click_scissors():
    cpu_choice()
    if CPU == scissors:
        lbl_output.config(text="Tie!")
    elif CPU == rock:
        lbl_output.config(text="You Lose!")
    elif CPU == paper:
        lbl_output.config(text="You win!")

lbl_output = tk.Label(root, text="waiting for action..", font=("Bebas Neue", 24, "bold"), height="2", width="20",bg="#4682B4", fg="#D3D3D3")
lbl_output.grid(row=1, column=1, padx=90, pady=180)

root.geometry("1280x720")

root.title("Rock, Paper, Scissors!")

btn_rock = customtkinter.CTkButton(root, text="Rock", command=on_click_rock, height=55, width=150, font=("Bebas Neue", 20) ,fg_color="#4682B4")
btn_rock.grid(row=2, column=0, padx=50, pady=0)
btn_paper = customtkinter.CTkButton(root, text="Paper", command=on_click_paper, height=55, width=150, font=("Bebas Neue", 20),fg_color="#4682B4")
btn_paper.grid(row=2, column=1, padx=50, pady=0)
btn_scissors = customtkinter.CTkButton(root, text="Scissors", command=on_click_scissors, height=55, width=150, font=("Bebas Neue", 20),fg_color="#4682B4")
btn_scissors.grid(row=2, column=2, padx=50, pady=0)

root.mainloop()