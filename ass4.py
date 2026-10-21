# Known facts
facts = {"Fever", "Cough"}

# Rules in the form: (conditions, conclusion)
rules = [
    (["Fever", "Cough"], "Flu"),
    (["Flu"], "Rest"),
    (["Rest"], "Recovery")
]

print("Initial Facts:", facts)
print("\nKnowledge Base Rules:")

for conditions, conclusion in rules:
    print("IF", " AND ".join(conditions), "THEN", conclusion)






def forward_chaining(facts, rules):
    known_facts = set(facts)
    inferred_facts = []

    while True:
        new_fact_found = False

        for conditions, conclusion in rules:
            if all(condition in known_facts for condition in conditions):
                if conclusion not in known_facts:
                    known_facts.add(conclusion)
                    inferred_facts.append(conclusion)
                    print("Inferred:", conclusion)
                    new_fact_found = True

        if not new_fact_found:
            break

    return known_facts, inferred_facts


print("FORWARD CHAINING")
print("Initial Facts:", facts)

final_facts, inferred = forward_chaining(facts, rules)

print("\nAll Known Facts:", final_facts)








def backward_chaining(goal, facts, rules, visited=None):
    if goal in facts:
        return True

    if visited is None:
        visited = set()

    if goal in visited:
        return False

    visited = visited | {goal}

    for conditions, conclusion in rules:
        if conclusion == goal:
            if all(
                backward_chaining(condition, facts, rules, visited.copy())
                for condition in conditions
            ):
                return True

    return False


print("BACKWARD CHAINING")

goal = "Recovery"
print("Goal to Prove:", goal)

if backward_chaining(goal, facts, rules):
    print("Result:", goal, "can be proved.")
else:
    print("Result:", goal, "cannot be proved.")






test_goals = ["Flu", "Rest", "Recovery", "Fever", "Headache"]

for goal in test_goals:
    result = backward_chaining(goal, facts, rules)

    if result:
        print(goal, "-> TRUE (Goal Proved)")
    else:
        print(goal, "-> FALSE (Goal Not Proved)")






