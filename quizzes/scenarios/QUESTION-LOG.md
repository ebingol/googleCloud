# Senaryo soru geçmişi

Bu dosya soru üretiminde tekrar kontrolü içindir; cevap ipuçları içerir. Öğrenci yeni seti çözerken açmamalı. Yeni set hazırlandığında satırları ekle; sadece planlanan soru çözülmüş sayılmaz.

| ID | Ölçülen karar / belirleyici koşul | Tür / benzerlik | İlk sonuç |
|---|---|---|---|
| S01-01 | Tek secret payload, runtime identity, secret kapsamı | İlk tanılama | Yanlış |
| S01-02 | %5 rollout ve rollback, minimum ek altyapı | İlk tanılama | Doğru |
| S01-03 | Sıralı build'de özel /tmp çıktısı kayıp, ortak workspace | İlk tanılama | Yanlış |
| S01-04 | Google kimliği olmayan müşteriye tek nesne, geçici signed URL | İlk tanılama | Doğru |
| S01-05 | Gelecekte HTTP gönderimi ve dispatch limiti, Cloud Tasks | İlk tanılama | Doğru |
| S01-06 | A→B: B üzerinde A'ya Invoker ve B audience'lı ID token | İlk tanılama | Yanlış |
| S01-07 | Eşzamanlı shared-state bozulması, sequential güvenli, concurrency 1 | İlk tanılama | Yanlış; dil güçlüğü |
| S01-08 | Dockerfile yok, desteklenen uygulama, buildpacks | İlk tanılama | Doğru |
| S01-09 | Son koltuk rezervasyonu, read/check/write atomik transaction | İlk tanılama | Doğru |
| S01-10 | Eventarc tekrarlı event, kalıcı atomik dedup ve güncelleme | İlk tanılama | Doğru |
| S01-11 | Local ADC ile gcloud login ayrımı, runtime SA | İlk tanılama | Doğru |
| S01-12 | Idle sonrası initialization gecikmesi, min instances | İlk tanılama | Doğru |
| S01-13 | allowFailure test hatasını yutuyor, deployment gate | İlk tanılama | Doğru |
| S01-14 | Global ilişkisel transaction + yatay write ölçeği, Spanner | İlk tanılama | Doğru |
| S01-15 | Sıralı dallanan süreç, uzun callback, Workflows | İlk tanılama | Doğru |
| R01-01 | Tek secret metadata, payload yasak, Viewer | Hedefli tekrar; S01-01'in gereksinimi ters | Doğru |
| R01-02 | Çıktı workspace'te, test yanlış /tmp yolunu okuyor | Hedefli tekrar; S01-03'e yakın | Doğru; gerekçe zayıf |
| R01-03 | orders→pricing rol + token birlikte | Hedefli yakın tekrar; S01-06 | Doğru |
| R01-04 | Process-wide buffer çakışıyor, concurrency 1 | Hedefli yakın tekrar; S01-07 | Doğru |
| R01-05 | Invoker mevcut; ID token audience çağıranı gösteriyor | Hedefli tanılama; S01-06'nın tek hata ayrımı | Yanlış; sonra sözlü doğru |

Tam metinler: [S01](PCD-S01.md), [R01](PCD-R01.md). Anahtarlar `../answers/scenarios/` altında. Sonuçlar `results/` altında.

## Rehberli görülen ek kararlar

- R10-04: revision tag URL, green URL öneki, trafik yüzdesi, in-flight requests, best-effort session affinity. 20 Eylül birlikte çözüldü; D/B/D/C/C, 4/5.
- R01-01 Q2: image + configuration revision'ı tanımlar. Çeviriyle doğru cevap açıklandı; bağımsız sonuç yok.
- F06-03 Q1/Q3: kernel paylaşımı; her build step'in container içinde çalışması. Açıklandı; bağımsız sonuç yok.
- Sözlü checkout→inventory: Invoker yönü ve audience doğru; R01-05 sonrası anlık kontrol. Yeni bağımsız sınav sayılmaz.

