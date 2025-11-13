def luaspersegi(sisi):
    luas = sisi * sisi
    print("Luas persegi adalah : " + str(luas))
    
    return luas

def volumepersegi(sisi):
    volume = luaspersegi(sisi) * sisi
    print("volume persegi adalah : " + str(volume))
    
    return volume

# Main
print("masukkan sisi")
sisi = int(input())
volumepersegi(sisi)
