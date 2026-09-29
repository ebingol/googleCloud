# PCD-S09 — İlk cevaplar, 50 soru tamamlandı

**S09 tamamlandı — ilk gönderilen cevaplar mevcut anahtara göre 37/50 (%74).** Q21–Q50 **23/30 (%76,7), 74 dakika**; Q1–Q20 **14/20, 54 dakika**. Toplam bildirilen çözüm süresi **128 dakika (2 saat 8 dakika)**; bölümler arasında açıklama ve öğretim vardı, kesintisiz yardımsız sınav değildir. 74 dakika son 30 sorunun süresi olarak alındı. Son bölüm ortalama 2:28/soru; tüm set yaklaşık 2:34/soru. Önerilen 120 dakika hedefinden toplam 8 dakika fazla; 120. dakikada hangi soruda olduğu bilinmiyor.

**Ayrı notlar:** Q9 kullanıcı beyanıyla aktarım hatası (A düşünülmüş, B gönderilmiş); bu beyanla toplam **38/50 (%76)**, ilk gönderilen B değiştirilmedi. Q19 soru belirsizliği korunur; anahtar toplamındaki yanlış işareti kesin teknik eksiklik değildir. Q19 puan dışı değerlendirilirse ilk gönderilen cevaplar 37/49 (%75,5), ayrıca Q9 aktarım beyanı uygulanırsa 38/49 (%77,6); bunlar tarihsel ilk anahtar toplamından ayrı değerlendirmelerdir.

Son bölüm yanlışları **Q26/29/35/38/45/49/50**; kullanıcının isteğiyle aşağıda topluca açıklandı, bağımsız kavrayış kontrolü yok. Q36 A+B ve Q42 D+E doğru; Q26 D+E ve Q50 A+B tam doğru küme değil. Son bölüm güven/gerekçe bildirilmedi. Yeni cevap kalmadı; tüm yanlışlar açıklandı; sonraki çalışma kullanıcının tercihine göre. Sonraki yeni set S10.

## Önceki ara sonuç — Q1–Q20 (tarihsel kayıt)

28 Eylül 2026. **14/20 (%70), 54 dakika.** Q1–Q10: 6/10; Q11–Q20: 8/10. Ortalama **2 dakika 42 saniye/soru**. Süre kullanıcının bu 20 soru için bildirimidir; alt bölümlerin süreleri ayrı bilinmiyor.

İlk cevaplar sohbette bildirildi ve aşağıda aynen korundu. Q6 C+D ve Q18 B+D tam doğru; çoklu seçimde yalnız tam doğru küme 1 puan. Eminlik, gerekçe, mola ve yardım koşulları bildirilmedi. Hata nedenleri yalnız seçilen harften teknik bilgi/İngilizce/yönerge diye sınıflandırılmadı. Soru dosyasındaki cevap alanları değiştirilmedi.

**Devam Q21. Q21–Q50 henüz cevaplanmadı; yanlış veya tamamlandı sayılmaz.** İlk 20 sonrası puan ve yanlış şık karşılaştırması verildi; sonraki bölümlerle birlikte sonuç kesintisiz geri bildirimsiz tam deneme diye sunulmaz. Q2 aşağıda açıklanarak incelendi; Q3/Q9 da aşağıdaki devam notunda incelendi; bağımsız kavrayış kontrolü yapılmadı.

| Soru | İlk cevap | Anahtar | Sonuç |
|---|---|---|---|
| 1 | D | D | Doğru |
| 2 | C | B | Yanlış |
| 3 | C | B | Yanlış |
| 4 | D | D | Doğru |
| 5 | A | A | Doğru |
| 6 | C + D | C + D | Doğru |
| 7 | D | D | Doğru |
| 8 | A | A | Doğru |
| 9 | B | A | Yanlış |
| 10 | D | B | Yanlış |
| 11 | C | C | Doğru |
| 12 | A | C | Yanlış |
| 13 | A | A | Doğru |
| 14 | B | B | Doğru |
| 15 | C | C | Doğru |
| 16 | D | D | Doğru |
| 17 | A | A | Doğru |
| 18 | B + D | B + D | Doğru |
| 19 | B | C | Yanlış |
| 20 | D | D | Doğru |