Yeni soru eklerken format: `ID | konu/karar/belirleyici koşul | yeni/karma/gecikmeli tekrar + benzer ID | henüz çözülmedi`. Eski sorulara yakınlığı yalnız anahtar kelimelerle değil çözüm mantığıyla değerlendir.

## PCD-S02 — 22 Eylül 2026, düzeltilmiş kapsam

[Sorular](PCD-S02.md) · [Anahtar](../answers/scenarios/PCD-S02.md). Kullanıcı Cloud Run, Cloud Run functions ve GKE sorularını tamamladığını bildirdi ve sınavı bu alanlardan istedi. 5 + 5 + 5 dağılımı kullanıldı. 11 yeni + 4 karma; bu sürümde gecikmeli tekrar yok.

İlk Cloud Run ağırlıklı taslak kullanıcı cevabı yokken değiştirildi; eski S02 soru numaraları geçersizdir. İlk taslakta görülen beş Cloud Run sorusu korunup yeni sıraya taşındı (eski 1→1, 3→4, 4→7, 11→10, 12→13); bunları S03'te hiç görülmemiş soru diye sunma. Çıkarılan taslak kararları: Error Reporting, Artifact Registry service agent, idle CPU, Eventarc parser, Direct VPC, Trace, job exit/retry, SIGTERM, push ack, env önceliği. Bunlar hazırlanmıştı ama kullanıcı çözümü yok; yeniden kullanılırsa bu geçmiş belirtilmeli.

| ID | Konu / ölçülen karar / belirleyici koşul | Tür / benzerlik | İlk sonuç |
|---|---|---|---|
| S02-01 | Cloud Run service/job; 80 dakika, HTTP yok, bitince çıkış | Yeni; R01-02, eski senaryoda yok | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-02 | Functions HTTP webhook; aynı istekte doğrulama yanıtı | Yeni; C01-02, S01 event koordinasyonundan farklı | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-03 | GKE Service selector yanlış; Ready Pod etiketleriyle eşleştirme | Yeni; T08-03 | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-04 | Cloud Run port açık ama initialization bitmemiş; HTTP startup | Yeni; S01-12 min instances kararından farklı | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-05 | Functions /tmp dosyaları birikiyor; hata dahil cleanup | Yeni; C05-01 | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-06 | GKE v2 rollout; tek Pod yerine Deployment template güncelleme | Karma; S01-02 rollout + T08-02 controller | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-07 | Cloud Run/Cloud SQL; process havuzu ve bağlantı iadesi | Yeni; R11-03, transaction ölçmüyor | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-08 | Functions; geçersiz olay kalıcı kaydı ve transient retry ayrımı | Karma; S01-10 event güvenilirliği + C05-04 | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-09 | GKE emptyDir kaybı; retained PVC ile Pod replacement | Yeni; T08-04 | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-10 | Cloud Run dış LB girişi, direct internet engeli; IAM korunacak | Yeni; S01-06 token kararından farklı ağ katmanı | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-11 | Functions; mevcut kayıtlı handler ile entry point uyuşmazlığı | Yeni senaryo; C01-05 kaynakları 21 Eylülde konuşuldu, bağımsız puan yok | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-12 | GKE geçici dependency kaybı; restart gerekmiyor, readiness | Yeni; T08-03 ilişkili, probe ayrıntısı ek resmî kaynak | Yanlış (kullanıcı beyanı); probe kavram eksikliği bildirildi, seçilen şık bilinmiyor |
| S02-13 | Cloud Run secret env; sürüm sabitleme ve rollback | Karma; S01-01 secret + S01-02 rollout | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-14 | Functions Firestore update; girdi değişmediyse yazmadan dön | Karma; C04-03 + S01-10 olay güvenilirliği, dedup ezberi değil | Doğru (kullanıcı beyanı); şık kaydı yok |
| S02-15 | GKE HPA CPU utilization; CPU request eksik | Yeni; HPA ek resmî kaynak | Doğru (kullanıcı beyanı); şık kaydı yok |

