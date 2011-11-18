About
=====
Picasa is an application from Google for Linux, Windows and MacOSX and lets you manage your photos. The Button API can send the selected images to an url, open with another programm or just execute a shell command. 

Django-picasabuttonizer uses the Button API.

Installation
============

    $ pip install -e git+ssh://git@github.com/fatrix/django-picasabuttonizer.git@v0.1.1b#egg=django-picasabuttonizer

or add 

    -e git+ssh://git@github.com/fatrix/django-picasabuttonizer.git@v0.1.1b#egg=django-picasabuttonizer
to a requirements.txt and then execute

    pip install -r requirements.txt
    
Dependencies
============
    * `Django`_ >= 1.3
    * `Mezzanine` (optional, Page processor included)
    * lxml

.. _`Django`: http://djangoproject.com/
.. _`Mezzanine`: http://mezzanine.jupo.org
