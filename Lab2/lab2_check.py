
from lab2_model import StatefulClassroomAgent

agent = StatefulClassroomAgent()
percepts = [(29, True), (29, True), (20, True),
            (26, True), (19, True), (29, False)]

for step, percept in enumerate(percepts, 1):
    prev = agent.previous_mode
    target, send = agent.act(*percept)
    if send:
        outcome = "SEND"
    else:
        outcome = "NO COMMAND"
    print(step, "| previous:", prev, "| percept:", percept,
          "| target:", target, "|", outcome)