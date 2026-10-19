BITBUCKET PR TOOLS — Windows CMD / Python 3.10+

Mevcut stash-review-batch/stash_batch.py uzerine stats ve ready komutlari
eklenmistir. pr_tools.py ortak tarama modulu olarak ayni klasorde bulunmalidir.
Eski run/start/status/import-legacy komutlari da korunmustur; bunlarin eski
dashboard kapsamli raporlari yeni stats raporuyla ayni kapsamda degildir.

KURULUM
1. ZIP dosyasini acin; tum dosyalari ayni klasorde tutun.
2. Python 3.10 veya daha yeni surum kurulu olmali (py -3 --version).
   Harici Python paketi / pip kurulumu gerekmez.
3. Kurum agina / VPN'e baglanin. CMD'de bu klasore gecin.

CALISTIRMA
  stats.cmd
  ready.cmd

Her komut once uname, sonra gizli access token ister:
  uname (e-posta veya Bitbucket kullanici adi): ezgi.bingol@turkcell.com.tr
  Access token (gizli): [yazarken gorunmez]

Herkes kendi e-postasi ve kendi Bitbucket PERSONAL access token'i ile kullanir.
E-posta LDAP adina tahmin yoluyla cevrilmez. REST'in X-AUSERNAME bilgisiyle
kimlik dogrulanir; bu baslik yoksa users aramasinda tam eslesme aranir.
E-posta gizliyse veya kullanici aramasi kisitliysa Bitbucket LDAP adini girin.
Token sadece bellekte tutulur; dosyaya, rapora, komut satiri argumanina yazilmaz.
Token'i sohbete veya Git'e eklemeyin; dogrudan kendi CMD pencerenize girin.
Yalnizca GET istekleri yapilir; yorum/review/approve/merge olusturulmaz.

1) ISTATISTIKLER
Varsayilan donemler: Eylul 2026 ve Ekim 2026.
  stats.cmd --months 2026-09 2026-10
  py -3 stash_batch.py stats --months 2026-09 2026-10

Her ay ve secili aylarin birlesimi icin:
- commented_prs / Yorumlu PR: o donemde en az bir yorum yazdiginiz benzersiz PR.
- review_only_prs / Sadece review PR: o donemde APPROVED, REVIEWED veya
  UNAPPROVED aktiviteniz olan, fakat AYNI DONEMDE yorumunuz olmayan PR.
- formal_review_prs: bu review aktivitelerinden en az biri olan PR.
- all_reviewed_prs / Tum review PR: yorumlu veya formal review yaptiginiz PR
  kumelerinin birlesimi. Sadece reviewer atanmak ve PR'i acip okumak sayilmaz.
- comments / Yorum: yorum ve yanitlarin toplami. Duzenleme yeni yorum sayilmaz.

Review aksiyonlari sunucunun activity action alanina dayanir. REVIEWED genelde
Needs work islemidir; plugin'e ozel review aksiyonlari bu sayima dahil degildir.
Silinen veya sunucunun artik gostermedigi yorumlar eksiksiz geri getirilemez.
Acik DELETED kaydi varsa o yorum toplamdan cikarilir. Tarihsel/silinmis yorumlari
iceren resmi audit sayimi degildir; API'nin gorunur kayitlarina dayanan rapordur.
Kendi PR'iniza yazdiginiz yorumlar istatistige dahildir.

Tarih, PR'in acilis tarihi degil yorumun createdDate / review aktivite tarihidir.
Saat dilimi Istanbul (UTC+03:00). Ay sinirlari bu saate gore hesaplanir.
Ekim ayinin gelecekteki gunleri icin veri yoktur; rapor calistigi ana kadardir.
TOTAL benzersiz PR sayisidir; ayni PR iki ayda da varsa toplamda bir kez sayilir.
Yorum toplami ise her benzersiz yorumu bir kez sayar.

Tarama tum erisilebilir repolardaki OPEN/MERGED/DECLINED PR'lari ve tum activity
sayfalarini okur. Eski acilmis PR'lardaki yeni yorumlari kacirmamak icin PR
acilis tarihine gore kisitlamaz. Buyuk kurumlarda bu islem uzun surebilir.

2) YENI REVIEW ADAYLARI
  ready.cmd
  ready.cmd --limit 3
  py -3 stash_batch.py ready --limit 3

Tum erisilebilir repolarin acik, taslak olmayan PR'lari incelenir.
Kendi actiginiz PR'lar ve herhangi bir tarihte yorum/yanit yazdiginiz gorunebilen
PR'lar elenir. Gorunen silinmis yorum gecmisi de adayi eler.
Kalanlar createdDate'e gore yeniden eskiye siralanir ve ilk 3 verilir.
UpdatedDate degil, acilis tarihi kullanilir. Reviewer atanmis olmaniz gerekmez.
Onceden Approve verdiginiz ama hic yorum yazmadiginiz PR listede olabilir.
Bu liste yorum yazilabilecek HATA oldugunu veya build/merge hazirligini garanti
etmez; inceleme icin aday listesidir. Tamamen silinip API'den kaybolan bir yorumun
gecmiste yazildigi tespit edilemez.

KAPSAM VE CIKTILAR
- /rest/api/1.0/repos ile tum projelerde token'in gorebildigi repolar bulunur;
  varsa erisilebilir kisisel repolar da dahildir. Tum endpoint'ler sayfalanir.
- Token kullanici yetkisinden daha dar kapsamliysa yalnizca token'in gordugu
  repolar sayilir. Sunucunun gizledigi repolar tespit edilemez.
