#!/usr/bin/python

import pandas as pd
import joblib
import sys
import os

def predict(Year, Mileage, State, Make, Model):
    
     
    xgb = joblib.load(os.path.dirname(__file__) + '/price.pkl') 
    data = {
    'Year':    Year, 
    'Mileage': Mileage, 
    'State':   State, 
    'Make':    Make, 
    'Model':   Model
    }
    
    df = pd.DataFrame([data])
    
    
    df["State"] = df["State"].astype("category")
    df["Make"]  = df["Make"].astype("category")
    df["Model"] = df["Model"].astype("category")    
    # Make prediction
    price = xgb.predict(df)[0]

    return price


if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Please add data')
        
    else:

        Year      = sys.argv[1]
        Mileage   = sys.argv[2]
        State     = sys.argv[3]
        Make      = sys.argv[4]
        Model = sys.argv[5]
        

        p1 = predict(Year, Mileage, State, Make, Model)
        
        #print(url)
        print('price: ', p1)
        