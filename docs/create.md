
mkvirtualenv cartotime --python=/usr/bin/python2.7

pip install django-leaflet django-bootstrap3 django-geojson
pip install -e git+https://github.com/Karmak23/django-timelinejs.git#egg=Django_TimelineJS-master

mkdir cartotime

git init .

django-admin startproject cartotime
