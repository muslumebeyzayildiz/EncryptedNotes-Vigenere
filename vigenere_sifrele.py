def vigenere_sifrele(metin, anahtar):
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'

    metin = ''.join(char for char in metin.lower() if char in alfabe)
    anahtar = ''.join(char for char in anahtar.lower() if char in alfabe)

    genisletilmis_anahtar = anahtar * (len(metin) // len(anahtar)) + anahtar[:len(metin) % len(anahtar)]

    sifreli_metin = ''
    for m, a in zip(metin, genisletilmis_anahtar):
        if m in alfabe:
            m_index = alfabe.index(m) #Şifrelenen metindeki karakterin alfabe içindeki dizinini bulur.
            a_index = alfabe.index(a) #Anahtar metindeki karakterin alfabe içindeki dizinini bulur.
            sifreli_index = (m_index + a_index) % len(alfabe)
            sifreli_metin += alfabe[sifreli_index]
        else:
            # Eğer karakter alfabede yoksa olduğu gibi bırak
            sifreli_metin += m

    return sifreli_metin

def vigenere_desifrele(sifreli_metin, anahtar):
    # Türkçe alfabeyi tanımla
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'

    # Şifreli metni ve anahtarı Türkçe alfabeye uyumlu hale getir
    sifreli_metin = sifreli_metin.lower()
    anahtar = ''.join(char for char in anahtar.lower() if char in alfabe)

    # Anahtarı şifreli metnin uzunluğuna genişlet
    genisletilmis_anahtar = anahtar * (len(sifreli_metin) // len(anahtar)) + anahtar[:len(sifreli_metin) % len(anahtar)]

    # Deşifreleme işlemi
    orijinal_metin = ''
    for s, a in zip(sifreli_metin, genisletilmis_anahtar):
        if s in alfabe:
            s_index = alfabe.index(s)
            a_index = alfabe.index(a)
            orijinal_index = (s_index - a_index) % len(alfabe)
            orijinal_metin += alfabe[orijinal_index]
        else:
            # Eğer karakter alfabede yoksa olduğu gibi bırak
            orijinal_metin += s

    return orijinal_metin