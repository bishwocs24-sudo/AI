class VacuumCleanerAgent:
    def __init__(self):
        self.position = "A"

    def perceive(self, environment):
        return environment[self.position]

    def act(self, environment):
        status = self.perceive(environment)

        if status == "Dirty":
            print(f"Room {self.position} is dirty → Suck")
            environment[self.position] = "Clean"

        elif self.position == "A":
            print("Room A is clean → Move Right")
            self.position = "B"

        elif self.position == "B":
            print("Room B is clean → Move Left")
            self.position = "A"


# Environment: A and B can be Dirty or Clean
environment = {
    "A": "Dirty",
    "B": "Dirty"
}

agent = VacuumCleanerAgent()

print("Initial Environment:", environment)
print()

# Run the agent
for step in range(6):
    print(f"Step {step + 1}:")
    agent.act(environment)
    print("Environment:", environment)
    print()

print("Final Environment:", environment)
