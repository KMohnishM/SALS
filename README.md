# SALS (Student Activity Learning System)

An intelligent learning system that uses AI to generate personalized quizzes, analyze performance, and create custom learning paths for students. The system focuses on reinforcement learning and continuous improvement tracking.

## Features

### 1. Dynamic Quiz Generation
- Generate topic-specific quizzes using AI
- Endpoint: `GET /api/generate-quiz/?topic=<topic_name>`
- Returns a structured quiz with questions and answers
- Questions include difficulty levels and concept mapping

### 2. Performance Analysis
- Analyze quiz responses to identify weak areas
- Endpoint: `POST /api/analyze-quiz/`
- Input: Questions and user answers
- Output: 
  - List of weak concepts that need improvement
  - Detailed performance metrics
  - Concept-specific analysis

### 3. Personalized Learning Path
- Generate custom learning paths based on weak concepts
- Endpoint: `POST /api/learning-path/`
- Input: List of weak concepts
- Output: 
  - Structured learning path with resources
  - Practice exercises
  - Concept-specific recommendations
  - Progress tracking

### 4. Reinforcement Learning & Final Assessment
- Generate a final quiz focusing on previously weak areas
- Endpoint: `POST /api/final-quiz/`
- Input: Topic and weak concepts
- Output: 
  - Customized quiz targeting improvement areas
  - Mix of reinforcement and new concept questions
  - Varying difficulty levels
  - Detailed explanations

### 5. Progress Tracking & Improvement Analysis
- Submit final quiz and get comprehensive feedback
- Endpoint: `POST /api/submit-final-quiz/`
- Input: Final quiz answers
- Output:
  - Improvement percentage
  - List of improved concepts
  - List of still-weak concepts
  - New areas of weakness
  - Detailed feedback and recommendations
  - Personalized study suggestions

## Project Structure

```
SALS/
├── backend/
│   ├── sals_backend/     # Main Django project directory
│   ├── learning/         # Django app with core functionality
│   │   ├── views.py      # API endpoint implementations
│   │   ├── prompts.py    # AI prompt templates
│   │   ├── models.py     # Database models
│   │   └── openrouter.py # AI integration
│   ├── manage.py         # Django management script
│   └── db.sqlite3        # SQLite database
```

## Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)
- OpenRouter API key

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

4. Set up environment variables:
Create a `.env` file in the backend directory with:
```
OPENROUTER_API_KEY=your_api_key_here
HTTP_REFERER=http://localhost:8000
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
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
  -d '{
    "quiz_id": "1",
    "user_answers": [
      {"question_id": 1, "answer": "A"},
      {"question_id": 2, "answer": "B"}
    ]
  }'
```

### Get Learning Path
```bash
curl -X POST http://localhost:8000/api/learning-path/ \
  -H "Content-Type: application/json" \
  -d '{
    "quiz_attempt_id": "1",
    "weak_concepts": ["concept1", "concept2"]
  }'
```

### Generate Final Quiz
```bash
curl -X POST http://localhost:8000/api/final-quiz/ \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Graphs",
    "weak_concepts": ["concept1", "concept2"]
  }'
```

### Submit Final Quiz
```bash
curl -X POST http://localhost:8000/api/submit-final-quiz/ \
  -H "Content-Type: application/json" \
  -d '{
    "quiz_id": "2",
    "user_answers": [
      {"question_id": 1, "answer": "A"},
      {"question_id": 2, "answer": "B"}
    ]
  }'
```

## Development

- Built with Django REST framework
- Uses OpenRouter for AI-powered features
- Implements custom prompt engineering for optimal learning outcomes
- RESTful API design with JSON responses
- Focuses on reinforcement learning and continuous improvement


## License

This project is licensed under the MIT License - see the LICENSE file for details.

