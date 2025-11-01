# Instrukcja uruchomienia strony MGWood

## Wymagania
- Python 3.8 lub nowszy
- pip (mened?er pakiet?w Python)

## Krok po kroku

### 1. Otw?rz terminal i przejd? do folderu projektu

```bash
cd /workspace/mgwood
```

### 2. Zainstaluj wymagane pakiety

```bash
pip install -r requirements.txt
```

lub

```bash
pip install Flask Werkzeug
```

### 3. Uruchom aplikacj?

```bash
python app.py
```

lub

```bash
python3 app.py
```

### 4. Otw?rz przegl?dark?

Wpisz w pasku adresu:

```
http://localhost:5000
```

lub

```
http://127.0.0.1:5000
```

## Strona jest gotowa!

Mo?esz teraz przegl?da? stron? MGWood z dzia?aj?c? baz? danych SQLite.

### Dost?pne strony:

- **Strona g??wna**: http://localhost:5000/
- **Wszystkie produkty**: http://localhost:5000/produkty
- **Sto?y**: http://localhost:5000/produkty/stoly
- **???ka**: http://localhost:5000/produkty/lozka
- **Schody**: http://localhost:5000/produkty/schody
- **O nas**: http://localhost:5000/o-nas
- **Kontakt**: http://localhost:5000/kontakt

### API REST:
- **Lista produkt?w (JSON)**: http://localhost:5000/api/produkty

## Zatrzymanie serwera

Aby zatrzyma? serwer, naci?nij `Ctrl + C` w terminalu.

## Baza danych

Baza danych SQLite (`mgwood.db`) jest automatycznie tworzona przy pierwszym uruchomieniu aplikacji i zawiera:
- 9 produkt?w (3 sto?y, 3 ???ka, 3 schody)
- Tabel? dla zapyta? kontaktowych

## Przegl?danie bazy danych

Mo?esz przegl?da? baz? danych u?ywaj?c komendy:

```bash
sqlite3 mgwood.db "SELECT * FROM produkty;"
```

lub

```bash
sqlite3 mgwood.db "SELECT * FROM zapytania;"
```

## Dodawanie nowych produkt?w

Mo?esz doda? nowe produkty bezpo?rednio przez SQLite:

```bash
sqlite3 mgwood.db
```

Nast?pnie:

```sql
INSERT INTO produkty (nazwa, kategoria, opis, cena, wymiary, material, zdjecie, aktywny)
VALUES ('Nazwa produktu', 'kategoria', 'Opis', 1000.00, '100x50x75 cm', 'D?b lite', 'zdjecie.jpg', 1);
```

## Funkcje strony

? **Responsywny design** - Strona dzia?a na wszystkich urz?dzeniach (desktop, tablet, mobile)
? **Baza danych SQLite** - Wszystkie produkty i zapytania przechowywane w bazie
? **Formularz kontaktowy** - Zapisuje wiadomo?ci do bazy danych
? **Filtrowanie produkt?w** - Po kategoriach (sto?y, ???ka, schody)
? **API REST** - Dost?p do produkt?w przez API
? **Minimalistyczny design** - Wzorowany na stronie kverko.pl

## Problemy?

Je?li aplikacja nie uruchamia si?:
1. Upewnij si?, ?e Python jest zainstalowany: `python --version`
2. Sprawd? czy Flask jest zainstalowany: `pip list | grep Flask`
3. Sprawd? czy port 5000 nie jest zaj?ty
4. Spr?buj uruchomi? na innym porcie dodaj?c w `app.py` na ko?cu:
   ```python
   app.run(debug=True, host='0.0.0.0', port=8080)
   ```

## Kontakt

Strona stworzona dla:
**MGWood - Marcin Grzanka**
Email: mgwood102@gmail.com
Tel: 695 129 969