22 Eylül sonuç güncellemesi: 14/15, 20 dakika; kaynak kullanıcı beyanı. Soru dosyası cevapları boş, anahtar kullanıcı cevabı olarak aktarılmadı. Q12 açıklaması ilk sonucu değiştirmez.

## PCD-S03 — 23 Eylül 2026

[Sorular](PCD-S03.md) · [Anahtar](../answers/scenarios/PCD-S03.md). 5 Cloud Run + 5 Functions + 5 GKE; 9 yeni karar + 4 karma + 2 gecikmeli uygulama. Uzun İngilizce senaryolar ve koşullara göre alternatif eleme korundu. Kaynaklar güncel resmî web belgeleri; anahtarda ek kaynak etiketi var. Yeni karar etiketi hiç görülmemiş tüm kavramlar anlamına gelmez.

| ID | Konu / ölçülen karar / belirleyici koşul | Tür / benzerlik | İlk sonuç |
|---|---|---|---|
| S03-01 | GKE ConfigMap; subPath güncellenmez, restart olmadan dosya projection ve yeniden okuma | Yeni; S02-06 rollout yerine canlı dosya yenilemesi | Yanlış; kullanıcı D, anahtar B |
| S03-02 | Cloud Run candidate tag destination ile normal service audience ayrımı; Invoker hazır | Gecikmeli tekrar; R01-05 + rehberli R10-04, yeni birleşik uygulama | Yanlış; kullanıcı C, anahtar D |
| S03-03 | Functions upload Promise tamamlanmadan handler dönüşü; sonucu Promise ile bağlama | Yeni; C05-01; S02-08 hata sınıflamasından farklı completion kararı | Yanlış; kullanıcı C, anahtar A |
| S03-04 | GKE dedicated KSA ve bucket üzerinde direct federated principal grant birlikte | Karma; S01-11 ADC/identity + GKE WIF | Eksik seçim; kullanıcı D, anahtar C, D |
| S03-05 | Functions gecikmiş Storage event; saklanan generation ile doğru input bytes seçme | Yeni; S01-10 dedup sorusundan farklı, dedup zaten sağlanmış | Yanlış; kullanıcı C, anahtar B |
| S03-06 | Cloud Run proxy ingress bind 0.0.0.0 ve aynı instance localhost sidecar | Yeni; R09-01 runtime contract genişletmesi | Yanlış; kullanıcı B, anahtar C |
| S03-07 | GKE voluntary eviction; 3 sağlıklı Pod, minAvailable 2; rollout ayarı yeterli değil | Yeni; S02-06 rollout mekanizmasından farklı eviction bütçesi | Yanlış; kullanıcı C, anahtar A |
| S03-08 | Cloud Run tek CPU hotspot; çok vCPU ortalaması ve concurrency ile request scaling | Gecikmeli uygulama; R01-04/S01-07 concurrency, yeni performans bağlamı | Yanlış; kullanıcı A, anahtar D |
| S03-09 | Functions sıra dışı Firestore snapshots; sürüm karşılaştırma ve atomik summary update | Karma; S01-09 transaction + S01-10 event; S02-14 self-loop kararından farklı | Doğru; kullanıcı C, anahtar C |
| S03-10 | GKE NetworkPolicy; source egress ve destination ingress izinleri birlikte | Karma; S02-10 ağ erişim katmanı + Pod selector, yeni GKE mekanizması | Doğru; kullanıcı A, B, anahtar A, B |
| S03-11 | Cloud Run 504 işlemi iptal/rollback etmez; retry öncesi sonuç belirsizliği | Yeni timeout teşhisi; S01-10 idempotency ile ilişkili, yalnız dedup tasarımı sorulmuyor | Doğru; kullanıcı B, anahtar B |
| S03-12 | Functions source build denied principal; builder/runtime ayrımı ve prod-data sınırı | Karma; S01-01 runtime kimlik + C01-06 build | Doğru; kullanıcı D, anahtar D |
| S03-13 | GKE Pending CPU; gerçek kullanım değil requests, tek node kapasitesi | Yeni; S02-15 HPA utilization değil scheduler kapasitesi | Doğru; kullanıcı A, anahtar A |
| S03-14 | Functions Pub/Sub CloudEvent adapter testi; zarf/base64/business JSON ayrımı | Yeni ölçülen adapter test kararı; S02 çıkarılan parser taslağıyla ilişkili, hiç görülmemiş konu iddiası yok | Doğru; kullanıcı C, anahtar C |
| S03-15 | Cloud Run public API static egress; private-ranges-only mevcut NAT yolunu atlıyor | Yeni ölçülen egress karar; S02 çıkarılan Direct VPC taslağıyla ilişkili | Doğru; kullanıcı B, anahtar B |

