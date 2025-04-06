Interview-Automation/
│
├── app.py                        # App entry point
├── requirements.txt              # All dependencies
├── .env                          # Environment variables
├── README.md
│
├── migrations/                   # Flask-Migrate DB version history
├── src/
│   ├── __init__.py               # App factory
│   ├── models/
│   │   └── userModel.py          # SQLAlchemy ORM User model
│   ├── controllers/
│   │   └── userController.py     # Logic for signup/login/get users
│   ├── routes/
│   │   └── userRoute.py          # API endpoints
|

<!-- clone repository -->
git clone https://github.com/yourname/interview-automation.git
cd interview-automation


<!-- database information on .env file -->
DB_USER='root'
DB_PASSWORD=''
DB_HOST='localhost'
DB_NAME='interview_automation' 

<!-- Virtual environment -->
python -m venv venv
venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For Linux/macOS

<!-- install required packages -->
pip install -r requirements.txt

<!-- Run database migrations -->
flask db init
flask db migrate -m "initial migration"
flask db upgrade


<!-- Run the flask app -->

flask run


<!-- Routes -->

<!-- Signup route -->

POST /users/signup
Content-Type: application/json

{
  "username": "raja",
  "email": "raja@example.com",
  "password": "secure123"
}

<!-- login route -->
POST /users/login
Content-Type: application/json

{
  "email": "raja@example.com",
  "password": "secure123"
}

On success returen
{
  "token": "JWT-TOKEN-HERE"
}