## İlk bölüm yanlışları — açıklamaları aşağıda

- Q2 C→B: Lokal ADC / service-account impersonation.
- Q3 C→B: Cloud Tasks worker başarı yanıtının tamamlanmaya bağlanması.
- Q9 B→A: Cross-project secret için runtime principal ve kaynak kapsamı.
- Q10 D→B: Firestore Rules testinde server SDK ile kullanıcı bağlamının ayrımı.
- Q12 A→C: Aynı image digest ile configuration-only revision.
- Q19 B→C: Dead-letter forwarding izinlerinin tamamlanması.

[Öğrenci soruları](../PCD-S09.md). İlk seçimler açıklama sonrası değiştirilmez; rehberli düzeltme ayrı kaydedilir.

## Q2 — Kullanıcının gerekçesi ve rehberli açıklama

Kullanıcı Token Creator rolünü çok büyük/geniş bir yetki gibi düşündüğünü söyledi. Yeniden okuyunca C'nin ilgili kimlik sorununu değiştirmediğini fark etti; staging/production ayrımını ve soru metninin tam Türkçe açıklamasını istedi. Bu, rol kapsamı ve senaryo amacını anlamlandırma ihtiyacına işaret eder; yalnız İngilizce veya yalnız teknik hata diye kesin sınıflandırılmaz.

Staging'in canlı öncesi test, production'ın gerçek kullanıcı ortamı olduğu; sorunun staging uygulamasındaki yetki hatasını laptop'ta aynı service-account kimliğiyle yeniden üretmeyi istediği açıklandı. Geliştiricinin geniş yetkili kişisel ADC'si hatayı gizler. C varsayılan gcloud projesini değiştirir fakat kişisel ADC kimliğini değiştirmez. B'de geliştiriciye hedef staging service account üzerinde Token Creator verilir; uygulamanın veri erişim rolleri artırılmaz. Desteklenen impersonated local ADC kısa ömürlü kimlik bilgileriyle aynı service account olarak test sağlar; indirilen kalıcı service-account key gerekmez. ADC'nin credential bulma yöntemi olduğu anlatıldı. A/B/C/D Türkçe anlam ve eleme koşulları verildi.

Örnek veri erişim senaryosu öğretim içindir; soru belirli bir veri ürününü veya eksik veri rolünü belirtmez. Token Creator önemsiz bir yetki diye sunulmaz; hedef service account kapsamına daraltılır. Kaynak: https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment?hl=en . İlk Q2 C ve 14/20 puanı korunur; açıklama sonrası yeni bağımsız yanıt veya kalıcılık ölçümü yok.

## Q2 devamı, Q3 ve Q9 rehberli inceleme

Q2: Token Creator ile veri erişiminin ayrı izinler olduğu; uygulamanın kişisel kimlik yerine SA adına kısa ömürlü token kullanması açıklandı. Kullanıcı sonraki soruya geçti; kavrayış teyidi yok.

Q3: İlk C, doğru B. Erken HTTP 200 task'ı başarılı onaylar; thread logu işi kalıcı tamamlamaz. Rapor kalıcı kaydedildikten sonra başarı dönülmesi açıklandı. Kullanıcı latency azaltma ifadesini korunan gereksinim olarak okuduğunu belirtti. Bu ifadenin mevcut tasarımın gerekçesi olduğu, güncel hedefin failure tracking/redelivery olduğu; worker→Cloud Tasks yanıtının public frontend yanıtından ayrı olduğu anlatıldı. İş deadline'a sığar. Bağımsız kontrol yok.

