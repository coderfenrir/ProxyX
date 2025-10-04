import os
import sys
import time
import random
import subprocess
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

init(autoreset=True)

# Renkler
R = '\033[91m'  # Kırmızı
G = '\033[92m'  # Yeşil
B = '\033[94m'  # Mavi
Y = '\033[93m'  # Sarı
W = '\033[97m'  # Beyaz
C = '\033[96m'  # Cyan
M = '\033[95m'  # Mor (Magenta)
RESET = '\033[0m'

def fenrir_clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def fenrir_banner():
    print(f"""
{B}
⠀⢀⣴⡾⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢻⣧⡀⠙⣿⡆⠀⠀⡐⠉⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⠟⣡⣾⠟⠁⠀⠀⢃⠀⠀⠇⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⡏⣼⠋⠀⠀⠀⢀⣀⡈⢢⡔⠀⣠⠞⠉⠙⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀
⢠⣿⠀⢿⣦⣤⣤⣶⡟⣿⣿⣿⣿⣾⣅⠀⠀⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠘⣿⣆⠈⠙⠛⠛⠋⣸⣿⣿⣿⣿⣿⣿⠀⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠿⣧⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⡇⠀⣿⣿⢻⣿⣿⣿⣿⣿⣿⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡇⠀⣿⣏⢸⣿⣿⣿⣿⣿⣿⠀⣸⡏⠀⠀⠀⠀⢀⣠⣴⣦⡄⠀
⠀⠀⠛⠚⠀⠀⢿⣿⠈⢹⣿⣿⣿⣿⡇⠀⣿⡇⠀⠀⢀⣴⡿⠋⢉⣿⡿⠀
⠀⠀⠀⠀⠀⠀⠘⣿⡄⠈⣿⣿⣿⣿⡇⠀⣿⣿⣦⣶⡿⠋⣠⣴⠟⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⣿⣿⣿⣿⣇⠀⠘⠛⠛⢉⣴⣾⣯⣤⣤⣄⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠈⣿⡀⣿⣿⣿⢻⣿⡀⠀⣠⣾⣿⣿⡿⠋⠉⠙⢿⣧⠀
⠀⠀⠀⠀⠀⣸⠀⠀⢸⣇⣿⣿⣿⠈⠻⢿⣾⣿⣿⡿⠃⠠⢢⣰⠀⢈⣿⡆
⠀⠀⠀⠀⡼⠃⠀⠀⠘⣿⢹⣿⡇⠀⢀⣿⣿⡏⢹⠀⠀⢤⠈⠉⠀⣸⣿⠇
⠀⠀⢀⡾⠁⠀⠀⠀⢠⣿⢸⣿⠃⠀⢸⣿⡿⠀⢸⡄⠀⠈⢷⣶⣾⣿⡿⠀
⠀⠀⣼⣧⠀⠀⠀⠀⣸⣿⢸⣿⠀⠀⢻⣿⣇⠀⣸⡇⠀⠀⠀⠉⠛⠋⠀⠀
⠀⠀⣿⣿⣦⣤⣠⣾⣿⡏⠸⣿⡀⠀⠘⣿⣿⣶⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⠻⣿⣿⣿⣿⡟⠀⠀⠻⠁⠀⠀⠈⠛⠛⠁⠀{R}https://github.com/coderfenrir{RESET}⠀⠀⠀⠀⠀⠀⠀⠀
{B}
░█████████                                            ░██    ░██ 
░██     ░██                                            ░██  ░██  
░██     ░██ ░██░████  ░███████  ░██    ░██ ░██    ░██   ░██░██   
░█████████  ░███     ░██    ░██  ░██  ░██  ░██    ░██    ░███    
░██         ░██      ░██    ░██   ░█████   ░██    ░██   ░██░██   
░██         ░██      ░██    ░██  ░██  ░██  ░██   ░███  ░██  ░██  
░██         ░██       ░███████  ░██    ░██  ░█████░██ ░██    ░██ 
                                                  ░██            
                                            ░███████             
{RESET}
{G}PROXY-X TOOL | {W}V1.2-BETA{W} {G}CODED BY • CODERFENRİR{RESET}
""")

