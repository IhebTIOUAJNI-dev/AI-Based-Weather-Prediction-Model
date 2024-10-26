import pandas as pd
import joblib


# function that gets input and return predicted data
def get_predictions(temp1, temp2,  light1, light2):
    model = joblib.load('model1.joblib')
    new_data = pd.DataFrame([[temp1, temp2, light1, light2]], columns=['Temperature1', 'Light Intensity1', 'Temperature2', 'Light Intensity2'])
    predictions = model.predict(new_data)
    print(predictions)
    
    return predictions


if __name__ == '__main__':
    get_predictions(26.819177526021974,25.34998381298152,1123.2353146084547,747.6986240736064)