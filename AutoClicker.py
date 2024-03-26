import tkinter as tk
import pyautogui
from time import *

class ClickerApp:
    def __init__(self, master):
        self.master = master
        master.title("Clicker App")

        self.label_clicks = tk.Label(master, text="Введите количество кликов:")
        self.label_clicks.pack()

        self.clicks_entry = tk.Entry(master)
        self.clicks_entry.pack()

        self.label_freq = tk.Label(master, text="Введите частоту кликов (в мс):")
        self.label_freq.pack()

        self.freq_entry = tk.Entry(master)
        self.freq_entry.pack()

        self.label_side = tk.Label(master, text="Введите используемую для кликов кнопку (правая, левая):")
        self.label_side.pack()

        self.side_entry = tk.Entry(master)
        self.side_entry.pack()

        self.button = tk.Button(master, text="Начать клики", command=self.start_clicks)
        self.button.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

    def start_clicks(self):
        try:
            clicks = int(self.clicks_entry.get())
            freq = int(self.freq_entry.get())/1000
            if self.side_entry.get().lower().startswith("п"):
                side = "right"
                self.status_label.config(text="Клики начались!")
            elif self.side_entry.get().lower().startswith("л"):
                side = "left"
                self.status_label.config(text="Клики начались!")
            else:
                self.status_label.config(text="Ошибка: введите используемую для кликов кнопку!")
            for i in range(clicks):
                pyautogui.click(button=side)
                sleep(freq)
            self.status_label.config(text="Клики завершены!")
        except ValueError:
            self.status_label.config(text="Ошибка: введите число и частоту кликов!")

root = tk.Tk()
my_clicker_app = ClickerApp(root)
root.mainloop()