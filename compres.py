__author__="S. Kağan Cin"

import os
import tinify

dosya_yolu="./resimler/"
cikti_yolu="./ciktilar/"
tinify.key='Buraya TniyPNG Api Keyinizi Yazınız'
fnames = []
cikti=0

def islemi_yap(resimYol,resimAd):
    global cikti
    cikti+=1
    print(cikti,".) "+ resimYol," Dosyası Sıkıştırılıyor.. ")
    say=0
    ciktininYolu=cikti_yolu+resimAd

    while os.path.exists(ciktininYolu) == True:
        say+=1
        fileName = resimAd.split('.')[0]
        fileType = resimAd.split('.')[1]
        ciktininYolu=cikti_yolu+fileName+str(say)+"."+fileType

    tinify.from_file(resimYol).to_file(ciktininYolu)
    print(resimYol, " Dosyası Sıkıştırıldı ")
def ayristir(path):
    dirList=os.listdir(path)
    dirList.sort()
    for fname in dirList:
        if os.path.isdir(path + fname):
            ayristir(path + fname + "/")
        if os.path.isfile(path + fname):
            fnames.append(path + fname)
    return fnames

dosyalar =ayristir(dosya_yolu)

print("İşlem Başladı")
print("*" * 20)
for item in dosyalar:
    dosyaDizi=item.split('/')
    dosyaAdi=dosyaDizi[len(dosyaDizi)-1]
    islemi_yap(item,dosyaAdi)
print("*"*20)
print("İşlem Tamamlandı")