- Sonuclar ekrana ve reports/<mod>_<zaman>/ altina yazilir.
- stats: summary.csv, events.csv, report.json
- ready: ready.csv, report.json
- CSV UTF-8 BOM'ludur; Excel'den acilabilir. events.csv yorum metni icermez;
  PR kimligi, olay tipi, olay kimligi ve tarih ile sayimi denetlemeyi saglar.
- Raporlar kurum ici PR basliklari/URL'leri ve kullanici adi icerebilir.
- Erişim hatasi olursa sessizce sifir sayilmaz: complete=false, hata listesi ve
  exit code 2 uretilir. Sayilar alt sinirdir; adaylar kesin global ilk 3 degildir.
- Exit code 0: tarama tamamlandi. 1: kimlik/ag/yapilandirma hatasi veya iptal.
- Tarama anlik snapshot degildir; tarama sirasindaki yeni degisiklikler icin
  komutu yeniden calistirin.

AYARLAR
  stats.cmd --output C:\PRRaporlari
  ready.cmd --ca-bundle C:\certs\corporate-ca.pem
  py -3 stash_batch.py stats --base-url https://your-bitbucket.example/git

TLS dogrulamasi aciktir. Sertifika hatasinda kurum CA PEM dosyasini kullanin;
sertifika kontrolunu kapatan bir secenek yoktur. HTTP yonlendirmeleri token'in
baska adrese tasinmamasi icin reddedilir. 429/502/503/504 icin sinirli retry vardir.

TEST
  py -3 -m unittest discover -s . -v
Bu paket yerel mock/unit testleriyle dogrulandi. Windows CMD ve Turkcell canli
REST servisinde token ile uctan uca calistirma henuz yapilmadi.

API REFERANSI
https://docs.atlassian.com/bitbucket-server/rest/7.15.3/bitbucket-rest.html
Server/Data Center REST: repositories, users, pull-requests ve activities.
Sunucunun yuklu surumu/plugin'leri farkli aktiviteler dondurebilir.

MAC KULLANIMI
Terminal'i acin, ZIP'ten cikan klasore gecin:
  cd ~/Downloads/bitbucket-pr-tools
  python3 stash_batch.py stats --months 2026-09 2026-10
  python3 stash_batch.py ready
python3 --version ile Python 3.10+ kurulu oldugunu kontrol edin.
Alternatif: stats.command / ready.command baslaticilarini kullanin.

BICIMLENDIRILMIS EXCEL
Istatistikte PR-raporu.xlsx, aday listesinde Review-adaylari.xlsx uretilir.
Excel'de renkli basliklar, genis sutunlar, filtreler, sabit baslik satirlari ve
sayisal hucreler vardir. Istatistik raporunda Ozet ve Islem detaylari sekmeleri
bulunur. CSV dosyalari istege bagli ek ciktilardir; .xlsx dosyasini acin.
Excel raporu icin de ek Python paketi kurmak gerekmez.


YENI TARAMA / DEVAM / PARALELLIK
Varsayilan her calistirma yeni klasorde bastan tarar. --fresh bunu acikca belirtir.
  python3 stash_batch.py stats --fresh --workers 4 --months 2026-09 2026-10
Baslangicta yazdirilan Tarama klasoru yolunu saklayin. Kesilirse:
  python3 stash_batch.py stats --resume "reports/stats_..." --workers 4 --months 2026-09 2026-10
Windows'ta python3 yerine py -3 veya stats.cmd kullanabilirsiniz.
--workers 1-8 arasi; varsayilan 4. --fresh onceki raporlari silmez.
Her tamamlanan PR atomik dosyaya kaydedilir. Devam ayni kullanici/sunucu/mod/ay
ile sinirlidir. Basarili PR'lar yeniden okunmaz; basarisiz istekler yeniden denenir.
Resume, kayitli kesif/sonuc snapshot'unu surdurur. Sonradan gelen yeni PR/yorumlari
yenilemek icin --fresh kullanin. Ayni checkpoint'te eszamanli iki tarama engellenir.
Ctrl+C sirasinda aktif isteklerin kapanmasi en fazla istek timeout'u kadar surebilir.
Calisan eski surumun bellek verisi bu ara kayitlara aktarilamaz.

Canli sayim: P=yorumlu PR, R=sadece review PR, Y=yorum/yanit.
Sayilar tarama bitene kadar gecicidir. Sifir kayitlar tek tek loglanmaz;
istenirse --verbose tum sonuclari gosterir. progress.json ara ozet icerir.
Tum repo ve PR sayfalari taranir; eski acilmis PR'daki yeni yorumu kacirmamak
icin guvenilmeyen acilis/son-guncelleme tarihi elemesi uygulanmaz. Hiz kazanci
sinirli paralellik ve resume'da tamamlanan islerin tekrar okunmamasindan gelir.

Bilinen PR kontrolu: TCEZBINGOL / Turkcell sunucusunda SOLID #5 icin en az 3
yorum dogrulanir; kontrol basarisizsa ana tarama durur. Baska kullanicilar icin:
  python3 stash_batch.py stats --verify-pr "PROJECT/REPO#ID" --expected-comments 1
Bu bir kimlik/yorum ayrisma kontroludur; tum review turlerini dogrulamaz.
Baska kullanicilar kontrol PR'i vermediginde bu kontrolun yapilmadigi belirtilir.
Token veya cookie icerikleri checkpoint'e kaydedilmez.