Q9: İlk B, doğru A. Runtime service account, Google'ın Cloud Run service agent'ı ve deployment operator ayrımı Türkçe açıklandı. Hata runtime SA'nın secret payload erişimini belirtir; güvenlik projesindeki belirli secret üzerinde o kimliğe Secret Accessor gerekir. B doğru rolü yanlış kimliğe verir; C metadata erişimi, D operatör ve yanlış kaynak kapsamıdır. Kaynak: https://docs.cloud.google.com/run/docs/configuring/services/secrets . İlk cevaplar ve 14/20 korunur; kavrayış kontrolü yok. Sonraki incelenmemiş yanlış Q10; ardından Q12/Q19. Yeni soru çözümü Q21'den devam eder.

## Q9 aktarım hatası beyanı ve Q10 incelemesi

Kullanıcı Q9 için aslında A düşündüğünü fakat mesajda B yazdığını, doğru cevap açıklandıktan sonra bildirdi. İlk gönderilen B ve ilk 14/20 korunur. Kullanıcı beyanına göre aktarım hatası düzeltmesiyle 15/20 (%75) ayrı değerlendirmedir; yeni bağımsız başarı sayılmaz. Q9 kesin teknik eksik diye sınıflandırılmaz.

Q10 ilk D, doğru B: Tarayıcı/mobil istemcilerin Firestore Security Rules denetimi ile administrative server SDK erişimi ayrıldı. Server SDK Rules'ı bypass ettiği için admin testinin başarısı müşteri izolasyonu kuralını doğrulamaz; production IAM'i daraltmak bu testi Rules testi yapmaz. Emulator'da iki sentetik kullanıcı bağlamıyla kendi belgesine izin, diğerinin belgesine ret sınanır. Türkçe senaryo, şıkların eleme nedenleri ve iki kullanıcı örneği verildi. Kaynak: https://firebase.google.com/docs/firestore/security/test-rules-emulator . Kavrayış/bağımsız kontrol yok. Sonraki yanlış Q12, ardından Q19; yeni çözüm Q21.

### Q10 güven düzeyi

Kullanıcı B ile D arasında kaldığını bildirdi. Q10 güven düzeyi K (kararsız); ilk seçim D korunur. İki seçenek arasındaki kararsızlık kullanıcı beyanıdır; doğru seçeneğin gerekçesini bağımsız bildiği veya konunun tamamen öğrenildiği sonucu çıkarılmaz. Ayırıcı koşul: administrative server SDK erişimini daraltmak client Security Rules testine dönüştürmez; B doğrudan Rules denetiminden geçen kullanıcı bağlamlarını sınar.

## Q12 rehberli inceleme

İlk A, doğru C. Güncel metin yeniden okundu; executable değişmiyor, sorun non-secret environment endpoint ayarında. A no-traffic test ve rollback sağlasa da aynı source'tan rebuild yaparak sorunun açık rebuild etmeme/test edilmiş artifactı koruma koşulunu bozar. C aynı test edilmiş image digest + düzeltilmiş config ile yeni revision, normal trafik vermeden doğrulama ve ardından trafik geçişi sağlar; eski revision rollback için korunur. Build/image ile deploy/revision ayrımı ve digest'in tam artifact kimliği olduğu Türkçe açıklandı. Database uyumu rollback engelini dışlayan koşul olarak belirtildi. İlk A ve ilk 14/20 korunur; kavrayış teyidi yok. Sonraki incelenmemiş yanlış Q19. Kaynak: https://docs.cloud.google.com/run/docs/configuring/services/environment-variables .

### Q12 güven düzeyi

Kullanıcı A ile C arasında kaldığını bildirdi. Güven K (kararsız), ilk seçim A korunur. Ayırıcı açık kısıt: test edilmiş artifactı koruma ve environment değeri için yeniden build yapmama; A rebuild içerir, C aynı digest'i kullanır. Kararsızlık beyanı bağımsız kavrayış veya kalıcılık kanıtı değildir.

## Q19 rehberli inceleme

