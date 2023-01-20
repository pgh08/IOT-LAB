# IOT-LAB.
Codes of IOT LAB MSRIT

# Installation of adafruit.
pip3 install Adafruit-DHT

# Installation of bluetooth.
sudo apt-get install python3-bluetooth
  or
sudo apt-get install python-bluetooth
 
# Installation of MySQL.
sudo apt update
sudo apt upgrade
sudo apt-get insatll mariadb-server
sudo apt-get install python3-mysqldb
 
# Initial setup for mariadb.
sudo mysql_secure_installtion

# For login into MySQL.
sudo mysql -u root -p

# For creating data base.
create database database_name;

# For creating new user.
create user 'user_name'@'localhost' identified by 'password';

# For switching database.
use database_name;

# For creating table.
create table table_name(column_1_name varchar(50), column_2_name float);

# To grant Privileges.
grant all privileges on database_name.* to 'user_name'@'localhost';
flush privileges;

# To view updated data in database.
use database_name;
select * from table_name;
