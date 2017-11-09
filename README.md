# README

Python Flask application to list jupyter notebooks file in the user home
directory.

## DEVELOPMENT

### Install

Ubuntu Dependencies:

    sudo apt install python3-venv

or

    sudo apt install python-virtualenv

Install the requirements with pip in the virtual environment

    virtualenv venv
    # or python3 -m venv venv 
    source venv/bin/activate
    pip install -r requirements.txt

Adjust the 'config.py' file to your needs.

### Run

To run it on localhost:5000

    source venv/bin/activate
    python run.py

## DEPLOYMENT

### Configuration

#### Application 

    cp config-example.py config.py
    # Modify the config file accordingly with your environment

#### Nginx configuration

This is an example on how to configure nginx to serve both static jupyter
notebooks files and our pages.
This examples assumes an url such as https://www.example.org/public_notebooks/username

    location ~ ^/public_notebooks/([a-zA-Z0-9\-_.]*)((/.*)?.ipynb)$ {
      alias /home/$1/public_notebooks$2;
    }
    location ~ ^/public_notebooks/([a-zA-Z0-9\-_.]*)(/)?$ {
      alias /home/$1/public_notebooks$2;
      include uwsgi_params;
      uwsgi_pass unix:/var/run/publicNotebooks.sock;
    }

#### Systemd

    # Modify the unit file accordingly with you environment
    # symlink it to /etc/systemd/system/publicNotebooks.service 
    ln -s /opt/publicNotebooks.service /etc/systemd/system/publicNotebooks.service