23 Eylül: Q2 C (anahtar D), Q8 A (anahtar D); yeni uygulamalarda tam doğru yok. Q2’de audience parçası doğru, tag hedeflemesi eksik; önceki tüm bilgiyi unuttuğu çıkarılamaz. Probe tekrarı 25 Eylül; workspace ve diğer bekleyen kararlar çözülmüş sayılmadı.

S03 ilk cevaplar: 7/15 (%46,7), süre bildirilmedi. [Sonuç](results/PCD-S03-attempt-01.md). Kullanıcı soyutlama/eşleştirme güçlüğü bildirdi; hata nedenleri rehberli ayrıştırılacak.

23 Eylül S03 Q1–Q8 tekrar: 1 B, 2 B, 3 A, 4 A+D, 5 D, 6 A, 7 D, 8 A → 2/8 (Q1/Q3 doğru). İlk sonuç sütunları korunur. [Ayrı kayıt](results/PCD-S03-retry-01.md). Gerekçe ve gecikmeli kalıcılık doğrulanmadı.

## PCD-S04 — 24 Eylül 2026

[Sorular](PCD-S04.md) · [Anahtar](../answers/scenarios/PCD-S04.md). Kullanıcının tüm konulardan 20 soru talebi, eski 15 soru/5+5+5 dağılımının önüne geçti. Dört ana alan 6/5/5/4; bütün alt maddeleri ölçme iddiası yok. 13 yeni karar + 6 karma + 1 erken pekiştirme. Yeni etiketi eski ders quizlerinde kavramın hiç bulunmadığı anlamına gelmez. Kaynaklar ek resmî web belgeleri. S01/S02/S03 tam metinleri ve S03 sonuçları kontrol edildi; puanlar korunur.

