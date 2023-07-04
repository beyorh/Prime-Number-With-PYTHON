
sayi=int(input('Bir Sayi Gidiriniz:'))
c=1

if sayi==1:
    print('Sayi Asal Değildir.')


for i in range(2,sayi):
    i+=1
    if(sayi%i==0):
        c=0
   
if(sayi%(i-1)!=0):
        print('Girilen Sayi Asaldır')    
if(c==0):
     print('Sayi Asal Değildir.')
