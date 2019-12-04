# Dependency Inversion

The EmployeeDao class requires a MySQL database to be up and running.

### Prerequesites:

In order to use the MySQL database functionality, install the following pip packages.

    $ pip install mysql
    
### DB Setup

Below are the steps used to create a database for use with the EmployeeDao class.

    $ mysql -u root
    > create database py_employees;
    > use database py_employees;
    > create table employees (
       id int not null auto_increment, 
       first varchar(30) not null, 
       last varchar(30) not null, 
       primary key(id));
    > insert into employees (first, last) 
       values ('Big', 'Bird')