| ID | Konu / ölçülen karar / belirleyici koşul | Tür / benzerlik | İlk sonuç |
|---|---|---|---|
| S04-01 | Bigtable timestamp hotspot; dengeli device prefix + zaman aralığı | Yeni; F03-02/U04-06 ile ders bağlantısı | Henüz çözülmedi |
| S04-02 | Cloud Build iki bağımsız check compile sonrası; package ikisini bekler | Karma; S01-03 workspace zaten işler, S01-13 failure flag değil DAG | Henüz çözülmedi |
| S04-03 | Test edilen digest ile gcloud deploy; mutable tag race ve rebuild yasak | Yeni karar; S02-06 image rollout değil artifact kimliği | Henüz çözülmedi |
| S04-04 | Pub/Sub her takıma tüm event; bağımsız subscription ve grup içi load sharing | Yeni; S01-10 duplicate kararından farklı fan-out | Henüz çözülmedi |
| S04-05 | Cloud SQL regional HA; synchronous zonal failover, schema korunacak | Yeni; S01-14 global Spanner scale kararı değil | Henüz çözülmedi |
| S04-06 | Firestore server emulator env; yerel endpoint ve production parity sınırı | Yeni; F02-03 emulator ders bağlantısı | Henüz çözülmedi |
| S04-07 | GKE rollout dört available, bir surge; maxUnavailable 0 / surge 1 | Karma; S02-06 rollout + S03-07 eviction ayrımı | Henüz çözülmedi |
| S04-08 | Storage create-only upload; generationMatch 0 ve uncertain response doğrulama | Karma; S03-05 generation okuma yerine atomic create, S03-11 uncertain result | Henüz çözülmedi |
| S04-09 | Apigee partner interval quota; burst policy zaten var | Yeni; F01-04 genel gateway'den ayrıntı | Henüz çözülmedi |
| S04-10 | Gemini test generation; contract oracle, time/API kontrolü, boundary tests | Yeni; AI destekli test değerlendirmesi | Henüz çözülmedi |
| S04-11 | Eventarc Storage finalized + doğru bucket; metadata event ayrımı | Yeni; S03-14 payload parser değil trigger filter | Henüz çözülmedi |
| S04-12 | Servisler arası trace context propagation ve span parent | Yeni ölçülen karar; S02 çıkarılmış Trace taslağıyla konu ilişkisi | Henüz çözülmedi |
| S04-13 | External CI WIF; repo claim restriction + repository IAM | Karma; S03-04 GKE KSA yerine external OIDC trust boundary | Henüz çözülmedi |
| S04-14 | Test onayı digest attestation; Binary Authorization admission gate | Yeni; S01-13 pipeline failure gate yerine cluster enforcement | Henüz çözülmedi |
| S04-15 | Cloud Run idle CPU, disposable refresh; min instance zaten var, billing değişimi | Yeni ölçülen karar; S02 çıkarılan idle CPU taslağı, S01-12 cold start değil | Henüz çözülmedi |
| S04-16 | Firestore retried callback dış ödeme; durable pending record + provider key | Karma; S01-09/10 atomik dedup'tan dış sistem crash penceresine genişleme | Henüz çözülmedi |
| S04-17 | Storage retention lock; admin süreyi azaltamamalı | Yeni; U04-01 lifecycle/versioning ayrımı | Henüz çözülmedi |
| S04-18 | Build secret; build identity specific secret + availableSecrets/secretEnv | Karma; S01-01 runtime secret + S03-12 build identity, yeni injection kararı | Henüz çözülmedi |
| S04-19 | GKE startup liveness'ı bekletir; steady deadlock hızını koruma | Erken pekiştirme; S02-12 ve 22 Eylül probe açıklaması, 25 Eylül kontrolünden erken | Henüz çözülmedi |
| S04-20 | Compute Engine compatible custom OS/kernel ve container yasağı | Yeni; S02-01 Run job değil host OS gereksinimi | Henüz çözülmedi |

Probe, workspace veya diğer tekrar kuyruğu yalnız soru hazırlandı diye tamamlanmadı. S04 sonucu yok; yeni set ID'si S05.


## PCD-S05 — 25 Eylül 2026

[Sorular](PCD-S05.md) · [Anahtar](../answers/scenarios/PCD-S05.md). Kullanıcı uzun paragraflı yeni S05 istedi. 20 soru; 18 tek + 2 çift seçim (Q16/Q18); 50 dakika kişisel hedef. Dört ana alan 6/5/5/4; 10 yeni ölçüm + 9 karma + 1 pekiştirme. Yeni ölçüm, daha önce hiç açıklama yapılmadığı anlamına gelmez. S04 değiştirilmedi; iki set için de sonuç yok. Airflow ek ürün kapsamı, Vision genel API performansı uygulamasıdır.

