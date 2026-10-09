# PCD-S13 — İlk gönderilen 50 cevap

9 Ekim 2026. Kullanıcı açıkça S13 için **112 dakika** ve 50 cevap bildirdi.

Ham gönderim:

```text
1-d,2-c,3-b,4-c,5-a,
6-d,7-c,8-b,9-b,10-b,
11-a,12-b,13-a,14-d,15-b,
16-b,17-d,18-a,19-b,20-c,
21-a,22-ab,23-a,24-b,25-a,
26-c,27-c,28-a,29-d,30-d,
31-a,32-d,33-a,34-d,35-c,
36-c,37-c,38-c,39-ad,40-d,
41-de,42-b,43-b,44-d,45-c,
46-b,47-c,48-d,49-a,50-a,
```

Mevcut anahtar tablosu ve 50 soru başlığı birbirleriyle eşleştirilerek puanlandı: **29/50 (%58)**. Yanlış sayısı **21**. Q22 A+B→A+C yanlış; Q39 A+D ve Q41 D+E doğru. Çift seçimde tam doğru küme 1 puan, kısmi puan yok.

120 dakikalık kişisel hedefin 8 dakika altında; ortalama 2 dakika 14,4 saniye/soru. Mola/yardım/kaynak kullanımı, güven/gerekçe bildirilmedi; kesintisiz yardımsız deneme veya hata nedeni varsayılmaz. Kullanıcının önceki konsantrasyon geri bildirimi korunur; bu denemenin yanlışlarına otomatik neden atanmaz.

| Soru | İlk cevap | Anahtar | Sonuç |
|---|---|---|---|
| 1 | D | C | Yanlış |
| 2 | C | A | Yanlış |
| 3 | B | B | Doğru |
| 4 | C | C | Doğru |
| 5 | A | A | Doğru |
| 6 | D | D | Doğru |
| 7 | C | D | Yanlış |
| 8 | B | A | Yanlış |
| 9 | B | B | Doğru |
| 10 | B | C | Yanlış |
| 11 | A | B | Yanlış |
| 12 | B | D | Yanlış |
| 13 | A | A | Doğru |
| 14 | D | B | Yanlış |
| 15 | B | B | Doğru |
| 16 | B | A | Yanlış |
| 17 | D | D | Doğru |
| 18 | A | A | Doğru |
| 19 | B | C | Yanlış |
| 20 | C | C | Doğru |
| 21 | A | B | Yanlış |
| 22 | A+B | A+C | Yanlış |
| 23 | A | B | Yanlış |
| 24 | B | B | Doğru |
| 25 | A | A | Doğru |
| 26 | C | C | Doğru |
| 27 | C | C | Doğru |
| 28 | A | A | Doğru |
| 29 | D | D | Doğru |
| 30 | D | D | Doğru |
| 31 | A | A | Doğru |
| 32 | D | D | Doğru |
| 33 | A | A | Doğru |
| 34 | D | A | Yanlış |
| 35 | C | D | Yanlış |
| 36 | C | C | Doğru |
| 37 | C | C | Doğru |
| 38 | C | C | Doğru |
| 39 | A+D | A+D | Doğru |
| 40 | D | A | Yanlış |
| 41 | D+E | D+E | Doğru |
| 42 | B | B | Doğru |
| 43 | B | B | Doğru |
| 44 | D | D | Doğru |
| 45 | C | B | Yanlış |
| 46 | B | C | Yanlış |
| 47 | C | D | Yanlış |
| 48 | D | D | Doğru |
| 49 | A | C | Yanlış |
| 50 | A | B | Yanlış |

## Birincil alan örneklemi

| Alan | Doğru / toplam |
|---|---|
| Tasarım | 11/16 |
| Geliştirme/test | 8/12 |
| Deployment | 3/12 |
| Entegrasyon | 7/10 |

Bu dağılım yalnız setin birincil rehber eşlemesidir; bütün alan hakimiyetini veya hata nedenini ölçmez.

## Yanlış anahtar eşlemesi

