# django_restaurant
## About
A company needs internal service for its 'employees which helps them to
make a decision at the lunch place. Each restaurant will be uploading menus
using the system every day over API.
Employees will vote for the menu before leaving for lunch on a mobile app
for whom the backend has to be implemented.
This is a food selection app by company employees. There is the following functionality:
- Authentication
- Creating restaurant
- Uploading menu for restaurant (There should be a menu for each day)
- Creating employee
- Getting current day menu
- Getting results for the current day
# Run
To run via docker. Use the command docker-compose up -d --build.
After you can create superuser (python manage.py createsuperuser)
Use link localhost:8000/......

If you want run server without docker
- Download the project and install requirements 
- Launch virtual environment. 
- Create postgresql db with name 'restaurant_service' 
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser (with your credentials)
- python manage.py runserver 
# API
Now you can use your admin profile to interact with apis.  
- To create an employee, you need to register it in the django admin panel, and then add its data in db through ../employee/ and select the desired user
- To create and view restaurants use ../restaurant/
- To add a menu, first create a menu with ../menu/. Then add a dish to the desired menu with ../dishes/
- To view the menu for a specific day, use ../menu/<str:day>/ where day print in a format mon, tue, wed, thu, etc.
- To get results on menu selection for all employees use ../result/
- To select a menu for an employee, use ../employee/menu/<int:pk>/ where pk is an index of menu in db
- To get a token go to ../token/
# Docker
 Change settings -> Database HOST to db if want to use with docker
