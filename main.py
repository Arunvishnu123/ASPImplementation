import clingo

file_path = r"C:\Users\ArunRAVEENDRANNAIRSH\Desktop\aspimplementation\asp.pl"
file = open(file_path, "r")
file_content = file.read()
file.close()

class Context:
        pass
def on_model(m):
        print(m)

ctl = clingo.Control()
ctl.add("base", [], file_content)
ctl.ground([("base", [])], context=Context())
ctl.solve(on_model=on_model)