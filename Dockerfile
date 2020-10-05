# создать образ на основе базового слоя python (там будет ОС и интерпретатор Python)
FROM ubuntu:latest
RUN apt-get update && apt-get install -y ubuntu-server ubuntu-desktop

RUN git clone https://watislaf:26122001f@github.com/watislaf/django_blog.git

RUN sudo apt install redis-server
RUN sudo systemctl start redis-server
RUN sudo apt-get install python3-dev
RUN sudo systemctl enable redis-server

RUN pip install -r django_blog/requirements.txt
 
 ###
 RUN pip install gunicorn
 RUN sudo apt install nginx -y
 RUN gunicorn --bind 0.0.0.0:8000 yatube.wsgi
# при старте контейнера выполнить runserver 
#CMD python /code/manage.py runserver 0:8000
