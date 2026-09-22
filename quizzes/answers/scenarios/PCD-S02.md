# PCD-S02 — Türkçe cevap anahtarı

**Soruları bitirmeden açma.** Hazırlama ve resmî kaynak kontrolü: 22 Eylül 2026.

Her soru 1 puan; Q7 için iki doğru seçeneğin birlikte seçilmesi gerekir. Teknik bilgi, İngilizce anlam, yönerge ve gerekçe eksikliğini ayrı değerlendir. Açıklama sonrası düzeltmeler ilk deneme puanını değiştirmez.

Bu sette aşağıdaki bağlantılar **Ek resmî kaynak** olarak kullanıldı; PDF sayfası doğrulanmış gibi gösterilmedi. Ders kapsamı ilişkisi COVERAGE.md üzerinden kuruldu. Alan kodları [resmî sınav rehberine](https://services.google.com/fh/files/misc/professional_cloud_developer_exam_guide_english.pdf) göre hazırlayanın eşleştirmesidir; bu dağılım sınav ağırlıklarını taklit etmez.


**Güncel kapsam:** Kullanıcının düzeltmesi üzerine 5 Cloud Run (1, 4, 7, 10, 13), 5 Cloud Run functions (2, 5, 8, 11, 14), 5 GKE (3, 6, 9, 12, 15). Functions soruları güncel Cloud Run functions bağlamındadır. HPA ve Kubernetes probe ayrıntıları ek resmî kaynaklarla desteklenir. İlk taslaktaki Eventarc tekrarı bu sürümde yoktur.

## 1 — C

**Gerekçe:** Bitince çıkan, HTTP sunmayan toplu iş için job uygundur; task timeout çalışma süresine göre ayarlanır. Başarıda 0, başarısızlıkta sıfır dışı çıkış kodu kullanılır.

**En yakın alternatif D:** VM üzerinde yapılabilir ama her koşuda VM yönetmek gereksiz operasyon yüküdür. A ayrıca uzun işi HTTP isteğine bağlar.

**Belirleyici ifade:** “does not serve HTTP requests” ve “a separate execution record for each run”.

**Alan:** 1.1 platform seçimi. **Ders ilişkisi:** R01-02, R09-01.

**Ek resmî kaynak:** [Container contract — jobs](https://docs.cloud.google.com/run/docs/container-contract#jobs).

## 2 — A

**Gerekçe:** Webhook aynı HTTP isteğinde yanıt bekliyor; HTTP handler bu istek/yanıt sözleşmesine uyar. İmza doğrulama kodda ayrıca yapılır.

**En yakın alternatif:** B asenkron mesaj işleme modelidir; CloudEvent handler dönüşü webhook çağıranına doğrudan HTTP yanıtı olmaz.

**Belirleyici ifade:** “in the same HTTP response”.

**Alan:** 3.1 function handler; 1.1 API tasarımı. **Ders ilişkisi:** C01-02.

**Ek resmî kaynak:** [Teknik açıklama](https://docs.cloud.google.com/run/docs/write-functions).

## 3 — D

**Gerekçe:** Service selector etiketlerle eşleşmediği için backend seçilmiyor. Selector düzeltmesi mevcut Service adını koruyarak doğru Pod'ları seçer.

**En yakın alternatif:** C daha çok Pod üretse de aynı etiket uyuşmazlığını çözmez. LoadBalancer türü de selector hatasını gidermez.

**Belirleyici ifade:** “all application Pods are Ready”.

**Alan:** 3.2 GKE servis yönlendirmesi. **Ders ilişkisi:** T08-03.

**Ek resmî kaynak:** [Teknik açıklama](https://kubernetes.io/docs/concepts/services-networking/service/).

## 4 — D

**Gerekçe:** TCP bağlantısı kurulması, uygulamanın tablosunun hazır olduğunu göstermez. HTTP startup endpoint'i gerçek hazırlığı kontrol etmelidir; probe süresi normal başlatmaya izin vermelidir.

**En yakın alternatif B:** Sıcak instance sayısını artırmak yeni instance'ların eksik başlangıç kontrolünü düzeltmez. Liveness ile startup farklı amaçlara hizmet eder.

**Belirleyici ifade:** “opens its HTTP port immediately” fakat “before the table is ready”.

**Alan:** 3.1 Cloud Run dağıtımı; 1.1 güvenilir uygulama. **Ders ilişkisi:** R02-01.

**Ek resmî kaynak:** [Cloud Run health checks — startup davranışı](https://docs.cloud.google.com/run/docs/configuring/healthchecks).

## 5 — B

**Gerekçe:** Geçici dosyalar belleği tüketir ve yeniden kullanılan instance'ta kalabilir. Başarı ve hata yollarında artık gerekmeyen dosyaları temizlemek birikmeyi önler.

**En yakın alternatif:** C aynı geçici dosya sisteminde taşıma yapar; bellek kullanımını serbest bırakmaz.

**Belirleyici ifade:** “temporary files are never removed”.

**Alan:** 1.1 kaynak kullanımı; 3.1 functions. **Ders ilişkisi:** C05-01.

**Ek resmî kaynak:** [Teknik açıklama](https://docs.cloud.google.com/run/docs/tips/functions-best-practices).

## 6 — C

**Gerekçe:** Deployment'ın istenen durumu Pod template'inde tanımlanır. Image'ı burada değiştirmek rollout başlatır ve yeni Pod'ların hedef sürümle oluşturulmasını sağlar.

**En yakın alternatif:** B tekil Pod düzeltmesidir; template v1 kaldığı sürece kalıcı dağıtım tanımını güncellemez.

**Belirleyici ifade:** “replacement Pods also use v2”.

**Alan:** 3.2 GKE dağıtımı. **Ders ilişkisi:** T08-02; S01-02 rollout'un GKE uygulaması.

**Ek resmî kaynak:** [Teknik açıklama](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

## 7 — B, C

**Gerekçe:** Her istekte yeni havuz oluşturmak yerine process başına sınırlandırılmış havuz yeniden kullanılır. Alınan bağlantı hata durumunda da iade edilmelidir. Instance sayısı arttıkça toplam bağlantı bütçesi ayrıca gözetilir.

**En yakın alternatif A:** Havuzları büyütmek mevcut çoğalma sorununu ağırlaştırabilir. IAM genişletmek bağlantı yaşam döngüsünü değiştirmez.

**Belirleyici ifade:** “a new connection pool for every HTTP request” ve “including when a request fails”.

**Alan:** 4.1 veri servisi bağlantıları. **Ders ilişkisi:** R11-03.

**Ek resmî kaynak:** [Cloud SQL — bağlantı yönetimi](https://docs.cloud.google.com/sql/docs/mysql/manage-connections).

## 8 — A

**Gerekçe:** Kalıcı veri hatası aynı payload'ı tekrar işleyerek düzelmez; kayıt tamamlandıktan sonra başarılı bitirmek tekrar döngüsünü keser. Geçici hatalar başarısız bildirilerek retry edilebilir. Geçersiz olayın kalıcı kaydı başarısızsa başarı dönülmemelidir.

**En yakın alternatif:** C kalıcı hatayı tekrarlar; inceleme kaydını da sağlamaz. B geçici hataları yutar.

**Belirleyici ifade:** “retrying cannot fix”.

**Alan:** 3.1 event functions; 4.2 hata yönetimi. **Ders ilişkisi:** C05-04; S01-10 olay işleme konusuna hata sınıflandırması ekler.

**Ek resmî kaynak:** [Teknik açıklama](https://docs.cloud.google.com/run/docs/tips/function-retries).

## 9 — D

**Gerekçe:** emptyDir Pod ömrüne bağlıdır. Uygun persistent volume ve korunan PVC, replacement Pod'un aynı kalıcı verilere erişmesini sağlar. PVC/PV silme politikası ayrıca yönetilmelidir; bu soru Pod değişimini ölçüyor.

**En yakın alternatif:** A kapasiteyi değiştirir, depolamanın ömrünü değil. Tek replica veriyi kalıcı yapmaz.

**Belirleyici ifade:** “across Pod replacement”.

**Alan:** 3.2 GKE depolama. **Ders ilişkisi:** T08-04.

**Ek resmî kaynak:** [Teknik açıklama](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

## 10 — D

**Gerekçe:** Internal and Cloud Load Balancing, dış Application Load Balancer yoluna izin verirken doğrudan dış internet ingress'ini kısıtlar. Ulaşabilen istekler için IAM doğrulaması ayrıca sürer.

**En yakın alternatif B:** Internal-only seçeneği, soruda gerekli dış Application Load Balancer giriş yolunu sağlamaz. IAM rolü ağ yolunu açmaz.

**Belirleyici ifade:** “through an external Application Load Balancer” ve “direct internet requests ... must be blocked”.

**Alan:** 1.2 erişim güvenliği. **Ders ilişkisi:** R04-02.

**Ek resmî kaynak:** [Cloud Run ingress](https://docs.cloud.google.com/run/docs/securing/ingress).

## 11 — B

**Gerekçe:** Entry point, çalıştırılacak kayıtlı handler'ın adını seçer. Kaynak ve bağımlılıklar doğru olduğuna göre hedef adını düzeltmek gerekir.

**En yakın alternatif:** D bekleme süresini değiştirir; bulunamayan handler'ı oluşturmaz. IAM da kod hedefini seçmez.

**Belirleyici ifade:** “passes local tests when targeting process_invoice”.

**Alan:** 3.1 function dağıtımı. **Ders ilişkisi:** C01-04/05; 21 Eylül kaynak konumu konuşuldu, bağımsız senaryoda ölçülmedi.

**Ek resmî kaynak:** [Teknik açıklama](https://docs.cloud.google.com/run/docs/write-functions).

## 12 — C

**Gerekçe:** Readiness başarısızlığı Pod'u servis trafiğine uygun olmaktan çıkarır; iyileşince tekrar hazır olabilir. Sağlıklı process'i yeniden başlatmak gerekmiyor.

**En yakın alternatif:** A gereksiz restart üretir. Startup probe yalnız başlangıç sürecini kontrol eder.

**Belirleyici ifade:** “can recover without restarting”.

**Alan:** 3.2 Kubernetes health checks. **Ders ilişkisi:** T08-03 ile ilişkili; probe davranışı ek resmî kaynak.

**Ek resmî kaynak:** [Teknik açıklama](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

## 13 — C

**Gerekçe:** Secret environment değeri instance başlangıcında çözülür. latest farklı başlangıçlarda farklı sürüm verebilir. Sayısal sürüm sabitleme, revision ile test edilmiş secret sürümünü eşler; eski sürüm kullanılabilir tutulduğu için rollback anlamlıdır.

**En yakın alternatif D:** latest dosya mount'u sürümü revision'a sabitlemez. Yeni image da latest referansının değişkenliğini gidermez.

**Belirleyici ifade:** “consistently” ve “rolling back must restore the previous release's secret version”.

**Alan:** 1.2 secret yönetimi; 1.1 rollout. **Ders ilişkisi:** R08-02; S01-01/02 ile karma. Rol ezberi veya tag URL tekrarı değildir.

**Ek resmî kaynak:** [Cloud Run secrets — environment ve volume davranışı](https://docs.cloud.google.com/run/docs/configuring/services/secrets).

## 14 — A

**Gerekçe:** Türetilen alan yazımı yeni update doğurur. Girdi alanı değişmemişse yazmadan dönmek kendi ürettiği olay zincirini keser; sonraki gerçek displayName değişiklikleri yine işlenir. Genel duplicate/out-of-order dayanıklılığı ayrı gereksinimdir.

**En yakın alternatif:** B döngüyü kesebilir ama gelecekteki isim düzenlemelerini işleme koşulunu bozar.

**Belirleyici ifade:** “continue handling future displayName edits”.

**Alan:** 3.1 Firestore trigger; 4.1 veri entegrasyonu. **Ders ilişkisi:** C04-03; S01-10 dedup yerine kendi yazımının tetiklediği döngü.

**Ek resmî kaynak:** [Teknik açıklama](https://docs.cloud.google.com/run/docs/triggering/trigger-functions-with-firestore-documents).

## 15 — B

**Gerekçe:** CPU utilization yüzdesi CPU request'e göre hesaplanır. Request eksikse yüzde hedefinin dayanağı yoktur; uygun request eklenmelidir.

**En yakın alternatif:** A payda eksikliğini çözmez. Max replicas artışı da ölçümü tanımlamaz.

**Belirleyici ifade:** “no CPU requests configured”.

**Alan:** 3.2 Horizontal Pod Autoscaler. **Ders ilişkisi:** GKE ek resmî kaynak; T08 dersinin ötesindeki HPA kararı açıkça etiketlendi.

**Ek resmî kaynak:** [Teknik açıklama](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/).

## Hazırlama ve değerlendirme notu

Bu sürüm kullanıcı talebiyle üç konuya eşit dağıtıldı; tek klasörden altı yeni soru kuralının yerine güncel istek uygulandı. Q6, Q8, Q13 ve Q14 eski konuları yeni servis/kararlarla birleştirir; diğer 11 soru önceki çözülmüş senaryo setlerinde ölçülmeyen kararları içerir. Zamanı gelmiş tekrar bu sürüme zorla eklenmedi. İlk taslak cevap alanları boşken güncellendi; kullanıcı cevabı veya puanı değiştirilmedi. Henüz çözülmedi.
