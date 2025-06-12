# 🗃️ Inventory Management Web App

This is a Flask-based inventory management system with user and admin dashboards, item tracking, purchase management, and PDF bill generation using ReportLab. The project supports deployment on [Vercel](https://vercel.com) using serverless functions.

## 🔧 Features

- 🧾 User Signup/Login & Admin Login
- 📦 Add, Update, and Delete Items
- 📍 Location-based Inventory View
- 📉 Stock Status: In Stock, Low Stock, Out of Stock
- 💸 Item Purchase & Order History
- 📄 PDF Bill Generation using ReportLab
- 🌐 Hosted on Vercel (serverless)

---

## 🗂️ Project Structure

inventory-app/
├── api/
│ └── index.py # Main Flask application
├── templates/ # HTML templates (Jinja2)
│ ├── index.html
│ ├── user_login.html
│ └── ...
├── static/ # Static files (CSS, JS, images, generated PDFs)
│ └── bill.pdf
├── inventory.db # SQLite3 database
├── requirements.txt # Python dependencies
├── vercel.json # Vercel configuration
└── README.md

git clone https://github.com/yourusername/inventory-app.git
cd inventory-app
pip install -r requirements.txt
python api/index.py

Email: admin@gmail.com
Password: admin123


📃 License
MIT License — feel free to use and modify this project.

Built with ❤️ by Yakshith S Y


---

Let me know if you'd like a version with screenshots, badges, or GIF previews!
