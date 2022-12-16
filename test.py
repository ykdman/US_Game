import pandas

data = pandas.read_csv("50_states.csv")

# for i in data:
#     data["state"] = data["state"].astype(str)
#     data["x"] = data["x"].astype(float)
#     data["y"] = data["y"].astype(float)
print(len(data))
states_list = data["state"].to_list()
x_list = data["x"].to_list()
y_list = data["y"].to_list()


