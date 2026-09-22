# Günlük quiz ve senaryo stratejisi

Kararlaştırma: 20 Eylül 2026. Hedef: Professional Cloud Developer. Kullanıcı yaklaşık üç hafta kaldığını söyledi; kesin sınav tarihi bilinmiyor. Eski 20–30 dakikalık günlük plan yerine aşağıdaki düzen geçerli.

## Günlük düzen

**22 Eylül kullanıcı güncellemesi:** Cloud Run, Cloud Run functions ve GKE konu soruları kullanıcı beyanına göre tamamlandı. Güncel 15 soruluk senaryo bu üç alandan 5'er soru içerecek. Bu istek, tek günlük klasörden en az altı yeni soru kuralından önce gelir. GKE tamamlanmasını tüm containeried klasörünün tamamlanması diye yorumlama; yeni puan bildirilmedi.

Kullanıcının hedefi **her gün bir ders quiz klasörü + bir senaryo seti**. Ders quizleri hem teknik hatırlama hem İngilizce soru diline alışma için önemli; atlanmayacak.

1. Günün klasöründeki henüz çözülmemiş quizleri 5 soruluk setler halinde çöz. Cevap ve eminlik kaydet. 4–5 setten sonra kısa mola ver.
2. Takılınan soru için önce İngilizceyi açıkla; istenmediği sürece çeviriyle birlikte cevabı da verme. Teknik eksik varsa ilgili PDF'nin dosya sayfasını göster.
3. Günün yeni senaryo setini çöz: normalde **15 soru**, 30 dakika çalışma hedefi; bu resmî sınav süresi değildir. Kullanıcı dil desteği isterse süreyi durdur ve rehberli çalışma olarak kaydet. Yoğun günlerde 5 soruluk kısa set yapılabilir; sessizce günlük hedefi değiştirme.
4. Yanlışları, kararsız doğruları ve gerekçesiz doğruları ayır. En fazla üç kısa açıklama önceliği seç; hepsini tek seferde uzun ders olarak sunma.
5. Sonucu, dil notlarını, kalan quizleri ve sonraki adımı `HANDOFF.md` içine işle.

Klasörler eşit büyüklükte değil:

| Önerilen ilk tur sırası | Klasör | Set / soru |
|---|---|---|
| 1, kullanıcı beyanıyla tamamlandı | cloudRun | 26 / 130 |
| 2 | containeried | 24 / 120 |
| 3, kullanıcı beyanıyla tamamlandı | cloudRunFunctions | 25 / 125 |
| 4 | orchestration | 8 / 40 |
| 5 | foundations | 32 / 160 |
| 6 | fundamentals | 37 / 185 |

“Bir klasör” hedefi 40–185 soru demektir; bunun 60–90 dakikaya sığacağını varsayma. Anlamadan geçmek yerine kalan setleri ertesi güne devret. Tamamlanmış klasör yoksa varmış gibi işaretleme. Tüm soruları bitirmek, senaryoya başlamanın ön koşulu değil.

## Üç haftanın dağılımı

- İlk hafta: altı klasörde ilk tur hedefi ve günlük senaryo. Yedinci gün yetişmeyenler + yanlış analizi. Çok zor gelen büyük klasör iki güne yayılabilir.
- İkinci hafta: klasörlerin yanlış/kararsız sorularına dönüş; her gün yeni karma senaryo. Aynı doğru soruları sırayla yeniden çözmek yerine eksik kararlara odaklan.
- Üçüncü hafta: güncel resmî sınav kapsamına göre karma çalışma ve iki tam deneme. Deneme gününde ayrıca 15 soruluk set yükleme; günlük senaryo çalışması denemedir. Tam deneme süresi/adedi hazırlanırken resmî biçimi yeniden doğrula. Son iki gün kısa tekrar, yeni ağır konu yok.

Apigee, GKE'nin ileri konuları, gözlemlenebilirlik ve AI gibi alanların yalnız bu altı klasörle eksiksiz kapsandığını varsayma. Resmî sınav rehberiyle boşluk kontrolü yap; eksik kaynağı resmî dokümanla tamamla ve bunu açıkça etiketle.

