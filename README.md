# clone this project
git clone https://github.com/kartik115/assignment.git

# enter into project
cd assignment

# install pip3
sudo apt-get install python3-pip

# install virtualenv
sudo pip3 install virtualenv

# create virtualenv
virtualenv -p python3 venv

# activate venv
source venv/bin/activate

# install dependancies from requirements.txt
pip3 install -r requirements.txt

# run your python server
python3 src/manage.py runserver

# copy env.examples file to .env
cp env.examples .env

# Change parameters in .env file

# make migrations
python3 src/manage.py makemigrations

# run migrations to insert in db
python3 src/manage.py migrate

# deactivate your virtualenv
deactivate

# postman collection link
https://www.getpostman.com/collections/ec026628f203b0c32949