# AirBnB Clone
Recreation of the AirBnB site, from the back-end data management to the front-end user interface. Written in Python and MySQL.

<h4>Third Phase</h4>
Description currently empty.

<h4>second phase</h4>
Command line interpretor can now save objects into a mysql database by setting the following environmental variables

* MySQL user = <HBNB_MYSQL_USER>
* MySQL password = <HBNB_MYSQL_PWD>
* MySQL host = <HBNB_MYSQL_HOST> (typically = localhost)
* MySQL database = HBNB_MYSQL_DB
* HBNB_TYPE_STORAGE = db

<h4>first phase</h4>
Where we are creating a command line interpretor to access objects that will store user data. Users can use the console to create objects, update object attributes, remove objects, list all objects, and store and read data from a .json file. 

## Install Dependencies 

<h6>Install MySql</h6>

1. ``MYSQL_APT=mysql-apt-config_0.8.3-1_all.deb``
2. ``wget https://dev.mysql.com/get/$MYSQL_APT``
3. ``sudo dpkg -i $MYSQL_APT``
4. ``sudo apt-get update``
5. ``sudo apt-get -y install mysql-server``

<h6>Install python3 modules</h6>

1. ``sudo apt-get -y install python3-pip``
2. ``sudo apt-get -y install python3-dev libmysqlclient-dev``
3. ``sudo -H pip3 install mysqlclient sqlalchemy Flask pep8``

## Usage
In order to begin the console, you can run either 'python3 console.py' or './console.py' in the command line.

Classes that are currently supported include BaseModel, User, City, State, Amenity, Review, and Place.

The console currently supports the following commands:
* ``create <class name>``, which will create an object of the class declared by user;
* ``show <class name> <id>``, which will display the object information if it exists;
* ``destroy <class name> <id>``, which will delete the object if it exists;
* ``all <class name>``, where the class name input is optional and the console will display all instances, or all instances of a specified object;
* ``update <class name> <id> <attribute name> <attribute value>``, whilch will update an instance attribute of a previously declared object.

Additionally, the console also supports the following command formats:
* ``<class name>.all()``, which will display all instances of the specified class;
* ``<class name>.count()``, whilch will display the number of instances of the specified class;
* ``<class name>.show(<id>)``, whilch will display the instance with correct id and class;
* ``<class name>.destroy(<id>)``, which will delete the instance with correct id and class;
* ``<class name>.update(<id>, <attribute name>, <attribute value>)``, which will update an instance of the given class and id with the new attribute;
* ``<class name>.update(<id>, <dictionary representation>)``, which will update an instance of the given class and id with a dictionary of key value pairs that will be new attributes for the objects. 
* ``<class name>.create(<key>=<value>)`` create an instance of the class

## Authors

<h6>Phase 3</h6>
* **Ian Liu-Johnston**, <ian.liu-johnson@holbertonschool.com>, Twitter: @concativerse

<h6>Phase 2</h6>
* **Anne Cognet**, <anne.cognet@holbertonschool.com>, @1million40
* **Richard Sim**, <richard.sim@holbertonschool.com>, @rdsim8589

<h6>Phase 1</h6>
* **Philip Yoo**, <philip.yoo@holbertonschool.com>, @philipYoo10
* **Jianqin Wang**, <jianqin.wang@holbertonschool.com>, @jianqinwang94
