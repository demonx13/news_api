# News API

test case by Sebbia realized on Django REST framework
http://testtask.sebbia.com/swagger-ui.html

* download project
* extract
* go to project folder in terminal

build project:

    docker-compose build


next:

    docker-compose run news_back ./manage.py migrate


    docker-compose run news_back ./manage.py createsuperuser


create data for test:

    docker-compose run news_back ./manage.py addfake
    
go to:
    
    http://127.0.0.1:8000/v1/swagger/


see data in admin panel:
    
    http://127.0.0.1:8000/admin