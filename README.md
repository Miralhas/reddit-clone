<h1 align="center"> ⬇️ Simple Reddit  Clone ⬆️ </h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-v0.1-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/Miralhas/reddit-clone" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
</p>

> This project is a simplified clone of Reddit, built using Django. It allows users to register, login, and post content. Other users can then comment on these posts and vote them up or down. The posts can be searched by their title and each user has a profile page displaying their posts.

### 🏠 [Homepage](https://github.com/Miralhas/reddit-clone)

![image](https://github.com/Miralhas/poll-app/assets/89564433/4bcfe6ee-ff75-4fd9-ab8f-9601cdad502c)

## Features
 - **User Registration and Authentication:**
	 - Users can register, login, and logout. The Django's built-in authentication system is used to manage these functionalities.
	  <br>
 - **Post Creation and Management:**
	 - Users can create, view, edit and delete posts. Each post has a title, content, and a vote count.
	<br>
- **Commenting on Posts:**
	- Users can comment on posts and delete their comments.
	<br>
- **Post Voting:**
	- Users can upvote or downvote posts. The vote count for each post is displayed and updated accordingly.
    <br>
- **Search Functionality:**
	- Users can search for posts based on their title. The search results are displayed on a separate page.
    <br>
- **User Profiles:**
	- Each user has a profile page that displays their owned posts.
    <br>

## Installation and Running the Project
To install and run this project locally, follow these steps:
1. Clone the repository to your local machine.
	```bash
	git clone https://github.com/your_username/reddit-clone.git
	```
2. Navigate into the project directory.
	```bash
	cd reddit-clone
	```
4. Install the django library.
	```python
	pip install django
	```
5. Run the Django migrations.
	```python
	python manage.py makemigrations
	python manage.py migrate
	```
6. Start the Django development server.
	```python
	python manage.py runserver
	```
	
Now, you can visit `http://localhost:8000` in your browser to view the application.

## Author

👤 **Victor Miralhas**

- Github: **[@Miralhas](https://github.com/Miralhas)**


## 📝 License

Copyright © 2023 **[Victor Miralhas](https://github.com/Miralhas)**.<br />
