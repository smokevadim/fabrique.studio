# Polls backend task

## Description 

This is the test task app that described in the [task.txt](task.txt) file (in Russian)
Its a REST backend app contains test Polls

## Installation

open terminal and run the following commands:

```shell script
git clone https://github.com/smokevadim/fabrique.studio.git
cd fabrique.studio
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata initial_data.json
```

## Usage

open terminal and run the following commands:

```shell script
python manage.py runserver
```

* open http://127.0.0.1:8000/

## API

`All routes compatible with CRUD`

####Get all active polls:
_GET: /api/polls/_

**Returns** active in this time polls.


#### Get poll questions
_GET: /api/polls/\<id\>/_

**Returns** all questions in poll with "id" 


#### Participation in poll
_POST: /api/polls/\<id\>/_

**Send** data in POST request with "user-id" in header (or without if anonymous) and body:
```
{           
            "poll": id,            
            "question": id,
            "answer": answer
}
```

#### Get details answered polls
_GET: /api/my_polls/_

**Send** GET request with "user-id" in HEADERS

**Returns** results of completed by "user_id" polls

## Models

* User
* Poll
* Question
* Answer

## Tech stack 

* Python 3.8: https://www.python.org/
* Django DRF: https://www.django-rest-framework.org/

## Tests

I'm going to use pytest-django implementation
* https://pytest-django.readthedocs.io/en/latest/

