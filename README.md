# Pur Beurre Web Application

Web application, build with Django, which allows users to find healthier food products.
This app uses the Open Food Facts API

## Link

Link to the app, hosted by Heroku: https://purbeurre-jm.herokuapp.com/


##features
- create a simple user account with the head icon in the menu bar
- login to user account with the mouse icon in the menu bar


- If not registered :
  - Search a product
    - the site will display all products in the same category with a better nutrient score
  - Access to the product details by clicking on his picture
  - Access to the Open Food Facts product page for all available details
    

- If registered, add :
    - add a product to user favorites with the "Enregistrer" button
    - delete a product from user favorites with the "Supprimer" button
    - access to user favorites with the carrot icon in the menu bar
    - access to user account informations with the mouse icon in the menu bar


- logout to user account with the logout icon in the menu bar


##Prerequisites
- Python 3.9
- PostgreSQL 
- All the other required modules are in the requirements.txt file to install before launching the app.


#Install Locally

_ clone git repository : https://github.com/J31NM/Pur_Beurre

_ Add your own DB_PASSWORD local variable in pur_beurre/settings/dev.py
- you also can modify the other DB local variables if you need

_ run in your terminal : 
- manage.py makemigrations
- manage.py migrate
- manage.py runserver

if you want to run unit tests : open pur_beurre/settings/__init__.py,
uncomment "from pur_beurre.settings.test import *",
comment "from pur_beurre.settings.dev import *"

## GOOD TO KNOW
_ The products available for research are on the FRENCH Open Food Facts




  






