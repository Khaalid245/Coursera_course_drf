# 🧠 Django & DRF Projects Collection

This repository includes a collection of small projects built during course learning. Each project demonstrates specific backend development skills using Django and Django REST Framework (DRF), such as database modeling, API creation, filtering, ordering, and search functionality.

---

## 📁 Projects Overview

This repo contains 3 projects:

1. 📚 **Bookshop** – Traditional Django website (no REST API)
2. 🔗 **DRF BookList API** – REST API using Django REST Framework
3. 🍋 **Little Lemon API** – DRF with filtering, searching, and ordering

---

## 📚 Bookshop (Django Only)

A traditional Django web application that simulates a simple bookshop.

- **Directory:** `Bookshop/`
- **Type:** Django (no DRF)

### 🚀 How to Run:

```bash
cd Bookshop
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### ✅ Features:
- Book model with title, author, and price
- Admin panel for book management
- Templates and views (no API)

---

## 🔗 DRF BookList API

This project is an API version of the book list using Django REST Framework. It focuses on serialization, API views, and RESTful operations.

- **Directory:** `DRF_BookList_API/`
- **Type:** Django REST Framework

### 🚀 How to Run:

```bash
cd DRF_BookList_API
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### ✅ Features:
- `Book` model with REST endpoints
- CRUD operations via API
- DRF views and serializers
- JSON responses with `GET`, `POST`, `PUT`, `DELETE`

---

## 🍋 Little Lemon API (Filtering + Search + Ordering)

A Django REST Framework project built for practicing **filtering**, **searching**, and **ordering** of data. It simulates a restaurant menu management system.

- **Directory:** `LittleLemon/`
- **Type:** Django REST Framework

### 🚀 How to Run:

```bash
cd LittleLemon
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### ✅ Features:
- `MenuItem` and `Category` models
- Nested serializers and foreign key relations
- Filtering by fields like `price` and `inventory`
- Search functionality on category titles
- Ordering support for price and inventory

### 🔎 Example Queries:

```
/api/menu-items/?search=Main
/api/menu-items/?price__lt=10
/api/menu-items/?ordering=inventory
```

---

## ⚙️ Common Setup for All Projects

All projects use the following setup:

```bash
# 1. Navigate into the project folder
cd <project-folder>

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate         # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the server
python manage.py runserver
```

---

## 🛠 Technologies Used

- Python 3.x
- Django
- Django REST Framework (DRF)
- SQLite (default database)
- `django-filter` for advanced filtering
- `djoser`, `SimpleJWT` for authentication (if included)

---

## 👨‍💻 Author

**Khalid Abdirahman Abdillahi**  
- 🌍 From Somalia  
- 🎓 Student at African Leadership University & KIIT University  
- 💡 Passionate about education, backend development, and community growth  
- 📫 [Your GitHub or LinkedIn Profile URL]

---

## 📌 Notes

- Each project folder contains its own `requirements.txt`
- Projects are independent; you can run them separately
- Best viewed and run in a Python virtual environment

---

## 🤝 Acknowledgements

Thanks to:
- Coursera instructors
- Django and DRF communities
- All who helped in creating these learning projects
