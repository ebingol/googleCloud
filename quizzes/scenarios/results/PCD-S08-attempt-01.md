# PCD-S08 — İlk cevaplar, 50 soru tamamlandı

**Nihai ilk cevap toplamı: 45/50 (%90).** Q41–Q50: **10/10, 14 dakika**. Bölümler: Q1–Q20 19/20 ve 45 dakika; Q21–Q40 16/20 ve 60 dakika; Q41–Q50 10/10 ve 14 dakika. Toplam bildirilen çözüm süresi **119 dakika (1 saat 59 dakika)**; soru başına ortalama yaklaşık 2:23. Bölümler arasında açıklama/geri bildirim ve ilgili konu çalışması vardı; bu sonuç kesintisiz yardımsız sınav simülasyonu değildir. İlk yanlışlar **Q1/21/35/36/37** korunur; sonradan açıklanan doğru cevaplarla değiştirilmedi. Tüm 50 soru cevaplandı. Son bölüm güven/gerekçe bildirilmedi.

**Önceki ara sonuç Q1–Q40: 35/40 (%87,5).** Q21–Q40: **16/20 (%80), 60 dakika**; bu süre son bölümün süresi olarak alındı. Önceki bölüm 19/20 ve 45 dakika korunur. Toplam bildirilen çözüm süresi **105 dakika (1 saat 45 dakika)**; bölümler arasında geri bildirim bulundu, kesintisiz tam deneme değildir. İlk yanlışlar Q1/21/35/36/37. Q41–Q50 henüz cevaplanmadı. Son bölüm eminlik/gerekçesi bildirilmedi.

27 Eylül 2026. Kullanıcı ilk 20 cevap için **45 dakika** bildirdi. Sonuç **19/20 (%95)**; ortalama **2 dakika 15 saniye/soru**. Yalnız Q1 B→D yanlış. Q7/Q15/Q17 çift seçimleri tam doğru. Q21–Q50 için cevap yok; yanlış veya tamamlandı sayılmaz.

İlk cevaplar sohbette bildirildi; öğrenci soru dosyasındaki boş alanlar değiştirilmedi. Eminlik, gerekçe ve kaynak/yardım koşulları bildirilmedi; yardımsız çözüm veya kalıcı öğrenme sonucu çıkarılmaz. Bu set öğretici ve temel tekrarlar içeriyor; önceki daha zor setlerle puan farkını tek başına yetkinlik artışı veya gerçek sınava hazır olma kanıtı sayma.

| Soru | İlk cevap | Anahtar | Sonuç |
|---|---|---|---|
| 1 | B | D | Yanlış |
| 2 | B | B | Doğru |
| 3 | B | B | Doğru |
| 4 | A | A | Doğru |
| 5 | B | B | Doğru |
| 6 | B | B | Doğru |
| 7 | A + E | A + E | Doğru |
| 8 | C | C | Doğru |
| 9 | A | A | Doğru |
| 10 | C | C | Doğru |
| 11 | C | C | Doğru |
| 12 | A | A | Doğru |
| 13 | C | C | Doğru |
| 14 | D | D | Doğru |
| 15 | A + D | A + D | Doğru |
| 16 | D | D | Doğru |
| 17 | A + C | A + C | Doğru |
| 18 | D | D | Doğru |
| 19 | B | B | Doğru |
| 20 | B | B | Doğru |
| 21 | A | C | Yanlış |
| 22 | B | B | Doğru |
| 23 | C | C | Doğru |
| 24 | B + D | B + D | Doğru |
| 25 | D | D | Doğru |
| 26 | B | B | Doğru |
| 27 | B | B | Doğru |
| 28 | C | C | Doğru |
| 29 | B | B | Doğru |
| 30 | A | A | Doğru |
| 31 | C | C | Doğru |
| 32 | C + E | C + E | Doğru |
| 33 | B | B | Doğru |
| 34 | A | A | Doğru |
| 35 | D | A | Yanlış |
| 36 | A | C | Yanlış |
| 37 | C | D | Yanlış |
| 38 | D | D | Doğru |
| 39 | A | A | Doğru |
| 40 | A | A | Doğru |
| 41 | C | C | Doğru |
| 42 | D | D | Doğru |
| 43 | D | D | Doğru |
| 44 | B + E | B + E | Doğru |
| 45 | A | A | Doğru |
| 46 | D | D | Doğru |
| 47 | A | A | Doğru |
| 48 | C | C | Doğru |
| 49 | D | D | Doğru |
| 50 | A | A | Doğru |

