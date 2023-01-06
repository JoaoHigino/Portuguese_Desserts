# PORTUGUESE DESSERTS

Portuguese Desserts is a blog for the people who missed the best desserts in the world and missed Portugal. In this blog, you can learn how to do your favorite desserts.

![screenshot](documentation/responsive.png)

The live link can be found here - [Portuguese Desserts](https://portuguese-desserts.herokuapp.com/)

## UX

A visitor to Portuguese Desserts would be someone who is most likely an adult who missed their traditional desserts and trying new recipes but also wants to save time and effort when deciding what to cook for a special occasion.

## Colour Scheme

Explain your colours and the colour scheme.

- `#445261` used as the primary text.
- `#f30c0c` used as the primary highlights.
- `#070707` used as the secondary text.
- `#6c757d` used as the secondary highlights.

I used [coolors.co](https://coolors.co/e84610-009fe3-4a4a4f-445261-d63649-e6ecf0-000000) to generate my colour palette.

![screenshot](documentation/colorpalette.png)

### Typography

The Robot Mono font is the main font used for the body of the website with the Playfair Display font used for the main headings on the home page. These fonts were imported via Google Fonts.

## User Stories

### New Site Users

- As a New Site User I can log into my own account so that I can manage Username and Password information.

### Returning Site Users

- As a Site User, I can view a paginated list of posts so that easily select a post to view.
- As a Site User, I can edit my comments so that I can change my opinion.
- As a Site User, I can delete my comments so that no one can read my comments again.
- As a Site User, I can view a paginated list of recipes so that I can select a recipe to view.
- As a Site User, I can view comments on an individual post so that I can read the conversation.
- As a Site User, I can search for a recipe so that I can minimize time searching for what I need.

### Site Admin

- As a Site administrator, I can add, filter, change and search for recipes so that I can easily manage my site content.
- As a Site administrator, I can view the number of likes on each post so that I can see which is the most viral.
- As a Site administrator, I can create, read, update and delete posts so that I can manage my blog content.

## Features

### Existing Features

### Home Page

- The homepage displays the logo name, About Us, Sign Up and Login are the options on the left. If you are logged as a superuser Add Recipe will appear too.
- The main body of the homepage contains 6 articles/posts and once more than 6 articles are posted pagination shows links to the next page.
- Social media network links are displayed in the footer.

![screenshot](documentation/mainpage.png)

### Logo

- A customized logo was created using free logo design which is a free logo generator.
- This logo is positioned in the top left of the navigation bar. The logo is linked to the home page for ease of navigation for the user.

![screenshot](documentation/logo_pd.png)

### Navigation Bar

- The navigation bar is present at the top of every page and includes all links to the various other pages.
- The My Account navigation link is a drop-down menu that includes the Sign-up and Log-in links. 
- When the user has logged in, the My Account drop-down menu changes to display the user's name and a profile icon.

![navbar](documentation/navbar.png)

### Navigation Bar - Superuser

- As a superuser you are able to add recipe.

![navbarsuper](documentation/navbarsuperuser.png)

### Create an account 

![signup](documentation/signup.png)

### Login 

![signin](documentation/signin.png)

### Logout

![signout](documentation/signout.png)

### Footer

![footer](documentation/footer.png)

### About Us

![aboutus](documentation/aboutus.png)

### Add Recipe Django - Admin Only

![django](documentation/addpostdjango.png)

### Add Recipe Blog - Admin Only

![addrecipe](documentation/addrecipe.png)

### Update/Delete Post - Admin Only

![update](documentation/update.png)

![updatepost](documentation/updatepost.png)

![delete](documentation/deletepost.png)

### Like/Comments

![likes](documentation/likescomment.png)

### New Comment

![likes](documentation/comment.png)

### 500 Page Error

- A 500 server error page was created to handle internal server errors.

![Error](documentation/error500.png)

### 404 Page Error

![Error](documentation/error404.png)

## Future Features

- Site Users be able to add recipes.
- Allows users to signup to a newsletter / mailing list.
- Contact Form.
- Search Recipes.

## Bugs / Errors encountered during development

* Manage.py was not in the root directory. [Click here](documentation/error3.png)
* Admin wasnt unique on urls. [Click here](documentation/error2.png)
* Error creating comments. [Click here](documentation/error.png)
* Error creating new users. [Click here](documentation/error4.png)

## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Tim Nelson](https://traveltimn.github.io/readme-builder) used to help generate the Markdown files.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.
- [Summernote](https://summernote.org/) Used to add a text area field to the admin setup to enable a list of ingredients and method steps.
- [amiresponsive](https://ui.dev/amiresponsive) to see how responsive the site is on different devices.
- [Grammarly](https://app.grammarly.com/) - used to proof read the README.md
- [FreeLogo](https://www.freelogodesign.org/) - used create the blog logo

## Database Design

**Django** Projects:

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models.
Understanding the relationships between different tables can save time later in the project.

Using your defined models (one example below), create an ERD with the relationships identified.

```python
class Post(models.Model):
    title = models.CharField(
        max_length=50, unique=True, null=False, blank=False)
    slug = models.SlugField(
        max_length=200, unique=True, null=False, blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    preparation_time = models.IntegerField(null=False, blank=False)
    cook_time = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    ingredients = models.TextField(null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=1)
    bookmarks = models.ManyToManyField(
        User, related_name='bookmark', default=None, blank=True)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
```

```python
class Comment(models.Model):
    recipe = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
```

![screenshot](documentation/diagramps.png)

## Agile Development Process

Github projects was used to manage the development process using an agile approach. Please see link to project board [here](https://github.com/users/JoaoHigino/projects/7)

The Epics listed above were documented within the Github project as Milestones. A Github Issue was created for each User Story which was then allocated to a milestone(Epic). Each User Story has defined acceptance criteria to make it clear when the User Story has been completed. The acceptance criteria are further broken down into tasks to facilitate the User Story's execution.

### GitHub Projects

[GitHub Projects](https://github.com/JoaoHigino/Portuguese_Desserts/projects) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

![agile](documentation/agile.png)

### GitHub Issues

[GitHub Issues](https://github.com/JoaoHigino/Portuguese_Desserts/issues) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories.

- [Open Issues](https://github.com/JoaoHigino/Portuguese_Desserts/issues)

    ![screenshot](documentation/openissues.png)

- [Closed Issues](https://github.com/JoaoHigino/Portuguese_Desserts/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](documentation/closedissues.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Manual Testing

* Manual testing was completed for each case and edge case scenario from user log in, user post article, user deleting the article, and user log out.
* The site was also manually tested on various browsers (Google Chrome, Safari, Microsoft Edge, and Firefox) and different screen sizes.
* I also used lighthouse reports to see the performance, quality, and correctness of the website.

### Defensive Design

- If you are not logged as superuser you can't add recipes

![screenshot](documentation/denyaddrecipe.png)

- You can't delete a comment that isn't yours.

![screenshot](documentation/denydeletecomment.png)

- You can't edit a comment that isn't yours.

![screenshot](documentation/denyeditcomment.png)

### More manual testing structure and results
|   | Pass/Fail |
| ------------- | :----: |
Selecting the Portuguese Desserts logo on the homepage directs the user back to the homepage  |  Pass |
| Selecting the about link directs the user to /about page  |  Pass |
| Selecting Sign Up directs the user to /accounts/signup/ page |  Pass |
| Selecting Login directs the user to /accounts/login/ page  |  Pass |
| Click on the pagination link at the bottom of the page returns results of the next page (example /?page=2) |  Pass |
| Registering as a user and entering a password to create a new user |  Pass |
| Logging in as superuser/admin |  Pass |
| "successfully signed in as (user name)" message shown to user |  Pass |
| Logging in as superuser/admin to approve post |  Pass |
| Navigating site as user/admin is permitted |  Pass |
| Creating a new post directs the user to "/new" and required fields send the data successfully to Django admin  |  Pass |
| As admin I can view and publish posts |  Pass |
| If no image is selected then the default image is used |  Pass |
| Posting comments as a user/admin on any article |  Pass |
| Liking a comment as a user/admin on any article |  Pass |
| Updating a post as the author |  Pass |
| User is prompted "are you sure you want to delete" before permitting deletion of a post |  Pass |
| Deleting a post as the author |  Pass |
| Confirmation message of deletion is shown |  Pass |
| Not permitted to update a post if not the author |  Pass |
| Not permitted to delete a post if not the author |  Pass |
| "You have signed out" message shows to the user when successfully signed out |  Pass |
| Logging out as a user/admin directs user to the homepage |  Pass |
| Posting a new article requires appropriate fields to be filled in |  Pass |
| Clicking on the social media icons in the footer opens the link in a new tab |  Pass |

### Responsiveness Browser Compatibility

|  | Chrome | Opera | Edge | Safari | Pass/Fail |
| ------------- |-------------| -----|  ---------- |  -----| :----: |
| Expected Appearance   | yes | yes  | yes  | yes | Pass |
| Expected Layout   | yes | yes  | yes  | yes | Pass |

- Chrome

![screenshot](documentation/chrome.png)

- Opera

![screenshot](documentation/opera.png)

- Edge

![screenshot](documentation/edge.png)

- Safari

![screenshot](documentation/safari.png)

### Lighthouse

- No errors were found when passing through Lighthouse

![screenshot](documentation/lighthouse.png)

![screenshot](documentation/lighthouseaboutus.png)

![screenshot](documentation/lighthouseaddrecipe.png)

![screenshot](documentation/lighthousebolo.png)

![screenshot](documentation/lighthousepage2.png)

![screenshot](documentation/lighthouseregister.png)

![screenshot](documentation/lighthousesignin.png)

![screenshot](documentation/lighthousesignout.png)

![screenshot](documentation/lighthouseedit.png)

![screenshot](documentation/lighthouseupdate.png)

![screenshot](documentation/lighthousedeletepost.png)

![screenshot](documentation/lighthousedelete.png)

### The W3C Markup Validator

![screenshot](documentation/html.png)

![screenshot](documentation/summernoterror2.png)

 - Error from summernote widget(https://github.com/summernote/django-summernote), the only code to makes Add Recipe have summernote and dont look like this:
 
 ![screenshot](documentation/summernoteerror.png)

![screenshot](documentation/html_page2.png)

![screenshot](documentation/html_signup.png)

![screenshot](documentation/html_login.png)

![screenshot](documentation/html_signout.png)

![screenshot](documentation/htmlaboutus.png)

![screenshot](documentation/html_add_recipe.png)

![screenshot](documentation/html_deletecomment.png)

![screenshot](documentation/html_deletepost.png)

![screenshot](documentation/html_updatecomment.png)

### W3C CSS Validator

- No errors found.

![screenshot](documentation/w3c.png)

### PEP8 online

- No errors found.

![screenshot](documentation/pep8.png)

![screenshot](documentation/pep8_blog_admin.png)

![screenshot](documentation/pep8_blog_forms.png)

![screenshot](documentation/pep8_blog_models.png)

![screenshot](documentation/pep8_blog_urls.png)

![screenshot](documentation/pep8_blog_views.png)

![screenshot](documentation/pep8_my_manage.png)

![screenshot](documentation/pep8_my_settings.png)

![screenshot](documentation/pep8_my_urls.png)

### JSHint

- No errors found.

![screenshot](documentation/jshint.png)

![screenshot](documentation/jshint2.png)

## Deployment

The live deployed application can be found deployed on [Heroku](https://portuguese-desserts.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: portuguese_desserts).
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
| `CLOUDINARY_URL` | insert your own Cloudinary API key here |
| `DATABASE_URL` | insert your own ElephantSQL database URL here |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | this can be any random secret key |

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

os.environ.setdefault("CLOUDINARY_URL", "insert your own Cloudinary API key here")
os.environ.setdefault("DATABASE_URL", "insert your own ElephantSQL database URL here")
os.environ.setdefault("SECRET_KEY", "this can be any random secret key")

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

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/JoaoHigino/Portuguese_Desserts) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/JoaoHigino/Portuguese_Desserts.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JoaoHigino/Portuguese_Desserts)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JoaoHigino/Portuguese_Desserts)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits

- [StackOverflow](https://stackoverflow.com/questions/72446262/git-pull-not-possible-to-fast-forward/72460052#72460052)
- [StackOverflow](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown)
- [StackOverflow](https://stackoverflow.com/questions/73964287/django-summernote-dont-form-is-not-displayed-outside-the-admin-panel)
- [Django Summernote](https://github.com/summernote/django-summernote)

### Content

- [Tim Nelson](https://traveltimn.github.io/readme-builder) | README and TESTING | tool to help generate the Markdown files |
- [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
|
### Media

- [Pastel de Nata](https://leitesculinaria.com/7759/recipes-pasteis-de-nata.html)
- [Bola de Berlim](https://www.sbs.com.au/food/recipes/portuguese-doughnuts-bola-de-berlim)
- [Serradura](https://aromaticessence.co/serradura-portuguese-sawdust-pudding/)
- [Arroz Doce](https://wetravelportugal.com/arroz-doce/)
- [Pao de Lo](https://www.authenticfoodquest.com/pao-de-lo-recipe-portuguese-sponge-cake/)
- [Queijadas](https://honestcooking.com/queijadas-portuguese-cheesecake-tarts/)
- [Pudim de Ovos](https://macanesekitchen.com/2020/12/portuguese-egg-pudding-pudim-de-ovos/)
- [Tarte Amendoa](https://leitesculinaria.com/7769/recipes-portuguese-almond-torte.html)
- [Leite Creme](https://www.recipezazz.com/recipe/leite-de-creme-portuguese-egg-custard-24324)
- [Farofias](https://www.foodfromportugal.com/recipes/farofias-portuguese-sweet/)

### Acknowledgements

- To my amazing wife Sandra, my best friend, my mentor, and my safe haven, without her, all my dreams will be impossible to achieve. She is everything.
- To my two kids, Maria and Thomas, with them life is easy and light. They make me laugh and think that our future is bright. 
- To my family and friends - for being a great support and providing a lot of the user testing for me, especially my friends from "Liga 7 BP" with their craziness helped me to clean my head.
- To my mentor Tim Nelson for all his guidance, support, tips, and feedback.
- The Code Institute community on slack and my classmates its been a pleasure so far.