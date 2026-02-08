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









if __name__ == '__main__':
    pass