## Hata ve devam noktası

Q1: Seçilen B, her interaktif HTTP isteğinde Cloud Run job execution başlatıyor. D, HTTP uygulamasını Cloud Run service olarak çalıştırıyor. Service/job amaç ayrımı kısa geri bildirimle açıklanır; yanlışın teknik eksik veya okuma hatası olduğu henüz doğrulanmadı. Açıklama sonrası yeni yanıt yok; ilk B korunur.

S08’in bütün soruları cevaplandı. Yanlışların açıklanması bağımsız tekrar başarısı sayılmaz. [Sorular](../PCD-S08.md) · [Türkçe anahtar](../../answers/scenarios/PCD-S08.md).


### S08 Q1 sonrası geri bildirim

Kullanıcı bu testi de çok kolay bulmadığını, aktarılan sınav deneyimine göre gerçek sınavın biraz daha zor olabileceğini ve geçebileceğini hissettiğini söyledi. 19/20 ve 45 dakika olumlu performans göstergesidir; bunu kolaylık veya kesin geçiş garantisi diye yorumlama. Service/job tetikleme farkını sordu: service HTTP endpoint’ine istek alır; job Console/CLI/Cloud Run Admin API, Scheduler veya orchestration üzerinden execution başlatılarak tamamlanana kadar çalışır. Job başlatma API’sine HTTP isteği ile job container’ının HTTP serving yapması ayrıldı. İlk Q1 B yanlışı korunur; açıklama sonrası bağımsız uygulama henüz yok. Q21–Q50 bekliyor.


### Q21–Q40 ilk cevapları

Kullanıcı “s08 60 dk” diyerek 21 A, 22 B, 23 C, 24 B+D, 25 D, 26 B, 27 B, 28 C, 29 B, 30 A, 31 C, 32 C+E, 33 B, 34 A, 35 D, 36 A, 37 C, 38 D, 39 A, 40 A bildirdi. 16/20; yanlışlar Q21 A→C (memory requests/limits), Q35 D→A (provenance), Q36 A→C (Bigtable row key), Q37 C→D (NetworkPolicy/IAM). Q24 ve Q32 çift seçimler tam doğru. Bu dört yanlışın ayrıntılı incelemesi yapılmadı; hata nedenleri harften çıkarılmadı. Q1 ilk B yanlışı açıklama sonrası değiştirilmez.


### S08 Q21 sadeleştirme

Kullanıcı ikinci bölümde zorlandığını belirtti ve Q21’i sadeleştirmeyi istedi. Güncel soru tekrar okundu: seçilen A, düşük memory limit’i koruyup HTTP readiness probe ekliyor; CPU artırma B şıkkıdır. Senaryo, iş başına gerekli RAM’in container limitini aşması ve node’da yeterli kapasite olması üzerinden sadeleştirildi. Request/limit anlamı ve dört şıkkın Türkçesi verildi; yeni seçim veya kavrayış teyidi yok. İlk Q21 A yanlışı ve toplam 35/40 korunur. Q35/36/37 incelemesi bekliyor.


### S08 Q21 anlam teyidi ve Q35 incelemesi

Kullanıcı Q21’de “identified a reasonable per-task memory requirement within its budget” ifadesinin yanılttığını söyledi. Identified (ihtiyacı belirlemek) ile configured (ayarı uygulamak) ve bütçe uygunluğu ile mevcut memory limit yeterliliği ayrıldı. Kullanıcı “anladım ... yine İngilizce yanlış anlama” dedi: kullanıcı beyanına göre dil kaynaklı hata, anlık kavrayış beyanı var; bağımsız yeni uygulama yok. İlk A yanlışı korunur.

