from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mgwood-secret-key-2024'

DATABASE = 'mgwood.db'

def get_db():
    """Po??czenie z baz? danych"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicjalizacja bazy danych"""
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Tabela produkt?w
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produkty (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nazwa TEXT NOT NULL,
                kategoria TEXT NOT NULL,
                opis TEXT,
                cena REAL,
                wymiary TEXT,
                material TEXT,
                zdjecie TEXT,
                aktywny INTEGER DEFAULT 1
            )
        ''')
        
        # Tabela zapyta? kontaktowych
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS zapytania (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                imie TEXT NOT NULL,
                email TEXT NOT NULL,
                telefon TEXT,
                wiadomosc TEXT NOT NULL,
                data_utworzenia TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Dodanie przyk?adowych produkt?w
        produkty = [
            # Sto?y
            ('St?? d?bowy rustykany', 'stoly', 'Masywny st?? wykonany r?cznie z litego drewna d?bowego. Idealny do salonu lub jadalni.', 2500.00, '180x90x76 cm', 'D?b lite', 'stol1.jpg', 1),
            ('St?? industrialny', 'stoly', 'Nowoczesny st?? w stylu loftowym z d?bowym blatem i metalowymi nogami.', 2200.00, '200x100x75 cm', 'D?b + metal', 'stol2.jpg', 1),
            ('St?? okr?g?y d?bowy', 'stoly', 'Elegancki okr?g?y st?? z litego d?bu, idealny dla rodziny.', 2800.00, '?120x75 cm', 'D?b lite', 'stol3.jpg', 1),
            
            # ???ka
            ('???ko d?bowe CLASSIC', 'lozka', 'Solidne ???ko z litego drewna d?bowego z wygodnym zag??wkiem.', 3500.00, '160x200 cm', 'D?b lite', 'lozko1.jpg', 1),
            ('???ko MODERN', 'lozka', 'Minimalistyczne ???ko w nowoczesnym stylu, wykonane z najwy?szej jako?ci drewna.', 3200.00, '180x200 cm', 'D?b lite', 'lozko2.jpg', 1),
            ('???ko RUSTIC', 'lozka', '???ko w stylu rustykalnym z naturalnym wyko?czeniem drewna.', 3800.00, '160x200 cm', 'D?b lite', 'lozko3.jpg', 1),
            
            # Schody
            ('Stopnie d?bowe proste', 'schody', 'Stopnie schodowe z litego d?bu, grubo?? 4 cm. Idealne do schod?w betonowych.', 450.00, '100x30x4 cm', 'D?b lite', 'schody1.jpg', 1),
            ('Stopnie d?bowe zabiegowe', 'schody', 'Stopnie zabiegowe wykonane z litego d?bu, dostosowane do Twoich wymiar?w.', 550.00, 'Wymiar indywidualny', 'D?b lite', 'schody2.jpg', 1),
            ('Komplet schod?w d?bowych', 'schody', 'Kompleksowe rozwi?zanie - stopnie, podstopnice i por?cze z litego d?bu.', 8500.00, 'Indywidualnie', 'D?b lite', 'schody3.jpg', 1),
        ]
        
        cursor.executemany('''
            INSERT INTO produkty (nazwa, kategoria, opis, cena, wymiary, material, zdjecie, aktywny)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', produkty)
        
        conn.commit()
        conn.close()
        print("Baza danych zosta?a zainicjalizowana!")

@app.route('/')
def index():
    """Strona g??wna"""
    return render_template('index.html')

@app.route('/produkty')
def produkty():
    """Lista wszystkich produkt?w"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produkty WHERE aktywny = 1 ORDER BY kategoria, nazwa')
    produkty = cursor.fetchall()
    conn.close()
    return render_template('produkty.html', produkty=produkty)

@app.route('/produkty/<kategoria>')
def produkty_kategoria(kategoria):
    """Produkty z danej kategorii"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produkty WHERE kategoria = ? AND aktywny = 1 ORDER BY nazwa', (kategoria,))
    produkty = cursor.fetchall()
    conn.close()
    return render_template('produkty.html', produkty=produkty, kategoria=kategoria)

@app.route('/produkt/<int:id>')
def produkt(id):
    """Szczeg??y produktu"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produkty WHERE id = ?', (id,))
    produkt = cursor.fetchone()
    conn.close()
    if produkt:
        return render_template('produkt.html', produkt=produkt)
    return "Produkt nie zosta? znaleziony", 404

@app.route('/kontakt', methods=['GET', 'POST'])
def kontakt():
    """Strona kontaktowa"""
    if request.method == 'POST':
        imie = request.form.get('imie')
        email = request.form.get('email')
        telefon = request.form.get('telefon')
        wiadomosc = request.form.get('wiadomosc')
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO zapytania (imie, email, telefon, wiadomosc)
            VALUES (?, ?, ?, ?)
        ''', (imie, email, telefon, wiadomosc))
        conn.commit()
        conn.close()
        
        return render_template('kontakt.html', sukces=True)
    
    return render_template('kontakt.html')

@app.route('/o-nas')
def o_nas():
    """Strona O nas"""
    return render_template('o_nas.html')

@app.route('/api/produkty')
def api_produkty():
    """API - lista produkt?w"""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produkty WHERE aktywny = 1')
    produkty = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(produkty)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
