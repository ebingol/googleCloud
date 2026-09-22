# PCD-R01 — İlk deneme değerlendirmesi

20 Eylül 2026. Sonuç: **4/5 (%80)**. Süre bildirilmedi; çalışma süresiz önerilmişti. Kullanıcı seti zorlayıcı buldu. Bu, konu tekrarı sonrası hedefli pekiştirmedir; tam deneme veya sınava hazır olma ölçümü değildir.

| Soru | Cevap | Anahtar | Sonuç | Güven |
|---|---|---|---|---|
| 1 | B | B | Doğru | Orta yüksek |
| 2 | D | D | Doğru | Orta yüksek |
| 3 | A, C | A, C | Doğru | Orta yüksek |
| 4 | C | C | Doğru | Orta yüksek |
| 5 | C | A | Yanlış | Belirtilmedi |

## Gözlemler

- 1: “one known secret” ifadesini kullanarak tek kaynak kapsamını doğru yakalamış. Viewer ile Accessor ayrımına ilişkin gerekçe yazılmadığından bu ayrımın gerekçesini ayrıca sözlü kontrol etmek yararlı.
- 2: Doğru cevap, ancak “Google mantığına daha yakın” gerekçesi teknik olarak yeterince somut değil. Dosya zaten `/workspace/generated` altında; testin okuduğu yolu düzeltmek yeterli. “smallest change” ek Cloud Storage aktarımını elemeyi sağlar.
- 3: İki doğru işlem birlikte seçilmiş; önceki setteki seçim sorunu bu örnekte tekrarlanmamış. Neden birlikte gerektiği alanı boş; gerekçenin anlaşıldığını yalnız seçimden kesinleştiremeyiz.
- 4: Doğru cevap. Kullanıcı eşzamanlı/sıralı çalışmanın farklı ifadelerle anlatıldığını fark etmiş. “one after another” = sırayla; “overlapping requests” = zaman olarak çakışan istekler.
- 5: Kullanıcı “The receiving pricing service has no custom audiences configured” cümlesini zorlandığı ifade olarak işaretlemiş. Teknik hata: daha geniş IAM rolü yanlış audience değerini düzeltmez. Dil güçlüğü ile audience bilgisinin katkısını ayrı bir sözlü örnekle kontrol etmeliyiz.

## 5. sorunun açıklaması

Takıldığı cümle: “Alıcı pricing servisine özel kabul edilen audience değerleri tanımlanmamış.” Bu senaryoda standart hedef olan pricing servis URL'sini kullanmalıyız.

`orders → pricing` çağrısında:

- Çağıranın pricing üzerinde Invoker rolü zaten var.
- Token doğru kimlikten ve süresi geçmemiş, ancak hedefi orders olarak yazılmış.
- Doğru çözüm: audience değeri pricing servis URL'si olan yeni ID token almak (A).
- Cloud Run Admin vermek yetkiyi genişletir ama token'ın hedefini değiştirmez.

## Sonraki kısa çalışma

**20 Eylül güncellemesi:** Audience ayrıca açıklandı. Kullanıcı `checkout → inventory` örneğinde çağıranın service account'una alıcı üzerinde Invoker ve audience olarak inventory cevabını doğru verdi. Anlık kontrol tamamlandı; ilk puan 4/5 olarak korunuyor. Sonraki gecikmeli kontrol hedefi 23 Eylül. Aşağıdaki önerinin audience kısmı artık tamamlandı.

Yeni sete geçmeden önce kullanıcıdan “çağıran / alıcı / audience” üçlüsünü yeni bir servis çifti için yazmasını iste. Ardından 2. sorunun teknik gerekçesini tek cümleyle ifade etmesini sağla. Boş bırakılan istek ve kısıt alanları nedeniyle tüm sorulardaki İngilizce anlama düzeyi henüz ölçülmüş değil.

[Sorular](../PCD-R01.md) · [Açıklamalı cevaplar](../../answers/scenarios/PCD-R01.md)
