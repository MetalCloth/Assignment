import re

def classify_and_respond(question: str) -> str:
    """
    Args:
        question: The user's input question as a string.

    Function:
        Classifies a user's question into 'factual', 'opinion', or 'math' and returns a response
        uses simple keyword and pattern matching for classification.

    Output:
        A string containing the classification and a corresponding response.
    """
    question_lower = question.lower().strip()

    # --- 1. Math Classification ---
    math_keywords = ['calculate', 'what is', 'plus', 'minus', 'times', 'divided by', 'multiplied by','polynomial']
    math_pattern = r'(\d+\s*[\+\-\*\/]\s*\d+)'

    if any(keyword in question_lower for keyword in math_keywords) or re.search(math_pattern, question_lower):
        classification = "Math"
        response = "This sounds like a math problem"
        return f"Classification: {classification}\nResponse: {response}"

    # --- 2. Opinion Classification ---
    opinion_keywords = ['think', 'believe', 'should', 'best', 'worst', 'favorite', 'opinion']
    if any(keyword in question_lower for keyword in opinion_keywords):
        classification = "Opinion"
        response = "This sounds like a opinion"
        return f"Classification: {classification}\nResponse: {response}"

    # --- 3. Factual Classification (Default) ---
    factual_keywords = ['who', 'what', 'when', 'where', 'why', 'how', 'is', 'are', 'was', 'were']
    if any(question_lower.startswith(keyword) for keyword in factual_keywords):
        classification = "Factual"
        response = "This sounds like a facts"
        return f"Classification: {classification}\nResponse: {response}"

    # Fallback for questions that don't fit the patterns
    return "Classification: Unclassified\nResponse: I'm not sure how to classify that question. Can you rephrase it?"

if __name__ == "__main__":
    print("Classifier Agent")
    print("Ask a question, or type 'exit' to quit.")

    while True:
        user_question = input("\nYour Question: ")
        if user_question.lower() == 'exit':
            break

        result = classify_and_respond(user_question)
        print(result)
