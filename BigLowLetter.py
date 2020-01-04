# -> Megetahui apakah string terdiri dari huruf kecil atau besar
CountBig = []
CountLow = []

t = input("Enter String : ")
for x in t:
    if x == x.upper():
        print('Huruf Besar :',x)
        CountBig.append(x)
    else:
        print('Huruf Kecil :',x)
        CountLow.append(x)
print('Jumlah Huruf Besar :',len(CountBig))
print('Jumlah Huruf Kecil :',len(CountLow))
