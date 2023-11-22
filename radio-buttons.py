import random
import tkinter as tk
from tkinter import ttk, messagebox

class EmotionalQuotientCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotional Quotient (EQ) Calculator")

        ttk.Label(self.root, text="Select the level:").pack()

        basic_button = ttk.Button(self.root, text="Basic Level", command=self.basic_level)
        basic_button.pack(side=tk.LEFT, padx=10)

        advanced_button = ttk.Button(self.root, text="Advanced Level", command=self.advanced_level)
        advanced_button.pack(side=tk.LEFT)

    def calculate_eq(self, factors):
        weights = {
            'Self-Awareness': 0.15,
            'Empathy': 0.15,
            'Self-Regulation': 0.15,
            'Social Skills': 0.15,
            'Motivation': 0.1,
            'Stress Management': 0.05,
            'Emotional Resilience': 0.1,
            'Adaptability': 0.1,
            'Emotional Expression': 0.05
        }

        total_score = sum(factors[key] * weights[key] for key in factors)
        max_score = 10 * sum(weights.values())

        eq_percentage = (total_score / max_score) * 100
        return eq_percentage

    def basic_level(self):
        basic_window = tk.Toplevel(self.root)
        basic_window.title("Basic Emotional Quotient (EQ) Calculator")

        ttk.Label(basic_window, text="Please rate yourself on a scale of 1 to 10 for the following factors:").pack()

        factors = {}
        weights = [
            'Self-Awareness', 'Empathy', 'Self-Regulation',
            'Social Skills', 'Motivation', 'Stress Management',
            'Emotional Resilience', 'Adaptability', 'Emotional Expression'
        ]

        for factor in weights:
            frame = ttk.Frame(basic_window)
            frame.pack(side=tk.TOP, pady=5)

            ttk.Label(frame, text=f"{factor}: ").pack(side=tk.LEFT)

            factors[factor] = tk.IntVar(value=0)  
            for i in range(1, 11):
                ttk.Radiobutton(frame, text=str(i), variable=factors[factor], value=i).pack(side=tk.LEFT)

        ttk.Button(basic_window, text="Calculate EQ", command=lambda: self.show_result(basic_window, factors)).pack(pady=10)
        ttk.Button(basic_window, text="Next", command=basic_window.destroy).pack()

    def advanced_level(self):
        advanced_window = tk.Toplevel(self.root)
        advanced_window.title("Advanced Emotional Quotient (EQ) Calculator")

        ttk.Label(advanced_window, text="You'll be presented with scenarios. Rate how you would respond on a scale of 1 to 10.").pack()

        scenarios_weights = {
            "You're in a team project, and a team member is not contributing. How would you handle this?": 'Adaptability',
            "You've received negative feedback on your work. How would you react and manage your emotions?": 'Emotional Resilience',
            "You've been assigned a task with a tight deadline. How do you plan to manage your stress and prioritize your work?": 'Stress Management',
            "A colleague appears upset. How would you approach and offer support?": 'Empathy',
            "You're in a disagreement with a friend. How would you handle resolving the conflict?": 'Social Skills',
            "You're faced with sudden changes in plans. How do you adapt and manage the situation?": 'Adaptability',
            "You've achieved a major goal. How do you express and celebrate your success?": 'Emotional Expression',
            "A difficult situation arises unexpectedly. How do you maintain emotional resilience?": 'Emotional Resilience',
            "You're dealing with criticism from someone close. How do you respond and handle your emotions?": 'Self-Regulation'
        }

        factors = {}
        chosen_scenarios = random.sample(list(scenarios_weights.keys()), 9)

        for scenario in chosen_scenarios:
            frame = ttk.Frame(advanced_window)
            frame.pack(side=tk.TOP, pady=5)

            ttk.Label(frame, text=f"{scenario} (1-10): ").pack(side=tk.LEFT)

            factors[scenarios_weights[scenario]] = tk.IntVar()
            for i in range(1, 11):
                ttk.Radiobutton(frame, text=str(i), variable=factors[scenarios_weights[scenario]], value=i).pack(side=tk.LEFT)

        ttk.Button(advanced_window, text="Calculate EQ", command=lambda: self.show_result(advanced_window, factors)).pack(pady=10)
        ttk.Button(advanced_window, text="Next", command=advanced_window.destroy).pack()

    def show_result(self, window, factors):
        eq_percentage = self.calculate_eq({k: v.get() for k, v in factors.items()})
        messagebox.showinfo("Result", f"Your Emotional Quotient (EQ) percentage is: {eq_percentage:.2f}%")
        window.destroy()

def main():
    root = tk.Tk()
    app = EmotionalQuotientCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
