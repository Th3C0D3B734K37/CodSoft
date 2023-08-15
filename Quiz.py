import tkinter as tk
from tkinter import messagebox, simpledialog

class Question:
    def __init__(self, question, choices, correct_choice):
        self.question = question
        self.choices = choices
        self.correct_choice = correct_choice

world_questions = [
    Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris"),
    Question("Which planet is known as the 'Red Planet'?", ["Mars", "Jupiter", "Venus", "Saturn"], "Mars"),
    Question("What is the largest mammal?", ["African Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "Blue Whale"),
    Question("Which mountain range is located in South America?", ["Himalayas", "Rocky Mountains", "Andes", "Alps"], "Andes"),
    Question("Which famous painting is known for its enigmatic smile?", ["Mona Lisa", "Starry Night", "The Scream", "The Persistence of Memory"], "Mona Lisa"),
    Question("What is the world's largest ocean?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "Pacific Ocean"),
    Question("What is the currency of Brazil?", ["Rupiah", "Yen", "Real", "Peso"], "Real"),
    Question("In which city is the iconic landmark, the Colosseum, located?", ["Rome", "Athens", "Cairo", "Barcelona"], "Rome"),
    Question("What is the largest desert in the world?", ["Sahara Desert", "Arabian Desert", "Gobi Desert", "Kalahari Desert"], "Sahara Desert"),
    Question("What is the national flower of Japan?", ["Rose", "Tulip", "Cherry Blossom", "Sunflower"], "Cherry Blossom"),
]

india_questions = [
    Question("Who was the first Prime Minister of India?", ["Jawaharlal Nehru", "Mahatma Gandhi", "Rajiv Gandhi", "Indira Gandhi"], "Jawaharlal Nehru"),
    Question("In which year did India gain independence?", ["1947", "1950", "1930", "1962"], "1947"),
    Question("Which river is the longest in India?", ["Ganges", "Yamuna", "Brahmaputra", "Godavari"], "Ganges"),
    Question("Who is known as the 'Father of the Indian Constitution'?", ["Sardar Vallabhbhai Patel", "B.R. Ambedkar", "Mahatma Gandhi", "Jawaharlal Nehru"], "B.R. Ambedkar"),
    Question("What is the national animal of India?", ["Tiger", "Lion", "Elephant", "Peacock"], "Tiger"),
    Question("Which Mughal emperor built the Taj Mahal?", ["Akbar", "Shah Jahan", "Aurangzeb", "Humayun"], "Shah Jahan"),
    Question("Which state is famous for the Sun Temple in Konark?", ["Tamil Nadu", "Odisha", "Karnataka", "Andhra Pradesh"], "Odisha"),
    Question("What is the traditional dance form of Kerala?", ["Kathak", "Kuchipudi", "Bharatanatyam", "Kathakali"], "Kathakali"),
    Question("Who wrote the Indian national anthem, 'Jana Gana Mana'?", ["Rabindranath Tagore", "Bankim Chandra Chattopadhyay", "Subhas Chandra Bose", "Mahatma Gandhi"], "Rabindranath Tagore"),
    Question("Which festival is known as the Festival of Lights in India?", ["Diwali", "Holi", "Eid", "Christmas"], "Diwali"),
]

state_questions = [
    Question("Which state in India is known as the 'Land of Five Rivers'?", ["Punjab", "Rajasthan", "Haryana", "Gujarat"], "Punjab"),
    Question("What is the capital of Karnataka?", ["Chennai", "Mumbai", "Bangalore", "Kolkata"], "Bangalore"),
    Question("Which state is famous for the Backwaters?", ["Kerala", "Tamil Nadu", "Karnataka", "Goa"], "Kerala"),
    Question("What is the state bird of Rajasthan?", ["Peacock", "Parrot", "Sparrow", "Crow"], "Peacock"),
    Question("Which state is known as the 'Spice Garden of India'?", ["Kerala", "Karnataka", "Tamil Nadu", "Andhra Pradesh"], "Kerala"),
    Question("In which state is the famous Rann of Kutch located?", ["Rajasthan", "Gujarat", "Haryana", "Madhya Pradesh"], "Gujarat"),
    Question("Which river is often referred to as the 'Ganga of the South'?", ["Godavari", "Krishna", "Cauvery", "Yamuna"], "Cauvery"),
    Question("In which state is the iconic Hawa Mahal located?", ["Rajasthan", "Uttar Pradesh", "Madhya Pradesh", "Gujarat"], "Rajasthan"),
    Question("Which state is famous for the Ajanta and Ellora Caves?", ["Maharashtra", "Madhya Pradesh", "Uttar Pradesh", "Bihar"], "Maharashtra"),
    Question("What is the state flower of Sikkim?", ["Orchid", "Rose", "Rhododendron", "Lily"], "Rhododendron"),
]

programming_questions = [
    Question("What language is known as the 'mother of all languages'?", ["Python", "C++", "Assembly", "Java"], "Assembly"),
    Question("What does HTML stand for?", ["Hyper Text Markup Language", "Highly Transferable Machine Language", "Hyper Transfer Markup Language", "Home Tool Markup Language"], "Hyper Text Markup Language"),
    Question("Which programming language is often used for web development?", ["Python", "C#", "Ruby", "JavaScript"], "JavaScript"),
    Question("What does SQL stand for?", ["Structured Query Language", "Simple Query Language", "System Query Language", "Standard Query Language"], "Structured Query Language"),
    Question("Which programming language is named after a mathematician and logician?", ["Ada", "Pascal", "Cobol", "Fortran"], "Ada"),
    Question("What is the purpose of a version control system like Git?", ["Manage databases", "Control user access", "Manage code versions", "Create web pages"], "Manage code versions"),
    Question("What is the acronym 'API' stand for in programming?", ["All-Purpose Interface", "Application Program Interface", "Automated Program Indicator", "Advanced Programming Integration"], "Application Program Interface"),
    Question("Which programming language is often used for machine learning and data analysis?", ["Python", "Java", "C#", "Ruby"], "Python"),
    Question("What is the difference between a compiler and an interpreter?", ["Interpreters are faster than compilers", "Compilers execute code directly", "Interpreters convert code to machine language", "Compilers translate code before runtime"], "Compilers translate code before runtime"),
    Question("What is the primary function of an 'if-else' statement in programming?", ["Loop through data", "Perform arithmetic operations", "Assign values to variables", "Make decisions based on conditions"], "Make decisions based on conditions"),
]

economics_questions = [
    Question("What is inflation?", ["Increase in the supply of money", "Decrease in the price level", "Increase in the price level", "Decrease in the supply of money"], "Increase in the price level"),
    Question("What is GDP?", ["Global Domestic Product", "Gross Domestic Product", "General Domestic Product", "Government Development Plan"], "Gross Domestic Product"),
    Question("What is the opportunity cost?", ["The total cost of production", "The cost of alternatives forgone", "The monetary cost of an item", "The cost of raw materials"], "The cost of alternatives forgone"),
    Question("What is a monopoly?", ["A type of board game", "A market structure with a single seller", "A government regulation", "A type of tax"], "A market structure with a single seller"),
    Question("What is the concept of 'supply and demand' in economics?", ["The quantity of goods available", "The willingness to buy goods", "The relationship between price and quantity", "The total value of goods produced"], "The relationship between price and quantity"),
    Question("Which economic term refers to the total value of all goods and services produced in a country?", ["Net worth", "Gross Domestic Product", "Inflation rate", "Trade balance"], "Gross Domestic Product"),
    Question("What is the role of the Federal Reserve in the U.S. economy?", ["Fiscal policy", "Monetary policy", "Tax collection", "Government spending"], "Monetary policy"),
    Question("What is a budget deficit?", ["When government revenues exceed expenditures", "When government expenditures exceed revenues", "The total amount of public debt", "A surplus of consumer spending"], "When government expenditures exceed revenues"),
    Question("What is the concept of 'opportunity cost'?", ["The next best alternative given up when a decision is made", "The total cost of production", "The monetary cost of an item", "The cost of raw materials"], "The next best alternative given up when a decision is made"),
    Question("What is the law of diminishing returns?", ["As production increases, output decreases", "As production increases, output remains constant", "As input increases, output increases proportionally", "As input increases, output eventually decreases"], "As input increases, output eventually decreases"),
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.welcome_text = tk.Label(root, text="Welcome to the Quiz App!")
        self.welcome_text.pack()

        self.world_button = tk.Button(root, text="World Quiz", command=self.start_world_quiz)
        self.india_button = tk.Button(root, text="India Quiz", command=self.start_india_quiz)
        self.state_button = tk.Button(root, text="State Quiz", command=self.start_state_quiz)
        self.programming_button = tk.Button(root, text="Programming Quiz", command=self.start_programming_quiz)
        self.economics_button = tk.Button(root, text="Economics Quiz", command=self.start_economics_quiz)

        self.world_button.pack()
        self.india_button.pack()
        self.state_button.pack()
        self.programming_button.pack()
        self.economics_button.pack()

    def start_world_quiz(self):
        self.start_quiz("World Quiz", world_questions)

    def start_india_quiz(self):
        self.start_quiz("India Quiz", india_questions)

    def start_state_quiz(self):
        self.start_quiz("State Quiz", state_questions)

    def start_programming_quiz(self):
        self.start_quiz("Programming Quiz", programming_questions)

    def start_economics_quiz(self):
        self.start_quiz("Economics Quiz", economics_questions)

    def start_quiz(self, quiz_title, questions):
        num_questions = len(questions)
        messagebox.showinfo(quiz_title, f"This segment has {num_questions} questions. If you want more questions, you can add them by accessing the code through the GitHub repository.")

        score = 0
        for idx, question in enumerate(questions, start=1):
            user_choice = self.show_question_dialog(quiz_title, question, idx, num_questions)
            if user_choice == question.correct_choice:
                score += 1

        messagebox.showinfo("Quiz Completed", f"You've completed the {quiz_title}! Your score: {score}/{num_questions}")

    def show_question_dialog(self, quiz_title, question, current_idx, total_questions):
        user_choice = simpledialog.askstring(f"{quiz_title} - Question {current_idx}/{total_questions}", 
                                             f"{question.question}\n\nSelect one of the following options:\n" + "\n".join(question.choices))
        return user_choice

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
