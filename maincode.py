import random

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

    total_score = float(sum(factors.get(key, 0) * weights[key] for key in weights))
    max_score = float(10 * sum(weights.values()))

    eq_percentage = (total_score / max_score) * 100
    return eq_percentage

def basic_level():
    print("Welcome to the Basic Emotional Quotient (EQ) Calculator!")
    print("Please rate yourself on a scale of 1 to 10 for the following factors:")

    factors = {}
    weights = [
        'Self-Awareness', 'Empathy', 'Self-Regulation',
        'Social Skills', 'Motivation', 'Stress Management',
        'Emotional Resilience', 'Adaptability', 'Emotional Expression'
    ]

    for factor in weights:
        while True:
            try:
                rating = int(input(f"{factor} (1-10): "))
                if 1 <= rating <= 10:
                    factors[factor] = rating
                    break
                else:
                    print("Please enter a rating between 1 and 10.")
            except ValueError:
                print("Please enter a valid integer.")

    eq_percentage = calculate_eq(factors)
    print(f"\nYour Emotional Quotient (EQ) percentage is: {eq_percentage:.2f}%")

def advanced_level():
    print("Welcome to the Advanced Emotional Quotient (EQ) Calculator!")
    print("You'll be presented with scenarios. Rate how you would respond on a scale of 1 to 10.")

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
    weights = {
        'Self-Awareness': 0.15,
        'Empathy': 0.15,
        'Self-Regulation': 0.15,
        'Social Skills': 0.15,
        'Mot ivation': 0.1,
        'Stress Management': 0.05,
        'Emotional Resilience': 0.1,
        'Adaptability': 0.1,
        'Emotional Expression': 0.05
    }

    chosen_scenarios = random.sample(list(scenarios_weights.keys()), 9)

    for scenario in chosen_scenarios:
        while True:
            try:
                rating = int(input(f"Scenario: {scenario} (1-10): "))
                if 1 <= rating <= 10:
                    factors[scenarios_weights[scenario]] = rating
                    break
                else:
                    print("Please enter a rating between 1 and 10.")
            except ValueError:
                print("Please enter a valid integer.")

    eq_percentage = calculate_eq({k: factors.get(k, 0) for k in weights})
    print(f"\nYour Emotional Quotient (EQ) percentage is: {eq_percentage:.2f}%")

def main():
    print("Select the level:")
    print("1. Basic Level")
    print("2. Advanced Level")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        basic_level()
    elif choice == '2':
        advanced_level()
    else:
        print("Invalid choice. Please enter 1 or 2.")
main()
