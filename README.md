# Logs Analysis Project
A Python PSQL Project in the Udacity Full Stack Nanodegree

## Set Up Instructions
Follow these instructions to set up the Vagrant Linux Environment and the Logs Analysis Project module.

### Prerequisite Resources
You will need the following Python resources for it to run:
<ul>
  <li>Python 2.7 and above (https://www.python.org/downloads/)
  <li>webbrowser
  <li>os
  <li>psycopg2
</ul>

Install Git

Install Vagrant and VirtualBox

Start Git and clone the repository to the local machine:

git clone https://github.com/

Navigate to the cloned repository using Git:
Such as cd desktop/logs_analysis/vagrant

Prepare the virtual machine for use:
1. Run the command 'vagrant up'to download and install the linux operating system.
2. Run the command 'vagrant ssh' to log in to the virtual machine.

Install Psycopg2

sudo apt-get install python-psycopg2

Download the newsdata.psl file and unzip to the vagrant folder in the virtual machine.

Setup the Database for use

Run the command psql -d news -f newsdata.sql;

After this it can be accessed through the psql -d news command. 

Make Views

Run the Module

Run the commmand python log.py in order to start the queries.

Module Output:

