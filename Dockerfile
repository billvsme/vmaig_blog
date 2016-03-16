FROM ubuntu:14.04
MAINTAINER billvsme "994171686@qq.com"

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y vim
RUN apt-get install -y nginx
RUN apt-get install -y postgresql
RUN apt-get install -y memcached
RUN apt-get install -y python-dev python-setuptools
# RUN apt-get install -y python3
# RUN apt-get install -y python3-dev python3-setuptools
RUN apt-get install -y python-pip

RUN git clone https://github.com/billvsme/vmaig_blog
WORKDIR ./vmaig_blog

RUN apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
RUN pip install -r requirements.txt
RUN apt-get install -y libpq-dev
RUN pip install psycopg2
RUN pip install gunicorn

USER postgres
RUN service postgresql start &&\
    psql --command "create user vmaig with SUPERUSER password 'password';" &&\
    psql --command "create database db_vmaig owner vmaig;"

USER root
RUN service postgresql start &&\
    sleep 10 &&\
    python manage.py makemigrations --settings vmaig_blog.settings_docker &&\
    python manage.py migrate --settings vmaig_blog.settings_docker &&\
    echo "from vmaig_auth.models import VmaigUser; VmaigUser.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell --settings vmaig_blog.settings_docker &&\
    echo 'yes' | python manage.py collectstatic --settings vmaig_blog.settings_docker

RUN ln -s /vmaig_blog/nginx.conf /etc/nginx/sites-enabled/vmaig
RUN rm /etc/nginx/sites-enabled/default

RUN pip install supervisor
COPY supervisord.conf /etc/supervisord.conf

RUN mkdir /var/log/supervisor
CMD supervisord -c /etc/supervisord.conf
EXPOSE 80
