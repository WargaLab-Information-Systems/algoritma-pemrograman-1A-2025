kalimat = input("masukkan kalimat ")
kata = 1
konsonan = 0
vokal = 0
for i in kalimat:
    if i == " ":
        kata += 1
    else:
        if i.lower() in "aiueo":
            vokal += 1
        else:
            konsonan +=1
            
print("jumlah kata adalah ",kata)
print("jumlah huruf vokal adalah ", vokal)
print("jumlah huruf konsonan adalah ", konsonan)