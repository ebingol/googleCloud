# Professional Cloud Developer kısa tekrar notu

Karar vermeden önce üç şeyi bul: **Ne isteniyor? Ne zaten sağlanmış? Hangi parça değişmeli?** Şıkları okurken seçeneğin hangi koşulu karşılamadığına bak.

## Kimlik ve erişim

**1. Build hesabı, runtime hesabı ve service agent**

Örnek: Pipeline image üretip registry’ye yüklüyor; çalışan uygulama Secret Manager’dan şifre okuyor. **Push izni build hesabına**, secret okuma izni **runtime hesabına** verilir. Service agent ise Google hizmetinin senin adına platform işlemleri yaptığı kimliktir; hata kaydında hangi principal reddedilmişse onu incele.

**2. Kimlik, izin ve token audience**

Örnek: Workflows özel Cloud Run servisini çağırıyor. Çağıran kimlikte **Invoker** izni ve hedefin beklediği **audience değerli OIDC ID token** gerekir. İzin doğruyken audience yanlışsa daha geniş rol vermek çözmez. WIF/ADC kimlik bilgisi edinmeyi sağlar; kaynak iznini otomatik vermez.

**3. IAM, RBAC ve şifreleme**

**IAM:** Google Cloud kaynağında izin; örneğin bucket’tan okuma. **RBAC:** Kubernetes API kaynaklarında izin; örneğin namespace içindeki Secret’ı okuma. **Şifreleme:** saklanan veriyi koruma. KMS şifrelemesi açık olsa da RBAC ile yetkilendirilmiş okuyucu Secret değerini API’den okuyabilir.

Rol örneği: Registry **Reader indirir**, **Writer yükleyebilir**. Workstations **User mevcut ortamı kullanır**; Admin yönetim yetkileri de verir. Rolü işi yapan kimliğe, gereken kapsamda ver.

## GKE

**4. Request ve limit**

Request, scheduler’ın yerleşim hesabındaki kaynak talebidir; limit kullanım sınırıdır. Başlangıçta 700 MiB gereken container’ın limiti 512 MiB ise node’da boş RAM olsa da OOMKilled olabilir. **Limiti uygun seviyeye yükselt; request’i ayrıca değerlendir.** Request’i mutlaka artırmak gerekmez; request limitten büyük olamaz. CPU limitine çarpma genellikle throttling, bellek limitini aşma OOM riski doğurur.

**5. Startup, readiness ve liveness**

- **Startup:** Başlangıç tamamlandı mı? Yavaş açılış sırasında readiness/liveness kontrollerini bekletir.
- **Readiness:** Şimdi trafik alabilir mi? Cache yenilenirken geçici başarısız olsun; süreç çalışmaya devam etsin.
- **Liveness:** Süreç toparlanamayacak biçimde takıldı mı? Yeniden başlatma gerekebilir.

Geçici veritabanı kesintisinde her Pod’u restart etmek sorunu büyütebilir; bağımlılık hatasını otomatik liveness hatası sayma.

**6. HPA, VPA, MPA, KEDA ve node ölçekleme**

| Araç | Örnek karar |
|---|---|
| HPA | Trafik arttı; 3 Pod yerine 8 Pod çalıştır. |
| VPA | Her Pod’un CPU/bellek request’ini ihtiyaca göre ayarla. |
| GKE MPA | CPU’ya göre replica sayısını, belleğe göre memory request’ini birlikte ayarla. |
| KEDA | Kuyrukta mesaj geldi; sıfır worker’dan etkin duruma geç, talebe göre ölçekle. |
| Cluster Autoscaler | Yerleşemeyen Pod’ların kaynak ihtiyacı için uygun koşullarda node ekle. |

CPU HPA hazır kaynak metriği kullandığı için az ek entegrasyon isteyebilir. İş yükünü CPU temsil etmiyorsa kuyruk uzunluğu gibi bir metrik daha uygun olabilir. KEDA sıfırdan aktivasyon için olay kaynağını izler, etkin ölçeklemede HPA ile çalışır.

**7. PDB ve rolling update**

Node drain sırasında 3 replica’dan en az 2’sini korumak: **PDB minAvailable: 2**. Uygulama sürümü değişirken 4 hazır replica’yı korumak: **maxUnavailable: 0, maxSurge: 1**. Önce beşinci Pod oluşur, hazır olunca bir eski kaldırılır. Cluster’da ek kapasite yoksa yeni Pod Pending kalıp rollout bekleyebilir. Surge/unavailable ikisi birden sıfır olamaz; PDB rollout ayarının yerine geçmez.

**8. Service selector ve HTTP yönlendirme**

Service selector, hangi Pod’lara gidileceğini belirler. `app=checkout` arayan Service, yalnız `app=checkout-api` etiketi taşıyan Pod’ları bulmaz. HTTPRoute/load balancer ise `/students` ve `/teachers` yollarını ayrı backend’lere eşler. Ayrı fonksiyonların kendi URL’lerine doğrudan erişmek için ayrıca load balancer şart değildir; ortak domain altında ayrı backend’lere yönlendirme için bir routing katmanı gerekir.

## Build ve deployment

**9. Queue, build ve step timeout**

