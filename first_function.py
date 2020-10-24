import random

def function():
    bangerz = ["As Much As I Ever Could", "Same Road", "Long Way", "Balloons",
                "Music Is Math", "Michicant", "Return of The Dreamer"]

    shuffle = random.choice(bangerz) 

    print(f"This current banger is {shuffle}")

function()