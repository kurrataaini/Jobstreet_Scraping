import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

url = "https://id.jobstreet.com/id/Data-scientist-jobs?sortmode=ListedDate"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.90"
}

s = rq.session()
s.headers.update(headers)

page = s.get(url)

if page.status_code == 200:
    print("Request berhasil")
else:
    print(f"Request gagal dengan kode status: {page.status_code}")

soup = BeautifulSoup(page.text, "html.parser")
joblist = soup.find('div', class_='gg45di0 _21bfxf1')
print(joblist.prettify())

jobs_data = []
for artikel in joblist.find_all('article', {'class': 'gg45di0 gg45di1 _1ubeeig8n _1ubeeig8o _1ubeeig7j _1ubeeig7k _1ubeeigav _1ubeeigaw _1ubeeig9r _1ubeeig9s _1ubeeigh _1ubeeig67 _1ubeeig5f efwo40b efwo409 efwo40a _1oxsqkd18 _1oxsqkd1b _1ubeeig33 _1ubeeig36'}):
    posisi = artikel.find('div', {'class' : 'gg45di0 _1ubeeig5h _1ubeeig53'})
    perusahaan = artikel.find(attrs={'data-automation':'jobCompany'})
    lokasi = artikel.find(attrs={'data-automation':'jobLocation'})
    gaji = artikel.find('span', {'class':'gg45di0 _1c7ocld2 _1ubeeig4z _1ubeeig0 _1ubeeigr _1c7ocld4'})
    waktu = artikel.find('span',{'class':'gg45di0 _1ubeeig4z _1oxsqkd0 _1oxsqkd1 _1oxsqkd22 _18ybopc4 _1oxsqkd7'})

posisi_text = posisi.get_text() if posisi else "Posisi tidak ditemukan"
perusahaan_text = perusahaan.get_text() if perusahaan else "Perusahaan tidak ditemukan"
lokasi_text = lokasi.get_text() if lokasi else "Lokasi tidak ditemukan"
gaji_text = gaji.get_text() if gaji else "Gaji tidak disebutkan"
waktu_text = waktu.get_text() if waktu else "Waktu tidak ditemukan"

print(posisi_text)
print(perusahaan_text)
print(lokasi_text)
print(gaji_text)
print(waktu_text)
print("====================================")

