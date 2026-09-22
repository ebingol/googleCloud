# Nex Arc PCD kursu — örneklem incelemesi

20 Eylül 2026. Kullanıcının satın aldığı kurs, Safari/Udemy arayüzünden incelendi. Bu bir kullanıcı sınav denemesi değildir.

## Kapsam

Test 1 soru panelinde görünen ilk 100 soru kökü tarandı. Q1, Q2, Q8 ve Q29 seçenekleri ve tüm cevap açıklamaları okundu; asistan pratik modunda bu dört sorunun cevap kontrolünü yaptı. Test bitirilmedi/gönderilmedi. Bu etkinlik Udemy pratik ilerlemesinde görünebilir; kullanıcı puanı veya öğrenme ilerlemesi olarak sayılmayacak. Diğer beş test ve 1020 sorunun bütünü incelenmedi.

## Bulgular

- Test 1: 170 soru, exam mode 5 saat 40 dakika, %75 eşik. Resmî PCD: 50–60 soru, 2 saat. Tam sınav simülasyonu olarak biçim eşleşmiyor.
- Kurs tanıtım dağılımı %36/23/20/21; güncel resmî rehber %32/23/24/21. Tanıtımın kapsam dağılımı güncel değil; soru bankasının tamamının eski olduğunu kanıtlamaz.
- Yakın tekrar örnekleri (soru köklerinden): Q6/Q11 GKE Secrets CMEK, Q26/Q37 sıfır trafik ve revision test URL, Q47/Q48 immutable ConfigMaps, Q64/Q73 kubectl rollback. 1020 soruyu 1020 ayrı karar diye varsayma.
- Q1 Cloud SQL Auth Proxy sidecar ana cevabı Google önerisiyle uyumlu; her seçenek için gerekçe ve resmî kaynak URL metni var.
- Q2 Cloud Tasks iki retry sınırının AND koşulu, verilen pozitif değerlerle dokümanla uyumlu.
- Q8: gereksinim veri kaybına tolerans olmaması. Anahtar Standard Tier + read replicas + backoff diyor. HA ve okuma ölçekleme için uygun ama asenkron replikasyon nedeniyle sıfır veri kaybı garanti etmez. Sorunun gereksinimi ile çözümü çelişiyor; açıklama bunu belirtmiyor. Kendi kaynak gösterdiği doküman acknowledged writes kaybını açıkça anlatıyor.
- Q29 doğrudan Cloud Run IAP ve service agent Invoker yaklaşımı içeriyor; güncel özellik örneği. Görülen dört açıklamada seçenek bazında gerekçeler ve kaynak URL'leri mevcut.

## Kaynaklar

- https://cloud.google.com/learn/certification/cloud-developer
- https://cloud.google.com/learn/certification/guides/cloud-developer
- https://docs.cloud.google.com/sql/docs/mysql/connect-kubernetes-engine
- https://docs.cloud.google.com/tasks/docs/configuring-queues
- https://docs.cloud.google.com/memorystore/docs/redis/high-availability-for-memorystore-for-redis
- https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run

## Değerlendirme

Ek soru pratiği olarak kullanılabilir; tek başına sınava hazır oluş ölçütü veya hatasız cevap anahtarı olarak güvenilmemeli. Yakın tekrarlar ve en az bir gereksinim/çözüm çelişkisi var. Kullanıcıya soru cevaplarını gereksiz yere ifşa etmeden bulgular aktarılmalı.
