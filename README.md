# AirBnB Clone
Recreation of the AirBnB site, from the back-end data management to the front-end user interface. Written in Python and MySQL.

<h4>Third Phase</h4>
Developing an api to interface with the database.

<h4>Second phase</h4>
Command line interpretor can now save objects into a mysql database by setting the following environmental variables. Not setting these variables defaults to using a json file. Listed below are the values for the example database:

* MySQL user: ``HBNB_MYSQL_USER=hbnb_dev``
* MySQL password: ``HBNB_MYSQL_PWD=hbnb_dev_pwd``
* MySQL host: ``HBNB_MYSQL_HOST=localhost``
* MySQL database:  ``HBNB_MYSQL_DB=hbnb_dev_db``
* Storage type: ``HBNB_TYPE_STORAGE=db`` -- db is the only variable here. Any other option (including not set) will default to the storage type as a json object.


<h4>First phase</h4>
Where we are creating a command line interpretor to access objects that will store user data. Users can use the console to create objects, update object attributes, remove objects, list all objects, and store and read data from a .json file. 

## Install Dependencies 

<h6>1. Install MySql</h6>

1. ``MYSQL_APT=mysql-apt-config_0.8.3-1_all.deb``
2. ``wget https://dev.mysql.com/get/$MYSQL_APT``
3. ``sudo dpkg -i $MYSQL_APT``
4. ``sudo apt-get update``
5. ``sudo apt-get -y install mysql-server``

<h6>2. Install python3 modules</h6>

1. ``sudo apt-get -y install python3-pip``
2. ``sudo apt-get -y install python3-dev libmysqlclient-dev``
3. ``sudo -H pip3 install mysqlclient sqlalchemy Flask pep8``

<h6>3. (Optional) Fill the sql databases with example SQL data.</h6>
1. ``cat "100-dump.sql" | mysql -uroot -hlocalhost -p``
2. ``cat "10-dump.sql" | mysql -uroot -hlocalhost -p``
3. ``cat "7-states_list.sql" | mysql -uroot -hlocalhost -p``
4. ``cat "setup_mysql_dev.sql" | mysql -uroot -hlocalhost -p``
5. ``cat "setup_mysql_test.sql" | mysql -uroot -hlocalhost -p``

## Usage

### Types of interfaces

#### Through Python directly:

Example of Console Usage without a db:
```
~> python3
Python 3.4.3 (default, Nov 17 2016, 01:08:31) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import models
>>> s = models.State()
>>> s.name = "Calveticus"
>>> models.storage.new(s)
>>> models.storage.save()
>>> models.storage.count("State")
1
>>> exit()
~>
```

Example of Python usage directly with a db
```
~> HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3
Python 3.4.3 (default, Nov 17 2016, 01:08:31) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import models
>>> models.storage.count("State")
58
>>> exit()
~>
```

#### The Console
``console.py`` -- Command line interface to directly interact with databases, or object methods.
In order to begin the console, you can run either ``python3 console.py`` or ``./console.py`` in the command line.

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

Classes that are currently supported include BaseModel, User, City, State, Amenity, Review, and Place.


#### API Access
* API -- interaction with the objects through HTTP GET requests

#### Front End Webserver
* Front end -- Website to display 


## Sample tests on the command-line
Check to see if the count method works with the ``test_get_count.py`` script.
```
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./test_get_count.py
```

Simple preliminary tests to see if the Flask app runs.
```
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5000 python3 -m api.v1.app
```

## Authors

<h6>Phase 3</h6>

- **Ian Liu-Johnston**, ian.liu-johnson@holbertonschool.com, Twitter: @concativerse

<h6>Phase 2</h6>

- **Anne Cognet**, anne.cognet@holbertonschool.com, @1million40
- **Richard Sim**, richard.sim@holbertonschool.com, @rdsim8589

<h6>Phase 1</h6>

- **Philip Yoo**, philip.yoo@holbertonschool.com, @philipYoo10
- **Jianqin Wang**, jianqin.wang@holbertonschool.com, @jianqinwang94
