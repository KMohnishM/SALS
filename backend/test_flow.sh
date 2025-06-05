#!/bin/bash

# 1. Generate initial quiz
echo "Generating initial quiz..."
QUIZ_RESPONSE=$(curl -s "http://localhost:8000/api/generate-quiz/?topic=Graphs")
QUIZ_ID=$(echo $QUIZ_RESPONSE | python -c "import sys, json; print(json.load(sys.stdin)['quiz_id'])")
echo "Got quiz_id: $QUIZ_ID"

# 2. Submit answers and get analysis
echo "Submitting answers..."
ANALYSIS_RESPONSE=$(curl -s -X POST http://localhost:8000/api/analyze-quiz/ \
  -H "Content-Type: application/json" \
  -d "{
    \"quiz_id\": \"$QUIZ_ID\",
    \"user_answers\": [
      {\"question_id\": 1, \"answer\": \"test_answer_1\"},
      {\"question_id\": 2, \"answer\": \"test_answer_2\"}
    ]
  }")
QUIZ_ATTEMPT_ID=$(echo $ANALYSIS_RESPONSE | python -c "import sys, json; print(json.load(sys.stdin)['quiz_attempt_id'])")
echo "Got quiz_attempt_id: $QUIZ_ATTEMPT_ID"

# 3. Generate learning path
echo "Generating learning path..."
LEARNING_PATH_RESPONSE=$(curl -s -X POST http://localhost:8000/api/learning-path/ \
  -H "Content-Type: application/json" \
  -d "{
    \"quiz_attempt_id\": \"$QUIZ_ATTEMPT_ID\",
    \"weak_concepts\": [\"concept1\", \"concept2\"]
  }")
LEARNING_PATH_ID=$(echo $LEARNING_PATH_RESPONSE | python -c "import sys, json; print(json.load(sys.stdin)['learning_path_id'])")
echo "Got learning_path_id: $LEARNING_PATH_ID"

# 4. Generate final quiz
echo "Generating final quiz..."
FINAL_QUIZ_RESPONSE=$(curl -s -X POST http://localhost:8000/api/final-quiz/ \
  -H "Content-Type: application/json" \
  -d "{
    \"topic\": \"Graphs\",
    \"weak_concepts\": [\"concept1\", \"concept2\"]
  }")
FINAL_QUIZ_ID=$(echo $FINAL_QUIZ_RESPONSE | python -c "import sys, json; print(json.load(sys.stdin)['quiz_id'])")
echo "Got final_quiz_id: $FINAL_QUIZ_ID"

# 5. Submit final quiz
echo "Submitting final quiz..."
FINAL_SUBMIT_RESPONSE=$(curl -s -X POST http://localhost:8000/api/submit-final-quiz/ \
  -H "Content-Type: application/json" \
  -d "{
    \"quiz_id\": \"$FINAL_QUIZ_ID\",
    \"user_answers\": [
      {\"question_id\": 1, \"answer\": \"final_answer_1\"},
      {\"question_id\": 2, \"answer\": \"final_answer_2\"}
    ]
  }")
echo "Final submission response: $FINAL_SUBMIT_RESPONSE"