| ID | Konu / ölçülen karar | Tür / benzerlik | İlk sonuç |
|---|---|---|---|
| S05-01 | Memorystore cache-aside, tenant key ve kontrollü fallback | Yeni; S01-07 process shared-state hatası yerine dağıtık cache tasarımı | Doğru |
| S05-02 | Cloud Workstations servis seçimi ve merkezi ortam | Yeni | Doğru |
| S05-03 | Canary ortak şema, expand-contract ve rollback | Karma; S01-02 rollout ve rehberli R10-04 traffic migration üzerine veri uyumluluğu, eski sorunun aynısı değil | Yanlış; kullanıcı A, anahtar D |
| S05-04 | Vision API offline batching/LRO ve kısmi retry | Yeni ölçüm; 25 Eylül konuşmasında async/sync ayrımı açıklandı | Doğru |
| S05-05 | Memorystore HA ile durability ayrımı | Karma; S04-05 Cloud SQL HA bilgisini Redis’e yanlış genellememe | Doğru |
| S05-06 | Workstations persistent home ve image toolchain | Yeni; Q2 servis seçiminden farklı yaşam döngüsü kararı | Doğru |
| S05-07 | GKE HPA external backlog vs CPU/node scaling | Karma; S02-15 HPA kaynak koşullarından farklı talep metriği | Doğru |
| S05-08 | BigQuery pagination token ve streaming tüketim | Yeni | Doğru |
| S05-09 | Spanner exact timestamp vs relative staleness | Yeni ölçüm; Gemini rehberindeki staleness konusu konuşuldu | Doğru |
| S05-10 | Gemini Code Assist bağlam ve pinned API doğrulama | Karma; S04-10 test oracle yerine implementation context | Doğru |
| S05-11 | Cloud Run secret volume latest vs startup env | Karma; S02 pinned secret/rollback yerine canlı rotation gereksinimi | Doğru |
| S05-12 | Spanner Query Stats vs tracing teşhis katmanı | Karma; S04-12 propagation tamam, Gemini metninde bu ayrım görüldü | Doğru |
| S05-13 | Airflow mevcut DAG migration vs Workflows | Yeni; S01-15 yeni workflow callback tasarımından farklı migration | Doğru |
| S05-14 | Gemini Code Assist vs Cloud Assist ürün rolü | Yeni ölçüm; 25 Eylül konuşmasında ürün ayrımı açıklandı | Doğru |
| S05-15 | GKE preStop + SIGTERM ortak termination bütçesi | Karma; S03-07 PDB ve S02 çıkarılmış SIGTERM taslağı, yeni hook bütçesi | Yanlış; kullanıcı B, anahtar D |
| S05-16 | API retry jitter, deadline ve layered retry | Karma; S03-11/S04-08 uncertain write yerine idempotent GET retry orchestration | Doğru |
| S05-17 | Storage Autoclass erişim paterni vs age lifecycle | Yeni; S04-17 retention kararından farklı maliyet/erişim tasarımı | Doğru |
| S05-18 | Cloud Build Docker layer ordering ve remote cache | Yeni; S04-02 step DAG ve S04-03 artifact kimliğinden farklı cache kararı | Yanlış; kullanıcı B, D, anahtar C, D |
| S05-19 | API Gateway backend identity ve service-level Invoker | Pekiştirme; S01-06/R01-03 invoker yönü gateway üzerinde, yeni temel karar sayılmaz | Doğru |
| S05-20 | IAM inherited allow daraltma ve bucket scope | Karma; S01-01 secret least privilege üzerine inherited izin kaldırma | Doğru |

Yalnız hazırlık tamamlandı; tekrar kuyruğunda başarı/kalıcılık teyidi yok. Sonraki yeni set S06.

25 Eylül S05 ilk cevaplar: **17/20 (%85), 70–80 dakika**. [Kayıt](results/PCD-S05-attempt-01.md). Q3/Q15/Q18 yanlış; ilk seçimler korundu. Gerekçe/güven ve bağımsız koşullar bilinmiyor. Açıklama sonrası kalıcılık teyidi yok.


## PCD-S06 — 25 Eylül 2026

[Sorular](PCD-S06.md) · [Anahtar](../answers/scenarios/PCD-S06.md). Kullanıcı daha uzun paragraflar, daha çetrefilli şıklar ve öncelikli dayanak olarak exam guide istedi. 20 soru; 18 tek + Q6/Q18 çift seçim. Birincil alan örneklemi 6/5/5/4; 11 yeni ölçüm + 9 karma, gecikmeli tekrar yok. Yeni ölçüm, kavramın ders bankasında/konuşmada hiç görülmediği anlamına gelmez. S05 Q3/Q15/Q18 anlık açıklamaları isim değiştirilerek tekrarlanmadı.

