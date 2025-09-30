# Introduction
> **Note:** this is a work in progress, this document may contain incomplete
> and inaccurate information. Nevertheless, this document serves as a way
> to share knowledge to the group

This document contains all the learnings and questions the developer
had while learning API automation testing.
---
In API testing, these are the things being verified and tested:

- Status code
- Response headers
- Deeplinks
- Media content

Automation can be done in Postman (Javascript) or in Python (Python requests)

There are 4 main activities in API

- GET
- POST
- PUT
- DELETE


## Headers

---
Headers are basically the head of the API message, this part contains the necessary
settings for receiving the response of the API.

Some common content of this are:
- `'Content-type': 'application/json'`
- `'Authorization': 'Bearer <auth_id'`
- `'Accept': 'text/plain'`

### Difference between `Accept` and `Content-type`
`Accept` is for receiving the response in a specific format.  
`Content-type` specifies what is the format of the body being sent by POST/PUT
so that the API would recognize it.

### Testing API with headers
A tester can test the security of API by checking if the API would accept content
that is different from the one that is being accepted by it.  
i.e. `'Content-type': 'application/json'`
Pass in content in XML, Javascript, etc.

Check if passing in no `'Content-type'` would still be accepted.

## Difference between POST and PUT

---
**POST** is for adding a new resource in the API.
**PUT** is for updating an existing resource in the API.  

### What happens when I use **POST** with an existing resource in the API?
Some API have a catch/handling for this specific scenario. A common catch is to
just update the existing resource.

If the API has no handling on this situation, then there will be duplication of data
that attackers can take advantage of to corrupt data or overload the server.

Since during GET requests, the GET must specify the resource, if there are duplication
of data, the GET request might behave differently from what is expected.

## Authorization

---
Authorization is needed to be passed in order to make sure only the user/creator 
can modify, add, and delete their content.

This is done by adding an `'Authorization': 'Bearer <auth_id>` in the header.

## Status Codes

---

`201` - Successful creation of a new resource.  
`200` - Successful access of resource/page.  
`404` - Resource/page not found.  

## Passing Parameters in URL

---
The basic format of a URL is  
`http://www.site.com/page.html?parameter1=value1&parameter2=value2`  
if we dissect this, we can arrive to each part:  

`http` - web protocol  
`www` - world wide web  
`http://www.site.com/page.html` - the actual url of the website  
`?` - the beginning of the query string  
`parameter1` - parameter name  
`=` - equal or equivalent value  
`value1` - the value inside the parameter that is being queried  
`&` - query string operator to indicate AND  
`parameter2=value2` - second query  

---
## Creating an API automation framework with PyTest

The prerequisite files are:
1. pytest.ini
2. requirements.txt
3. conftest.py
4. utils/api_client.py

### pytest.ini
this contains the settings/configuration of the pytest

### requirements.txt
this contains the required libraries to install

### conftest.py
this contains the setup and teardown of the pytest (fixture)  
this also contains the creation of reports using pytest.html (hookimpl)  

## utils/api_client.py
this contains the class to test the api

## Issue with running with PyTest
Encountered issue:  
When I run pytest in terminal, I get ModuleNotFoundError for `git_common`  
Even if Python itself can find it (no errors shown in code), PyTest can't
seem to see it.  

Solution:  
Add `__init__.py` to the class module and the test folder and then run
`python -m pytest` instead of just pytest.  
Working theory as to why this is is because, running pytest might be
calling the Python in your system and not the one in your venv