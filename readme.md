# Portfolio Website hosted on Linode

This is a personal portfolio website that is hosted on [linode](www.linode.com) using flask. Hosting a website on a linux server has the big advantage that you are able to publish portfolio projects with working examples (i.e. python projects) directly on your website. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

This project is hosted on Linode and runs on nginx webserver. Renting a linode server is not free, but you can get one for only 5$/month. However, there exist alternative products.

In addition, I also recommend to buy a personal domain, such as e.g myawesomeportfolio.com.

## How to use it

### Setting up the Linode

After registration on linode, you can create a new linode and choose a Distribution, Linode Plan (for this purpose, the cheapest one is perfectly fine).
When the server is ready, several steps are needed to securing your server, as described [here](https://www.linode.com/docs/guides/securing-your-server/)

### Deploy on a Linux Server using Nginx and Gunicorn

- Clone the repository on your server
- Install the requirements from the requirements.txt

### Install Nginx and Gunicorn

> Install Nginx and Gunicorn

'''bash
sudo apt install nginx

pip install gunicorn 
'''

- Remove the default Nginx config file
'''bash
sudo rm /etc/nginx/sites-enabled/default
'''

- Update the Nginx configuration file /config/nginx.conf 

> Run gunicorn with supervisor
## Built With

* [BOOTSTRAPMADE](https://bootstrapmade.com/) - Bootstrap Template

## License

Find out available licensing options for the BootstrapMade tempalte [here](https://bootstrapmade.com/license/)

