import sqlite3

class VeritabaniYoneticisi:
    def __init__(self,db_adi = "kutuphane.db"):
        self.db_adi = db_adi
        self.baglanti_kur()

    def baglanti_kur(self):
        """veritabanına bağlanır ve tabloyu oluşturur."""
        try:
            self.conn = sqlite3.connect(self.db_adi)
            self.cursor = self.conn.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS kitaplar(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    isim TEXT NOT NULL,
                    yazar TEXT NOT NULL,
                    sayfa_sayisi INTEGER
                )
            ''')
        except sqlite3.Error as e:
            print(f"veritabanı hatası: {e}")

    def kitap_ekle(self,isim,yazar,sayfa_sayisi):
        try:
            sorgu = "INSERT INTO kitaplar (isim,yazar,sayfa_sayisi) VALUES (?,?,?)"
            self.cursor.execute(sorgu,(isim,yazar,sayfa_sayisi))
            self.conn.commit()
            print(f"{isim} başarıyla eklendi.")

        except sqlite3.Error as e:
            print(f"kitap eklenirken bir hata oluştu. {e}")

    def kitapları_listele(self):
        try:
            self.cursor.execute("SELECT * FROM kitaplar")
            kitaplar = self.cursor.fetchall()

            if not kitaplar:
                print("kütüphane şuan boş")
                return
            for kitap in kitaplar:
                print(f"ID: {kitap[0]} | isim: {kitap[1]} | sayfa_sayisi: {kitap[2]}")
        except sqlite3.Error as e:
            print(f"listeleme hatası: {e} ")

    def baglantiyi_kapat(self):
        self.conn.close()

# --- Ana Program Döngüsü ---
def main():
    db = VeritabaniYoneticisi()
    while True:
        print("\n1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Çıkış")
        secim = input("Seçiminiz (1/2/3): ")

        if secim == "1":
            isim = input("Kitap İsmi: ")
            yazar = input("Yazar: ")
            try:
                sayfa = int(input("Sayfa Sayısı: "))
                db.kitap_ekle(isim, yazar, sayfa)
            except ValueError:
                print("Hata: Sayfa sayısı rakam olmalıdır!")

        elif secim == "2":
            db.kitaplari_listele()

        elif secim == "3":
            db.baglantiyi_kapat()
            print("Görüşmek üzere! 👋")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()









if __name__ == '__main__':
    pass