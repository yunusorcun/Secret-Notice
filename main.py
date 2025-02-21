import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import base64
def encode(key,clear):
    enc=[]
    for i in range(len(clear)):
        key_c= key[i%len(key)]
        enc_c=chr((ord(clear[i])+ord(key_c))%256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key,enc):
    dec=[]
    enc= base64.urlsafe_b64encode(enc).decode()
    for i in range(len(enc)):
        key_c=key[i%len(key)]
        dec_c= chr((256+ord(edc[i])-ord(key_c))%256)
        dec.append(dec_c)
    return "".join(dec)

def save_and_encrypt_notes():
    title = title_entry.get()
    message = secrets_text.get("1.0", tk.END)  #  imput_text -> secrets_text
    master_secret = master_secrets_entry.get()
    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error", message="Please enter all info")
    else:
        #encryption
        massage_encrypted=encode(master_secret,message)
        with open("mysecret.txt", "a") as data_file:  # Append modunda açıyoruz.
            data_file.write(f"\n{title}\n{massage_encrypted}")  # Python string de yeni satıra geçme.
        title_entry.delete(0, END) #mysecret i silmek için.
        secrets_text.delete("1.0", END)
        master_secrets_entry.delete(0, END)
# Ekran oluşturma
window = tk.Tk()
FONT = ("Verdana", 20, "normal")
window.title("Secret Notice")
window.minsize(width=350, height=600)
window.config(padx=10, pady=10, bg="black")

# Görüntü dosyasının yolu
image_path = "E:/Pyton Öğreniyorum/Pycharm/pythonProject/Secret_Notice/arma.jpg"

# Pillow kullanarak resmi açma ve yeniden boyutlandırma
try:
    pil_image = Image.open(image_path)
    pil_image = pil_image.resize((100, 100), Image.LANCZOS)  # Resmi boyutlandırma (100x100)
    tk_image = ImageTk.PhotoImage(pil_image)

    image_label = tk.Label(window, image=tk_image)
    image_label.image = tk_image  # Referansı saklamak için bu satır önemli
    image_label.pack(padx=10, pady=10)
except Exception as e:
    print(f"Error: {e}")

# Başlık oluşturma alanı oluşturmak için
title_input_label = Label(text="Enter your title", font=FONT)
title_input_label.config(padx=10, pady=10, bg="black", fg="white")
title_input_label.pack()

# İsteklerimizi almak için Entry widget'i oluşturuyoruz.
title_entry = tk.Entry(width=30, bg="white")
title_entry.focus()
title_entry.pack()

# Saklamak istediğin bilgiyi gir.
secrets_input_label = Label(text="Enter Your Secret", font=FONT)
secrets_input_label.config(padx=10, pady=10, bg="black", fg="white")
secrets_input_label.pack()

secrets_text = Text(width=30, bg="white", height=10)
secrets_text.pack()

# Bilgi almak için key girmemiz gerekiyor bu kısım onun için.
key_input_label = Label(text="Enter Master Key", font=FONT)
key_input_label.config(padx=10, pady=10, bg="black", fg="white")
key_input_label.pack()

master_secrets_entry = tk.Entry(width=30, bg="white")  # Değişken adı düzeltildi
master_secrets_entry.focus()
master_secrets_entry.pack()

# Save button
save_button = tk.Button(text="Save & Encrypt", command=save_and_encrypt_notes)
save_button.pack()

# Girdiğimiz verileri karşılaştırmak için buton eklemeliyiz.
decrypt_button = Button(text="Decrypt")  # Command kısmı girilmedi
decrypt_button.pack()

# Ekranı başlatma
window.mainloop()
