import pandas as pd
import config
import pickle
import numpy as np
import json

class Iris():
    def __init__(self,sepalwidth,petallength,petalwidth,species):
        self.sepalwidth=sepalwidth
        self.petallength=petallength
        self.petalwidth=petalwidth
        self.species=species.lower().strip()
    
    def load_model(self):
        # loading the model
        with open(config.model_path,'rb') as file:
            self.model=pickle.load(file)

        # loading the json path
        with open(config.json_path,'r') as file:
            self.json=json.load(file)

    # method for prediction
    def get_sepallength(self):
        # calling the method to load the model
        self.load_model()

        # creating a test array
        test_array=np.zeros(4)
        test_array[0]=self.sepalwidth
        test_array[1]=self.petallength
        test_array[2]=self.petalwidth
        test_array[3]=self.json["species"][self.species]
    
    
        
        prediction=self.model.predict([test_array])
        return np.around(prediction,1)