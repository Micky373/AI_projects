import numpy as np
import pickle
import streamlit as st

# Getting the model
model = pickle.load(open("../models/machine_learning_models/diabetes_model.h5",'rb'))

# Creating a prediction function

def diabetes_prediction(data):

    # Changing the input data into an array
    data = np.array(data)

    # Since the model recieves 2D array we are changing our data into 2D array
    data = np.expand_dims(data,0)

    # Predicting the result using our model
    pred = model.predict(data)

    # Returning the result
    if pred == 1:
        return 'The person is diabettic'
    else:
        return 'The person is healthy'


# Creating a streamlit app
def app():

    # Adding a title for the page
    st.title('Diabetes Prediction Web App')

    # Recieving inputs from the user
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood pressure')
    SkinThickness = st.text_input('Skin tickness')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('Body Mass Index')
    DiabetesPedigreeFunction = st.text_input('Diabetes pedigree function value')
    Age = st.text_input('Age')

    # Initializing the diagnosis result as an empty string
    diagnosis = ''

    
    if st.button('Diabetes test result'):

        # If the button is clicked we will do the following action
        try:
            input_data = [Pregnancies,
                        Glucose,
                        BloodPressure,
                        SkinThickness,
                        Insulin,
                        BMI,
                        DiabetesPedigreeFunction,
                        Age
                        ]

            # Predicting using the input data passed by the user
            diagnosis = diabetes_prediction(input_data)

        # Handling exception if the user passes bad values    
        except:
            diagnosis = "You didn't pass the correct input values!!!!"
    
    # Upon successful clicking we will display the diagnosis result
    st.success(diagnosis)


if __name__ == '__main__':
    app()