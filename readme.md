# Portfolio Website hosted on Linode

This is my personal [portfolio website](https://www.patrickstaehli.ch) that is hosted on [linode](www.linode.com) using flask. Hosting a website on a linux server gives you great flexibiltiy, as e.g to 
publish projects with working examples directly on your website. 

## Prerequisites

This project is hosted on Linode and runs on an nginx webserver. Renting a linode server is not free, but you can get one for only 5$/month.

## How to use it

### Setting up the Linode

After registration on linode, you can create a new linode, choose a distribution and Linode plan (for this purpose, the cheapest one is perfectly fine).
When the server is ready, several steps are needed securing your server, as described [here](https://www.linode.com/docs/guides/securing-your-server/).
After setting up the server:

- Clone the repository on your server
- Install the requirements from the requirements.txt

### Setting up Nginx
Nginx is the webserver that handles all the static files located in /webapp/static.
#### Install Nginx

	sudo apt install nginx 

#### Remove the default Nginx config file
	sudo rm /etc/nginx/sites-enabled/default

#### Update the Nginx configuration 
Update the Nginx configuration file /config/nginx.conf and copy it to /etc/nginx/sites-enabled/default and restart Nginx.

	sudo systemctl restart nginx

### Setting up Gunicorn
Gunicorn is a Python Web Server Gateway Interface (WSGI) HTTP server that handles the python code, i.e. the flask application.
Gunicorn is launched via a supervisor so that the flask app autorestarts when it crashes or when the server is restarted.

#### Install Gunicorn and supervisor
	
	pip install gunicorn
	sudo apt install supervisor
	
#### Update the supervisor config 
Update the supervisor configuration file /config/supervisor.conf and copy it to /etc/supervisor/conf.d/

Run Gunicorn via the supervisor by restarting the supervisor

	sudo supervisorctl restart
	
## Built With

[BOOTSTRAPMADE](https://bootstrapmade.com/) - Bootstrap Template

## License

Find out available licensing options for the BootstrapMade template [here](https://bootstrapmade.com/license/)