**queueTtl:** başlamadan kuyrukta bekleme. **Build timeout:** çalışan bütün build’in bütçesi. **Step timeout:** bir adımın sınırı. Toplam sınır 20 dakika iken teste 40 dakika vermek build’i uzatmaz. Toplam 35 dakikalık iş için build bütçesini örneğin 40 dakika yap; step süreleri toplam bütçeyi aşamaz ve her adımda build saati sıfırlanmaz.

**10. Paralellik, veri paylaşımı ve cleanup**

İki test hemen başlasın: ikisine `waitFor: ["-"]`. Paketleme ikisini beklesin: `waitFor: ["unit", "integration"]`. **waitFor, başarısız adımdan sonra mutlaka çalıştır anlamına gelmez.**

`/workspace` dosyaları aynı build’in adımları arasında paylaşılır; build sonrasında kalıcı arşiv değildir. Raporu sonra okumak için örneğin Cloud Storage’a artifact olarak çıkar. Geçici test fonksiyonunu hata halinde de temizleme örneği: sonucu dosyaya kaydet → cleanup yap → kaydedilen sonucu değerlendirip gerekirse build’i başarısız bitir.

**11. Retry sayısı ve toplam süre**

Kubernetes Job’da **backoffLimit** başarısızlık/retry bütçesi; **activeDeadlineSeconds** toplam aktif süre sınırıdır. Sürekli hata veren işi retry bütçesi, hiç bitmeyen işi süre sınırı durdurabilir. `restartPolicy: Never`, aynı Pod içindeki restart’ı kapatır; Job controller’ın yeni Pod oluşturmasını engellemez.

**12. Provenance ve rollout işlemleri**

Provenance, image’ın build kökeni hakkında kayıttır; elle eklenen commit label aynı kanıt değildir. Cloud Build’de uygun build için `images` ve `options.requestedVerifyOption: VERIFIED` kullanılır. Binary Authorization kanıtı değerlendirir; eksik provenance’ı üretmez. Provenance, testlerin geçtiği veya image’ın zafiyetsiz olduğu garantisi değildir.

**Advance:** aynı rollout’ta %10 → %50 gibi sonraki canary aşaması. **Promote:** release’i sıradaki target’a taşıma. **Rollback:** önceki sürüme dönüş. Üç revision oluşturmak tek başına kullanıcıları dağıtmaz; traffic splitting de yapılandırılmalı.

## Veri ve olaylar

**13. Firestore transaction, batch ve emulator**

“Bakiye yeterliyse aktar”: okumaya göre karar var → **transaction**. “Önceden belirlenmiş 200 fiyatı hep birlikte yaz”: okuma kararı yok → **batched write**. `Promise.all` bağımsız yazmaları atomik yapmaz. Emulator işlev ve Security Rules testinde kullanılır; gerçek hizmetin performans/ölçek ölçümünün yerine geçmez. Rules testi için Admin SDK kullanma; istemci kurallarını bypass eder.

**14. Retention, versioning ve lifecycle**

“7 yıl silinmesin” → **retention policy**. “Eski sürümler de tutulsun” → **versioning**. “3 yıl sonra Archive’a geçsin” → **lifecycle**. Versioning tek başına yedi yıllık silinmeme garantisi vermez. Retention süresinin dolması da kendi başına nesneyi silmez; silme işlemi/kuralı gerekir.

**15. Pub/Sub tüketimi, trigger ve tekrar işleme**

İki worker aynı işi paylaşacak → **aynı subscription**. Billing ve audit her mesajı ayrı ayrı alacak → **ayrı subscription’lar**. ACK/retry durumları bağımsızdır; iki hedefe atomik yazım sağlamaz. Pub/Sub tetiklemeli fonksiyonda mesaj event içinde gelir; ayrıca yeni subscription oluşturup pull yapmak gerekmez.

İş yapıldı, cevap ağda kayboldu: aynı mesaj/istek tekrar gelebilir. **Idempotency**, tekrarın aynı iş etkisini çoğaltmamasıdır. Cloud Tasks’ta başarıyla tamamlanan iş için **2xx** dön; **429 başarı değildir**. Deterministik task ID, desteklenen pencere içinde task oluşturmayı tekilleştirmeye yardım eder; handler’ın tekrar çalışmaya dayanıklılığının yerine geçmez.

## Hızlı okuma kontrolü

**Already:** zaten sağlanmış; aynı şeyi tekrar kurma. **Only:** kapsamı sınırla. **Without:** yasaklanan değişikliği ele. **Least effort:** şartları sağlayan seçenekler içinde daha az ek iş isteyeni seç. **Choose two:** iki koşulu da karşılayan tam kümeyi bul.

Her nottan sonra şu cümleyi tamamla: **“Bunu seçerim, çünkü …; diğer seçenek … şartını karşılamıyor.”**

## Resmî kaynaklar

- [Kimlik ve Cloud Run çağrıları](https://docs.cloud.google.com/run/docs/authenticating/service-to-service), [Kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [Request ve limit](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/), [probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/), [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/), [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
- [GKE MPA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multidimensional-pod-autoscaling), [KEDA](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scale-to-zero-using-keda)
- [Cloud Build yapılandırması](https://docs.cloud.google.com/build/docs/build-config-file-schema), [canary aşamaları](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary/cloud-run)
- [Firestore transaction ve batch](https://firebase.google.com/docs/firestore/manage-data/transactions), [retention](https://docs.cloud.google.com/storage/docs/bucket-lock), [Pub/Sub modeli](https://docs.cloud.google.com/pubsub/docs/pubsub-basics)
