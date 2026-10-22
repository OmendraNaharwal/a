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

expected_actions = [
    "AC OFF",
    "AC OFF",
    "AC OFF",
    "AC ON",
    "AC ON",
    "AC ON"
]




for temperature in temperatures:
    action = smart_home_agent(temperature)
    print(f"Temperature: {temperature}°C -> {action}")






score = 0

for i, temperature in enumerate(temperatures):
    action = smart_home_agent(temperature)

    if action == expected_actions[i]:
        score += 1

accuracy = (score / len(temperatures)) * 100

print(f"Correct Decisions: {score}/{len(temperatures)}")
print(f"Decision Accuracy: {accuracy:.2f}%")