def fenrir_secim_al():
    print(f"{C}Proxy türünü seçin:{RESET}")
    print(f"{G}[1]{RESET} HTTP")
    print(f"{G}[2]{RESET} HTTPS")
    print(f"{G}[3]{RESET} SOCKS4")
    print(f"{G}[4]{RESET} SOCKS5")
    print(f"{G}[5]{RESET} Tümü (HTTP + HTTPS + SOCKS4 + SOCKS5)")
    print(f"{G}[00]{RESET} Çıkış")
    while True:
        secim = input("\n\033[1;37m[\033[1;32m?\033[1;37m] Seçiminiz (1-5, 00): \033[0m").strip()
        if secim == '00':
            print(f"{R}Çıkış yapılıyor...{RESET}")
            sys.exit(0)
        if secim in {'1', '2', '3', '4', '5'}:
            return secim
        print(f"{R}Geçersiz seçim. Lütfen 00, 1, 2, 3, 4 veya 5 girin.{RESET}")

def fenrir_adet_al():
    while True:
        try:
            adet = int(input(f"{C}Kaç adet proxy çekilsin? (1-5000): {RESET}"))
            if 1 <= adet <= 5000:
                return adet
            print(f"{C}Lütfen 1 ile 5000 arasında bir sayı girin.{RESET}")
        except ValueError:
            print(f"{R}Geçersiz giriş. Lütfen bir tam sayı girin.{RESET}")

def fenrir_requests_ile_get(url, timeout=10):
    try:
        import requests
        yanit = requests.get(url, timeout=timeout)
        if yanit.status_code == 200:
            return yanit.text
    except Exception:
        pass
    return None

def fenrir_curl_ile_get(url, timeout=10):
    try:
        sonuc = subprocess.run(
            ['curl', '-s', '-m', str(timeout), url],
            capture_output=True,
            text=True
        )
        if sonuc.returncode == 0:
            return sonuc.stdout
    except Exception:
        pass
    return None

def fenrir_sayfayi_getir(url, timeout=10):
    icerik = fenrir_requests_ile_get(url, timeout)
    if icerik is None:
        icerik = fenrir_curl_ile_get(url, timeout)
    return icerik

def fenrir_tablodan_proxy_cek(html, limit):
    proxyler = []
    if not html:
        return proxyler
    try:
        soup = BeautifulSoup(html, 'lxml')
        tablo = soup.find('table', {'id': 'proxylisttable'})
        if not tablo:
            tablo = soup.find('table', class_='table table-striped')
        if not tablo:
            return proxyler
        satirlar = tablo.find_all('tr')[1:]
        for satir in satirlar:
            if len(proxyler) >= limit:
                break
            hucreler = satir.find_all('td')
            if len(hucreler) >= 2:
                ip = hucreler[0].get_text(strip=True)
                port = hucreler[1].get_text(strip=True)
                if ip and port and ip.replace('.', '').isdigit():
                    proxyler.append(f"{ip}:{port}")
    except Exception:
        pass
    return proxyler

def fenrir_proxyscrape_cek(protokol, limit):
    proxyler = []
    url = f"https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol={protokol}&timeout=10000&country=all&limit={limit}&format=text"
    
    # Önce requests dene
    try:
        import requests
        yanit = requests.get(url, timeout=15)
        if yanit.status_code == 200:
            satirlar = [satir.strip() for satir in yanit.text.splitlines() if satir.strip()]
            proxyler = satirlar[:limit]
    except Exception:
        pass

    # Başarısızsa curl ile dene
    if not proxyler:
        try:
            sonuc = subprocess.run(
                ['curl', '-s', '-m', '15', url],
                capture_output=True,
                text=True
            )
            if sonuc.returncode == 0:
                satirlar = [satir.strip() for satir in sonuc.stdout.splitlines() if satir.strip()]
                proxyler = satirlar[:limit]
        except Exception:
            pass
    return proxyler