Sonraki isteğiyle Q35’e geçildi: ilk D, doğru A. Image üzerindeki insan tarafından yazılan commit label ile digest’e bağlı doğrulanabilir build provenance kaydı ayrımı açıklanıyor. Test/scan/build-origin kanıtlarının amaçları ayrıldı. Q35 hata nedeni ve açıklama sonrası kavrayış henüz doğrulanmadı. Q36 ve Q37 sonraki yanlışlar; Q41–Q50 cevaplanmadı. Toplam 35/40 korunur.


### S08 Q35 kavrayış beyanı ve Docker dependency cache tekrarı

Kullanıcı provenance’ın ne olduğunu ve nasıl üretildiğini sordu; Cloud Build üretim metadata’sı, images ile Artifact Registry’ye push ve requestedVerifyOption: VERIFIED örneği açıklandı. Ardından “şimdi tamam oldu” dedi: anlık kavrayış beyanı var, bağımsız yeni uygulama yok. İlk Q35 D yanlışı korunur. Docker dependency cache sorusuna geçildi: package.json/package-lock.json önce COPY, sonra RUN npm ci, değişken source sonra COPY; değişmeyen bağımlılık layer’ının tekrar kullanılması ile npm paket indirme cache’i ayrıldı. Q36/Q37 incelemesi ve Q41–Q50 cevapları bekliyor.


### S08 Q36 incelemesi

Kullanıcı sonraki yanlışı istedi. Q36 ilk A, doğru C: timestamp-first row key ile device-first/time-second tasarım sade örneklerle karşılaştırıldı. İstenen sorgu bir bilinen cihazın zaman aralığı; cihaz kimlikleri iyi dağılmış ve trafik benzer. Timestamp-first yeni yazmaları dar aralığa toplarken device-first bu varsayımlarda dağıtım ve cihaz bazlı range read’i birlikte destekler. Gerekçe/kavrayış kullanıcıdan henüz gelmedi; ilk cevap ve 35/40 değişmez. Sıradaki yanlış Q37; Q41–Q50 bekliyor.


### S08 Q36 — dağıtımın mekanizması

Kullanıcı “A proposed row key...” ifadesindeki hazır tanımı şart gibi okuduğunu belirtti; proposed=önerilen tasarım, zorunlu doğru yapı değil ayrımı açıklandı. Ardından Bigtable’ın distribution verimliliğini sordu. Row key sırasıyla tutulan kayıtlar, contiguous tablet aralıkları, tabletlerin node’lara otomatik atanması; timestamp-first aktif uç hotspot’u ile well-distributed device-first/time-second modelinin yazma dağılımı ve range-read locality dengesi anlatıldı. Node başına tek cihaz veya hash ile doğrudan node seçimi olmadığı, tek sıcak cihaz halinde tasarımın ayrıca değerlendirilmesi gerektiği belirtildi. Q36 bağımsız yeni yanıt yok; ilk A ve 35/40 korunur. Q37 sıradaki yanlış.


### Firestore temel kurallarına ara tekrar

Kullanıcı scan/subdocument konularını hatırlatmamızı istedi. Klasik Firestore Standard/Core sorgu kapsamıyla index gereksinimi ile bütün collection’ı okumanın maliyetinin ayrılması; map field ile ayrı subcollection document farkı; parent read/delete işlemlerinin subcollection’ı otomatik getirmemesi/silmemesi; document boyutu ve büyüyen listeleri alt koleksiyona ayırma; Security Rules’ın query filtresi olmaması anlatılıyor. Enterprise/Pipeline davranışına koşulsuz genelleme yapılmaz. Yeni cevap veya bağımsız kavrayış teyidi yok; S08 35/40, Q37 incelemesi ve Q41–Q50 cevapları bekliyor.


