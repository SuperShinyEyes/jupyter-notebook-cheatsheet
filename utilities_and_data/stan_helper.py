import os, sys
import pickle

def get_stan_model(model_name, model_code):
    path = os.path.abspath(os.path.join(os.path.curdir, model_name))

    if os.path.exists(path):
        print("Model exists already! Returning pickle.")
        return pickle.load(open(path, 'rb'))
    
    print("Path doesn't exist. Compiling model. It might take few minutes...")
    import pystan
    sm = pystan.StanModel(model_code=model_code)
    with open(model_name, 'wb') as f:
        pickle.dump(sm, f)
    return sm
