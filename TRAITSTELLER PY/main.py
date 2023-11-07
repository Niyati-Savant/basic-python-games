import random

# Define the questions with their associated trait and polarity (+ or -)
questions = [
    ('OPN1', 'Openness', '+', "I have a rich vocabulary"),
    ('OPN2', 'Openness', '-', "I have difficulty understanding abstract ideas"),
    ('OPN3', 'Openness', '+', "I have a vivid imagination"),
    ('OPN4', 'Openness', '-', "I am not interested in abstract ideas"),
    # ('OPN5', 'Openness', '+', "I have excellent ideas"),
    # ('OPN6', 'Openness', '-', "I do not have a good imagination"),
    # ('OPN7', 'Openness', '+', "I am quick to understand things"),
    # ('OPN8', 'Openness', '+', "I use difficult words"),
    # ('OPN9', 'Openness', '+', "I spend time reflecting on things"),
    # ('OPN10', 'Openness', '+', "I am full of ideas"),

    # Add questions for other traits: Conscientiousness, Extroversion, Agreeableness, Emotional Stability
    ('CNS1', 'Conscientiousness', '+', "I am always prepared"),
    ('CNS2', 'Conscientiousness', '+', "I Like order"),
    ('CNS3', 'Conscientiousness', '-', "Leave my belongings around."),
    ('CNS4', 'Conscientiousness', '-', "Often forget to put things back in their proper place."),

    ('EXT1', 'Extroversion', '+', "I am the life of the party"),
    ('EXT2', 'Extroversion', '+', "Feel comfortable around people"),
    ('EXT3', 'Extroversion', '-', "Am quiet around strangers."),
    ('EXT4', 'Extroversion', '-', "I don't talk a lot"),

    ('AGR1', 'Agreeableness', '+', "I am interested in people"),
    ('AGR2', 'Agreeableness', '+', "I Sympathize with others' feelings."),
    ('AGR3', 'Agreeableness', '-', "I insult people"),
    ('AGR4', 'Agreeableness', '-', "Feel little concern for others."),

    ('ES1', 'Emotional Stability', '+', "I seldom feel blue"),
    ('ES2', 'Emotional Stability', '+', "Am relaxed most of the time."),
    ('ES3', 'Emotional Stability', '-', "I get stressed out easily"),
    ('ES4', 'Emotional Stability', '-', "Worry about things.")

    # Continue adding the remaining questions...
]

# Define the scoring system
scoring = {
    '+': {'VI': 1, 'MI': 2, 'N': 3, 'MA': 4, 'VA': 5},
    '-': {'VI': 5, 'MI': 4, 'N': 3, 'MA': 2, 'VA': 1}
}

# Shuffle the questions randomly
random.shuffle(questions)

# Collect user responses and calculate trait scores
trait_scores = {'Openness': 0, 'Conscientiousness': 0, 'Extroversion': 0, 'Agreeableness': 0, 'Emotional Stability': 0}
print(
    "Response options: VI-Very Inaccurate, MI-Moderately Inaccurate, N-Neither Inaccurate nor Accurate,MA-Moderately Accurate,VA-Very Accurate")
for question_id, trait, polarity, question_text in questions:
    print(question_text)

    response = input("Your response: ")

    while response not in scoring['+'] and response not in scoring['-']:
        print("Invalid response. Please enter a valid response.")

    score = scoring[polarity][response]
    trait_scores[trait] += score

# Display the trait scores
sorted_trait_scores = {k: v for k, v in sorted(trait_scores.items(), key=lambda item: item[1], reverse=True)}
print("\nTrait Scores (in descending order):")
for trait, score in sorted_trait_scores.items():
    print(f"{trait}: {score}")

# Maximum possible score for each trait (sum of scores for all questions related to that trait)
max_scores = {
    'Openness': sum([scoring[question[2]]['VA'] for question in questions if question[1] == 'Openness']),
    'Conscientiousness': sum([scoring[question[2]]['VA'] for question in questions if question[1] == 'Conscientiousness']),
    'Extroversion': sum([scoring[question[2]]['VA'] for question in questions if question[1] == 'Extroversion']),
    'Agreeableness': sum([scoring[question[2]]['VA'] for question in questions if question[1] == 'Agreeableness']),
    'Emotional Stability': sum([scoring[question[2]]['VA'] for question in questions if question[1] == 'Emotional Stability']),
}

# Calculate trait scores as percentages
# Calculate trait scores as percentages
trait_scores_percentage = {trait: (score / (5 * len([q for q in questions if q[1] == trait]))) * 100 for trait, score in trait_scores.items()}

# Display the trait scores as percentages
print("\nTrait Scores as Percentages (in descending order):")
for trait, score in sorted(trait_scores_percentage.items(), key=lambda item: item[1], reverse=True):
    print(f"{trait}: {score:.2f}%")

import matplotlib.pyplot as plt

# ... (Your existing code to calculate trait_scores_percentage)

# Extract trait names and percentage scores
traits = list(trait_scores_percentage.keys())
scores = list(trait_scores_percentage.values())

# Create a horizontal bar graph
plt.figure(figsize=(10, 5))
plt.barh(traits, scores, color='skyblue')
plt.xlabel('Percentage (%)')
plt.title('Trait Scores as Percentages')

# Display the bar graph
plt.show()
