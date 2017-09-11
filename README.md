# Logs Analysis Project
A Python PSQL Project in the Udacity Full Stack Nanodegree

## Set Up Instructions
Follow these instructions to set up the Vagrant Linux Environment and the Logs Analysis Project module

### Prerequisite Resources
You will need the following Python resources for it to run:
<ul>
  <li>Python 2.7 or above (https://www.python.org/downloads/).
  <li>psycopg2 (http://initd.org/psycopg/docs/install.html) to be installed within the virtual machine
</ul>

You will need the following other resources for it to run:
<ul>
  <li>Git (https://git-scm.com/downloads).
  <li>VirtualBox (https://www.virtualbox.org/wiki/Downloads).
  <li>Vagrant (https://www.vagrantup.com/).
</ul>

### Installation

<ul>
  <li>Install Git (https://git-scm.com/downloads) on the local machine
  <li>Install Python 2.7 or above (https://www.python.org/downloads/) on the local machine
  <li>Install VirtualBox (https://www.virtualbox.org/wiki/Downloads) on the local machine
  <li>Install Vagrant (https://www.vagrantup.com/) on the local machine
</ul>

### Preparing the Virtual Machine
<ol>
  <li>Use git clone https://github.com/ to clone this repository..
  <li>Navigate to the cloned repository using Git i.e. cd desktop/logs-analysis/vagrant
  <li>Run the command 'vagrant up' to download and install the linux operating system
  <li>Run the command 'vagrant ssh' to log in to the virtual machine
  <li>Install Psycopg2 with sudo apt-get install python-psycopg2
 </ol>

### Setup the Database
After the initial setup it can be accessed through the psql -d news command 
<ol>
  <li>Download the newsdata.psl file [I'm an inline-style link with title](https://www.google.com "Google's Homepage")
  <li>Unzip and move this file to the vagrant folder of the virtual machine
  <li>Run the command psql -d news -f newsdata.sql 
</ol>

### Contents of the Module
It uses python to access a database that includes the following tables:
<ul>
  <li>Authors table with a list of article authors.
  <li>Articles table with a list of articles.
  <li>Log table with entries on user access to the site.
</ul>
With these tables the following queries are answered:
<ol>
  <li>What are the most popular three articles of all time?
  <li>Who are the most popular article authors of all time?
  <li>On which days did more than 1% of requests lead to errors?
</ol>

The following functions are used to carry out the queries:
<ul>
  <li>con_news_Query(query): Connects to the database 'news', executes queries, and returns connection errors.
  <li>popular_articles_show(): Shows a view of the top three popular articles, and their views.
  <li>popular_authors_show(): Shows a view of the top three popular authors, and their views.
  <li>percentage_error_show(): Shows the days that more than 1% of access requests have errors.
</ul>

### Preparing the Module
In order to run the module you must first make the following views:

1. Create Views for article authors
> CREATE VIEW author_of_articles AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;
2. Create Views for article views
> CREATE VIEW articles_viewed AS
SELECT articles.title, COUNT(log.id) AS views
FROM articles, log
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY views desc;
3. Create Views for errors
> CREATE VIEW d_errors AS
SELECT DATE(time) as day, CAST(COUNT(status) AS FLOAT) AS d_errors
FROM log
WHERE NOT status='200 OK'
GROUP BY day
ORDER BY day;
4. Create Views for the totals
> CREATE VIEW final AS
SELECT DATE(time) AS day, CAST(COUNT(status) AS FLOAT) AS final
FROM log
GROUP BY day
ORDER BY day;

This is achieved by:
<ol>
  <li>Entering the psql command while in vagrant, and logged into the virtual machine.
  <li>Connecting to the news database with the \c news command.
  <li>Inputting the CREATE VIEWS above.
  <li>Exiting with the \q command.
</ol>

### Run the Module
Run the commmand python project_log_analysis.py in order to start the queries.

Module Output:

![Image of Output](https://github.com/petergns/logs-analysis/blob/master/Queries%20Finished.PNG)

## Author
[petergns](https://github.com/petergns)

## Acknowledgments
Acknowledgments to [Udacity](https://www.udacity.com/) for the resources that helped me develop this.

