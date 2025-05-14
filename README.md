# VideoCardCatalog_1alv
Šis Python skripts ņem videokartes produkta informāciju no Latvijas e-komercijas vietnes 1a.lv, konkrēti no videokaršu kategorijas. Tas izgūst produktu nosaukumus, cenas un tehniskās specifikācijas un pēc tam saglabā datus Excel failā.


# Funkcijas
Iegūst produktu nosaukumus un cenas no kategoriju sarakstiem

Apmeklē katru produkta lapu, lai iegūtu specifikācijas

Saglabā datus vienkāršā Excel failā ar divām kolonnām:

kolonna: Produkta nosaukums ar specifikācijām

kolonna: Cena

Ietver pieklājīgas pauzes, lai izvairītos no servera pārslodzes

Apstrādā biežāk sastopamās datu iegūšanas kļūdas


# Instalēšana
Pārliecinieties, vai jums ir instalēta Python 3.6+ versija.

Instalējiet nepieciešamās pakotnes:
pip install requests beautifulsoup4 pandas openpyxl

# Lietojums
Palaist skriptu:
python scraper.py


# Faila struktūra
scraper.py - Galvenais datu iegūšanas skripts

video_cards.xlsx - Rezultātu fails (izveidojas pēc palaišanas)


# Izvades formāts
Excel tabula, kurā ir divas kolonnas
Video Card : Sapphire Radeon RX 7800 XT
Atmiņa: 16GB GDDR6
Takts frekvence: 1800MHz

Price: 551,00 €