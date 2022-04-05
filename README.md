# Instagram Clone
Instagram Clone. Built with Django.

## Table of contents
  <!-- - [Screenshot](#screenshot) -->
  - [Project Visual](#Screenshot)
  - [Project Description](#Project-description) 
  - [Built with](#built-with)
  - [Usage](#Getting-Started)
  - [License & Copywright Information](#License-and-Copywright-Information)
  - [Author](#author)

---
___

### Screenshot
![Website](static/images/image.png)
___
---
### Introduction
Instahram Clone.
A basic clone of the famos Instagram app. Performs user authentication, stores user data in a database. Images are also stored in a CDN.

The goal of this project is to provide minimalistic django configurations that stores your image files on a CDN and that anyone can use, It also _just works_ out of the box and has the basic setup you can expand on. 

Project is written with django 4.0.3 and python 3 in mind.

---
___

### BDD
 #### Context
  Given that a user creates an account.
 #### Event
  When the user logs in or interacts with the page
#### Outcomes
  Then a user should be able to create a new Image/post with a caption.\
  Each Image should have an edit and delete button.\
  Each post should have a comment section and other users can share their opinions.\
  Each post should have a like and unlike option.\
  When the user tries to query the data(from an Post's details e.g caption or user) only relevant posts that much the specific query should be displayed.

* [x] A user can create an account and login.
* [x] Users can make posts.
* [x] Users can comment and like on posts
* [x] Each user has a user profile.
* [x] Each profile filters that specific users details.
* [x] Data can be queried using the search feature.

---
___
### Built with / Technologies Used

- Python
    - Django
    - PostgresSQL
    - Cloudinary
---
___


# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:LemmyMwaura/Instagram-Clone.git
    $ cd Instagram-Clone
    
Activate the virtual environment for the project.

     $ pipenv shell
    
Install project dependencies:

    $ pipenv install
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

<br>

---
___

## License and Copywright Information
(c) Stephen Lemmy Mwaura, Software Engineer.

Licensed under the [MIT License](LISENCE)

---
___
## Author 
Hi there, I'm Lemmy and i love to code. Connect With me:

- 🎱 Github - [@lemmyMwaura](https://github.com/LemmyMwaura)

---
___

