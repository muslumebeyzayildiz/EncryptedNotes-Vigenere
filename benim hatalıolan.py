from tkinter import *

from vigenere_sifrele import *

window = Tk()
window.title("Secret Note App with Tkinter Python")
window.minsize(width=600,height=600)
window.config(padx=10,pady=10)
img = PhotoImage(file="pngSecret.png")

def saveEncryptionBTTN():
    title = ttlEntry.get()
    metin = secretText.get("1.0",END)
    anahtar = masterKeyEntry.get()
    sifrelenmis_metin = vigenere_sifrele(metin, anahtar)
    print("Şifrelenmiş Metin:", sifrelenmis_metin)
    orijinal_metin = vigenere_desifrele(sifrelenmis_metin, anahtar)
    print("Orijinal Metin:", orijinal_metin)

    dosyayaKaydet()


def decryptBTTN():
    pass

def dosyayaKaydet():
    file = open("mysecret.txt","w")
    file.write("Project name: \n")
    file.write("as")#projects[0] + "\n")
    file.close()






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