## Bugünkü set nasıl hazırlandı?

- PCD-S01: IAM/ADC, Cloud Run, CI/CD, veri ve event/koordinasyon alanlarından üçer soru; 15 soruluk tanılama. Sonuç 11/15, 20 dakika.
- PCD-R01: S01'de zorlanılan secret rolleri, build dosya paylaşımı, servis çağrı izni/token ve concurrency için hedefli 5 soru. Sonuç 4/5. Bu yüzden aynı konular bilerek tekrarlandı; her gün kullanılacak dağılım bu değil.
- R01'de secret değerini okumak yerine metadata inceleme, dosyanın yazıldığı yol yerine okunduğu yol ve mevcut izin varken yanlış audience gibi değişiklikler yapıldı. Concurrency ve invoker soruları yakın tekrardı; bunları yeni konu kapsamı olarak sayma.
- “No custom audiences” ayrıntısı ders PDF'sinden değil resmî web dokümanından eklenmişti. Bundan sonra PDF dışı ayrıntılar cevap anahtarında “Ek resmî kaynak” olarak açıkça belirtilecek.

## Yeni 15 soruluk setin dağılımı

- **9 soru:** daha önce senaryoda ölçülmemiş kararlar; en az 6'sı o günün klasöründen.
- **4 soru:** önceki konuları başka servislerle birleştiren yeni problemler. Aynı cevaba aynı ipucuyla götüren isim değişiklikleri yeterli değil.
- **2 soru:** zamanı gelmiş zayıf konuların farklı uygulaması. Tekrar zamanı gelmediyse bu yerler yeni konulara verilir.

Sorular günün klasörünün bölüm sırasıyla gelmesin; konuları karıştır. İlk hafta çoğu soru iki belirleyici kısıt içersin; giderek çok adımlı kararlar ekle. Cevap için gerekli olmayan uzun cümlelerle yapay zorluk yaratma.

## Tekrarı nasıl önleyeceğiz?

Her soru için `QUESTION-LOG.md` içinde konu, ölçülen karar, belirleyici koşul, önceki benzer soru ve yeni/karma/tekrar türünü kaydet. Kayıt özeti tek başına yetmez; yakın görünen önceki soruların tam metnini de oku.

- Servis/şirket/kişi adını veya seçenek sırasını değiştirmek yeni soru değildir.
- Bilerek tekrar edilecekse “gecikmeli tekrar” olarak kaydet; yeni kapsam sayma.
- Aynı teknik karar ardışık günlük setlerde sorulmasın; kullanıcının açıkça istediği anlık pekiştirme istisna.
- İlk açıklamadan **3 gün sonra**, sonra **7 gün sonra** farklı problemle kontrol et; gerekirse 14. gün. Kaçırılan tarih sonraki oturuma taşınır. Her gün bütün yanlışları yeniden sorma.
- Açıklama hemen sonrasında doğru cevap, gecikmeli kalıcılık kanıtı değildir. Yeni bir bağlamda gerekçeli doğru cevap ve sonraki oturum kontrolü ayrı kaydedilir.
- Cevap harflerini makul dağıt, ancak denge için teknik doğruluğu bozma. Belirsiz iki doğru seçenek bırakma; çoklu seçim sayısını açıkça yaz.

## Kaynak ve değerlendirme standardı

- Sorular İngilizce, cevap açıklamaları Türkçe ve ayrı dosyada. Yeni set ID'si PCD-S02, ardından S03…; kısa hedefli ekler R02… olarak ayrı sayılır.
- Her cevaba teknik gerekçe, en yakın alternatifin neden elendiği ve belirleyici İngilizce ifade ekle.
- Her soru: PDF yolu + doğrulanmış 1 tabanlı sayfa veya açıkça etiketlenmiş resmî web kaynağı; değişebilen davranışı güncel dokümandan doğrula. PDF'de olmayan bilgiyi oradaymış gibi sunma.
- Sınav rehberi alanını cevap anahtarına kaydet. Resmî sınav sorusu veya sınav zorluğuyla kalibre edilmiş set iddiasında bulunma.
- Hata sınıfları: teknik bilgi / İngilizce anlam / yönerge / gerekçe eksikliği. Çeviri desteği verildiyse belirt. Çoklu seçimde tam doğru küme 1 puan.
- Dil notlarını kaydet: “define”, “consists of”, “specific”, “already”, “neither…nor”, “one after another”, “overlapping”, “best effort”, “instantaneous”, “receiving”, “audience”. Aynı anlamın farklı ifadelerini zamanla kullan; teknik anlamı değiştirme.
- Yalnız dil sorulduğunda önce çeviri ve cümle çözümlemesi; kullanıcı cevap vermeden doğru seçeneği açıklama. Birlikte çözümde tek soru sor, yanıtını bekle.
- VS Code'da beyaz tema ve düzenlenebilir Markdown tercih ediliyor. Kullanıcının cevaplarını koru; dosyayı otomatik temizleme veya üzerine yeni soru seti yazma.

