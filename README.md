Django Blog Platform

A blog platform built using Python and Django where users can create, manage, explore, and comment on blog posts.

Features
User registration and login
User authentication and logout
Create, edit, and delete blog posts
Public and private blog visibility
Explore public blog posts
View individual blog details
User profile pages
Comment on public blog posts
User-specific blog dashboard
Django ORM for database operations
Technologies Used
Backend: Python, Django
Frontend: HTML, CSS
Database: SQLite
Version Control: Git and GitHub
Project Structure
text
myproject/
│
├── codehere/
│   ├── migrations/
│   ├── templates/
│   │   ├── blog_detail.html
│   │   ├── create_blog.html
│   │   ├── dashboard.html
│   │   ├── edit_blog.html
│   │   ├── explore_blogs.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── profile.html
│   │   └── signup.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md

Installation and Setup
1. Clone the repository
bash
git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the project directory
bash
cd myproject

3. Create a virtual environment
bash
python -m venv venv

4. Activate the virtual environment

Windows:

bash
venv\Scripts\activate

5. Install dependencies
bash
pip install -r requirements.txt

6. Apply migrations
bash
python manage.py migrate

7. Run the development server
bash
python manage.py runserver


Open your browser:

http://127.0.0.1:8000/

Database Models
Blog
user
title
content
created_at
is_public
Comment
blog
user
content
created_at
Learning Outcomes

Through this project, I practiced:

Django models and database relationships
Django authentication
CRUD operations
Django views and URL routing
Template rendering
QuerySets and Django ORM
User permissions and access control
Future Improvements
Responsive UI design
Blog search functionality
Pagination
User profile editing
Blog likes and bookmarks
Image uploads
Author

Developed as a personal learning project to practice Python and Django web development.