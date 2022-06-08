def chkSum(message): 
    IndexData=0
    checksum=0
    for i in message:   
        IndexData=ord(i)  # Türkce karakterlerin ascii karsılıgı icin böyle bir kosul yazıyoruz.
        if i=="Ç": 
            IndexData=199
        elif i=="Ğ":
            IndexData=208
        elif i == "İ":
            IndexData=221
        elif i=="Ö":
            IndexData=214
        elif i=="Ş":
            IndexData=222
        elif i=="Ü":
            IndexData=220    
        checksum = checksum ^ IndexData #checksum degerini bulmak için xor hesaplanıyor     
        
    return checksum