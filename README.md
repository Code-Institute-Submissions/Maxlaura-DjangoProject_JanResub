

## Overview

[The News Paper](https://newsdemoapp.herokuapp.com/) is a concept website where user is able to read the latest news published by the journalistic editorial staff.

The platform offers also Premium news under a monthly payment fee. The concept is that not all news area freely readable, there can be also "specific" news wich are under payment. 

The news are dispayed using table for a fully responsive and mobile friendly website.

------



## UX

### User

As a user what i am able to do?

- Access the free news displayed on the home page
- Create a new account
- Login into your existing account
- Subscribe with for the Premium news under a montly fee
- Get access to exclusive Premium News

### Design

The project is very clean, user have the main and core functionality availlable on a responsive web application. The goal was to keep it as clean as possibile avoiding user on doing mistakes using the app.

### Wireframes

The project wireframes was build using wireframe.cc. An online free tool for online wireframes.

#### Base 

[Here](https://wireframe.cc/I85El6) is the base wireframe, used to describe and understand also the Base.html template.


#### Login (Sing in)
[Here](https://wireframe.cc/4rOKw4) is the customer login page. The page describes all inputs user needs to fill to correctly login.

#### New account (Sign up)
[Here](https://wireframe.cc/T1oBCe) is the sign up page. This page also is very simple and very clear, because this is the goal of the app, being clear and fast to the final user.

#### Premium news
[Here](https://wireframe.cc/I85El6) same template as the homepage, with dedicated premium news. This is shown after payment.


### Code structure

The project code structure is showed below. It tries to be as clean as possibile.

```bash
.
├── newspaper
│   ├── static
│   │   ├── admin
│   │   ├── css
│   │   ├── vendor
│   │   ├── main.js
│   │   └──  payment.js
│   └── admin.py
│   └── apps.py
│   └── models.py
│   └── urls.py
│   └── views.py
├── templates
│   ├── account
│   │   ├── base.html
│   │   ├── login.html
│   │   └──  signup.html
│   ├── newspaper
│   │   ├── base.html
│   │   ├── index.html
│   │   └──  premium.html
│   ├── cancel.html
│   ├── success.html
└── manage.py

```

### Database structure
Everything is based on SQLite3 DB, the main db is hosted on free tire.
There are 2 main collections: "Users" and "News"

User:
```json
{
    "username" : "",
    "password" : "",
    "email" : "",
    "is_premium":""
}
```
News:
```json
{
    "title" : "",
    "description" : "",
    "is_premium" : "",
    "creation_date" : "",
    "creation_time" : ""
}
```

### Features to Implement

Would be cool to have those features:

- Detailed page for the news
- Include social media like whatsapp or telegram for direct messages and share the news


---

## Technologies Used

The following list contains used technology for this project.

- Python 
- PostgreSQL
- Bootstrap
- Django
- allauth
    - Used to handle the login and signup part, user part
- stripe api
    - Used to setup the montly payment fee


### Other Tools

- Wireframecc
    - Used to create web app wireframes


------

## Testing

This is the list of testing has done on the web application.

### W3C Validation
A W3C HTML validation test has done on the website wich can be found [here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewsdemoapp.herokuapp.com%2F) to check out if everything is correct and no errors appears.

### User testing
The list of tests that has been done:
- Test insert a new news
    - Test insert a new news with different data, this part is done into the /admin part of the web application
- Check the visibility of the inserted news
    - The last news inserted must appear first on the list of the news
- Check the inserting also of premium newses
- Test the login
    - Check if fields are correclty validated
- Check the signup
    - Check if fields are correclty validated
    - Check if correctly received the signup email for email address confirmation
    - Try to login after the signup
- Access premium news
    - Test if accessibility to premium news is locked until a correct payment
- Stripe montly payment
    - Test, after a login, to purchase the montly premium news, and if all redirects works correctly, website is currently on sandbox
- Test if the website is responsive, open it with the browser and using mobile devices, also try to resize the window to see if the menu handles accordly.



------



### Deployment

The project is hosted on Github and uses Heroku as main platform for deployment. In order to contibute to the repository you should have a Github Account. A Heroku account is also suggested. 

#### Prerequisites

In order to contribute to this repository you will need to have the following installed:

- Python 3.8.3 or higher
- Git version control
- Code editor, for this project Pycharm was used

#### Development

How to local deploy the project.

##### Requirements

After clonig the project to your local machine, you will need to install all the projects dependencies type `pip install -r requirements.txt`. If you add or update any new packages to the project use `pip freeze --local > requirements.txt ` to update the requirements.txt file with the new dependencies

##### Environment Variables

You will need to setup the following environment variables.

* DATABASE_URL : This is the URI to connect to the databse
* EMAIL_HOST_USER : Host account for sending the signin emails
* EMAIL_HOST_PASSWORD : Host account password for sendint signin emails
* SECRET_KEY : Your secret key
* STRIPE_PUBLISHABLE_KEY : For Stipe payments, you can find in your stripe account
* STRIPE_SECRET_KEY : For Stripe paymens, you can find in your stripe account


##### Contribution

- If you want to make changes on this project is better to use a different branch
- Use `git checkout -b <branchname>` to create a new branch and edit the files
- If you are happy with the changes to use `git commit -m "my commit message"` to commit the changes.
- Use `git push `to push the changes to the repository
- If youd like to see those changes online, please do a pull request

##### Deployment

You can easely pull request on this project on master banch. If accepted all the edits that was made, will be deployed to Heroku. You can run your own heroku application by creating an account on the Heroku website and following the tutorial on how to deploy a Python project wich can be find here: https://devcenter.heroku.com/articles/getting-started-with-python 
For questions or errors, i suggest use StackOverflow or simply ask here. A Stripe account is also needed in order to test the payment part.
