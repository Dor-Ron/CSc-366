from copycat import Copycat

base_terms = []
target_terms = []

# read analogy files and represent as data
with open('letter_analogies.txt') as analogy_list:
    for line in analogy_list:
        line = str(line)
        a = line[:line.index(":") - 1]
        b = line[:line.index("::") - 1]
        c = line[:line.index(":", line.index(":") + 1) - 1]
        d = line[line.index(":", line.index(":") + 1):]

        base_terms.append((a, b, c))
        target_terms.append(d)

        with open('test.nlg') as test_file:
            test_file.write("{} : {} :: {} :\n". format(
                a, b, c
            ))

        with open('solutions.txt') as test_file:
            test_file.write("{}\n". format(
                d
            ))

copycat_objects = []
for triplet in base_terms:
    copycat_objects.append(
        Copycat().run(triplet[a], triplet[b], triplet[c], 10)
    )

copycat_solutions = []
for obj in copycat_objects:
    solution_key, _ = max(obj.items()[1].count, key = obj.items()[0])
    copycat_solutions.append(solution_key)


total = len(target_terms)
correct_count = 0

for i in range(total):
    if target_terms[i] == copycat_solutions[i]:
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