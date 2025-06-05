import json
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .openrouter import call_openrouter
from .prompts import generate_quiz_prompt,generate_analysis_prompt,generate_learning_path_prompt,generate_final_quiz_prompt


@csrf_exempt
def generate_quiz(request):
    topic = request.GET.get("topic", "Graphs")
    prompt = generate_quiz_prompt(topic)
    result = call_openrouter(prompt)

    try:
        quiz_raw = result['choices'][0]['message']['content']

        # Remove the triple backticks and 'json' language tag
        cleaned = re.sub(r"^```json\n|```$", "", quiz_raw.strip())

        # Parse the cleaned JSON string
        quiz_data = json.loads(cleaned)

        return JsonResponse({"quiz": quiz_data}, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e), "response": result})


@csrf_exempt
def analyze_quiz(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        data = json.loads(request.body)
        questions = data.get("questions", [])
        answers = data.get("user_answers", [])
        print(questions, answers)
        prompt = generate_analysis_prompt(questions, answers)
        result = call_openrouter(prompt)
        print(result)
        raw = result['choices'][0]['message']['content']
        weak_concepts = json.loads(raw.strip().replace("```json", "").replace("```", ""))

        return JsonResponse({"weak_concepts": weak_concepts})

    except Exception as e:
        return JsonResponse({"error": str(e)})


@csrf_exempt
def learning_path(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        data = json.loads(request.body)
        weak_concepts = data.get("weak_concepts", [])

        prompt = generate_learning_path_prompt(weak_concepts)
        result = call_openrouter(prompt)

        raw = result['choices'][0]['message']['content']
        learning_path = json.loads(raw.strip().replace("```json", "").replace("```", ""))
        return JsonResponse({"learning_path": learning_path})

    except Exception as e:
        return JsonResponse({"error": str(e)})


@csrf_exempt
def final_quiz(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        data = json.loads(request.body)
        topic = data.get("topic", "Graphs")
        weak_concepts = data.get("weak_concepts", [])

        prompt = generate_final_quiz_prompt(topic, weak_concepts)
        result = call_openrouter(prompt)

        try:
            raw_quiz = result['choices'][0]['message']['content']
            cleaned = raw_quiz.strip().replace("```json", "").replace("```", "")
            quiz = json.loads(cleaned)
            return JsonResponse({"quiz": quiz})
        except Exception as inner:
            return JsonResponse({"error": str(inner), "response": result})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    