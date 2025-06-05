import json

def generate_quiz_prompt(topic):
    return f"""You are an expert DSA instructor.

Generate a 10-question diagnostic quiz on the topic: "{topic}".
Rules:
- 3 easy, 4 medium, 3 hard MCQs
- Cover a wide range of sub-concepts
- Use clear, concise questions and 4 options (A–D)
- Each must include: question, options, correct answer (A/B/C/D), difficulty, and concept

Return output in *pure* JSON format (no explanation, no markdown), like:
[
  {{
    "question": "...",
    "options": ["A", "B", "C", "D"],
    "answer": "B",
    "difficulty": "medium",
    "concept": "Topological Sort"
  }},
  ...
]
"""

def generate_analysis_prompt(questions, answers):
    qa_pairs = json.dumps([
        {
            "question": q["question"],
            "concept": q["concept"],
            "correct": q["answer"],
            "user": a
        }
        for q, a in zip(questions, answers)
    ], indent=2)

    return f"""
You're an AI mentor evaluating a student's quiz answers.

Each entry below includes:
- The quiz question
- The concept it tests
- The correct answer
- The student's submitted answer

Identify which concepts the student struggled with (wrong answers only).
Return a *deduplicated* JSON list of weak concepts, no markdown, no explanation.

Example format: ["Binary Search", "Dynamic Programming"]
Quiz Attempts:
{qa_pairs}
"""

def generate_learning_path_prompt(weak_concepts):
    concept_list = ', '.join(weak_concepts)
    return f"""
You are an expert tutor guiding a student through weaknesses in DSA.

For each of these concepts: {concept_list}
Do the following:
1. Give a brief 2–3 line explanation (not definition, a teaching tip)
2. Suggest a high-quality online resource (GFG, YouTube, docs)

Return as a pure JSON array:
[
  {{
    "concept": "Dynamic Programming",
    "explanation": "...",
    "resource": "https://..."
  }},
  ...
]
No markdown. No extra text.
"""

def generate_final_quiz_prompt(topic, weak_concepts):
    weak = ", ".join(weak_concepts)
    return f"""
You are designing a final reinforcement quiz on the DSA topic "{topic}".

Guidelines:
- 6 medium-level MCQs from these weak concepts: {weak}
- 4 hard-level MCQs from other key concepts in "{topic}"
- Each MCQ must include: question, options (A–D), correct answer (A/B/C/D), difficulty, and concept

Return as a *pure JSON array*. No markdown, no explanation.
[
  {{
    "question": "...",
    "options": ["A", "B", "C", "D"],
    "answer": "A",
    "difficulty": "medium",
    "concept": "..."
  }},
  ...
]
"""
