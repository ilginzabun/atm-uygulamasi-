print("""************* ATM UYGULAMASINA HOŞ GELDİNİZ!
      İşlemler;
      1. Bakiye Sorgulama
      2. Para Yatırma
      3. Para Çekme

      Programdan çıkmak için 'q' ya basınız!
       *************""")

bakiye = 1000

while True:
    islem = input("İşlemi Seçiniz (1, 2, 3) veya Çıkmak için 'q' : ")

    if islem == "q":
        print("Çıkış yapılıyor. İyi günler!")
        break
    elif islem == "1":
        print(f"Bakiyeniz: {bakiye} ₺")
    elif islem == "2":
        try:
            miktar = int(input("Hesabınıza yatırmak istediğiniz miktarı giriniz: "))
            if miktar > 0:
                bakiye += miktar
                print(f"{miktar} ₺ hesabınıza yatırıldı. Güncel bakiye: {bakiye} ₺")
            else:
                print("Geçersiz miktar! Yatırılacak miktar sıfırdan büyük olmalıdır.")
        except ValueError:
            print("Lütfen geçerli bir miktar giriniz.")
    elif islem == "3":
        try:
            miktar = int(input("Hesabınızdan çekmek istediğiniz miktarı giriniz: "))
            if miktar > 0:
                if bakiye >= miktar:
                    bakiye -= miktar
                    print(f"{miktar} ₺ hesabınızdan çekildi. Güncel bakiye: {bakiye} ₺")
                else:
                    print("Yetersiz bakiye!")
            else:
                print("Geçersiz miktar! Çekilecek miktar sıfırdan büyük olmalıdır.")
        except ValueError:
             # Kullanıcı geçersiz değer girerse  'valueError' ile hata mesajı verir.
            print("Lütfen geçerli bir miktar giriniz.")
    else:
        print("Geçersiz işlem! Lütfen tekrar deneyiniz.")
