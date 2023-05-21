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

---

### **Epic 6: Documentation and Testing**

Create both my TESTING.md and this README.md to document the creation and implementation to this project.

---

## **Non Essential Epics**

### **Epic 7: User Accounts**

User accounts have been extended slightly to allow for email and phone numbers to be taken on registration and then used to autopopulate the bookings form. My plan was for more extension to the model and to use it for the creation of user generated restaurants. 

Extending the user profile while using django-allauth turned out to be fairly cumbersome and lacking in documentation so due to time constraints I didn't fully realize this feature.

---

### **Epic 9: Unique Error Pages**

Low down the list but easy to implement I added unique 404 and 500 error pages. Although this was only realistically one task I added this as an epic as it was something I had never done and contained a bit of both front end and django work. 

---


## **Unresolved Epics**

### **Epic 8: Restaurant Creation**

Something planned for the future I will 100% add in my own time but having two types of accounts. One for customers and restaurants and then another DB model for restaurants was just too much to attempt while first getting my head around django.

---

## Skeleton Plane

### Wireframes 

Using [Balsamiq](https://balsamiq.com/wireframes/) I created the skeleton and initial layout.

### Schema

## Scope Plane

- Landing page which conveys what the website is used for.
- Allow a user to create an account which will then allow them to make, update and delete bookings.
- Make sure the website is functional and presentable in all formats and screen sizes.

## Structure Plane 

### Features

#### Navbar

![navbar](/documentation/navbar.png)
![navbar-closed](/documentation/navbar-closed.png)
![navbar-open](/documentation/navbar-open.png)

Navbar was designed with the glass and 'clean' motif I had planned for the website, it features throughout the website and is responsive due to bootstrap stylings.

Options available change depending on the logged in status of the user.

#### Hero/Landing 

![Hero](/documentation/desktop-img.png)

### Design 

#### Colour pallette 

![Colour pallette](/documentation/colour-pallette.png)

I knew I wanted a light blue teal as the main colour throughout. Then instead of just a pure black the off black I have included contains a hint of blue. As a tertiary I thought having a unique colour for the usual error and delete red that I could use in other places too without having too many colors. Another "Colour" used throughout is a white with an alpha value of less than 1 with a blur effect added to give of a glassy feel.

#### Typography 

For typography I decided to go for a singular font from [Google Fonts](https://fonts.google.com) called [Wix Madefor Display](https://fonts.google.com/specimen/Wix+Madefor+Display). After trying a few out I felt it meshes well with the soft, rounded feel I have aimed for with the design. 

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
- [MDB-Material Design Bootstrap:](https://mdbootstrap.com/)
    - MDB was used for some of the theming.
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

The live deployed application can be found deployed on [Heroku](https://simply-service.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: simply-service).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.
- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |
| `EMAIL_KEY` | your own Gmail pw/key |

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("EMAIL_KEY", "your own Gmail pw/key")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

Note: To get the email functionality working for your own local project, you will need to update the settings.py file variable for `EMAIL_HOST_USER` to your own email address.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/EeeBeeDee/simply-service) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/EeeBeeDee/simply-service.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/EeeBeeDee/simply-service)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/EeeBeeDee/simply-service)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

# Testing

All Testing is documented separately in the [TESTING.md](/TESTING.md) file.

# Credits

- [Login mixin for classes](https://stackoverflow.com/questions/72602785/django-attributeerror-function-object-has-no-attribute-as-view-showing-in)
- [Understanding reverses](https://stackoverflow.com/questions/11241668/what-is-reverse)
- [Update and edit databases](https://www.youtube.com/watch?v=jCM-m_3Ysqk)
- [Net Ninja in general but this one in particular linking forms to model and frontend](https://www.youtube.com/watch?v=jBGmqxpw0V8)
- [Go directly to a section of a page with a django link](https://stackoverflow.com/questions/55055523/how-to-configure-django-url-to-point-to-a-specific-section-in-the-page)
- [Update form instances](https://www.youtube.com/watch?v=jCM-m_3Ysqk)
- [Help customizing all auth forms and models](https://dev.to/gajesh/the-complete-django-allauth-guide-la3)