### Storage ürünleri ayrımı

Kullanıcı Filestore ile Cloud Storage farkını sordu. Filestore yönetilen NFS/shared filesystem; Cloud Storage bucket/object modeli ve API erişimi olarak karşılaştırıldı. Önceki Firestore’un document database olduğu ayrıca belirtildi. Mount edebilmenin tek başına filesystem semantiği anlamına gelmediği; Cloud Storage FUSE’un NFS/POSIX eşdeğeri olmadığı kısa sınırla anlatılıyor. Kullanıcıdan bağımsız seçim yok; S08 35/40 değişmez. Q37 ve Q41–Q50 bekliyor.


### Firestore composite index ve ilişkili veri okuma

Kullanıcı composite index/JOIN ve veri çekme mantığını sordu. Klasik Firestore Standard/Core sorguları kapsamında users ve orders örneğiyle where + orderBy, composite index’in birden çok alan için tek collection sorgusunu desteklemesi; SQL JOIN yerine ayrı okumalarla uygulamada birleştirme veya denormalization anlatılıyor. Otomatik index ile gerektiğinde composite index, eksik index hatası ve collection group’un JOIN olmadığı ayrılıyor. Enterprise/Pipeline özellikleriyle koşulsuz ürün genellemesi yapılmaz. Yeni yanıt/kavrayış teyidi yok; S08 ilk 35/40 ve kalan Q37/Q41–Q50 durumu korunur.


### Firestore index ve sorgu kavramlarını ayırma

Kullanıcı composite index’in tanımını ve sorgu çeşitlerini sordu. Birden fazla field’ı belirli sırayla düzenleyen index, status/createdAt örneğiyle açıklanıyor. Index türü ile query işlemi ayrıldı; document ID ile okuma, collection query’de where/orderBy/limit/cursor, collection group kapsamı ve get/realtime dinleme farkı temel öğretim olarak veriliyor. Bunlar sabit toplam ürün özelliği sayısı değildir. Kavrayış teyidi veya yeni soru yanıtı yok; S08 ilk 35/40 korunur.


### Firestore index oluşturma ve eksik index

Kullanıcı index’in nasıl tanımlandığını ve tanımlanmazsa ne olduğunu sordu. Standard/Core kapsamıyla varsayılan otomatik single-field index’ler ve sorgunun gerektirdiği composite index ayrıldı; hata mesajındaki console bağlantısı veya Console Indexes/Create index ile collection, field sırası/direction ve scope seçimi; build tamamlanınca query’yi yeniden çalıştırma açıklandı. Eksik gerekli index’te otomatik full scan yerine query hatası; her sorguya elle index gerekmediği vurgulandı. Kavrayış henüz doğrulanmadı, ilk puanlar değişmedi.


### S08 Q37 incelemesi

Kullanıcı sonraki yanlışı istedi. Q37 ilk C, doğru D. Payments Pod’larına yalnız frontend’den belirli portta bağlantı şartı; ingress NetworkPolicy ile hedef/source selector ve port sınırı, Google Cloud IAM ile resource yetkisinden ayrıldı. Uygulama authentication’ı ağ izninden bağımsız korunur. C yalnız IAM rolünü daraltıp Pod network trafiğini değiştirmediği için elenir. Kullanıcının hata gerekçesi veya yeni kavrayış teyidi yok; ilk 35/40 korunur. Q21/35/36/37 açıklamaları verildi, hepsinin bağımsız öğrenildiği söylenmez. Q41–Q50 bekliyor.


### Son bölüm Q41–Q50

Kullanıcı 14 dakika ve C/D/D/B+E/A/D/A/C/D/A verdi; tümü doğru. İlk toplam 45/50; süre 45+60+14=119 dakika. Yeni yanlış yok. Önceki beş yanlış açıklandı; Q21 için dil kaynaklı hata ve anlık anlama beyanı, Q35 için anlık anlama beyanı var. Diğer açıklamaları kalıcı kavrayış diye işaretleme.
