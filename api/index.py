from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import base64
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os

app = Flask(__name__,
            template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
            static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'))
app.secret_key = 'qwertyuiopasdfghjklzxcvbnm'

def generate_bill_reportlab(row, output_filename="static/bill.pdf"):
    category, item, location, description, price = row
    c = canvas.Canvas(output_filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, height-50, "INVOICE / BILL")

    c.setFont("Helvetica", 12)
    c.drawString(50, height-80, f"Bill Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height-130, "Item Details:")

    c.setFont("Helvetica", 12)
    y_position = height-160
    details = [
        ("Item:", category),
        ("Category:", item),
        ("Location:", location),
        ("Description:", description),
        ("Price:", f"Rs. {price}")
    ]

    for label, value in details:
        c.drawString(50, y_position, f"{label} {value}")
        y_position -= 20

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y_position-30, f"Total: Rs. {price}")

    c.setFont("Helvetica-Oblique", 10)
    c.drawCentredString(width/2, 50, "Thank you for your business!")
    c.save()
    print(f"Bill generated successfully: {output_filename}")

# Database setup
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    item TEXT,
    quantity INTEGER,
    location TEXT,
    description TEXT,
    price TEXT,
    image TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    password TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id TEXT,
    category TEXT,
    item TEXT,
    quantity INTEGER,
    location TEXT,
    description TEXT,
    price TEXT,
    image TEXT,
    email TEXT
);
""")
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

# Remaining route handlers should be added below here as needed.

if __name__ =="__main__":
    app.run(debug=True)

def handler(event, context):
    from werkzeug.middleware.dispatcher import DispatcherMiddleware
    from werkzeug.wrappers import Response
    return DispatcherMiddleware(Response('Not Found', status=404), {
        "/": app
    })
