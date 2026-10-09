# PCD-S14 — İlk gönderilen 20 cevap

9 Ekim 2026. Kullanıcı S14 için **54 dakika** ve aşağıdaki ilk cevapları bildirdi.

Ham gönderim:

```text
1-b,2-c,3-a,4-be,5-d,
6-c,7-a,8-b,9-a,10-c,
11-d,12-b,13-c,14-d,15-a,
16-a,17-b,18-d,19-ab,20-a
```

Mevcut anahtara göre **17/20 (%85)**. Yanlışlar **Q07, Q08, Q19**. Q04 B+E doğru; Q19 A+B, anahtar A+C. Çift seçimde tam küme 1 puan; kısmi puan yok.

50 dakikalık kişisel hedefin 4 dakika üzerinde; ortalama 2 dakika 42 saniye/soru. 50. dakikadaki cevaplar, ek 4 dakikada yapılan değişiklikler, mola/yardım/kaynak kullanımı, güven/gerekçe bildirilmedi. İlk gönderilen sonuç olarak kaydedilir; kesintisiz yardımsız koşullar veya hata nedeni varsayılmaz.

| Soru | İlk cevap | Anahtar | Sonuç |
|---|---|---|---|
| 1 | B | B | Doğru |
| 2 | C | C | Doğru |
| 3 | A | A | Doğru |
| 4 | B+E | B+E | Doğru |
| 5 | D | D | Doğru |
| 6 | C | C | Doğru |
| 7 | A | B | Yanlış |
| 8 | B | D | Yanlış |
| 9 | A | A | Doğru |
| 10 | C | C | Doğru |
| 11 | D | D | Doğru |
| 12 | B | B | Doğru |
| 13 | C | C | Doğru |
| 14 | D | D | Doğru |
| 15 | A | A | Doğru |
| 16 | A | A | Doğru |
| 17 | B | B | Doğru |
| 18 | D | D | Doğru |
| 19 | A+B | A+C | Yanlış |
| 20 | A | A | Doğru |

## Değerlendirme sonrası kısa açıklamalar

- Q07 A→B: task-caller Invoker zaten mevcut; handler başlamadan yanlış token tipi reddediliyor. Hedef Cloud Run için task-caller kimliğini temsil eden, hedef service URL audience değerli OIDC ID token gerekir. image-runtime hesabına Invoker eklemek incoming authentication hatasını düzeltmez.
- Q08 B→D: Eventarc olayı bucket/object bilgilerini taşır; PDF bytes değildir. Retry aynı metadata’yı binary PDF’ye dönüştürmez. Yetkili worker Storage’dan belgeyi okur.
- Q19 A+B→A+C: API administrator tarafından etkinleştirilir (A); model çağrısını yapan ai-runtime için prediction yetkisi ayrı gerekir (C). API enable yetkisi prediction yetkisi değildir.

Bu açıklamalar rehberli öğretimdir; ilk cevaplar/puan değişmez, kavrayış veya kalıcılık teyidi yok. Sonraki adım kullanıcı isterse bu üç mekanizmayı mevcut sorular üzerinden çalışmak. Yeni set veya otomasyon oluşturulmadı.


9 Ekim — S14 anahtarlı tekrar / konsantrasyon: Kullanıcı tüm soruları cevaplarıyla yeniden istedi ve yoğun sorularda zihninin/konsantrasyonunun bir noktadan sonra yetişmediğini belirtti. Bu kullanıcı beyanıdır; bütün yanlışların nedeni veya teknik bilginin tamlığı diye yorumlanmaz. [Açıklamalı tekrar](../answers/scenarios/PCD-S14-REVIEW.md) oluşturuldu: 20 özgün İngilizce soru/tüm seçenekler ve soru altında doğru cevap, kısa gerekçe/eleme koşulu/kaynak; 4×5 bölüm. İlk 17/20, 54 dakika ve ilk seçimler korunur. 20 soru/20 cevap/özgün metin eşleşmesi kontrol edildi. Anahtarlı turda süre hedefi yok, kısa molalar mümkün; soru kısaltma talebi yok. Rehberli çalışma, kavrayış veya kalıcılık teyidi yok. Sonraki adım kullanıcı seçtiği bölüm/yanlışın mekanizmasını inceleyebilir; yeni set veya otomasyon yok.
