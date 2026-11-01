 
from lab2_model import StatefulClassroomAgent

agent = StatefulClassroomAgent()
percepts = [(26.1, True), (25.9, True), (26.1, True), (25.9, True)]

for step, percept in enumerate(percepts, 1):
    prev = agent.previous_mode
    target, send = agent.act(*percept)
    outcome = "SEND" if send else "NO COMMAND"
    print(step, "| previous:", prev, "| percept:", percept,
          "| target:", target, "|", outcome)