| ID | Konu / ölçülen karar | Tür / benzerlik | İlk sonuç |
|---|---|---|---|
| S06-01 | Cloud Tasks schedule/rate/concurrency seçimi | Yeni; S01-15 callback workflow yerine zamanlanmış tek hedef dispatch | Henüz çözülmedi |
| S06-02 | ADC credential-source precedence ve IDE environment | Karma; S01-11 CLI/ADC ayrımına environment precedence ekleniyor | Henüz çözülmedi |
| S06-03 | Cloud Run cross-project image pull kimliği | Karma; S03-12 builder/runtime ayrımına platform service agent ekleniyor; S02 çıkarılmış taslakta konu vardı | Henüz çözülmedi |
| S06-04 | Pub/Sub ordering scope ve regional publishing | Yeni ölçüm; Gemini setinde ordering bölgesellik konusu incelendi; S04-04 fan-out değil | Henüz çözülmedi |
| S06-05 | Storage signed GET URL kapsam ve expiry | Yeni; S03-05 object generation ve Gemini POST policy konuşmasından farklı download yetkisi | Henüz çözülmedi |
| S06-06 | AI IDE/MCP tool yüzeyi ve credential sınırı | Yeni; S05-10 context seçimi yerine MCP execution permissions | Henüz çözülmedi |
| S06-07 | GKE memory request/limit ve OOM teşhisi | Karma; S03-13 CPU scheduling üzerine per-container memory failure | Henüz çözülmedi |
| S06-08 | Cloud SQL Auth Proxy ile private network reachability | Karma; S02-07 connection pool değil ağ önkoşulu; Gemini private-pool topoloji incelemesiyle ilişkili | Henüz çözülmedi |
| S06-09 | Bigtable replicated instance app-profile consistency | Yeni; S04-01 row-key hotspot değil replicated routing; S05-09 Spanner snapshot’tan farklı | Henüz çözülmedi |
| S06-10 | Cloud Build integration-test isolation ve failure preservation | Karma; S01-13 gate ve S04-02 dependency sırasına eşzamanlı test isolation ekleniyor | Henüz çözülmedi |
| S06-11 | Apigee API contract versioning ve backend routing | Yeni; S04-09 quota parametresi değil birlikte yaşayan API contract | Henüz çözülmedi |
| S06-12 | Observability metric cardinality ve structured logs | Yeni; S04-12 trace propagation/S05-12 Query Stats yerine label tasarımı | Henüz çözülmedi |
| S06-13 | KMS rotation ile eski ciphertext migration ayrımı | Yeni; S05-11 secret rotation yerine encryption-key lifecycle | Henüz çözülmedi |
| S06-14 | Cloud Build provenance output ve verification gate | Karma; S04-14 admission attestation yerine builder provenance üretimi | Henüz çözülmedi |
| S06-15 | Cloud Run HTTP/2 h2c ve TLS termination | Yeni; S03-06 bind/sidecar port yerine transport protocol sınırı | Henüz çözülmedi |
| S06-16 | BigQuery Storage Write API pending streams atomic commit | Yeni; S05-08 result pagination değil batch write visibility | Henüz çözülmedi |
| S06-17 | Storage lifecycle Delete ile retention birleşimi | Karma; S04-17 lock ve S05-17 Autoclass yerine retention/deletion etkileşimi | Henüz çözülmedi |
| S06-18 | Artifact Analysis bulgusundan rebuild ve verified rollout | Karma; S04-03 digest kimliği yeni vulnerability-remediation bağlamında; S05-18 layer cache tekrarı değil | Henüz çözülmedi |
| S06-19 | GKE regular init container ve shared emptyDir | Karma; S02-04 startup ve S02-09 volume lifetime üzerine process-start dependency; aynı probe sorusu değil | Henüz çözülmedi |
| S06-20 | Firestore index exemptions ve write fanout | Yeni; S04-06 emulator/S04-16 transaction değil schema-index tasarımı | Henüz çözülmedi |

S06 yalnız hazırlandı; yeni kullanıcı yanıtı/süre/puan yok. Sonraki yeni set S07.
