# Kaynak ve sürüm notları

Bu bankanın cevapları repodaki PDF sürümlerine dayanır. Dosya sayfası referansları esas alınır; eski quiz geri bildirimleri PDF açıklamalarının önüne geçirilmez. Bu dosya bazı kaynak ifadelerinin kapsamını sınırlar; güncel ürün dokümantasyonunun tamamını doğrulayan bir denetim değildir.

## 1. Cloud Run ve gRPC

Eski `foundations-quiz-results.txt` geri bildirimindeki gRPC desteklenmediği ifadesi, Foundations M7 içinde HTTP ve gRPC desteğini açıkça belirten [PDF s. 28](../foundations/Module7-ComputeOptionsForYourApplication.pdf#page=28) ve [PDF s. 34](../foundations/Module7-ComputeOptionsForYourApplication.pdf#page=34) ile çelişir. F07-04 cevapları PDF açıklamasını esas alır.

## 2. Pod IP ile Service IP ayrımı

Fundamentals M5 [PDF s. 11](../fundamentals/M5%20_%20Containers%20in%20the%20Cloud%20v5.2%20_%20ILT.pdf#page=11) başlığı Pod IP’si hakkında yanıltıcıdır. Aynı slaydın açıklaması ve [PDF s. 12](../fundamentals/M5%20_%20Containers%20in%20the%20Cloud%20v5.2%20_%20ILT.pdf#page=12) sabit endpoint’i Service’e bağlar, Pod IP’lerinin zamanla değiştiğini söyler. U05-02 bu ayrımı sorar.

## 3. CI/CD branch akışı bir örnektir

Foundations M1 [PDF s. 14](../foundations/Module1-BestPracticesForCloudApplicationDevelopment.pdf#page=14) ile M6 [PDF s. 4](../foundations/Module6-DeployingApplications.pdf#page=4) farklı örnek anlatımları kullanır. M6 soruları o slaydın feature-branch/main-branch akışına özgüdür. Her CI/CD sisteminin yalnız bu branch düzeninde çalışabileceği sonucu çıkarılmamalıdır.

## 4. Cloud Run eski limit ve fiyat anlatımları

Fundamentals M6 [PDF s. 8](../fundamentals/M6%20_%20Applications%20in%20the%20Cloud%20v5.2%20_%20ILT.pdf#page=8) eski CPU/bellek üst sınırları ve istek bazlı ücret örneği içerir. Bu değerler güncel genel limit olarak soru anahtarına alınmadı. Foundations M7’deki GPU sorusu yalnız [PDF s. 27](../foundations/Module7-ComputeOptionsForYourApplication.pdf#page=27) üzerinde verilen özellikleri ölçer.

## 5. Sayısal tablolar ve tarihli hedefler

Nesne boyutu, Firestore entity boyutu, storage sınıfı erişim örüntüsü, gecikme karşılaştırması, bağlantı boyutu ve sürdürülebilirlik hedefleri soruda belirtilen PDF sürümünün bilgisidir. Bunlar güncel kota/SLA garantisi değildir. Özellikle 2030 hedefi gerçekleşmiş sonuç gibi yorumlanmaz. Storage gecikme tablosu karşılaştırmadır; uygulamanın her isteğine garanti edilen gecikme değildir.

## 6. Ürün özelliklerine ilişkin aşırı genel kaynak cümleleri

Fundamentals M4 tablosundaki Bigtable için mutlak SQL yokluğu ifadesi güncel ürün iddiasına dönüştürülmedi ([PDF s. 47](../fundamentals/M4%20_%20Storage%20in%20the%20Cloud%20v5.2%20_%20ILT.pdf#page=47)). Sorular veritabanı modeli ve iş yükü seçimine odaklanır. Benzer şekilde Fundamentals M2 [PDF s. 21](../fundamentals/M2%20_%20Resouces%20and%20Access%20in%20the%20Cloud%20v5.2%20_%20ILT.pdf#page=21) içindeki billing administrator sınıflandırması, temel IAM rollerinin ezberlenecek listesine eklenmedi.

## 7. LLM sınırlamaları ve örnek mimari

Fundamentals M7 [PDF s. 13](../fundamentals/M7%20_%20Prompt%20Engineering%20v5.2%20_%20ILT.pdf#page=13) modelin gerçek zamanlı bilgiye veya ek bağlam istemeye erişemeyeceği gibi mutlak ifadeler kullanır. Bunlar her araç destekli ürün için evrensel kural olarak sorulmadı. Eğitim verisi, yetersiz bağlam ve kısıtlar gibi listelenen hata faktörleri esas alındı ([PDF s. 14](../fundamentals/M7%20_%20Prompt%20Engineering%20v5.2%20_%20ILT.pdf#page=14)).

Aynı modülün sonundaki hub-and-spoke önerisi yalnız Sasha örneğinin cevabıdır ([PDF s. 38](../fundamentals/M7%20_%20Prompt%20Engineering%20v5.2%20_%20ILT.pdf#page=38)). Tek başına bütün gerçek ağlarda merkezi firewall yönetimini garanti eden bir tasarım onayı sayılmaz.

## 8. Kapsam ve izlenebilirlik

İlk iki bölümün 15 modülü konu gruplarına ayrılmıştır. Kapak, gündem, tekrarlanan özet sayfaları ve laboratuvar yönergeleri ayrı soru seti oluşturmaz. Her cümleyi ezberleten eksiksiz bir soru dökümü olduğu iddia edilmez. [Kapsam haritası](COVERAGE.md) setleri listeler. [Kaynak manifesti](source-manifest.json) PDF sayfa sayılarını ve SHA-256 özetlerini kaydeder. Cevap anahtarları konu açıklamasıyla birlikte soru bazında PDF sayfasına bağlanır.

## 9. Orchestration kaynak kapsamı

O01 setlerinin kaynağı Introduction to Microservices PDF’idir. OQ setleri paylaşılan quiz ve resmî dokümanlarla desteklenir. Eventarc taşıma soruları Standard kapsamındadır. Cloud Tasks token seçeneğinin işaretlenmemiş olması onun yanlışlığını kanıtlamaz; [bölüm analizi](orchestration/README.md) kimlik ayrımını açıklar.

## 10. Cloud Run Functions: ders sürümü ve çelişkiler

25 set (C01–C05) yalnız yüklenen beş PDF’ye dayanır. Sayfa numaraları PDF dosyasının 1 tabanlı sayfalarıdır. Kaynaklar toplam 146 sayfadır. Başlık/gündem/tekrar sayfaları bağımsız konu sayılmadı; lab akışlarının Redis yazma-okuma ve özel VM bağlantısı gibi somut adımları kapsama alındı.

- M1 s. 18’deki 32 GiB/4 vCPU, 1000 concurrency, HTTP 60 dakika/event 10 dakika değerleri **PDF’ye göre** sorulur. Üst sınır, varsayılan ve güncel kullanılabilir konfigürasyon aynı değildir.
- M1 s. 17’deki runtime/CloudEvent/Background sınıflandırması ve s. 30–31’deki repository deployment yolu dersin nesil ayrımını korur. M2 s. 5’teki tek trigger bağlama sınırı bu deployment anlatımına aittir; tüm çağdaş Cloud Run/Eventarc yapılandırmalarına genellenmez.
- M3 s. 11’de cloudfunctions.functions.invoke izni bulunur. S. 13’te açıklama yeni Cloud Run functions için roles/run.invoker, 1st gen için roles/cloudfunctions.invoker der; CLI kutusunda eski rol vardır. C03-02, soruda nesli belirterek açıklamadaki ayrımı kullanır.
- M3 s. 17 anahtar erişimi kaybını genel anlatırken s. 23, hâlihazırda çalışan execution’ların devam ettiğini belirtir. Aynı s. 23’te aktif instance’a gelen yeni çağrılar slaytta “may fail”, konuşmacı notunda “will fail” diye geçer. Bu tartışmalı kesinlik sınav sorusuna dönüştürülmedi; devam eden execution ve yeni instance ayrımı soruldu.
- M3 s. 19 “service accounts” der; s. 21 ilgili Cloud Run functions, Artifact Registry ve Cloud Storage **service agent** kimliklerini açıklar. CMEK yetkisi bu kimliklerle sorulur; runtime service account ile karıştırılmaz.
- M4 s. 16–18 eski Firebase SDK biçimindeki onCreate/onWrite ve snapshot örneklerini içerir. Native/Datastore destek ifadesi güncel ürün desteğine genellenmedi. M4 s. 21’de volume üzerinden latest okuma, latest sürümünü izleyen bağlantı için sorulur; sabit secret version’ın kendiliğinden yenilendiği iddia edilmez.
- M5 s. 11–12’de retry kapalı varsayılanı ve yedi günlük süre anlatılır. C05-04 bunları yalnız dersin deployment modeli için sorar. HTTP istemcisinin retry davranışı veya başka Eventarc/API yolları için genel kural değildir.
- M5 s. 16’daki varsayılan tek istek ifadesi bütün güncel konfigürasyonlara genellenmedi. C05-05 concurrency güvenliği, min/max instance ayrımı, geçici limit aşımı ve immutable revision davranışını ölçer.

Bu bölüm için kurs quiz sonucu henüz paylaşılmadı. Başarı puanı veya çözülmüş durum uydurulmadı; takip tablosu boş satırlarla genişletildi.

## 11. Containers, Cloud Run ve GKE: örnekleri doğru yorumlama

T01–T09, `containeried/` klasöründeki 9 PDF’ye (112 sayfa) dayanan 24 set / 120 sorudur. Dosya adları korunmuştur; T01–T05 ilk ana modülü, T06–T09 ikinci ana modülü kapsar. Sayfa numaraları PDF dosyasındaki 1 tabanlı sayfalardır. Başlık, gündem ve tekrar slaytları ayrı konu sayılmadı.

- T01 kaynağı s. 12–13: Node örneğinde `_dirname` ve büyük harfle yazılmış package alanları görülür. Bunlar çalıştırılabilir kod olarak çoğaltılmadı; dosyaların görevleri ve bağımlılık/runtime ayrımı soruldu. PORT ile 8080 fallback'i, sabit 8080 zorunluluğuyla karıştırılmadı.
- T04 kaynağı s. 11: Docker build örneğinin argümanlarında image tag öncesi `-t` görünmüyor. Örnek kopyalanıp çalıştırılacak komut olarak sunulmadı. S. 13 yalnız Dockerfile/build config derken s. 14 Buildpacks seçeneğini de listeler; sorularda yalnız iki yöntem varmış gibi bir çıkarım yapılmadı. Skaffold API sürümü, eski beta komutlar ve repository ürün adları ders sürümüne aittir.
- T05 kaynağı s. 8: Sadece CMD/ENTRYPOINT yazmak bütün shell-wrapper biçimlerinde sinyallerin uygulamaya ulaşacağını garanti etmez. Docker belgesi exec ve shell biçimlerini ayırır; shell form ENTRYPOINT uygulamayı PID 1 yapmayabilir. Sorular sinyalin ana sürece ulaşması ve handler kaydı üzerinde durur. [Dockerfile reference](https://docs.docker.com/reference/dockerfile/).
- T06 kaynağı s. 6 services ve jobs ayrımını yapar; s. 7 HTTP dinleme gereksinimi services bağlamındadır. Jobs için aynı zorunluluk çıkarılmadı. Fiyatlama soruları PDF’deki iki modelin kavramsal farkını ölçer, güncel fiyat teklifi değildir.
- T07 kaynağı s. 4’teki Pub/Sub delivery ifadesinden exactly-once iş sonucu türetilmedi. Bölge içi çok-zon dağılımı, kendiliğinden çok-bölge deployment olarak yorumlanmadı; s. 11’de global load balancer ve ayrı regional services gerekir.
- T08 kaynağı s. 6–8: Slaytlarda `apiVersion: v1.1`, Deployment örneğinde `Metadata` ve eksik selector yapısı var. Resmî Deployment örneği `apiVersion: apps/v1`, küçük harfli `metadata` ve `spec.selector.matchLabels` kullanır; Service örneği `apiVersion: v1` kullanır. Sorular hatalı YAML'ı ezberletmez; replicas, selector, template, port/targetPort ayrımını ölçer. [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) · [Service](https://kubernetes.io/docs/concepts/services-networking/service/).
- T08 kaynağı s. 9: Pod içindeki mount görünümü ile Secret/ConfigMap API nesnesinin ömrü ayrıdır. Pod silinince bu API nesnelerinin mutlaka silineceği sonucu çıkarılmaz. Volume, gereken container’a ayrıca mount edilir; bütün container’larda kendiliğinden görünür değildir. Ephemeral storage ile Pod’dan bağımsız durable storage ayrımı korunur. [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/).
- T09’daki COS güncelleme, runtime, toolbox ve destek sınırlamaları PDF’ye göre sorulur. Haftalık güncelleme veya üçüncü taraf driver kapsamı bütün güncel sürümlere koşulsuz genellenmez.

Resmî bağlantılar 19 Eylül 2026 tarihinde kaynak çelişkilerini açıklamak için kontrol edildi. Bu bölüm için sınav sonucu paylaşılmadı; yeni quizlerin çözüm durumu boş bırakıldı.
