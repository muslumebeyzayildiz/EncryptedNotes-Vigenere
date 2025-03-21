from tkinter import *
from tkinter import messagebox

from vigenere_sifrele import *

window = Tk()
window.title("Secret Note App with Tkinter Python")
window.minsize(width=600,height=600)
window.config(padx=10,pady=10)
img = PhotoImage(file="pngSecret.png")

def saveEncryptionBTTN():
    title = ttlEntry.get().strip()#strip() ile boşluklardan arındırılır.
    metin = secretText.get("1.0", END).strip()
    anahtar = masterKeyEntry.get().strip()

    if title == "" or metin == "" or anahtar == "":
        messagebox.showwarning("Warning","Please fill in all fields.")
        return""
    # Sadece Türkçe harfler içeren metin oluştur
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    temiz_metin = ''.join(c for c in metin.lower() if c in alfabe)

    if not temiz_metin:
        messagebox.showwarning("Uyarı","Metin şifrelenebilir karakter içermiyor (sadece Türkçe harfler desteklenir).")
        return


    sifrelenmis_metin = vigenere_sifrele(metin, anahtar)

    try:
        with open("mysecret.txt", "a", encoding="utf-8") as file:
            file.write(f"TITLE: {title}\n")
            file.write(f"ENCRYPTED: {sifrelenmis_metin}\n")
            file.write("-----\n")
            #"mysecret.txt": Bu isimle dosya oluşturur veya varsa açar.
            #Append mod — dosya varsa üzerine yazmaz, en sona ekleme yapar.
            #encoding="utf-8": Türkçe karakterlerin bozulmaması için.
            #with: Dosya ile işimiz bittiğinde otomatik olarak kapatır (güvenlidir).

            secretText.delete("1.0", END)

        messagebox.showinfo("Successful", "Note encrypted and saved successfully!")
    except:
        messagebox.showerror("Mistake", "Error saving the file.")


def decryptBTTN():
    title = ttlEntry.get().strip()
    anahtar = masterKeyEntry.get().strip()

    if title == "" or anahtar == "":
        messagebox.showwarning("Uyarı", "Lütfen başlık ve anahtarı girin.")
        return

    try:
        with open("mysecret.txt", "r", encoding="utf-8") as file:#Dosyayı okuma modunda ("r") aç
            lines = file.readlines()#tüm satırları bir listeye alır (lines[0], lines[1]...

        found = False#Şifrelenmiş başlık bulundu mu kontrol etmek için
        for i in range(len(lines)):#TITLE: ile başlayan satırlardan biri kullanıcının girdiği başlıkla eşleşirse, doğru not bulundu demektir.
            if lines[i].startswith(f"TITLE: {title}"):
                encrypted_line = lines[i+1]
                if encrypted_line.startswith("ENCRYPTED: "):#"ENCRYPTED: " kısmını çıkarSadece şifreli metni alıyoruz.
                    encrypted_text = encrypted_line.replace("ENCRYPTED: ", "").strip()
                    try:
                        decrypted_text = vigenere_desifrele(encrypted_text, anahtar)
                        secretText.delete("1.0", END)#Ekrandaki metin kutusunu önce temizle
                        secretText.insert(END, decrypted_text)#çözülen metni göster
                        messagebox.showinfo("Successfully ", "The note was successfully deciphered.")
                        found = True
                        break
                    except Exception as e:
                        messagebox.showerror("Mistake", f"Decryption error: {str(e)}")
                        return
        if not found:
            messagebox.showwarning("Not Found", "Title not found or incorrect key.")
    except:
        messagebox.showerror("Mistake", "An error occurred while reading the file.")




image_label = Label(window, image=img)
image_label.pack()
titleLBL=Label(text="Enter your title")
titleLBL.pack()
ttlEntry=Entry(width=50)
ttlEntry.pack()

secretTextLBL=Label(text="Enter your Secret text   {Enter the text you want to encrypt with the VIGENERE algorithm}")
secretTextLBL.pack()
secretText=Text(height=15)
secretText.pack()

masterKeyLBL=Label(text="Enter master key   {enter STRING text as key}")
masterKeyLBL.pack()
masterKeyEntry=Entry(width=50)
masterKeyEntry.pack()

saveEncryptionButton = Button(text="Save and Encryption", command=saveEncryptionBTTN)
saveEncryptionButton.pack()

decryptButton = Button(text="Decode", command=decryptBTTN)
decryptButton.pack()



window.mainloop()



