import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Ekran oluşturma
window = tk.Tk()
FONT=("Verdana",20,"normal")
window.title("Secret Notice")
window.minsize(width=350, height=600)
window.config(padx=10, pady=10)
window.config(bg="black")


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

#butona atama yapma

def Save_Encrypt():
    title = title_input.get()



#Başlık oluşturma alanı oluşturmak için
title_input_label= Label(text="Enter your title",font=FONT)
title_input_label.config(padx=10,pady=10)
title_input_label.config(bg="black",fg="white")
title_input_label.pack()

#İsteklerimizi almak için Entry widget'i oluşturuyoruz.
title_input = Entry(width=30, bg="white")
title_input.focus()
title_input.pack()

#Saklamak istedğin bilgiyi gir.
secrets_input_label= Label(text="Enter Your Secret")
secrets_input_label.config(padx=10,pady=10)
secrets_input_label.config(bg="black",fg="white")
secrets_input_label.pack()

secrets_text=Text(width=30,bg="white",height=10)
secrets_text.pack()

#Bilgi almak için key girmemiz gerekiyor bu kısım onun için.
key_input_label= Label(text="Enter Master Key")
key_input_label.config(padx=10,pady=10)
key_input_label.config(bg="black",fg="white")
key_input_label.pack()

title_input = Entry(width=30, bg="white")
title_input.focus()
title_input.pack()

#save button
save_button=Button(text="Save & Encrypt",command=Save_Encrypt)
save_button.pack()

#Girdiğimiz verileri karşılaştırmak için buton eklemeliyiz.
decrypt_button=Button(text="decrypt") #command kısmı gir
decrypt_button.pack()



# Ekranı başlatma
window.mainloop()
