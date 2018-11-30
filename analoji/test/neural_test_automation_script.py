from string import ascii_lowercase

actual_solutions = []
model_solutions = []

with open('neural_network_output.txt') as model_solutions_file:
    for line in model_solutions_file:
        model_solutions.append(str(line))

with open('solutions.txt') as solutions_file:
    for line in solutions_file:
        actual_solutions.append(str(line))

total = len(actual_solutions)
correct_count = 0

for i in range(total):
    if actual_solutions[i] == model_solutions[i]:
        correct_count += 1

print("""
Total analogies: {}
Correct solution count: {}
Accuracy: {}
""".format(
    total,
    correct_count,
    float(total) / correct_count
))