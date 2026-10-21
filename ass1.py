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


