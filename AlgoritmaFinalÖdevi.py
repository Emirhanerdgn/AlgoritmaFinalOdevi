#EMİRHAN ERDOĞAN
#1904107028
# ÖDEV1
e = (input("Gün-Ay-Yıl olarak tarih giriniz: "))
m = (e[:3])
i = (e[3:5])
r = (e[5:])
h= {1:"Ocak",2:"Subat",3:"Mart",4:"Nisan",5:"Mayıs",6:"Haziran",7:"Temmuz",8:"Agustos",9:"Eylül",10:"Ekim",11:"Kasım",12:"Aralık"}
if(i=="01"): print(m ,(h[1]),  r)
elif(i=="02"): print(m ,(h[2]),  r)
elif(i=="03"): print(m ,(h[3]),  r)
elif(i=="04"): print(m ,(h[4]),  r)
elif(i=="05"): print(m ,(h[5]),  r)
elif(i=="06"): print(m ,(h[6]),  r)
elif(i=="07"): print(m ,(h[7]),  r)
elif(i=="08"): print(m ,(h[8]),  r)
elif(i=="09"): print(m ,(h[9]),  r)
elif(i=="10"): print(m ,(h[10]), r)
elif(i=="11"): print(m ,(h[11]), r)
elif(i=="12"): print(m ,(h[12]), r)
else: print("Hatalı Değer Girişi\nnot:tarih değerleri tek haneli ise başına 0 koyunuz")

#ÖDEV2
e = int(input("Sayı giriniz:"))
m = e
r = e*2
h = e*3
if(e>16):
    print("HATA: 16dan küçük değer giriniz")
elif(e<0):
    print("HATA: negatif sayı girmeyiniz")
else:
    if(9<= e< 16):
        print("sayı 9 ve 16 arasında")
    if(9>e>=0):
        print("sayı 0 ve 9 arasında")
    for i in range(r):
        r = r - 1
        e = e + m
    print("cevap:",e)

#ÖDEV3
a =[[1,2,-1],
    [2,5,2],
    [-1,-2,2]]
isim = "emirhanerdogann"
alfabe={"e":5,"m":13,"i":9,"r":18,"h":8,"a":1,"n":14,"d":4,"o":15,"g":7}
üclüler = ([alfabe["e"],alfabe["m"],alfabe["i"]],[alfabe["r"],alfabe["h"],alfabe["a"]],[alfabe["n"]
,alfabe["e"],alfabe["r"]],[alfabe["d"],alfabe["o"],alfabe["g"]],[alfabe["a"],alfabe["n"],alfabe["n"]])
x = 0
for i in range(5):
    şifre = [a[0][0] * üclüler[x][0] + a[0][1] * üclüler[x][1] + a[0][2] * üclüler[x][2],
             a[1][0] * üclüler[x][0] + a[1][1] * üclüler[x][1] + a[1][2] * üclüler[x][2],
             a[2][0] * üclüler[x][0] + a[2][1] * üclüler[x][1] + a[2][2] * üclüler[x][2]]
    x=x+1
    print(şifre)
#ÖDEV4
e=[]
for m in range(2,28):
    i = 0
    for r in range(2,m):
            if m%r == 0: i=1
    if i != 1:
        e.append(m)
print("ASAL SAYILAR:\n",e)
