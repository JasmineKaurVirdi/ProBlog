# 📰 Django Blog Web Application

A full-stack *Django-based Blog Web App* that allows users to register, log in, create, edit, and delete blog posts.  
Built using *HTML, CSS, Bootstrap, Python, Django, and **SQLite database*.

---

## 🚀 Features

- 🔐 User Authentication (Register, Login, Logout)
- ✍️ Create, Edit, and Delete Blog Posts
- 🏠 Homepage showing all posts
- 👤 User-specific posts page
- 💾 SQLite database integration
- 🎨 Responsive UI using *Bootstrap*
- 🧠 Django Template Inheritance (base.html)
- 🧹 Admin Panel for managing posts

---

## 🧩 Tech Stack

*Frontend:*  
- HTML5  
- CSS3  
- Bootstrap 5  

*Backend:*  
- Django (Python)  
- SQLite (Default Django Database)

*Deployment:*  
- Render (for hosting)  
- GitHub (for version control)

---

## ⚙️ Installation and Setup

Follow these steps to run the project locally 👇  

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2️⃣ Create a virtual environment

python -m venv venv

3️⃣ Activate the environment

On Windows:


venv\Scripts\activate

On macOS/Linux:


source venv/bin/activate

4️⃣ Install dependencies

pip install -r requirements.txt

5️⃣ Run migrations

python manage.py makemigrations
python manage.py migrate

6️⃣ Run the server

python manage.py runserver

Now open your browser and go to 👉 http://127.0.0.1:8000/


---

🗂️ Project Structure

blogsite/
│
├── blog/                     # Main Django app
│   ├── migrations/
│   ├── templates/blog/        # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── edit_post.html
│   │   └── post_detail.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── blogsite/                 # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── Procfile


---

🧑‍💻 Author

Jasmine Kaur
💼 Django Developer | 💻 Web Development Enthusiast
🌐 https://github.com/JasmineKaurVirdi


---

📜 License

This project is licensed under the MIT License — feel free to use and modify it for your own learning or projects.


---

⭐ If you like this project, don’t forget to star the repo on GitHub! 🌟

---