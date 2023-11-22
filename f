import random
import tkinter as tk
from tkinter import messagebox

def calculate_eq(factors):
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

def basic_level():
    basic_window = tk.Tk()
    basic_window.title("Basic Emotional Quotient (EQ) Calculator")

    tk.Label(basic_window, text="Please rate yourself on a scale of 1 to 10 for the following factors:").pack()

    factors = {}
    weights = [
        'Self-Awareness', 'Empathy', 'Self-Regulation',
        'Social Skills', 'Motivation', 'Stress Management',
        'Emotional Resilience', 'Adaptability', 'Emotional Expression'
    ]

    for factor in weights:
        frame = tk.Frame(basic_window)
        frame.pack(side=tk.TOP)

        tk.Label(frame, text=f"{factor}: ").pack(side=tk.LEFT)

        factors[factor] = tk.IntVar(value=0)  # Set initial value to 0
        for i in range(1, 11):
            tk.Radiobutton(frame, text=str(i), variable=factors[factor], value=i).pack(side=tk.LEFT)

    def calculate_percentage():
        eq_percentage = calculate_eq({k: v.get() for k, v in factors.items()})
        messagebox.showinfo("Result", f"Your Emotional Quotient (EQ) percentage is: {eq_percentage:.2f}%")
        basic_window.destroy()

    calculate_button = tk.Button(basic_window, text="Calculate EQ", command=calculate_percentage)
    calculate_button.pack()

    next_button = tk.Button(basic_window, text="Next", command=basic_window.destroy)
    next_button.pack()

    basic_window.mainloop()

def advanced_level():
    advanced_window = tk.Tk()
    advanced_window.title("Advanced Emotional Quotient (EQ) Calculator")

    tk.Label(advanced_window, text="You'll be presented with scenarios. Rate how you would respond on a scale of 1 to 10.").pack()

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
        # Add more scenarios here if needed
    }

    factors = {}
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

    chosen_scenarios = random.sample(list(scenarios_weights.keys()), 9)

    for scenario in chosen_scenarios:
        frame = tk.Frame(advanced_window)
        frame.pack(side=tk.TOP)

        tk.Label(frame, text=f"{scenario} (1-10): ").pack(side=tk.LEFT)

        factors[scenarios_weights[scenario]] = tk.IntVar()
        for i in range(1, 11):
            tk.Radiobutton(frame, text=str(i), variable=factors[scenarios_weights[scenario]], value=i).pack(side=tk.LEFT)

    def calculate_percentage():
        eq_percentage = calculate_eq({k: v.get() for k, v in factors.items()})
        print(eq_percentage)
        messagebox.showinfo("Result", f"Your Emotional Quotient (EQ) percentage is: {eq_percentage:.2f}%")
        advanced_window.destroy()

    ok_button = tk.Button(advanced_window, text="OK", command=calculate_percentage)
    ok_button.pack(pady=10)

    next_button = tk.Button(advanced_window, text="Next", command=advanced_window.destroy)
    next_button.pack()

    advanced_window.mainloop()

def main():
    main_window = tk.Tk()
    main_window.title("Emotional Quotient (EQ) Calculator")

    tk.Label(main_window, text="Select the level:").pack()

    basic_button = tk.Button(main_window, text="Basic Level", command=basic_level)
    basic_button.pack(side=tk.LEFT)

    advanced_button = tk.Button(main_window, text="Advanced Level", command=advanced_level)
    advanced_button.pack(side=tk.LEFT)

    main_window.mainloop()

if __name__ == "__main__":
    main()
