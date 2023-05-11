# Simply | Service

![Website homepage](documentation/desktop-img.png)

Simply Service is a hospitality app designed to be the one stop shop for restaurants and customers to combat the use of individual booking systems and websites of restaurants. This is my portfolio project 4 for Code Institutes full stack diploma.

[Link to Simply | Service](https://simply-service.herokuapp.com/)

# UX

# The Stratagy Plane

## Agile Planning

This project has been approached with an Agile mindset. Using epics, tasks and user stories. I have laid out not only what I plan to achieve with this website but what I expect users hitting the home page will want. This approach has helped to compartmentalize development and make what I hope to achieve much more manageable. 

This can be seen implemented on my projects [Kanban.](https://github.com/users/EeeBeeDee/projects/3/views/1)

## Epics and Tasks

The First 6 Epics are essential and the minimum needed to deliver the basic application so their tasks were prioritized with any following epics designated as extras with descending priority.

### **Epic 1: Project Initialization & Deployment**

This includes the initial project setup, installing the framework, dependencies and libraries. Setting up ElephantSQL. Configuring our settings.py file and Heroku Application so that everything is connected and running on the live site as early as possible.

---

### **Epic 2: Databases & Migration**

This includes the model setup for the booking system and general connection to the DB.  Any extra apps will have their model set up included with them. 

---

### **Epic 3: Bookings**

With the model already set up this included the booking form creation and views creation, making sure post and get requests worked as intended and information was retrieved in a parsable way.

---

### **Epic 4: Front End Design**

With the back end functionality in place this epic included all design and front end functionality. Making information easily accessible.

---

### **Epic 5: Responsiveness** 

As Bootstrap was used fairly extensively, not many media queries were needed to facilitate a responsive design and this epic ended up being a lot smaller than I had imagined when planning the site.

### **Epic 6: Documentation and Testing**

## **Non Essential Epics**

### **Epic 7: User Accounts**

### **Epic 8: Restaurant Creation**

### **Epic 9: Unique Error Pages**


## **Unresolved Epics**

## Skeleton Plane

### Wireframes 

Using [Balsamiq](https://balsamiq.com/wireframes/) I created the skeleton and initial layout.

### Schema


# Technologies Used

### Languages and Frameworks Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python3](https://www.python.org/)
-   [Django](https://www.djangoproject.com/)

### Libraries and Django Plugins Used
- [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used for the chevron arrows used for navigation through the site
- [Bootstrap:](https://getbootstrap.com/)
    - Bootstrap was used manly for formatting, positioning and responsive design throughout the project.
- [JQuery:](https://jquery.com/)
    - Used very lightly as not much JS was needed in the final version of the website.
- [Django-Allauth:](https://django-allauth.readthedocs.io/en/latest/index.html)
    - Used to control user profile functionality.

### Tools Used

- [VScode](https://code.visualstudio.com/)
    - Vscode was my code editor for this project.
- [Git](https://git-scm.com/)
    - Git was used for version control and to Push to GitHub.
- [GitHub:](https://github.com/)
    - GitHub is used to store the project's code remotely and then to host the static website on GitHub Pages.
- [Heroku:](https://signup.heroku.com/login)
    - Heroku is where the app is hosted online.
- [ElephantSQL:](https://www.elephantsql.com/)
    - ElephantSQL is where the database is hosted
- [Cloudinary:](https://cloudinary.com/)
    - Cloudinary is connected to the project but not fully utilized due to time constraints, future plans are to have it host pictures restaurants can use for their own generated 

### Linters used 

-   [W3C - HTML](https://validator.w3.org/)
-   [Jigsaw - CSS](https://jigsaw.w3.org/css-validator/)
-   [JSHint - JS](https://jshint.com/)
-   [PEP8CI - Python](https://pep8ci.herokuapp.com/)


# Deployment

### Local Deployment

In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/EeeBeeDee/simply-service.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/EeeBeeDee/simply-service)

### Remote Deployment


These steps can be taken to deploy the cloned site from above to [Heroku](https://signup.heroku.com/login):

- Create an account with [Heroku](https://signup.heroku.com/login).
- Once on your Dashboard select "New" first followed by "Create a new app".
- Create a unique name for the app. It must be unique as it will be used for the applications URL.
- Once created you will see a "Settings" button at the end of this apps dashboards navbar.
- Find the config Vars you will have to create key value pairs that match up with your settings.py file. I suggest using an env.py file which you include in your .gitignore file. A good guide on how to do so can be found [here.](https://www.twilio.com/blog/environment-variables-python)
- Your key value pairs should look like this:
    - SECRET_KEY: The Secret Key for your project, this can be anything you choose.
    - DATABASE_URL: The URL from your ElephantSQL dashboard. Use the [ElephantSQL Docs](https://www.elephantsql.com/docs/index.html) if you are not sure how.
    - CLOUNDINARY_URL: The URL from your Cloudinary account.
- Then navigate to "Deploy". 
- Use the connect to github button then search for the correct repo then select which branch is to be deployed, most likely main by default.

# Testing

All Testing is documented separately in the [TESTING.md](/TESTING.md).