def fenrir_proxy_topla(proxy_turu, adet):
    toplanan = set()
    print(f"\n{C}{proxy_turu.upper()} proxy'leri toplanıyor...{RESET}")

    if proxy_turu in ('http', 'https'):
        # Kaynak 1: sslproxies.org
        html = fenrir_sayfayi_getir("https://www.sslproxies.org/", 10)
        proxyler = fenrir_tablodan_proxy_cek(html, adet)
        toplanan.update(proxyler)
        print(f"{C}sslproxies.org → {W}{len(proxyler)}{C} proxy eklendi.{RESET}")

        # Kaynak 2: free-proxy-list.net
        if len(toplanan) < adet:
            html = fenrir_sayfayi_getir("https://free-proxy-list.net/", 10)
            proxyler = fenrir_tablodan_proxy_cek(html, adet - len(toplanan))
            toplanan.update(proxyler)
            print(f"{C}free-proxy-list.net → {W}{len(proxyler)}{C} proxy eklendi.{RESET}")

        # Kaynak 3: ProxyScrape
        if len(toplanan) < adet:
            proxyler = fenrir_proxyscrape_cek('http', adet - len(toplanan))
            toplanan.update(proxyler)
            print(f"{C}ProxyScrape (HTTP) → {W}{len(proxyler)}{C} proxy eklendi.{RESET}")

    elif proxy_turu == 'socks4':
        # Kaynak: socks-proxy.net
        html = fenrir_sayfayi_getir("https://www.socks-proxy.net/", 10)
        proxyler = fenrir_tablodan_proxy_cek(html, adet)
        toplanan.update(proxyler)
        print(f"{C}socks-proxy.net → {W}{len(proxyler)}{C} proxy eklendi.{RESET}")

        # Kaynak: ProxyScrape
        if len(toplanan) < adet:
            proxyler = fenrir_proxyscrape_cek('socks4', adet - len(toplanan))
            toplanan.update(proxyler)
            print(f"{C}ProxyScrape (SOCKS4) → {W}{len(proxyler)}{C} proxy eklendi.{RESET}")

    elif proxy_turu == 'socks5':
        # Kaynak: ProxyScrape
        proxyler = fenrir_proxyscrape_cek('socks5', adet)
        toplanan.update(proxyler)
        print(f"{C}ProxyScrape (SOCKS5) → {W}{len(proxyler)}{C} proxy eklendi.{RESET}")

    return list(toplanan)[:adet]


def fenrir_dosyaya_kaydet(proxyler, dosya_adi="proxylist.txt"):
    try:
        with open(dosya_adi, "w") as dosya:
            for proxy in proxyler:
                dosya.write(proxy + "\n")
        print(f"\n{C}Toplam {W}{len(proxyler)}{C} proxy '{W}{dosya_adi}{C}' dosyasına kaydedildi.{RESET}")
    except Exception as hata:
        print(f"{R}Dosya kaydedilirken hata oluştu: {hata}{RESET}")


def fenrir_calistir():
    fenrir_clear()
    fenrir_banner()

    secim = fenrir_secim_al()
    adet = fenrir_adet_al()

    tur_haritalama = {
        '1': ['http'],
        '2': ['https'],
        '3': ['socks4'],
        '4': ['socks5'],
        '5': ['http', 'https', 'socks4', 'socks5']
    }

    tum_proxyler = []
    secilen_turler = tur_haritalama[secim]

    for tur in secilen_turler:
        gerekli_adet = adet if secim != '5' else max(1, adet // len(secilen_turler))
        proxyler = fenrir_proxy_topla(tur, gerekli_adet)
        tum_proxyler.extend(proxyler)
        time.sleep(random.uniform(0.5, 1.2))

    if tum_proxyler:
        fenrir_dosyaya_kaydet(tum_proxyler)
    else:
        print(f"\n{R}Hiç proxy toplanamadı. İnternet bağlantınızı kontrol edin.{RESET}")


if __name__ == "__main__":
    try:
        fenrir_calistir()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as genel_hata:
        print(f"{R}Genel hata: {genel_hata}{RESET}", file=sys.stderr)
        sys.exit(1)