## PCD-S02 — güncel kapsam, 22 Eylül

[PCD-S02](PCD-S02.md) kullanıcı beyanıyla 14/15, 20 dakikada tamamlandı; Q12 yanlış. Dosyadaki cevap alanları boş, şık bazında kontrol yapılmadı. Kullanıcının kapsam düzeltmesiyle 5 Cloud Run + 5 Cloud Run functions + 5 GKE olarak yeniden düzenlendi. İlk Cloud Run ağırlıklı taslağın boş cevap alanları kontrol edildi; kullanıcı yanıtı değiştirilmedi.

- Cloud Run: service/job, startup probe, Cloud SQL havuzu, ingress/IAM, secret sürümü/rollback.
- Cloud Run functions: HTTP webhook, geçici dosya temizliği, kalıcı/geçici hata ayrımı, entry point, Firestore kendi kendini tetikleme döngüsü.
- GKE: Service selector, Deployment template rollout, PVC ile kalıcılık, readiness/liveness, CPU request ve HPA.

Q6/Q8/Q13/Q14 karma; diğer 11 soru önceki çözülmüş senaryolarda ölçülmeyen kararlardır. Yeni kullanıcı kapsamı nedeniyle bu sette zorunlu gecikmeli tekrar yok; eski Eventarc tekrar taslağı kaldırıldı. Audience/concurrency/workspace tekrar kuyruğu korunuyor, çözülmüş sayılmıyor. HPA ve Kubernetes probe davranışları ek resmî kaynak olarak ayrıştırıldı.

Sonraki yeni set ID'si PCD-S03. Yeni seti S02 sonuçlarına ve kullanıcının o günkü tercihine göre hazırla.

## 22 Eylül — kullanıcının düzelttiği uzunluk ve zorluk tercihi

**Cümleleri kısaltma.** Kullanıcı uzun İngilizce senaryolara alışmak istiyor; yorgunluk/odaklanma geri bildirimi sadeleştirme talebi değildi. Önceki 2–3 kısa cümle önerisi iptal edildi.

Kullanıcı S02'yi çok kolay buldu ve gerçek sınavın daha zor olacağını düşünüyor. Hazırlayan değerlendirmesi: bazı yanlış seçenekler açıkça ilgisizdi ve doğru cevap tek ipucuyla bulunabiliyordu. 14/15 sonucu korunur; gerçek sınav zorluğuyla kalibre edilmiş başarı veya hazır olma kanıtı sayılmaz.

Sonraki setlerde uzunluk ve İngilizce okuma yükünü koru; makul ve birbirine yakın alternatifler, birden çok belirleyici koşul, servisler arası etkileşim ve maliyet/güvenilirlik/operasyon yükü ödünleşimleri kullan. Zorluğu gereksiz kelime veya belirsizlikle artırma; koşullarla tek en iyi cevap belirlenebilsin. Gerçek sınavla eşdeğer zorluk iddiası kullanma.

Q12: Kullanıcı readiness/liveness/startup probe konularına tam hakim olmadığını açıkça belirtti. Hata sınıfı kullanıcı beyanıyla teknik kavram eksikliği; yorgunluğa atfetme. Seçilen yanlış şık hâlâ bilinmiyor. Açıklama sonrası kavrayış veya kalıcılık henüz doğrulanmadı.
