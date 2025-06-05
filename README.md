# SALS (Student Activity Learning System)

A Django-based backend system for managing student activities and learning processes.

## Project Structure

```
SALS/
├── backend/
│   ├── sals_backend/     # Main Django project directory
│   ├── learning/         # Django app directory
│   ├── manage.py         # Django management script
│   └── db.sqlite3        # SQLite database
```

## Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd SALS
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## Features

- Django-based backend system
- SQLite database for data storage
- RESTful API endpoints
- Student activity management
- Learning process tracking

## Development

- The project uses Django's built-in development server for local development
- Database migrations are managed through Django's migration system
- API endpoints are defined in the `urls.py` file

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/SALS](https://github.com/yourusername/SALS) 