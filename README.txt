Setup instructions:

1. Create a virtual environment
2. cd to the assignment directory
3. pip install -r requirements.txt
4. python manage.py runserver

APIs:

1. Register [POST]:
	"Register a new user"

	Route: /auth/registration/
	Sample body: 
	{
		"username": "user7",
		"password1": "user7pass1",
		"password2": "user7pass1",
		"phone_number": "9307873079"
	}

2. Login [POST]:
	"User login"

	Route: /auth/login/
	Sample body:
	{
		"username": "user2",
		"password": "user2pass1"
	}

3. Report Spam [POST]:
	"Report a phone number as spam."

	Route: /report/
	Sample body:
	{
		"user_reported": "9307873014"
	}
	Auth: access_token

4. Search by name [GET]:
	"Search global database for users by username"

	Route: /search-by-username/?username={{username}}
	Auth: access_token

5. Search by phone number [GET]:
	"Search global database for users by phone_number"

	Route: /search-by-phone-number/?phone_number={{phone_number}}
	Auth: access_token


Testing the APIs:

Import the Postman Collection, send a request to the login or register API, and set the access token as bearer token to test other views.

Django admin credentials:
username: admin
password: adminpass1