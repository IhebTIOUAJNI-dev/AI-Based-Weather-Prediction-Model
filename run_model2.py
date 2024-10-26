import pandas as pd
import joblib

# functions that gets productivity as input and 
def get_work_conditions(writing1, writing2, writing3):
    model = joblib.load('model2.joblib')
    new_data = pd.DataFrame([[writing1, writing2, writing3]], columns=['Typing Speed1 (words per minute)','Typing Speed2 (words per minute)','Typing Speed3 (words per minute)'])
    predictions = model.predict(new_data)
    print(predictions)

    return predictions

if __name__ == '__main__':
    print("success")