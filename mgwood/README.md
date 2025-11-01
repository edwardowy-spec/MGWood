# MGWood - Strona internetowa z baz? danych SQLite

Strona internetowa dla firmy MGWood specjalizuj?cej si? w produkcji r?cznie wykonanych mebli z drewna.

## Funkcjonalno?ci

- ? Pe?na baza danych SQLite z produktami
- ? Kategorie produkt?w: Sto?y, ???ka, Schody
- ? Szczeg??owe informacje o produktach
- ? Formularz kontaktowy z zapisem do bazy danych
- ? Responsywny design (mobile-first)
- ? Minimalistyczny styl wzorowany na kverko.pl
- ? API REST dla produkt?w

## Technologie

- **Backend**: Python Flask
- **Baza danych**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Responsywno??**: Mobile-first design

## Instalacja i uruchomienie

### 1. Zainstaluj wymagane pakiety

```bash
cd mgwood
pip install -r requirements.txt
```

### 2. Uruchom aplikacj?

```bash
python app.py
```

Aplikacja uruchomi si? na `http://localhost:5000`

### 3. Dost?pne strony

- **Strona g??wna**: http://localhost:5000/
- **Produkty**: http://localhost:5000/produkty
- **Sto?y**: http://localhost:5000/produkty/stoly
- **???ka**: http://localhost:5000/produkty/lozka
- **Schody**: http://localhost:5000/produkty/schody
- **O nas**: http://localhost:5000/o-nas
- **Kontakt**: http://localhost:5000/kontakt
- **API Produkty**: http://localhost:5000/api/produkty

## Struktura bazy danych

### Tabela: produkty
- id (INTEGER, PRIMARY KEY)
- nazwa (TEXT)
- kategoria (TEXT)
- opis (TEXT)
- cena (REAL)
- wymiary (TEXT)
- material (TEXT)
- zdjecie (TEXT)
- aktywny (INTEGER)

### Tabela: zapytania
- id (INTEGER, PRIMARY KEY)
- imie (TEXT)
- email (TEXT)
- telefon (TEXT)
- wiadomosc (TEXT)
- data_utworzenia (TIMESTAMP)

## Dane kontaktowe

- **W?a?ciciel**: Marcin Grzanka
- **Firma**: MGWood
- **Adres**: 58-512 Rybnica 140 lok. 1
- **Telefon**: 695 129 969
- **Email**: mgwood102@gmail.com

## Funkcje dla rozwoju

### Dodawanie nowych produkt?w

Mo?esz doda? nowe produkty bezpo?rednio do bazy danych lub poprzez rozszerzenie aplikacji o panel administracyjny.

### API

Dost?pne endpoint API:
- `GET /api/produkty` - Lista wszystkich produkt?w w formacie JSON

## Licencja

? 2024 MGWood - Marcin Grzanka. Wszystkie prawa zastrze?one.
