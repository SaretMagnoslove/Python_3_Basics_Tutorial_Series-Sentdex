import pickle
# creating an example dict to pickle
example_dict = {1:"6",2:"2",3:"f"}
# pickling the dict
pickle_out = open("dict.pickle", "wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()
# then back to dict format
pickle_in = open("dict.pickle", "rb")
example_dict = pickle.load(pickle_in)

print(example_dict)