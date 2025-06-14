# Inventory Management Web App

This is a Flask-based inventory management system designed to help businesses manage their inventory efficiently. The system includes user and admin dashboards, item tracking, purchase management, and PDF bill generation.

## Deployment
Live Demo

You can view the live demo of the application at the following link:
https://inventory-app-6nkm.onrender.com

## Features

- 🧾 User Signup/Login & Admin Login
- 📦 Add, Update, and Delete Items
- 📍 Location-based Inventory View
- 📉 Stock Status: In Stock, Low Stock, Out of Stock
- 💸 Item Purchase & Order History
- 📄 PDF Bill Generation using ReportLab
- 🌐 Hosted on Vercel (serverless)

## Requirements

- Python 3.8 or higher
- Flask 2.0 or higher
- Docker 20.10 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yakshith123/inventory-app.git

## Create a new virtual environment:

2. python -m venv venv
Activate the virtual environment:

2 a. On macOS/Linux:
source venv/bin/activate
2 b.On Windows:
venv\Scripts\activate

## Install the required dependencies:
pip install -r requirements.txt

## Run the application:
flask run

## Dockerization
Build the Docker image:
docker build -t inventory-app .

## Run the Docker container:
docker run -p 5000:5000 inventory-app

## API Documentation
The API documentation is available at /api/docs.
Test Instructions
## Run Tests:

Ensure your virtual environment is activated.
Run the following command to execute tests:
pytest
## Test Coverage:

To check test coverage, you can use:
pytest --cov=your_module_name

## License
This project is licensed under the MIT License.


