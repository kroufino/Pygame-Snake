
## Úvod
* Jedná se o snake hru naprogramovanou pomocí knihovny Pygame v jazyce Python, za účelem školního projektu.
* Hra je rozdělena do vícero souborů pro snažší čitelnost
* Hra obsahuje možnost zvolení obtížnosti(více k obtížnostem níže), obsahuje možnost nápovědy, zobrazení a vynulování hodnot skóre dosažených uživatelem 
* Hra je ve dvou variantách. [První](https://github.com/kroufino/Pygame-Snake/tree/prod/offline) nabízí ukládání skóre do souboru na aktuálně používaném počítači, [druhá](https://github.com/kroufino/Pygame-Snake/tree/prod/online) nabízí ukládání skóre do databáze
* Online varianta, která ukládá výsledky skóre do Vámi zvolené databáze nabízí možnost zobrazit nejlepšího hráče pro jednotlivou obtížnost!
* U online varianty jste při prvním spuštění dotázáni na svůj nickname. Program se dotazuje jednou, a "session" ukládá do TEMP path, proto je možné, že se po restartu pc bude dotazovat znovu (toto se týká spíše Linuxu).

> ℹ️ **Info:**
> U volby nickname byl brán zřetel na možné `SQLi`, vůči kterým by měl být program imunní

> ⚠️ **Pozor:**
> Program může obsahovat chyby, pokud nějaké naleznete, prosím kontaktujte mě.

`Kompatibilní s Unix a Windows based systémy`

---

## Stažení

[![Online verze](https://img.shields.io/badge/Online%20verze-green?style=for-the-badge)](https://downgit.github.io/#/home?url=https://github.com/kroufino/Pygame-Snake/tree/prod/online)
&nbsp;
[![Offline verze](https://img.shields.io/badge/Offline%20verze-blue?style=for-the-badge)](https://downgit.github.io/#/home?url=https://github.com/kroufino/Pygame-Snake/tree/prod/offline)

> ⚠️ **Pozor:**
> Stažené .zip soubory obsahují pouze .py soubory, nikoli `requirements.txt` nebo `donotshowup.vbs`

---
## ▶️ Jak spustit

1. Bude potřeba Python 3.8+.
2. Nainstalujte knihovny:

```bash
pip install -r requirements.txt
```

3. (pouze u `online` varianty) Nakonfigurujte připojení k MySQL v souboru `snake-game.py`:

```python
host = "<Váš_host>"
username = "<Vaše_uživatelské_jméno>"
password = "<Vaše_heslo>"
database = "<název_databáze>"
```

4. Spusť hru:

```bash
python snake-game.py
```

---

<div style="display: flex; gap: 10px;">
    <img src="https://github.com/kroufino/PyGame-Snake/blob/prod/img/1.png" width="30%" height="40%">
    <img src="https://github.com/kroufino/PyGame-Snake/blob/prod/img/2.png" width="30%" height="40%">
</div>
<div style="display: flex; gap: 10px;">
    <img src="https://github.com/kroufino/PyGame-Snake/blob/prod/img/3.png" width="30%" height="40%">
    <img src="https://github.com/kroufino/PyGame-Snake/blob/prod/img/4.png" width="30%" height="40%">
</div>


---


## Žebříčky (Dostupné pouze u online varianty)

<div style="display: flex; gap: 10px;">
    <img src="https://github.com/kroufino/PyGame-Snake/blob/prod/img/6.png" width="30%" height="40%">
    <img src="https://github.com/kroufino/PyGame-Snake/blob/prod/img/5.png" width="30%" height="40%">
</div>

---

## Volba nickname (Dostupné pouze u online varianty)

<div style="display: flex; gap: 10px;">
    <img src="https://github.com/kroufino/PyGame-Snake/blob/prod/img/7.png" width="30%" height="40%">
    <img src="https://github.com/kroufino/PyGame-Snake/blob/prod/img/8.png" width="30%" height="40%">
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
│   │   └── block.py
│   │   └── nickname.py
│   │   └── okno_volby.py
│   │   └── funkce.py
│   └── snake-game.py
├── offline/           #Verze hry umožňující ukládání skóre do lokálního souboru
│   ├── packages/
│   │   └── block.py
│   │   └── okno_volby.py
│   │   └── funkce.py
│   └── snake-game.py
├── img/               #Obrázky pro účely tohoto README
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.jpg
│   ├── 4.jpg
│   ├── 5.jpg
│   ├── 6.jpg
│   ├── 7.jpg
│   └── 8.jpg
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


