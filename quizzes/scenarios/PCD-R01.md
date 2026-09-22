# PCD-R01 — İlk set sonrası pekiştirme

5 özgün İngilizce soru. Süre tutma. Her sorunun altındaki alanları doldur; isteneni ve kısıtları Türkçe yazabilirsin. `Select one` bir, `Select two` iki cevap demektir. Güven için E (emin), K (kararsız), T (tahmin) kullan.

Bu set hedefli öğrenme içindir; tam sınav denemesi değildir. Cevaplar ayrı dosyadadır. Çözerken kaynakları kapat.

## 1

A compliance tool running on Cloud Run must inspect the labels and version states of one known Secret Manager secret. It must neither read the secret's payload nor modify the secret. The tool uses a dedicated runtime service account with no existing Secret Manager permissions. Which predefined role and scope best meet these requirements?

**Select one.**

- A. Secret Manager Secret Accessor on the specific secret.
- B. Secret Manager Viewer on the specific secret.
- C. Secret Manager Viewer on the project containing the secret.
- D. Secret Manager Admin on the specific secret.

**Benden istenen:**

**Kısıtlar:**

**Cevabım ve güven düzeyim:**b orta yüksek 

**En yakın diğer seçeneği neden eledim:** one known secret diyor

**Takıldığım İngilizce ifade:**

## 2

During a Cloud Build execution, a code-generation step writes files to `/workspace/generated`. A later test step waits for generation to finish but looks for these files in `/tmp/generated`, where it finds nothing. No step deletes the generated files. You want the smallest change that lets the test step use the output within the same build. What should you do?

**Select one.**

- A. Add a delay after code generation so that the files can become visible in `/tmp/generated`.
- B. Assign the same service account to both steps so that their private temporary directories are shared.
- C. Upload the generated files to Cloud Storage and add a download step before testing.
- D. Configure the test step to read the files from `/workspace/generated`.

**Benden istenen:**

**Kısıtlar:**

**Cevabım ve güven düzeyim:** d orta yğksek 

**En yakın diğer seçeneği neden eledim:**c yi eledim çünkü d google mantığına daha yakın buldum

**Takıldığım İngilizce ifade:**

## 3

A Cloud Run service named `orders` calls another Cloud Run service named `pricing`. Both use dedicated service accounts. The `pricing` service requires authenticated invocations, and network connectivity is already configured. Neither account has invocation permissions on the other service. You must allow only the `orders` identity to make this call without downloading service-account keys. Which two actions should you take together?

**Select two.**

- A. Grant the `orders` service account Cloud Run Invoker on the `pricing` service.
- B. Grant the `pricing` service account Cloud Run Invoker on the `orders` service.
- C. Have `orders` obtain a Google-signed ID token using its runtime identity, with the `pricing` service URL as the audience, and include it in the request.
- D. Have `orders` obtain an OAuth access token using its runtime identity and use that token instead of an ID token to invoke `pricing`.

**Benden istenen:**You must allow only the `orders` identity 

**Kısıtlar:**

**İki cevabım ve güven düzeyim:** a, c orta yüksek

**Neden iki işlem birlikte gerekli:**

**Takıldığım İngilizce ifade:**

## 4

A Cloud Run service uses a legacy rendering library. The library keeps a process-wide buffer that is reset at the start of each request. Results are correct when requests run one after another, but overlapping requests within an instance can overwrite each other's data. The library cannot be changed before tomorrow's release. Requests do not need to share state across instances. Which configuration directly addresses this problem?

**Select one.**

- A. Enable session affinity while keeping the current per-instance concurrency.
- B. Set the maximum number of instances to one while keeping the current per-instance concurrency.
- C. Set the maximum concurrent requests per instance to one.
- D. Increase the minimum number of instances while keeping the current per-instance concurrency.

**Benden istenen:**

**Kısıtlar:**

**Cevabım ve güven düzeyim:** c orta yüksek 

**En yakın diğer seçeneği neden eledim:** 

**Takıldığım İngilizce ifade:** burada da simultanously ve sequential kelimelrinin farklı söylenişleri var

## 5

The `orders` runtime service account already has Cloud Run Invoker on `pricing`. The application sends a valid, unexpired Google-signed ID token for that account, but the token's audience is the URL of `orders`. The receiving `pricing` service has no custom audiences configured. Its authentication check rejects the request before the application handles it. Network connectivity is working. What should you change?

**Select one.**

- A. Obtain a new ID token whose audience is the `pricing` service URL and send it to `pricing`.
- B. Grant the `pricing` service account Cloud Run Invoker on `orders` and reuse the same token.
- C. Grant the `orders` service account Cloud Run Admin on the project and reuse the same token.
- D. Replace the ID token with an OAuth access token for the same service account.

**Benden istenen:**

**Kısıtlar:**

**Cevabım ve güven düzeyim:** c

**En yakın diğer seçeneği neden eledim:**

**Takıldığım İngilizce ifade:**The receiving `pricing` service has no custom audiences configured.

---

Kaydet ve kontrol için “bitti” de. [Cevaplar — yalnızca çözümden sonra aç](../answers/scenarios/PCD-R01.md) · [Senaryo dizini](README.md)
