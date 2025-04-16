
## Úvod
* Jedná se o snake hru naprogramovanou pomocí knihovny Pygame v jazyce Python, za účelem školního projektu.
* Hra je rozdělena do vícero souborů pro snažší čitelnost
* Hra obsahuje možnost zvolení obtížnosti(více k obtížnostem níže), obsahuje možnost nápovědy, zobrazení a vynulování hodnot skóre dosažených uživatelem 
* Hra je ve dvou variantách. [První](https://github.com/kroufino/Pygame-Snake/tree/master/offline) nabízí ukládání skóre do souboru na aktuálně používaném počítači, [druhá](https://github.com/kroufino/Pygame-Snake/tree/master/online) nabízí ukládání skóre do databáze
* Online varianta, která ukládá výsledky skóre do Vámi zvolené databáze nabízí možnost zobrazit nejlepšího hráče pro jednotlivou obtížnost!

> ⚠️ **Pozor:**
> Program může obsahovat chyby, pokud nějaké naleznete, prosím kontaktujte mě.

`Kompatibilní s Unix a Windows based systémy`

---

## Stažení

[![Online verze](https://img.shields.io/badge/Online%20verze-green?style=for-the-badge)](https://downgit.github.io/#/home?url=https://github.com/kroufino/Pygame-Snake/tree/master/online)
&nbsp;
[![Offline verze](https://img.shields.io/badge/Offline%20verze-blue?style=for-the-badge)](https://downgit.github.io/#/home?url=https://github.com/kroufino/Pygame-Snake/tree/master/offline)

> ⚠️ **Pozor:**
> Stažené .zip soubory obsahují pouze .py soubory, nikoli `requirements.txt` nebo `donotshowup.vbs`

---
## ▶️ Jak spustit

1. Bude potřeba Python 3.8+.
2. Nainstaluj knihovny:

```bash
pip install -r requirements.txt
```

3. (pouze u `online` varianty) Nakonfiguruj připojení k MySQL v souboru `snake-game.py`:

```python
host = "<tvůj_host>"
username = "<tvé_uživatelské_jméno>"
password = "<tvoje_heslo>"
database = "<název_databáze>"
```

4. Spusť hru:

```bash
python snake-game.py
```

---
## Changelog

`!` `08.03.25` `Hra obsahuje prvky nutné k samotnému fungovaní hry, zjednodušeně, toto je kostra programu. Veškteré funkce, které budou v budoucnosti přidávány, jsou považovány za dodatkové`

`!` `13.03.25` `Ve hře jsou nyní obtížnosti, které jsou volitelné + byla upravena logika fps`

`!` `14.03.25` `Oprava chyby v určování pozice jídla zavisejíc na obtížnosti uživatelem zvolené`

`!` `19.03.25` `Nyní je možnost zastavit zobrazování se okna programu cmd.exe po každém zapnutí programu užitím donotshowup.vbs souboru fungujicího na Windows systémech. Více níže...`

`!` `20.03.25` `Nyní je ve hře ukládání nejlepšího skóre pro každou obtížnost. Také je nově ve hře možnost nápovědy + drobné úpravy`

`!` `21.03.25` `Drobné úpravy`

`!` `26.03.25` `Rozdělení do vícero souborů za účelem snažší čitelnosti + zlepšení komentářů`

`!` `30.03.25` `Drobné úpravy`

`!` `6.04.25` `Přidání varianty pro ukládání dat do databáze`

`!` `9.04.25` `Přidání varianty zobrazení nejlepšího hráče u online varianty hry`

---

<div style="display: flex; gap: 10px;">
    <img src="https://github.com/kroufino/PyGame-Snake/blob/master/img/1.png" width="30%" height="40%">
    <img src="https://github.com/kroufino/PyGame-Snake/blob/master/img/2.png" width="30%" height="40%">
</div>
<div style="display: flex; gap: 10px;">
    <img src="https://github.com/kroufino/PyGame-Snake/blob/master/img/3.png" width="30%" height="40%">
    <img src="https://github.com/kroufino/PyGame-Snake/blob/master/img/4.png" width="30%" height="40%">
</div>

---

## Žebříčky (Dostupné pouze u online varianty)

<div style="display: flex; gap: 10px;">
    <img src="https://github.com/kroufino/PyGame-Snake/blob/master/img/6.png" width="30%" height="40%">
    <img src="https://github.com/kroufino/PyGame-Snake/blob/master/img/5.png" width="30%" height="40%">
</div>


---

## 📁 Struktura

```
.
├── LICENSE        
├── requirements.txt
├── donotshowup.vbs    #Pouze pro Windows, více níže
├── .gitignore         
├── online/            #Verze hry umožňující ukládání skóre do databáze a zobrazování nejlepších hráčů
│   ├── packages/
│   │   └── okno_volby.py
│   │   └── funkce.py
│   └── snake-game.py
├── offline/           #Verze hry umožňující ukládání skóre do lokálního souboru
│   ├── packages/
│   │   └── okno_volby.py
│   │   └── funkce.py
│   └── snake-game.py
├── img/               #Obrázky pro účely tohoto README
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.jpg
│   ├── 4.jpg
│   ├── 5.jpg
│   └── 6.jpg
└── README.md
```

## Obtížnosti

| Obtížnost | Easy  | Medium  | Hard |
| ------- | --- | --- | --- |
| Popis | jídlo nebude nikdy na okraji obrazovky | jídlo může, ale nemusí být na okraji obrazovky (50%) | jídlo je vždy na okraji obrazovky |

## VBS soubor(Pouze pro Windows)

Pokud se chcete zbavit vyskakovacího cmd.exe okna, stačí spouštět program přes .vbs soubor
> ⚠️ **Pozor:**
> Pokud přejmenujete .py soubor, je třeba upravit obsah souboru .vbs pro opětovné fungování

> ⚠️ **Pozor:**
> .vbs a snake-game.py se musí nacházet ve stejném adresáři!


