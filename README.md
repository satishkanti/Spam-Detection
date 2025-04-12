# 📱 Spam Detection API (Phone Number Lookup)

A Django REST API backend built to support a mobile app that helps users identify spam phone numbers and search for contacts by name or number — inspired by apps like Truecaller.

---

## 🔧 Features

- ✅ User registration with phone number (email optional)
- ✅ JWT-based user login & authentication
- ✅ Add personal contacts (automatically imported in actual app)
- ✅ Mark any number as spam
- ✅ Search for a person by name or phone number
- ✅ Calculate and display **spam likelihood**
- ✅ Restrict email visibility unless the searching user is in the contact list
- ✅ All endpoints protected (no public access)

---

## 🧱 Tech Stack

- **Framework:** Django 4.2.3
- **API:** Django REST Framework (DRF)
- **Auth:** JWT (via `djangorestframework-simplejwt`)
- **Docs:** Swagger / ReDoc (via `drf-yasg`)
- **Database:** SQLite (for development)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/spam-detection-api.git
   cd spam-detection-api
2. Create and activate a virtual environment
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
3. Install dependencies
   pip install -r requirements.txt
4. Apply migrations
   python manage.py migrate
5. Create a superuser
   python manage.py createsuperuser
6. Populate the database with sample data (Optional)
   python manage.py populatedb
7. Run the development server
   python manage.py runserver

---

🔐 Authentication

This project uses JWT authentication.
-> Obtain token:
      POST /api/token/
     {
        "username": "your_username",
        "password": "your_password"
     }
-> Use the token: Add to headers:
      Authorization: Bearer <access_token>

---

📚 API Endpoints
Method	Endpoint	Description
POST	/api/users/	Register a new user (name, phone number, password, and optional email)
POST	/api/token/	Obtain access and refresh JWT tokens
POST	/api/token/refresh/	Refresh the JWT access token
GET	/api/contacts/	Get the list of authenticated user's contacts
POST	/api/contacts/	Add a new contact to the authenticated user
POST	/api/contacts/{id}/mark_as_spam/	Mark a contact (by ID) as spam
GET	/api/search/name/?q=<name>	Search for contacts by full or partial name
GET	/api/search/number/?q=<phone_number>	Search by phone number. Returns results from global database

📌 All routes are protected — must be logged in using JWT.

---

🧪 Sample Data Script
A management command is included to generate random users and contacts:
    python manage.py populatedb

---

🧾 Requirements
    Django==4.2.3
    djangorestframework==3.14.0
    djangorestframework-simplejwt==5.2.2
    drf-yasg==1.21.5

---

📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


