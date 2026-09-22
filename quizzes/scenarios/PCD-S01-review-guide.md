# İlk set sonrası teknik tekrar

Amaç: PCD-S01'deki dört tekrar alanını ders dokümanından okuyup yeni senaryolara uygulamak. Sayfalar PDF dosyasındaki 1'den başlayan sayfa numaralarıdır.

## Bugünkü sıra

1. Aşağıdaki bölümleri oku; yaklaşık 15–20 dakika ayır.
2. İlk dört ders quizini çöz: toplam 20 soru. Yanlışların ve kararsız doğruların açıklamasını kontrol et.
3. [PCD-R01 pekiştirmesini](PCD-R01.md) süre tutmadan çöz. Her soruda isteneni ve kısıtı Türkçe yaz.
4. Kaydedip “bitti” dediğinde cevapları, İngilizce yorumunu ve gerekçelerini birlikte değerlendirelim.

## Doküman ve quiz eşleştirmesi

| Konu | Ders dokümanı ve PDF sayfası | Quiz |
|---|---|---|
| Secret erişimi ve runtime kimliği | [Cloud Run secrets](../../cloudRun/T-DVCRUN-B-m2-l5-file-en-11.en.pdf), s. 5–7; özellikle s. 7 “Allowing access to secrets” | [R08-02](../cloudRun/R08-02.md) |
| Cloud Build adımları arasında dosya paylaşımı | [Deploying Applications](../../foundations/Module6-DeployingApplications.pdf), s. 15–16; özellikle `/workspace` açıklaması | [F06-03](../foundations/F06-03.md) |
| Servisten servise çağrı: izin ve kimlik doğrulama | [Service communication](../../cloudRun/T-DVCRUN-B-m2-l1-file-en-8-new.en.pdf), s. 12–14 | [R05-02](../cloudRun/R05-02.md) |
| Concurrency ve paylaşılan değişkenler | [Cloud Run scaling](../../cloudRun/T-DVCRUN-B-m1-l4-file-en-5-new.en.pdf), s. 7–8 | [R03-02](../cloudRun/R03-02.md) |
| Ek karşılaştırma: session affinity | [Traffic management](../../cloudRun/T-DVCRUN-B-m3-l2-file-en-14.en.pdf), s. 18 “Splitting traffic” | [R10-04](../cloudRun/R10-04.md), özellikle soru 5 |

Secret PDF'si Accessor rolünü anlatıyor. Viewer ile payload erişimi farkını ayrıca [resmî IAM rol tablosundan](https://docs.cloud.google.com/secret-manager/docs/access-control) karşılaştır: Viewer metadata, Secret Accessor secret değeri içindir. Yetkinin hangi kimliğe, hangi kaynak üzerinde verildiğine dikkat et.

R03-02'nin 3. sorusu PDF'deki varsayılan ve maksimum değerleri sorar; bunları her ortam için güncel bir ayar garantisi olarak ezberleme. Bu tekrarda esas hedef concurrency'nin anlamını ve uygulamanın neden düşük concurrency gerektirebileceğini öğrenmek.

## Ders bankasını üç haftada kullanma

Ana bankada 152 set, toplam 760 soru var. Bunları konu hatırlama çalışması olarak kullan; tek başına sınava hazır olma ölçütü sayma. Bazı seçenekler senaryo setlerine göre kolay eleniyor.

- Normal günlerde 15–20 ders sorusu; bugün yukarıdaki dört set yeterli.
- Yanlış veya gerekçesini açıklayamadığın doğruları 2–3 gün sonra tekrar çöz.
- Senaryo çalışmalarını bankanın tamamını bitirene kadar erteleme.
- Hataları “teknik bilgi”, “İngilizce anlam”, “yönerge / seçilecek cevap sayısı” olarak ayrı değerlendir.

[Senaryo dizini](README.md)