- Q01 D→C: İlk lint adımı başlar; unit-test waitFor:[-] ile bağımsız başlar. Integration iki IDye bağlı olduğu için ikisinin başarıyla bitmesini bekler.
- Q02 C→A: Skaffold manual sync kuralları eşleşen dosyaları container hedef yoluna taşır. Static server yeni içeriği diskten okuyabilir.
- Q07 C→D: Delayed destruction sürümü önce disabled yapıp kalıcı yok etmeyi ayarlanan süre sonrasına bırakır. Böylece native recovery penceresi oluşur.
- Q08 B→A: Native secret environment variable yeni instance başlamadan çözümlenir. Erişilemeyen secretla instance startup başarısız olur. Pinned version belirli değeri seçer.
- Q10 B→C: Her region için serverless NEG, tek global backend service ve global external Application Load Balancer kullanılır. Multi-region düzeninde Premium Tier gerekir.
- Q11 A→B: CPU utilization requeste oranla hesaplanır. Limit bulunması eksik requestin yerini tutmaz; request eklenmelidir.
- Q12 B→D: Outlier detection gözlenen başarısız yanıtları kullanarak sağlıksız serverless backendleri geçici dışlar; aktif probe istemeyen koşula uyar.
- Q14 D→B: Read-only transaction okumaları tek snapshot üzerinde toplar ve read lock almaz. Ayrı okumalarda araya yeni commit girebilir.
- Q16 B→A: Log-based alert matching entry üzerinden incident oluşturur. Sayısal trend gerekmeyen tek kritik olay için doğrudan mekanizmadır.
- Q19 B→C: Admission kuralında iki attestor requireAttestationsBy listesine konur; image iki gerekli doğrulamayı da taşımalıdır ve enforcement mode uyumsuz imageı bloke etmelidir.
- Q21 A→B: Client dependency olarak verilir; test double dış servisi değiştirirken business logic gerçek kalır. Network ve credential ihtiyacı kaldırılır.
- Q22 A+B→A+C: Object finalized event tipi ve bucket filtresi doğru olayı seçer. Eventarc HTTP CloudEvents teslim eder; handler event içindeki object bilgisini işler.
- Q23 A→B: Manifestte replicas desired value tutmamak GitOpsun HPA sayısını tekrar üçe çekmesini önler. Deployment template yönetimi devam eder.
- Q34 D→A: Builder stage compile eder; runtime stage yalnız gerekli JAR ve runtime dosyalarını alır. Araçlar final image katmanlarına taşınmaz.
- Q35 C→D: Immutable ConfigMap/Secret güncellenmeyen nesnelerde watch ihtiyacını azaltır ve accidental in-place mutationı engeller. Yeni içerik yeni nesneyle dağıtılır.
- Q40 D→A: BackendConfig healthCheck ayarlarını Service üzerindeki backend-config annotationıyla bağlar. GKE generated health checki bu kaynaktan yönetir.
- Q45 C→B: onSnapshotın döndürdüğü unsubscribe eski room listenerını kapatır; ardından yeni room listenerı oluşturulur.
- Q46 B→C: Autopilotta WIF tüm nodelarda hazırdır; Standard için kullanılan metadata-server nodeSelector kaldırılır. KSA/IAM bağlantısı korunur.
- Q47 C→D: ContainerResource metriği yalnız adı belirtilen application containerın CPU kullanımını izler. Sidecar Pod içinde kalır.
- Q49 A→C: Tüm namespace Podlarını seçen default-deny egress politikası outbound başlangıcını kapatır. Sonra gerekli DNS ve servis yolları ayrı allow politikalarıyla eklenir.
- Q50 A→B: ADC quota project ayarı doğru consumer projeyi seçer. Kullanıcı kimliği ve resource izinleri değişmeden kalır.

Yukarıdaki kısa karar notları mevcut anahtardan değerlendirme kaydına alınmıştır; kullanıcının açıkladığı gerekçe değildir. Sohbette ilk turda sonuç ve yanlış şık eşlemeleri sunuldu; tüm 21 mekanizma öğretilmiş veya kavranmış sayılmaz. İlk seçimler korunur. Sonraki adım kullanıcı tercihiyle az sayıda yanlışın özgün gövde ve seçeneklerini incelemek; yeni set/otomasyon yok.


9 Ekim — S13 sonrası ara: Kullanıcı moralinin bozulduğunu ve yarın (10 Ekim) cevapların üzerinden geçeceğini belirtti. Bugün yeni soru/öğretim yükü ekleme. Kullanıcı geri geldiğinde mevcut S13 anahtarını küçük gruplarla incelemek öncelikli; tüm soru+cevap tekrar dosyası henüz oluşturulmadı, talep gelirse hazırlanabilir. Hatırlatma/otomasyon kurulmaz. İlk 29/50, 112 dakika korunur; yeni cevap veya kavrayış teyidi yok.


9 Ekim — S13 bilgi ağırlığı geri bildirimi: Kullanıcı S13’ün daha çok bilgi sorduğunu düşündüğünü belirtti. Setin bazı soruları belirli ürün ayarı/alan bilgisine dayanıyor: Skaffold sync (Q02), delayed secret destruction (Q07), immutable ConfigMap/Secret (Q35), BackendConfig (Q40), HPA ContainerResource (Q47). Bu gözlem önceki “entegrasyon sınırları” açıklamasını genişletir; tüm hata nedenleri ürün bilgisi diye atanmaz ve diğer setlerle nicel zorluk eşdeğerliği iddia edilmez. Sonraki incelemede bilinmeyen ürün ayrıntısını bilinen kavramda koşul kaçırmadan ayır. İlk 29/50,112 dakika korunur; bugün ara/yarın cevap inceleme tercihi sürer.


9 Ekim — S13 tüm sorular + bilgi notları: Kullanıcı yarın incelemek için soruları/cevapları birlikte ve bilgi gereken yerlerde ek açıklama istedi. [PCD-S13-REVIEW](../answers/scenarios/PCD-S13-REVIEW.md) oluşturuldu: 50 özgün İngilizce gövde/tüm seçenekler, her soruda ilk cevap/doğru cevap/gerekçe/50 kısa bilgi notu/eleme koşulu/mevcut resmî kaynak. 10×5 bölüm, süre hedefi yok; tamamını bir oturumda bitirme zorunluluğu yok. Özellikle Skaffold sync, secret delayed destruction, HPA request/GitOps/ContainerResource, BackendConfig, immutable ConfigMap, listener cleanup ve quota project notları eklendi. Ek bilgi mekanizmaları ilgili resmî belgelerle kontrol edildi; cloud lab yapılmadı. 50 soru/metin/cevap/not, 10 bölüm ve 21 ilk yanlış eşleşmesi doğrulandı. İlk 29/50,112 dakika korunur. Hazırlanan anahtarlı öğretim bağımsız puan veya kavrayış/kalıcılık teyidi değildir; kullanıcının tüm yanlışları bilgi eksikliği diye sınıflandırılmaz. Sonraki adım kullanıcı döndüğünde seçtiği beşlik bölüm veya yanlışlarla devam etmek; yeni set/otomasyon yok. Önceki “S13 tüm soru+cevap tekrar dosyası yok” notu tarihsel kaldı.
