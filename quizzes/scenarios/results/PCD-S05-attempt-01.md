# PCD-S05 — İlk bildirilen cevapların değerlendirmesi

25 Eylül 2026. Kaynak: kullanıcının sohbette gönderdiği 20 cevap ve 70–80 dakika süre beyanı. Harfler büyük harfe, çoklu seçimler ayrı harflere çevrildi; ilk seçimler korunmuştur.

**Sonuç: 17/20 (%85). Süre: 70–80 dakika.** Soru başına ortalama 3,5–4 dakika; 50 dakikalık kişisel hedeften 20–30 dakika uzun. Q3, Q15, Q18 yanlış; diğer 17 soru doğru. Q18'de D doğru parça, B yanlış ve C eksik; tam küme kuralıyla 0 puan. Q16 B+E tam doğru.

Güven, gerekçe, mola ve dış kaynak kullanımı bildirilmedi; bağımsız koşullar ayrıca doğrulanmadı. Kullanıcının Q3/Q15/Q18'i kalın yazması kaydedildi, anlamı varsayılmadı. Hata nedenlerini yalnız seçimlerden dil/teknik/dikkat olarak kesin sınıflandırma.

| Soru | Kullanıcı cevabı | Anahtar | Sonuç |
|---|---|---|---|
| 1 | C | C | Doğru |
| 2 | A | A | Doğru |
| 3 | A | D | Yanlış |
| 4 | B | B | Doğru |
| 5 | C | C | Doğru |
| 6 | D | D | Doğru |
| 7 | A | A | Doğru |
| 8 | C | C | Doğru |
| 9 | B | B | Doğru |
| 10 | A | A | Doğru |
| 11 | D | D | Doğru |
| 12 | B | B | Doğru |
| 13 | C | C | Doğru |
| 14 | A | A | Doğru |
| 15 | B | D | Yanlış |
| 16 | B, E | B, E | Doğru |
| 17 | A | A | Doğru |
| 18 | B, D | C, D | Yanlış |
| 19 | B | B | Doğru |
| 20 | C | C | Doğru |

## Alan örneklemi

Tasarım 6/6; geliştirme-test 4/5; deployment 3/5; entegrasyon 4/4. Bunlar S05'in birincil atamalarıdır; tüm alt alanlarda ustalık veya gerçek sınav geçme olasılığı değildir. Q19 önceki Invoker kararının pekiştirmesidir.

## Üç inceleme noktası

- Q3 A → D: Shared DB kolonunu baştan rename etmek hâlâ çalışan eski revision'ı kırar. Önce additive değişim, eski/yeni yazmaları uyumlu tutan geçiş ve backfill; eski kolon ancak rollback penceresi kapanınca kaldırılır.
- Q15 B → D: preStop 20 saniye + uygulama drain 25 saniye aynı grace budget içindedir. 30 saniye yetmez; payla artırılmalı. PDB shutdown süresini uzatmaz. Kaynak: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/ .
- Q18 B+D → C+D: Eski final image'ı yeniden deploy etmek yeni kaynak kodunu dağıtmaz. Manifest/lockfile → npm ci → source sırası dependency layer'ı korur; önceki image cache source olarak ayrıca alınır. Kaynak: https://docs.cloud.google.com/build/docs/optimize-builds/speeding-up-builds .

Açıklama sonrası kavrayış veya yeni bağımsız yanıt henüz yok. Önce bu üç ayrımı, sonra süreyi incele; uzun paragrafları kullanıcının isteği dışında kısaltma. S04 için sonuç bildirilmedi. İlk puan açıklama sonrası değiştirilmeyecek.

[Sorular](../PCD-S05.md) · [Anahtar](../../answers/scenarios/PCD-S05.md)


## Sonraki kullanıcı açıklaması

Kullanıcı Q3'te “additive schema changes” ifadesini anlamadığını bildirdi; ifade eksikliği doğrulandı. Ardından rollback, Pod açılma/kapanma ve maintenance sürecini karıştırdığını belirterek konu anlatımı istedi. Rehberli açıklama yapıldı; bağımsız yeni yanıt veya kalıcılık teyidi henüz yok. İlk seçimler ve 17/20 korunur.


### S05 Q3 — rehberli rollback kontrolü

Kullanıcı, v2 geçişinde name kolonu silindikten sonra v1 Pod'larını geri getirmenin sorunu düzeltmeyeceğini “hayır kolon silinmiş bir kere” yanıtıyla doğru açıkladı. Uygulama rollback'i ile veritabanı şema değişikliğinin geri alınması ayrımında açıklama sonrası gerekçeli doğru yanıt var. Additive schema changes ifadesinin önceki belirsizliğinden sonra anlık uygulama başarısı; bağımsız/gecikmeli kalıcılık sayılmaz. İlk S05 17/20 korunur.


### S05 Q18 — rehberli image/cache kontrolü

Kullanıcı uygulama kodu değiştiğinde build atlanıp eski image tekrar deploy edilirse yeni kodun ulaşmayacağı sorusuna “hayır” diyerek doğru yanıt verdi. Eski final image ile yeni kodu build etme ayrımında açıklama sonrası doğru kontrol; Docker layer sırası ve cache invalidation bilgisi henüz ayrıca uygulanmadı. İlk S05 17/20 korunur; bağımsız/gecikmeli başarı sayılmaz.


### S05 Q18 — cache ve yeni kaynak kodu rehberli kontrolü

Doğru Dockerfile sıralaması (manifest/lock → npm ci → source), erişilebilir cache ve yalnız server.js değişikliği koşullarında npm ci yeniden çalışmadan yeni kodun image'a girip girmeyeceği soruldu. Kullanıcı “girer” diyerek doğru yanıtladı. Cache edilmiş dependency sonucu ile yeni source COPY adımını bir arada uygulayabildi; açıklama sonrası rehberli kontrol, bağımsız/gecikmeli kalıcılık değil. Lockfile değişikliği sorusuna ayrı yanıt henüz yok. S05 ilk 17/20 korunur.
