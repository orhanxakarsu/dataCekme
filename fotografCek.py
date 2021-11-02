import requests
from bs4 import BeautifulSoup
headers_parameters={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}#Kendi user agentinizi buraya yapıştırabilirsiniz :
def resimCek(aranilacakBaslik,turSayisi,dosyaYolu=""):
    path ="https://www.istockphoto.com/tr/search/2/image?phrase="
    splitVeri = aranilacakBaslik.split(" ")
    print(splitVeri)
    for i in range(0,len(splitVeri)-1):
        path=path+splitVeri[i]+"%20"
    path=path+splitVeri[-1]
    path=path+"&page=1"
    print(path)
    butunIdler = []
    for i in range(1,turSayisi+1):            
        adres=path[:len(path)-1]       
        siteAdresi_=adres+str(i)       
        r = requests.get(siteAdresi_,headers=headers_parameters)
        soup = BeautifulSoup(r.content, "lxml", from_encoding='UTF-8')       
        resimId = soup.find_all("img",{"class":"MosaicAsset-module__thumb___tdc6z"})
        butunIdler.append(resimId)
           
    #Cektigimiz resim adreslerini bilgisayara kaydediyoruz :
    index=0
    for a,resimAdresi in enumerate(butunIdler):   
        for j in range(len(resimAdresi)):
            adres=requests.get(resimAdresi[j]["src"],headers=headers_parameters)
            file = open(f"{dosyaYolu}/{index}.jpg", "wb")
            file.write(adres.content)
            file.close()
            index+=1   
    
def main():
    resimCek("car",10,"images")


if __name__=='__main__':
    main()
