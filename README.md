# Educated Citizen Project

It can be hard keeping track of who represents you. The Educated Citizen Project is here to help users learn more about their legislator's voting records and campaign contributions. VoteSmart API and OpenSecrets API are used to retrieve data on congressional representatives. This app was built using a Python/Flask backend and PostgreSQL database.

## About Me:

Whitney comes from a background in banking, but has been interested in software engineering for a few years. Whitney began learning how to code with freeCodeCamp's platform, learning HTML, CSS, Sass, and Javascript. After obtaining their Responsive Web Design Certification, Whitney wanted to continue learning in a more structured classroom setting. In her spare time, she loves creating: DIY home projects, cooking and painting. Part of why she joined Hackbright is to learn how to create her own tech projects. 


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


## Future Implementations
Several features have been planned out to grow Educated Citizen app:
* autocomplete feature for forms
* charts to better show contribution information
* addition of bill summaries 

## Installation
You are welcome to run this app on your own machine.

Install PostgresQL 

Clone this repo:
https://github.com/adinahhh/educated-citizen.git

Create a virtual environment inside your project directory:
```
virtualenv env
source env/bin/activate
```

Next, install dependencies:

`pip3 install -r requirements.txt`

Register for a key with [VoteSmart API](https://votesmart.org/share/api#.XoNy3ZNKjBJ).

Register for a key with [OpenSecrets API](https://www.opensecrets.org/open-data/api).

Create a **`secrets.sh`** file. Save your keys in the file using the syntax below:
```
export VOTESMART_API_KEY="your_new_key"
export OPEN_SECRETS_API_KEY="second_new_key"
```

Activate your secrets.sh file into your current terminal session using command:
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

## License:

MIT License

Copyright (c) 2020 Whitney Zilton

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
