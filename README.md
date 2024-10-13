# News Website

## Introduction
**Project Name:** News Website  
**Project Objective:** To create a web application for reading, editing, and publishing news articles, showcasing my skills and experience developed as part of the Python Profession course at Armenian Code Academy (ACA).

## Development Process
**Project Start Date:** September 19, 2024  
**Development Stages:** Design, implementation, testing.

## Technologies
- **Programming Language:** Python
- **Framework:** Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Containerization:** Docker
- **Version Control System:** GitHub

## Achievements
### Functionality
Key features include:
- Creation and editing of news articles.
- Assigning categories to each article.
- Adding images.
- Publishing and deleting articles.
- Viewing the homepage with the latest news.
- Filtering news by categories.
- Full view of individual articles.
- Editing the view count.

### Problems and Solutions
Throughout the development process, both minor and significant issues arose. I documented each one, which helped me find solutions and improve my analytical and development skills.

## Conclusion
**Takeaways:** Working on this project was a valuable experience. I learned far more than I would have by just reading or watching tutorial videos. Practical experience significantly enhanced my programming skills and boosted my confidence.

## Technical Documentation
### Introduction
**Documentation Purpose:** This documentation is intended for developers who will work with the project.

### Application Architecture
**Overview of the Application:** News Website is a web application for reading, editing, and publishing news articles.

#### Application Components:
- **Frontend:** HTML, CSS, and Bootstrap for displaying news and forms.
- **Backend:** Django for handling requests and interacting with the database.
- **Database:** SQLite for storing news, user, and category data.
- **Docker:** Ensures a consistent deployment environment.

### Installation and Deployment
#### Installation Steps
For convenience, please follow the copy-and-paste principle: copy the commands from this README and paste them into your Git Bash terminal or your IDE.

#### Local Setup
1. **Clone the GitHub repository:**
   ```bash
   git clone https://github.com/HarutyunDanielyan/django-site.git && cd django-site
   ```

2. **Create and activate a virtual environment:**
   - For **Linux/macOS:**
   ```bash
   python -m venv venv && source venv/bin/activate
   ```
   - For **Windows:**
   ```bash
   python -m venv venv && source venv/Scripts/activate
   ```

3. **Install all necessary dependencies from the `requirements.txt` file:**
   ```bash
   python -m pip install --upgrade pip && pip install -r testsite/requirements.txt
   ```

4. **Run migrations, create a superuser, and start the application:**
   ```bash
   cd yatube && \
      python manage.py makemigrations && \
      python manage.py migrate && \
      python manage.py prepare_load_data && \
      python manage.py loaddata dump.json && \
      python manage.py createsuperuser && \
      python manage.py runserver && cd ..
   ```

5. **The server will start locally at:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage
### Instructions for Use
**Overview:** News Website allows users to view, create, and edit news articles.

#### Viewing News
The homepage displays the latest news. Click on the article title to open the full content.

#### Creating a New Article
1. Click the "Create Article" button.
2. Fill out the form with the title, content, and category.
3. Click the "Save" button.

#### Editing and Deleting Articles
- To edit an article, navigate to it and click the "Edit" button.
- To delete an article, click the "Delete" button and confirm the action.

### Additional Information
1. **Feedback:** If you have any questions, you can reach out to us through the 
feedback section on our website or send an email to [danielyan.harutyun@inbox.ru](mailto:danielyan.harutyun@inbox.ru).

## License
This project is released without a license.

**Author:** Danielyan Harutyun
