# Educated Citizen Project

## About Me:

## Technologies:
* Python
* Flask
* PostgreSQL
* SQLAlchemy
* HTML
* XML
* CSS
* Bootstrap
* jQuery
* Javascript (AJAX, JSON)

## Features:

### Landing Page

This is the first feature of the app. Users are asked to enter their zip code and select a political issue that matters to them. This data is sent as a request to VoteSmart API. Using Jinja2 templating, a new webpage shows all elected officials in the user's district and any legislation passed on their selected political issue.

< screenshot of landing page goes here >

### Voting History

The second feature of this app provides the user with a legislator's voting record on a selected political issue. The user submits a form, typing in a legislator's last name, state, and a political issue. A query is made to the SQLAlchemy database, and a legislator's votesmart id is used to make a request to VoteSmart API. If the user doesnt agree with how a legislator has voted, the user can click on a button to request the legislator's contact information via an AJAX request.

< screenshot of voting page goes here >

### Contributions

The final feature of this app allows the user to view a legislator's top contributors by industry. A user types in a legislator's last name and state into a form. This information is queried to the SQLAlchemy database and the id selected is sent as a request to OpenSecrets API. A user can discover the legislator's contact information if they do not agree with how the legislator obtains campaign contributions.

< screenshot of contributions goes here >


### Future Implementations
Several features have been planned out to grow Educated Citizen app:
* autocomplete feature for forms
* charts to better show contribution information
* addition of bill summaries 

### Installation
You are welcome to run this app on your own machine.

Install PostgresQL 

Clone this repo:
https://github.com/adinahhh/educated-citizen.git

Create a virtual environment inside your project directory:

`virtualenv env`

`source env/bin/activate`

Next, install dependencies:

`pip3 install -r requirements.txt`

Register for a key with [VoteSmart API](https://votesmart.org/share/api#.XoNy3ZNKjBJ).

Register for a key with [OpenSecrets API](https://www.opensecrets.org/open-data/api).

Save your keys in **`secrets.sh`** file like below:
```
export VOTESMART_API_KEY="your_new_key"
export OPEN_SECRETS_API_KEY="second_new_key"
```

Activate your secrets.sh file into the new terminal session using command:
`source secrets.sh`

Create the database using the following commands:
```
createdb legislature
python3 model.py
python3 seed.py
```

Run the app locally on your machine:
`python3 server.py`

In a new tab or window, using address http://0.0.0.0:5000/ will pull up the Educated Citizen app.

-------
unclear what to do with below info:

### **Planning:**
Project board: https://github.com/adinahhh/educated-citizen

Data Model in google drive: https://drive.google.com/open?id=1RQHNn84aayKCSCODIZT771bfV3PcZccs
