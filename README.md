# SALS (Student Activity Learning System)

An intelligent learning system that uses AI to generate personalized quizzes, analyze performance, and create custom learning paths for students.

## Features

### 1. Dynamic Quiz Generation
- Generate topic-specific quizzes using AI
- Endpoint: `GET /api/generate-quiz/?topic=<topic_name>`
- Returns a structured quiz with questions and answers

### 2. Performance Analysis
- Analyze quiz responses to identify weak areas
- Endpoint: `POST /api/analyze-quiz/`
- Input: Questions and user answers
- Output: List of weak concepts that need improvement

### 3. Personalized Learning Path
- Generate custom learning paths based on weak concepts
- Endpoint: `POST /api/learning-path/`
- Input: List of weak concepts
- Output: Structured learning path with resources and recommendations

### 4. Final Assessment Quiz
- Generate a final quiz focusing on previously weak areas
- Endpoint: `POST /api/final-quiz/`
- Input: Topic and weak concepts
- Output: Customized quiz targeting improvement areas

## Project Structure

```
SALS/
├── backend/
│   ├── sals_backend/     # Main Django project directory
│   ├── learning/         # Django app with core functionality
│   │   ├── views.py      # API endpoint implementations
│   │   ├── prompts.py    # AI prompt templates
│   │   └── openrouter.py # AI integration
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

## API Usage Examples

### Generate a Quiz
```bash
curl "http://localhost:8000/api/generate-quiz/?topic=Graphs"
```

### Analyze Quiz Results
```bash
curl -X POST http://localhost:8000/api/analyze-quiz/ \
  -H "Content-Type: application/json" \
  -d '{"questions": [...], "user_answers": [...]}'
```

### Get Learning Path
```bash
curl -X POST http://localhost:8000/api/learning-path/ \
  -H "Content-Type: application/json" \
  -d '{"weak_concepts": ["concept1", "concept2"]}'
```

### Generate Final Quiz
```bash
curl -X POST http://localhost:8000/api/final-quiz/ \
  -H "Content-Type: application/json" \
  -d '{"topic": "Graphs", "weak_concepts": ["concept1", "concept2"]}'
```

## Development

- Built with Django REST framework
- Uses OpenRouter for AI-powered features
- Implements custom prompt engineering for optimal learning outcomes
- RESTful API design with JSON responses

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