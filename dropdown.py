import random
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle

class EmotionalQuotientCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotional Quotient (EQ) Calculator")

        self.initialize_gui()

    def initialize_gui(self):
        font = ('Arial', 12)

        # Use ThemedStyle for a more modern look
        style = ThemedStyle(self.root)
        style.set_theme("radiance")  

        center_frame = ttk.Frame(self.root)
        center_frame.pack(expand=True)

        ttk.Label(center_frame, text="Select the level:", font=font).pack()

        basic_button = ttk.Button(center_frame, text="Basic Level", command=self.start_basic_level, style='Large.TButton')
        basic_button.pack(side=tk.LEFT, padx=20)

        advanced_button = ttk.Button(center_frame, text="Advanced Level", command=self.start_advanced_level, style='Large.TButton')
        advanced_button.pack(side=tk.LEFT)

        ttk.Style().configure('Large.TButton', font=font)

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

    def create_rating_widgets(self, window, items):
        font = ('Arial', 12)
        factors = {}

        for item in items:
            frame = ttk.Frame(window)
            frame.pack(side=tk.TOP, pady=10)

            ttk.Label(frame, text=f"{item}: ", font=font).pack(side=tk.LEFT)

            factors[item] = tk.StringVar(value='0') 
            rating_dropdown = ttk.Combobox(frame, values=[str(i) for i in range(1, 11)], textvariable=factors[item], state='readonly', font=font)
            rating_dropdown.pack(side=tk.LEFT)

        return factors

    def start_basic_level(self):
        basic_window = tk.Toplevel(self.root)
        basic_window.title("Basic Emotional Quotient (EQ) Calculator")

        font = ('Arial', 12)

        ttk.Label(basic_window, text="Please rate yourself on a scale of 1 to 10 for the following factors:", font=font).pack()

        weights = [
            'Self-Awareness', 'Empathy', 'Self-Regulation',
            'Social Skills', 'Motivation', 'Stress Management',
            'Emotional Resilience', 'Adaptability', 'Emotional Expression'
        ]

        factors = self.create_rating_widgets(basic_window, weights)

        ttk.Button(basic_window, text="Calculate EQ", command=lambda: self.show_result(basic_window, factors), style='Large.TButton').pack(pady=20)
        ttk.Button(basic_window, text="Next", command=basic_window.destroy, style='Large.TButton').pack()

    def start_advanced_level(self):
        advanced_window = tk.Toplevel(self.root)
        advanced_window.title("Advanced Emotional Quotient (EQ) Calculator")

        font = ('Arial', 12)

        ttk.Label(advanced_window, text="You'll be presented with scenarios. Rate how you would respond on a scale of 1 to 10.", font=font).pack()

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
            frame.pack(side=tk.TOP, pady=10)

            ttk.Label(frame, text=f"{scenario}: ", font=font).pack(side=tk.LEFT)

            factors[scenarios_weights[scenario]] = tk.StringVar(value='0') 
            rating_dropdown = ttk.Combobox(frame, values=[str(i) for i in range(1, 11)], textvariable=factors[scenarios_weights[scenario]], state='readonly', font=font)
            rating_dropdown.pack(side=tk.LEFT)

        ttk.Button(advanced_window, text="Calculate EQ", command=lambda: self.show_result(advanced_window, factors), style='Large.TButton').pack(pady=20)
        ttk.Button(advanced_window, text="Next", command=advanced_window.destroy, style='Large.TButton').pack()

    def show_result(self, window, factors):
        eq_percentage = self.calculate_eq({k: int(v.get()) for k, v in factors.items()})
        messagebox.showinfo("Result", f"Your Emotional Quotient (EQ) percentage is: {eq_percentage:.2f}%")
        window.destroy()

def main():
    root = tk.Tk()
    app = EmotionalQuotientCalculator(root)

    # Use ThemedStyle for the root window
    style = ThemedStyle(root)
    style.set_theme("radiance")

    ttk.Style().configure('Large.TButton', font=('Arial', 12))

    root.mainloop()

if __name__ == "__main__":
    main()