İlk B, doğru C. Pub/Sub dead-letter iş akışı Türkçe açıklandı: tekrar başarısız mesajın ayrı topic'e yönlendirilmesi ve inspection subscription ile incelenmesi. Forwarding için subscription projesinin Pub/Sub service agent'ına hedef dead-letter topic üzerinde Publisher, kaynak subscription üzerinde Subscriber gerekir. B yalnız hedef Publisher ve inspection subscription sağlar, kaynak iznini tamamlamaz; C forwarding permissions ifadesiyle gerekli izinlerin tamamını kapsar. C'deki ifade rol adlarından daha genel olduğu için açıklamada iki rol/kaynak açıkça eşlendi. A erken ack ile hatayı başarı sayar; D deadline artışı bozuk içeriği düzeltmez. Delivery attempt eşiği best-effort, tam sayıda kesin taşıma değildir. Kaynak: https://docs.cloud.google.com/pubsub/docs/dead-letter-topics . İlk B korunur, güven/gerekçe ve kavrayış teyidi yok.

İlk 20'nin gönderilen altı yanlışının açıklaması verildi (Q2/3/9/10/12/19); bu öğrenme veya bağımsız tekrar başarısı değildir. Q9 kullanıcı beyanıyla aktarım hatası ayrı kayıttır. Yeni soru çözümü Q21'den devam eder.

### Q19 şık yakınlığı ve soru kalitesi notu

Kullanıcı B/C şıklarını çok yakın bulduğunu belirtti; ilk çözümde kararsız kaldığını açıkça söylemediği için güven K varsayılmadı. B hedef Publisher ve inspection subscription'ı somut sayarken C genel “forwarding permissions” diyor. Soru kökü eksik forwarding izinlerini adlandırmıyor; kaynak Subscriber izninin zaten mevcut olup olmadığını açıkça belirtmediği için B'nin yetersizliği yazımda tam kesinleştirilmemiş. Anahtarın C niyeti tüm gerekli izinleri tamamlama; kaynak izni zaten varsa B de yeterli olabilir. Bu soru kalitesi sınırlaması, hatanın yalnız kullanıcı bilgi/okuma eksikliğine bağlanmasını engeller. İlk B ve tarihsel anahtar puanı korunur; soru/anahtar sessizce değiştirilmedi. Gelecek sürümde iki eksik izin açık yazılmalı ve C bunları adlandırmalıdır.

## Q21–Q50 ilk cevap tablosu

| Soru | İlk cevap | Anahtar | Sonuç |
|---|---|---|---|
| 21 | B | B | Doğru |
| 22 | D | D | Doğru |
| 23 | A | A | Doğru |
| 24 | A | A | Doğru |
| 25 | B | B | Doğru |
| 26 | D + E | A + E | Yanlış |
| 27 | D | D | Doğru |
| 28 | B | B | Doğru |
| 29 | D | C | Yanlış |
| 30 | C | C | Doğru |
| 31 | A | A | Doğru |
| 32 | D | D | Doğru |
| 33 | A | A | Doğru |
| 34 | B | B | Doğru |
| 35 | A | C | Yanlış |
| 36 | A + B | A + B | Doğru |
| 37 | C | C | Doğru |
| 38 | C | D | Yanlış |
| 39 | B | B | Doğru |
| 40 | B | B | Doğru |
| 41 | D | D | Doğru |
| 42 | D + E | D + E | Doğru |
| 43 | D | D | Doğru |
| 44 | C | C | Doğru |
| 45 | C | B | Yanlış |
| 46 | A | A | Doğru |
| 47 | C | C | Doğru |
| 48 | C | C | Doğru |
| 49 | D | A | Yanlış |
| 50 | A + B | A + E | Yanlış |

## Q21–Q50 yanlışlarının toplu açıklaması

Kullanıcı yanlış sayısını fazla buldu ve tüm açıklamaları birlikte istedi. Son bölümdeki yedi yanlışın Türkçe senaryosu, ilk seçimi eleyen koşul, doğru yaklaşım ve kısa örnek birlikte açıklandı:

