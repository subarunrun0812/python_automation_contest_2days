# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, scrolledtext, PhotoImage
from auto_login import run_playwright

# スタイル設定
FONT = ("Arial", 12)
LABEL_BG = "#ffffff"  # 明るい青色の背景
BUTTON_BG = "#336699"  # 濃い青色
BUTTON_FG = "#000000"  # 黑色のテキスト（コントラストを高める）
ENTRY_BG = "#ffffff"  # 白色の背景
ENTRY_FG = "#000000"  # 黒色のテキスト
LISTBOX_BG = "#ffffff"  # 明るい白の背景
SWITCH_BG = "#f0f0f0"  # 明るいグレーの背景

def submit_form():
    username = entry_username.get()
    password = entry_password.get()
    insta1 = entry_insta1.get()
    insta2 = entry_insta2.get()
    # Call the Playwright function with the input data
    result = run_playwright(username, password, insta1, insta2)
    messagebox.showinfo("送信情報", "ユーザ名: {}\nパスワード: {}\nインスタ1: {}\nインスタ2: {}".format(username, password, insta1, insta2))
    display_list(result)

def load_list_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        messagebox.showerror("エラー", f"ファイルが見つかりません: {file_path}")
        return []

def display_list(result):
    list_items = result # ファイルパスを適宜変更
    listbox.delete('1.0', tk.END)
    for i, item in enumerate(list_items, start=1):
        listbox.insert(tk.END, f"{i}. {item}\n")

app = tk.Tk()
app.title("フォームアプリ")
app.geometry("400x600") 

# 背景画像を読み込む
bg_image = PhotoImage(file="../background .png")  # 画像ファイル名を適宜変更

# 背景画像を表示するラベルを作成
bg_label = tk.Label(app, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ユーザ名入力
label_username = tk.Label(app, text="自分のユーザ名:", bg=LABEL_BG, font=FONT)
label_username.pack(pady=5)
entry_username = tk.Entry(app, font=FONT, bg=ENTRY_BG, fg=ENTRY_FG, borderwidth=2, relief="groove")
entry_username.pack(pady=5)

# パスワード入力
label_password = tk.Label(app, text="パスワード:", bg=LABEL_BG, font=FONT)
label_password.pack(pady=5)
entry_password = tk.Entry(app, show="*", font=FONT, bg=ENTRY_BG, fg=ENTRY_FG, borderwidth=2, relief="groove")
entry_password.pack(pady=5)

# インスタアカウント名1
label_insta1 = tk.Label(app, text="対象のインスタアカウント名1:", bg=LABEL_BG, font=FONT)
label_insta1.pack(pady=5)
entry_insta1 = tk.Entry(app, font=FONT, bg=ENTRY_BG, fg=ENTRY_FG, borderwidth=2, relief="groove")
entry_insta1.pack(pady=5)

# インスタアカウント名2
label_insta2 = tk.Label(app, text="対象のインスタアカウント名2:", bg=LABEL_BG, font=FONT)
label_insta2.pack(pady=5)
entry_insta2 = tk.Entry(app, font=FONT, bg=ENTRY_BG, fg=ENTRY_FG, borderwidth=2, relief="groove")
entry_insta2.pack(pady=5)

# 送信ボタン
submit_button = tk.Button(app, text="送信", command=submit_form, bg=BUTTON_BG, fg=BUTTON_FG, font=FONT)
submit_button.pack(pady=10)

# スクロール可能なリストボックスのスタイルを調整
listbox = scrolledtext.ScrolledText(app, height=10, font=FONT, bg=LISTBOX_BG, fg=ENTRY_FG, borderwidth=4, relief="groove")
listbox.pack(pady=10)

app.mainloop()
