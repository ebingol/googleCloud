# PCD-S01 — Cevaplar ve gerekçeler

**Önce [soru setini](../../scenarios/PCD-S01.md) tamamla.**

Kaynak kontrolü: 20 Eylül 2026. Sorular özgün çalışma senaryolarıdır. Ürün belgeleri teknik gerekçeyi destekler; Google bu soruları onaylamamıştır. Sınav rehberi eşleştirmesi aşağıda ayrı gösterilmiştir.

## 1. C — Runtime identity ve kaynak kapsamı

- **C doğru:** API çağrısını yapan runtime kimliğidir. ADC bu kimliği kullanır; secret üzerindeki Secret Accessor rolü yalnız gereken kaynağın değerine erişim verir.
- **A:** Build kimliğine verilen izin farklı runtime kimliğine aktarılmaz.
- **B:** Proje kapsamındaki erişim diğer secret'ları da kapsar; gereksinimden geniştir.
- **D:** Viewer metadata içindir; secret payload erişimi sağlamaz.

**Belirleyici koşul:** Tek secret, farklı proje, anahtar dosyası yok.

**Kaynak:** [Cloud Run secrets](https://docs.cloud.google.com/run/docs/configuring/services/secrets) · [ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

## 2. A — Kontrollü dağıtım

- **A doğru:** Yeni revision başlangıçta trafik almadan dağıtılabilir; ardından revision yüzdeleriyle kademeli geçiş ve geri dönüş yapılabilir.
- **B:** Instance sayısı oranı, gelen isteklerin dağılım oranı değildir.
- **C:** DNS ağırlıkları cache ve istemci davranışı nedeniyle kesin istek yüzdesi vermez; ek servis de gereksizdir.
- **D:** Revision yerinde değiştirilmez. Mevcut R1'e trafik döndürmek yeniden build gerektirmez.

**Belirleyici koşul:** Aynı servis, şema uyumlu, ek altyapı en az. Trafik değişimi anlık değildir; işlemdeki istekleri geri almaz. %5 yönlendirme hedefidir, her küçük örneklemde tam %5 garantisi değildir.

**Kaynak:** [Traffic migration](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration).

## 3. D — Build adımları arasında veri

- **D doğru:** `/workspace` içindeki dosyalar aynı build'in sonraki adımlarına taşınır. Paylaşılan özel bir volume da mümkün olurdu.
- **A:** IAM kimliği container dosya sistemlerini ortaklaştırmaz.
- **B:** Adımlar zaten sıralı; beklemek ayrı `/tmp` dizinlerini birleştirmez.
- **C:** Dış depolama ekler; yalnız aynı build içinde aktarım koşuluna uymaz.

**Belirleyici koşul:** Sorun zamanlama değil, adımların dosya sistemi sınırıdır.

**Kaynak:** [Passing data between build steps](https://docs.cloud.google.com/build/docs/configuring-builds/pass-data-between-steps).

## 4. B — Sınırlı süreli nesne erişimi

- **B doğru:** Yetkilendirme sonrası belirli nesne ve GET yöntemi için imzalı URL üretmek doğrudan, süreli erişim sağlar.
- **A:** Uygulama içi kullanıcı ID'si kendiliğinden bir Google IAM principal'ı değildir.
- **C:** Bucket genelinde erişim açar; tek müşteri ve tek nesne sınırını aşar.
- **D:** Uygulamanın erişim token'ını müşteriye aktarır; erişimi yalnız o nesneye sınırlandırmaz.

**Belirleyici koşul:** URL'yi elinde tutan kişinin kullanabilmesi kabul edilmiş. Signed URL kullanıcı oturumu yerine geçmez; link korunmalıdır. İmzalayan kimliğin gereken izni olmalıdır.

**Kaynak:** [Signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).

## 5. C — Zamanlanmış, hedefi belirli iş

- **C doğru:** Cloud Tasks hedef HTTP endpoint'i, ileri teslim zamanını ve kuyruk dispatch hızını kontrol etmeye uygundur. Handler tekrar çalışmaya dayanıklı olmalıdır.
- **A:** Ack deadline ilk teslimat zamanlayıcısı değildir.
- **B:** Event filtresi ileri tarihli iş zamanlama mekanizması değildir.
- **D:** Saatlerce açık HTTP isteği dayanıklı kuyruk ve zamanlama yerine geçmez.

**Belirleyici koşul:** Tek bilinen hedef, ileri zaman, kontrollü hız. Zamanlama tam o anda çalışma garantisi değildir.

**Kaynak:** [Choose Cloud Tasks or Pub/Sub](https://docs.cloud.google.com/tasks/docs/comp-pub-sub).

## 6. A, D — Çağıran kimlik ve ID token

- **A doğru:** Yetki hedef B üzerinde, çağıran A'nın runtime kimliğine verilir.
- **D doğru:** ID token hedefin beklediği audience ile çağıranın kimliğini doğrular. Runtime kimliğinden keyless token alınabilir.
- **B:** Cloud Run IAM invocation için bu senaryoda OAuth access token yerine ID token gerekir.
- **C:** Yetkilendirme yönünü ters çevirir; A'nın B'yi çağırmasını sağlamaz.

**Belirleyici koşul:** Ağ erişimi zaten sağlanmış; authentication ile authorization ikisi de gerekli.

**Kaynak:** [Service-to-service authentication](https://docs.cloud.google.com/run/docs/authenticating/service-to-service).

## 7. B — Instance içindeki eşzamanlılık

- **B doğru:** Concurrency 1 aynı instance'taki paralel HTTP isteklerini sınırlar. Soruda ardışık işleme güvenli olduğu belirtilmiştir.
- **A:** Tek instance yine birden fazla eşzamanlı istek alabilir.
- **C:** CPU artırmak mutable state yarışını çözmez.
- **D:** Session affinity eşzamanlı istekleri sıraya koymaz.

**Belirleyici koşul:** Hata aynı instance'taki paralel isteklerden kaynaklanıyor. Bu geçici önlem kütüphaneyi thread-safe yapmaz; instance'lar arası ortak veri yarışını da çözmez.

**Kaynak:** [Maximum concurrency](https://docs.cloud.google.com/run/docs/about-concurrency).

## 8. D — Kaynaktan container üretimi

- **D doğru:** Desteklenen uygulama için source deployment ve buildpacks, Dockerfile bakımını azaltır; arka planda container image üretilir.
- **A:** Registry kaynak kodunu kendiliğinden çalıştırılabilir image'a dönüştürmez.
- **B:** Dockerfile geçerli bir yöntemdir; burada gereksiz build bakımını artırır.
- **C:** Job tamamlanacak işler içindir; sürekli HTTP hizmeti için uygun model değildir.

**Belirleyici koşul:** Desteklenen runtime ve bağımlılıklar, özel OS paketi yok. Buildpack kullanımı testlerin otomatik olarak doğru tasarlandığı veya uygulamanın hatasız olduğu anlamına gelmez.

**Kaynak:** [Google Cloud buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview).

## 9. A — Okuma sonucuna bağlı atomik yazma

- **A doğru:** Transaction güncel sayıyı kontrol eder ve iki değişikliği birlikte commit eder. Çakışmada transaction yeniden çalışabilir; kapasite kalmadığında rezervasyon reddedilir.
- **B:** Batch yazmaları atomiktir ancak transaction dışındaki eski okumayı korumaz.
- **C:** Atomik decrement sıfır altına inmeyi tek başına engellemez; ayrı yazı da iki işlemi atomik yapmaz.
- **D:** Instance içi mutex diğer instance'ları koordine etmez; ayrı yazılar kısmen başarılı olabilir.

**Belirleyici koşul:** Okuma-kontrol-yazma bütünü korunmalı. Transaction callback'inde e-posta veya ödeme gibi dış yan etki üretme; tekrar çalışabilir.

**Kaynak:** [Firestore transactions](https://docs.cloud.google.com/firestore/native/docs/manage-data/transactions).

## 10. C — Tekrar teslimde güvenli işleme

- **C doğru:** Kalıcı dedup anahtarı ve inventory değişikliğinin aynı transaction'da tutulması, eşzamanlı tekrarları ve crash sonrası tutarsız marker durumunu önler.
- **A:** Bellek restart'ta kaybolur ve başka instance'larla paylaşılmaz.
- **B:** Marker sonrası crash olursa inventory güncellenmeden event işlenmiş sayılabilir.
- **D:** Retention kısaltmak duplicate işlemeyi önlemez; geçici hatalarda kurtarma imkânını azaltabilir.

**Belirleyici koşul:** Yan etki aynı transaction'a katılabilen veri tabanında. Dış ödeme servisi olsaydı ayrıca idempotency key/outbox gibi tasarım gerekirdi. Kaynak ve event ID birlikte kullanılır; bütün farklı iş olaylarının aynı ID'ye sahip olduğu varsayılmaz.

**Kaynak:** [Eventarc retry and idempotent handlers](https://docs.cloud.google.com/eventarc/docs/retry-events).

## 11. B, C — Local ADC ve production kimliği

- **B doğru:** CLI login ile yerel ADC kurulumu ayrıdır. Bu komut client library'lerin yerelde bulabileceği ADC'yi oluşturur.
- **C doğru:** Cloud Run'da ADC bağlı runtime service account'u kullanır; bu kimliğin kaynak izinleri gerekir.
- **A:** Geliştirici kimliğini production image'a taşır; hedeflenen kimlik ayrımını bozar.
- **D:** Deploy edebilmek, çalışan uygulamaya kaynak erişimi vermez.

**Belirleyici koşul:** Kod aynı kalır, credential kaynağı ortamla değişir. Local test kimliğinin de eriştiği kaynaklara gerekli izni olmalıdır.

**Kaynak:** [How ADC works](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

## 12. A — Ölçülmüş cold start gecikmesi

- **A doğru:** Hazır instance kapasitesi, sıfırdan başlangıç ihtiyacını azaltır. İş yüküne göre ölçülerek boyutlandırılmalıdır.
- **B:** Timeout beklemeye izin verir; initialization süresini azaltmaz.
- **C:** Maximum instances üst sınırdır, boşta hazır kapasite oluşturmaz.
- **D:** Session affinity durmuş instance'ı hazır tutmaz.

**Belirleyici koşul:** Trace'te initialization baskın. Minimum instance ayarı bütün cold start'ları yok etmez; restart, yeni revision veya artan kapasite ihtiyacında yine başlangıç olabilir.

**Kaynak:** [Minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances).

## 13. D — Testi gerçek bir yayın kapısı yapmak

- **D doğru:** Hata toleransı kaldırılınca başarısız test build'i durdurur; sıralı deployment çalışmaz.
- **A:** Bildirim başarısız sürümün yayınını engellemez.
- **B:** Bitişi beklemek, başarısızlığı kabul eden ayarı değiştirmez.
- **C:** İstenen yayın öncesi kontrolü kaldırır; rollback ayrı bir kurtarma önlemidir.

**Belirleyici koşul:** Test zaten nonzero çıkıyor, adımlar sıralı. Test script'inin hataları yutması veya bağımsız paralel deploy başka sorunlar olurdu.

**Kaynak:** [Build and test Node.js applications](https://docs.cloud.google.com/build/docs/building/build-nodejs) · [Build configuration schema](https://docs.cloud.google.com/build/docs/build-config-file-schema).

## 14. B — İlişkisel, yatay büyüyen transaction yükü

- **B doğru:** Spanner uygun yapılandırmayla ilişkisel erişim, yatay ölçekleme ve güçlü transaction tutarlılığı gereksinimlerini karşılar.
- **A:** Read replica eklemek yazmaları tüm replica'lara dağıtan yatay yazma mimarisi oluşturmaz.
- **C:** Analitik ve periyodik uzlaştırma, işlem anındaki hesap transferi transaction'ının yerine geçmez.
- **D:** Cross-row transaction sorumluluğunu uygulamaya yükler; ilişkisel SQL ve yönetilen transaction gereksinimine uymaz.

**Belirleyici koşul:** Yalnızca güçlü tutarlılık değil; ilişkisel transaction, yüksek yazma ölçeği ve uygulama sharding'inden kaçınma birlikte isteniyor. Küçük bir bölgesel uygulama için otomatik olarak Spanner seçilmez.

**Kaynak:** [Spanner transactions](https://docs.cloud.google.com/spanner/docs/transactions) · [External consistency](https://docs.cloud.google.com/spanner/docs/true-time-external-consistency).

## 15. C — Durumu gözlemlenebilir koordinasyon

- **C doğru:** Workflows açık adımlar, koşullar, retry ve callback beklemeyi yönetilen bir execution olarak ifade eder.
- **A:** Choreography bağımsız tüketiciler için yararlıdır; burada istenen merkezî süreç durumu ve koordinasyonu ayrıca kurmak gerekir.
- **B:** Tasks iş teslimini yönetir; tam iş akışının dallanma ve kalıcı durum mantığını handler'lara bırakır.
- **D:** Saatlerce HTTP bağlantısı tutmak dayanıklı bir süreç koordinatörü oluşturmaz.

**Belirleyici koşul:** Sıralı bağımlılıklar, uzun bekleme, execution görünürlüğü. Retry edilen dış işlemler yine idempotent tasarlanmalıdır.

**Kaynak:** [Workflows overview](https://docs.cloud.google.com/workflows/docs/overview) · [Callbacks](https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints).

## Kapsam ve değerlendirme

[20 Eylül 2026'da kontrol edilen resmî PCD rehberi](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf) ile konu eşleştirmesi:

| Çalışma alanı | Sorular | Rehber başlıkları |
|---|---|---|
| IAM, ADC, servis kimliği | 1, 6, 11 | 1.2, 4.2 |
| Cloud Run, performans ve dağıtım | 2, 7, 12 | 1.1, 3.1 |
| Build, test ve CI/CD | 3, 8, 13 | 2.2, 2.3, 3.1 |
| Veri ve depolama | 4, 9, 14 | 1.3, 4.1 |
| Event ve koordinasyon | 5, 10, 15 | 1.1, 3.1, 4.1 |

Her sorunun tam doğru seçenek kümesi 1 puandır; çoklu seçimde eksik/fazla işaretleme 0 puandır. Toplam 15 puan bir çalışma ölçüsüdür, resmî geçme puanı değildir.

- Yanlış + emin: yanlış zihinsel modeli düzelt; öncelikli tekrar.
- Yanlış + kararsız/tahmin: konu ve seçenek ayrımlarını çalış.
- Doğru + kararsız/tahmin: öğrenilmiş sayma; yeni senaryoyla yeniden dene.
- Doğru + emin: en yakın yanlış seçeneği neden elediğini de açıklayabiliyorsan olumlu işaret.

Pilot; GKE health checks/HPA, Apigee, AI destekli geliştirme, observability ve kapsamın diğer alanlarını tamamlamaz. Sonraki setlerde genişletilmelidir. Teknik doğruluk kaynaklarla gözden geçirildi; zorluk seviyesi ilk çözümden sonra ayarlanacaktır.
