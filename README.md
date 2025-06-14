Inventory Management Web App

Inventory Management Web App
This is a Flask-based inventory management system designed to help businesses manage their inventory efficiently. The system includes user and admin dashboards, item tracking, purchase management, and PDF bill generation.

deployment on [Vercel](https://vercel.com) using serverless functions.

Features

- 🧾 User Signup/Login & Admin Login
- 📦 Add, Update, and Delete Items
- 📍 Location-based Inventory View
- 📉 Stock Status: In Stock, Low Stock, Out of Stock
- 💸 Item Purchase & Order History
- 📄 PDF Bill Generation using ReportLab
- 🌐 Hosted on Vercel (serverless)

Requirements
Python 3.8 or higher
Flask 2.0 or higher
Docker 20.10 or higher

Installation
Clone the repository using git clone https://github.com/yakshith123/inventory-app.git
Create a new virtual environment using python -m venv venv
Activate the virtual environment using source venv/bin/activate
Install the required dependencies using pip install -r requirements.txt
Run the application using flask run

Dockerization
Build the Docker image using docker build -t inventory-app .
Run the Docker container using docker run -p 5000:5000 inventory-app

API Documentation
The API documentation is available at /api/docs

License
This project is licensed under the MIT License.
