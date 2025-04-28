import tkinter as tk
import random
from tkinter import messagebox

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

MOVE_STEP = 50

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu du Lapin Intelligent 🐰")

        # Canvas
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="lightgreen")
        self.canvas.pack()

        # Charger et redimensionner l'image du lapin
        self.rabbit_img = tk.PhotoImage(file="rabbit.png")
        self.rabbit_img = self.rabbit_img.subsample(7, 7)  # Plus petit (divisé par 7)

        # Position initiale du lapin
        self.rabbit = self.canvas.create_image(50, WINDOW_HEIGHT//2, anchor="nw", image=self.rabbit_img)

        # Question
        self.question_label = tk.Label(root, text="", font=("Arial", 24), bg="lightgreen")
        self.question_label.pack(pady=10)

        # Champ pour réponse
        self.answer_entry = tk.Entry(root, font=("Arial", 24), justify="center")
        self.answer_entry.pack(pady=10)

        # Bouton de validation
        self.submit_button = tk.Button(root, text="Valider ma réponse ✅", font=("Arial", 20),
                                       bg="#4CAF50", fg="white", padx=20, pady=10, command=self.check_answer)
        self.submit_button.pack(pady=10)

        # Démarrer première question
        self.new_question()

    def new_question(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-", "*", "/"])

        if operation == "+":
            self.current_answer = num1 + num2
        elif operation == "-":
            self.current_answer = num1 - num2
        elif operation == "*":
            self.current_answer = num1 * num2
        elif operation == "/":
            self.current_answer = num1 // num2  # division entière

        self.current_question = f"{num1} {operation} {num2}"
        self.question_label.config(text=f"Résous : {self.current_question}")
        self.answer_entry.delete(0, tk.END)

    def check_answer(self):
        user_answer = self.answer_entry.get()
        try:
            if int(user_answer) == self.current_answer:
                self.canvas.move(self.rabbit, MOVE_STEP, 0)  # avancer
            else:
                self.canvas.move(self.rabbit, -MOVE_STEP//2, 0)  # reculer un peu
        except:
            pass

        # Vérifier si le lapin a atteint la fin
        pos = self.canvas.coords(self.rabbit)
        if pos[0] >= WINDOW_WIDTH - 100:
            messagebox.showinfo("Victoire 🎉", "Bravo Zaza ! Tu as gagné 🏆")
            self.root.quit()

        self.new_question()

# Lancer le jeu
root = tk.Tk()
game = Game(root)
root.mainloop()
