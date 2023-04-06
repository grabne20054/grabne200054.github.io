import random
from fpdf import FPDF

class Question:
    def __init__(self, topic, text):
        self.topic = topic
        self.text = text
    
    def __str__(self):
        return f"{self.topic}: {self.text}"
    
class QuestionBank:
    def __init__(self):
        self.topics = ["Geography", "Physics", "Chemistry", "Biology", "History"]
        self.questions = {}
        
        self.questions["Geography"] = [
            "What is the capital of France?",
            "Which is the largest continent in the world?",
            "What is the highest mountain peak in the world?"
        ]
        
        self.questions["Physics"] = [
            "What is the formula for force?",
            "What is the unit of electric current?",
            "What is the law of conservation of energy?"
        ]
        
        self.questions["Chemistry"] = [
            "What is the atomic number of carbon?",
            "What is the pH of a neutral solution?",
            "What is the chemical symbol for gold?"
        ]
        
        self.questions["Biology"] = [
            "What is the smallest unit of life?",
            "What is the largest organ in the human body?",
            "What is the process of photosynthesis?"
        ]
        
        self.questions["History"] = [
            "Which civilization built the Pyramids of Giza?",
            "Who was the first emperor of Rome?",
            "What was the main cause of World War II?"
        ]
    
    def get_question(self, topic):
        if topic not in self.topics:
            return None
        
        if not self.questions[topic]:
            return None
        
        index = random.randint(0, len(self.questions[topic])-1)
        question = self.questions[topic][index]
        self.questions[topic].pop(index)
        
        return Question(topic, question)

class Exam:
    def __init__(self, num_questions):
        self.num_questions = num_questions
        self.question_bank = QuestionBank()
        self.questions = []
        
        for i in range(num_questions):
            topic = random.choice(self.question_bank.topics)
            question = self.question_bank.get_question(topic)
            while question is None:
                topic = random.choice(self.question_bank.topics)
                question = self.question_bank.get_question(topic)
            self.questions.append(question)
            
    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        for i, question in enumerate(self.questions):
            text = f"Q{i+1}. {str(question)}"
            pdf.cell(0, 10, text, ln=1)
            pdf.cell(0, 5, "", ln=1)
        
        pdf.output("exam.pdf")
        
if __name__ == "__main__":
    exam = Exam(10)
    exam.generate_pdf()
