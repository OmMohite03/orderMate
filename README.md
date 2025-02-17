# OrderMate

OrderMate is a Django REST Framework (DRF) application that tracks orders, dispatches, and received items for a computer parts business. It provides a monthly summary of transactions and allows filtering data by specific months. The application includes both API endpoints and a simple frontend for visualization.

## Features
- **CRUD Operations** for Orders, Dispatches, and Received Items
- **REST API** built using Django REST Framework (DRF)
- **Monthly Summary API** to fetch order, dispatch, and received counts
- **Interactive Frontend** with filtering and sorting
- **PostgreSQL Database** for data persistence

## Project Structure
```
orderMate/
│── manage.py
│── orderMate/           # Main Django project settings
│── users/               # Users app (handles user management)
│── orders/              # Orders app (handles orders, dispatches, and received)
│── templates/           # Contains summary.html for UI
│── db.sqlite3           # (If using SQLite) or PostgreSQL database
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- PostgreSQL (or SQLite for development)
- Django 4+
- Django REST Framework

### Steps to Run Locally
1. **Clone the Repository**
   ```bash
   git clone https://github.com/OmMohite03/orderMate.git
   cd orderMate
   ```

2. **Create a Virtual Environment & Install Dependencies**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Database (PostgreSQL)**
   Update `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'ordermate_db',
           'USER': 'yourusername',
           'PASSWORD': 'yourpassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

4. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   Access the app at `http://127.0.0.1:8000`

## API Endpoints
| Method | Endpoint             | Description                   |
|--------|----------------------|-------------------------------|
| GET    | /api/orders/         | List all orders              |
| POST   | /api/orders/         | Create a new order           |
| GET    | /api/orders/{id}/    | Retrieve order by ID         |
| PUT    | /api/orders/{id}/    | Update an order              |
| DELETE | /api/orders/{id}/    | Delete an order              |
| GET    | /api/summary/        | Get monthly summary          |
| GET    | /api/summary/?month=January | Get summary for a specific month |

## Frontend (HTML UI)
- Located in `templates/summary.html`
- Uses **JavaScript Fetch API** to interact with the backend
- Provides **monthly filtering and sorting**

## Contributing
Pull requests are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

