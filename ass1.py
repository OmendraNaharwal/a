print("Smart Home Intelligent Agent")
print("Temperature Based AC Controller")

def smart_home_agent(temperature):
    
    if temperature > 25:
        action = "AC ON"
    else:
        action = "AC OFF"
    
    return action


temperature = 30

action = smart_home_agent(temperature)

print("Temperature:", temperature, "°C")
print("Agent Action:", action)


temperatures = [20, 24, 25, 27, 30, 35]

for temperature in temperatures:
    action = smart_home_agent(temperature)
    print("Temperature:", temperature, "°C ->", action)










# PR1: Intelligent Agents and PEAS Representation (CO1)

print("=" * 55)
print("       SMART HOME INTELLIGENT AGENT")
print("       Temperature-Based AC Controller")
print("=" * 55)










# 5. PERFORMANCE MEASURE

print("\n\n5. PERFORMANCE MEASURE")
print("-" * 55)

# Expected action according to the agent's control rule
expected_actions = [
    "AC OFF",
    "AC OFF",
    "AC OFF",
    "AC ON",
    "AC ON",
    "AC ON"
]

score = 0

for i, temperature in enumerate(temperatures):
    action, reason = smart_home_agent(temperature)

    if action == expected_actions[i]:
        score += 1

total_tests = len(temperatures)
accuracy = (score / total_tests) * 100

print(f"Correct decisions: {score}/{total_tests}")
print(f"Decision accuracy: {accuracy:.2f}%")