- Q26 D+E→A+E: Floating tag yerine gözden geçirilip test edilerek güncellenen base digest; E lockfile zaten doğru. Pinning güncellemeden vazgeçmek değildir. No-cache tek başına yeni base image çekme garantisi değildir.
- Q29 D→C: Config'teki image referansını görmek aktif eski session'ı yenilemez; işi kaydet, restart, sürümü doğrula. Persistent home korunur, kaydedilmemiş bellek durumu ayrı.
- Q35 A→C: Güvenlik ve functional-test onayı birbirinin yerine geçmez; iki onay aynı digest için AND.
- Q38 C→D: Version history silmeyi engelleme garantisi değildir. Seçili nesnelere temporary hold, vaka kapanınca explicit release; diğer nesnelerde lifecycle devam eder.
- Q45 C→B: Canlı veriler yeni key version'a taşınsa da backup eski version'a bağımlıdır. Gerekli eski sürümleri kullanılabilir tut; disable geri alınabilir ama disabled iken decrypt yapılamaz, disable ile destroy aynı değil.
- Q49 D→A: Backoff denemeleri aralıklandırır; deadline sınırı ayrıca gerekir. Optional metin için süre bitince fallback ve hata kaydı.
- Q50 A+B→A+E: A doğru; commit sonrası ack kaybı simülasyonu ve aynı operation'ı tekrar gönderme E ile gerçek failure window ölçülür. B uygulamanın çıktısını beklenen değer yaparak testi döngüsel kılar. 100+10 tek işlem, tekrar teslimatta 110 kalmalı.

Açıklamalar bağımsız yeni yanıt veya öğrenme/kalıcılık doğrulaması değildir. İlk seçimler, 37/50 anahtar toplamı, Q9 ayrı aktarım beyanı ve Q19 belirsizliği değişmedi. Tüm gönderilmiş yanlışlar artık açıklanmıştır; sonraki çalışma kullanıcının istediği ayrımı derinleştirmek veya bağımsız tekrar, yeni set yalnız istekle.

## Dil yükü ve sınav kıyası

Kullanıcı yaklaşık İngilizce anlamanın yetmediğini, kesin koşulları anlamanın gerektiğini söyledi ve analistlerin nasıl geçtiğini/gerçek sınavlarının daha kolay olup olmadığını sordu. Bahsedilen kişilerin tam sertifikası ve hazırlığı bilinmiyor. Web araması aynı PCD sınavına girmiş analistler için daha kolay sınav kanıtı vermedi. S09'un bilinçli uzun/yakın seçenekli, gerçek sınavla kalibre edilmemiş tasarımı ve Q19 belirsizliği nedeniyle puanı gerçek sınav geçiş tahminine çevirmemek gerekir. Q35 neither/either ve Q49 until/deadline dil koşulları; Q38 hold/versioning ve Q45 backup-key bağımlılığı teknik kavrayışla birlikte değerlendirilir. Sonraki öğretimde bütün paragrafı kelime kelime çevirmek yerine hedef, değişmemesi gereken şey ve seçeneğin bozduğu koşul çıkarılır. Yeni puan veya kavrayış doğrulaması yok.

## 29 Eylül — Mekanizma rehberi ve kullanıcı beyanı

Kullanıcı bazı mekanizma/kavramları tanımamasının hızlı ve tam anlamayı zorlaştırdığını belirtti; Storage, Workstations ve GKE Workload Identity örneklerini verdi. Bütün 50 soruyu Pub/Sub'daki somut varlık ve akış örneği gibi açıklamamızı istedi. [S09 mekanizma rehberi](../PCD-S09-MECHANISMS.md) hazırlandı: Q01–Q50 için varlıklar, somut olay/akış, çözüm mekanizması ve İngilizce karşılıklar; ayrıca ortak kimlik sözlüğü ve GKE WIF temeli. Bu kayıt materyal hazırlığıdır; bütün bölümlerin kullanıcı tarafından okunduğu veya kavrandığı doğrulanmadı. Yeni bağımsız yanıt, süre veya puan yok; mevcut ilk cevaplar, Q9 beyanı ve Q19 belirsizliği korunur. Bundan sonraki açıklamalarda önce mekanizmayı kurup İngilizce koşulları bu akışa bağla.
