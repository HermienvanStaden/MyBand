# MyBand-website

MyBand-website is a Django project containing three apps, set up to use Docker for local deployment.

## Description

This website for a fictional band contains three Django apps: homepage, blog and tour information page.
It offers visitors the opportunity to register as a user or sign in to view tour dates and the blog.
This Django project is containerized on Docker

## Table of contents
    1. Getting started
        Prerequisites
        Usage
    2. Built with
    3. Version
    4. Author
    5. Acknowledgements

## 1. Getting Started

### Prerequisites

In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

1. The required dependencies for the container will be downloaded by the Dockerfile, 
    by executing the following command:

        pip install -r requirements.txt

    For this command pip is needed. If pip is not installed yet, run:

        python get-pip.py (Windows)
        python -m ensurepip (mac/os) 

2. Create a virtual environment for the container:

    Run in CMD or terminal:

        python -m virtualenv [name of virtual environment] 

    or, if an error occurs:

        python3 -m virtualenv [name of virtual environment]
    
    Activate virtual environment, by running:

        workon [name of virtual environment]

        or:

        .\[name of virtual environment]\Scripts\activate  

3. Pull image from DockerHub, by running:

        docker pull hermienvanstaden/myband-website

4. Create image by running:

        docker build -t myband-website ./

5. Create container by running:

        docker run -d -p 8000:8000 myband-website

6. To create an superuser account, use this command:

        python manage.py createsuperuser


## 2. Built With

* Python 3.11.8
* Bootstrap5.23.4
* Django 4.2.11
* django-crispy-forms 2.1
* HTML5
* Sphinx 7.2.6

## 3. Version

0.0.1

## 4. Author

**Hermien van Staden** 

* [GitHub] (https://github.com/hermienvanstaden)
* [LinkedIn] (www.linkedin.com/in/hermien-van-staden-1a03b6106)
* [Email] hermienvanstaden@gmail.com

## 5. Acknowledgments

* hyperiondev.com
* Sam Parrott for Sickamore font