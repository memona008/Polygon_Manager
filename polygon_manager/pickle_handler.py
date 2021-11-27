import pickle
def load_pickle(filename):
    with open(filename, 'rb') as handle:
        return pickle.load(handle)

def save_pickle(filename, data):
    with open(filename, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)