# Python Quiz Program with Multiple Choice Options

# List of questions with options
questions = [
    {
        "question": "1. What is the full form of HTML?",
        "options": ["A. Hyper Text Markup Language", "B. High Text Machine Language", "C. Hyperlinks and Text Markup Language", "D. Home Tool Markup Language"],
        "answer": "A"
    },
    {
        "question": "2. What is the use of CSS?",
        "options": ["A. To create web structure", "B. To design web pages", "C. To program backend", "D. To store data"],
        "answer": "B"
    },
    {
        "question": "3. For unordered list which type of marking is used?",
        "options": ["A. Numbers", "B. Roman Numerals", "C. Bullet points", "D. Letters"],
        "answer": "C"
    },
    {
        "question": "4. What does <em> tag in HTML do?",
        "options": ["A. Bold the text", "B. Emphasize the text (italic)", "C. Make text underlined", "D. Insert an image"],
        "answer": "B"
    },
    {
        "question": "5. Which tag is used to bold text in HTML?",
        "options": ["A. <bold>", "B. <strong>", "C. <bld>", "D. <em>"],
        "answer": "B"
    },
    {
        "question": "6. What is the use of hyperlink in HTML?",
        "options": ["A. Display images", "B. Connect to another page", "C. Create a list", "D. Make a table"],
        "answer": "B"
    },
    {
        "question": "7. Which is the correct syntax?",
        "options": ["A. <p>Paragraph<p>", "B. <p>Paragraph</p>", "C. <p>Paragraph>", "D. p>Paragraph</p>"],
        "answer": "B"
    },
    {
        "question": "8. Which attribute is used for inserting image in HTML?",
        "options": ["A. href", "B. link", "C. src", "D. img"],
        "answer": "C"
    },
    {
        "question": "9. For ordered list which type of marking is used?",
        "options": ["A. Numbers", "B. Dashes", "C. Bullets", "D. Symbols"],
        "answer": "A"
    },
    {
        "question": "10. <title> tag comes in which section of HTML?",
        "options": ["A. Body section", "B. Style section", "C. Footer section", "D. Head section"],
        "answer": "D"
    }
]

score = 0 


for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.\n")

print(f"Quiz Finished! Your Score: {score}/{len(questions)}")
