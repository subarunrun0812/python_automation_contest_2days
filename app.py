# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox

def submit_form():
    username = entry_username.get()
    password = entry_password.get()
    insta1 = entry_insta1.get()
    insta2 = entry_insta2.get()
    messagebox.showinfo("送信情報", "ユーザ名: {}\nパスワード: {}\nインスタ1: {}\nインスタ2: {}".format(username, password, insta1, insta2))

app = tk.Tk()
app.title("フォームアプリ")

# ユーザ名入力
label_username = tk.Label(app, text="自分のユーザ名:")
label_username.pack()
entry_username = tk.Entry(app)
entry_username.pack()

# パスワード入力
label_password = tk.Label(app, text="パスワード:")
label_password.pack()
entry_password = tk.Entry(app, show="*")
entry_password.pack()

# インスタアカウント名1
label_insta1 = tk.Label(app, text="対象のインスタアカウント名1:")
label_insta1.pack()
entry_insta1 = tk.Entry(app)
entry_insta1.pack()

# インスタアカウント名2
label_insta2 = tk.Label(app, text="対象のインスタアカウント名2:")
label_insta2.pack()
entry_insta2 = tk.Entry(app)
entry_insta2.pack()

# 送信ボタン
submit_button = tk.Button(app, text="送信", command=submit_form)
submit_button.pack()

app.mainloop()
