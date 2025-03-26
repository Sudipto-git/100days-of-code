import requests

def get_questions(amount=100, category=None, difficulty=None, question_type="boolean"):
    """
    Fetch questions from the Open Trivia Database API
    
    Parameters:
        amount: Number of questions (default 100)
        category: Category ID (optional)
        difficulty: easy, medium, hard (optional)
        question_type: boolean or multiple (default boolean for True/False questions)
    """
    url = "https://opentdb.com/api.php?amount=49"
    params = {
        "amount": amount,
        "type": question_type
    }
    
    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty
        
    response = requests.get(url, params=params)
    data = response.json()
    
    if data["response_code"] == 0:  # Success
        return data["results"]
    elif data["response_code"] == 1:  # Not enough questions
        print("Not enough questions available with your criteria. Trying with fewer constraints...")
        # Try without difficulty constraint
        if difficulty:
            return get_questions(amount=amount, category=category, difficulty=None, question_type=question_type)
        # Then try without category constraint
        elif category:
            return get_questions(amount=amount, category=None, difficulty=None, question_type=question_type)
        else:
            # If still not enough questions, get what's available
            print("Fetching maximum available questions...")
            return get_questions(amount=50, category=None, difficulty=None, question_type=question_type)
    else:
        print(f"Error fetching questions: {data['response_code']}")
        return []

# Example categories:
# 9: General Knowledge, 18: Computers, 23: History, 27: Animals
question_data = get_questions(amount=100, category=18, difficulty="medium")

# Print the number of questions fetched
print(f"Successfully fetched {len(question_data)} questions")

# If the API is unavailable, use these fallback questions
if not question_data:
    question_data = [
        {"question": "A slug's blood is green.", "correct_answer": "True"},
        # ...rest of fallback questions...
    ]