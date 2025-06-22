# 🐢 Catch The Turtle!

Bu oyun, Python'un Turtle modülü kullanılarak geliştirdiğim **ilk oyunumdur**.

🎯 **Oyun Amacı:**
Amaç, ekranda rastgele beliren kaplumbağayı tıklayarak **yakalamak**. Her başarılı tıklamada **5 puan kazanırsınız** ve arka planda bir ses efekti çalar.

📊 **Yüksek Skor Sistemi:**
- Yaptığınız en yüksek skor, **SQLite veritabanı** (`high_score.db`) içerisine kaydedilir.
- Eğer mevcut skorunuz en yüksek skoru geçerse, bu veritabanı güncellenir ve ekranda gösterilir.

🔁 **Yeniden Oynama:**
- Oyuna başlamak için `Enter` tuşuna basın.
- Oyun bittiğinde tekrar başlatmak için `R` tuşuna basabilirsiniz.
- Her yeniden başlatmada, **skor** ve **zamanlayıcı sıfırlanır**.

🎮 **Nasıl Oynanır:**
- Kaplumbağa ekranda rastgele yerlerde belirir.
- Belirli bir süreniz vardır; bu süre içinde kaplumbağaya olabildiğince fazla tıklayarak skorunuzu artırmaya çalışın.
- Amaç, kendi **yüksek skorunuzu geçmek**!

---

## 💾 Gerekli Kurulumlar

- Python 3.x
- Turtle (Python ile birlikte gelir)
- `winsound` (sadece Windows'ta çalışır, ses efekti için)
- `sqlite3` (Python ile birlikte gelir)

---

## 📁 Kullanılan Dosyalar

Projenizin çalışabilmesi için aşağıdaki dosyaların proje klasörünüzde bulunması gerekir:

- `LittleTurtle.gif` – Kaplumbağa görseli
- `BackGroundTurtle.gif` – Arka plan görseli
- `tıklama.wav` – Ses efekti dosyası

---

## 📸 Ekran Görüntüsü

![CatchTheTurtle](https://github.com/user-attachments/assets/de264fd9-cc12-4b6b-8d09-3712075e372e)

---
Python Turtle ile ❤️ sevgiyle kodlandı.
