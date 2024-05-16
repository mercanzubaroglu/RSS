import feedparser

rss_url = "https://www.cnnturk.com/feed/rss/ekonomi/news"
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    print("Başlık:", entry.title)
    print("Bağlantı:", entry.link)
    print("-----------------------")
    
#RSS(Rich Site Summary veya Really Simple Syndication), web sitelerinin içeriğini otomatik olarak toplamak ve kullanıcılara sunmak için kullanılan bir standarttır.
#Web siteleri, RSS formatında yapılandırılmış XML dosyaları oluşturur ve bu dosyalar, sitenin güncel içeriğini başlık, özet ve bağlantı gibi bilgilerle birlikte sunar.
#Kullanıcılar, bir RSS okuyucu kullanarak bu beslemelere abone olabilir ve farklı kaynaklardan gelen içeriği tek bir yerden takip edebilirler.