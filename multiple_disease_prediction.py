import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

st.set_page_config(
    page_title = 'Disease prediction',
    page_icon="random",
)

diabetes_model = pickle.load(open("models/machine_learning_models/diabetes_model.h5",'rb'))
heart_disease_model = pickle.load(open(
                                "models/machine_learning_models/heart_disease_model.h5",
                                'rb')
                                )


# Creating a prediction function

def diabetes_prediction(data):

    # Changing the input data into an array
    data = np.array(data)

    # Since the model recieves 2D array we are changing our data into 2D array
    data = np.expand_dims(data,0)

    # Predicting the result using our model
    pred = diabetes_model.predict(data)

    # Returning the result
    if pred == 1:
        return 'The person is diabettic'
    else:
        return 'The person is healthy'


def heart_disease_prediction(data):

    # Changing the input data into an array
    data = np.array(data)

    # Since the model recieves 2D array we are changing our data into 2D array
    data = np.expand_dims(data,0)

    # Predicting the result using our model
    pred = heart_disease_model.predict(data)

    # Returning the result
    if pred == 1:
        return 'The person has heart disease'
    else:
        return 'The person is healthy'


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction using Machine Learning',
                        [
                            'Diabetes disease prediction',
                            'Heart disease prediction'
                        ],
                        icons = ['bandaid','heart'],
                        default_index = 0,                        
                        )

if selected == 'Diabetes disease prediction':

    # Adding a title for the page
    st.title('Diabetes Prediction Web App')

    # Recieving inputs from the user
    col1,col2,col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of pregnancies')

    with col2:
        Glucose = st.text_input('Glucose level')

    with col3:
        BloodPressure = st.text_input('Blood pressure')

    with col1:
        SkinThickness = st.text_input('Skin tickness')

    with col2:
        Insulin = st.text_input('Insulin level')

    with col3:
        BMI = st.text_input('Body Mass Index')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes pedigree function value')
    
    with col2:
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

if selected == 'Heart disease prediction':
    # Adding a title for the page
    st.title('Heart Disease Prediction Web App')

    # Recieving inputs from the user
    col1,col2,col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex: 1 if Male and 0 if female')

    with col3:
        cp = st.text_input('chest pain type (4 values): put 0,1,2 or 3')

    with col1:
        trestbps = st.text_input('Resting Blood pressure')

    with col2:
        chol = st.text_input('Cholestrol Level')

    with col3:
        fbs = st.text_input('Fasting blood sugar: should be > 120')
    
    with col1:
        restecg = st.text_input('Resting ecg result')
    
    with col2:
        thalach = st.text_input('Maximum heart rate achieved')
    
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    
    with col1:
        oldpeak = st.text_input('oldpeak = ST depression induced by exercise relative to rest ')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment ')

    with col3:
        ca = st.text_input('Number of major vessels (0-3) colored by flourosopy')
    
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # Initializing the diagnosis result as an empty string
    diagnosis = ''

    
    if st.button('Heart Disease test result'):

        # If the button is clicked we will do the following action
        try:
            input_data = [age,
                        sex,
                        cp,
                        trestbps,
                        chol,
                        fbs,
                        restecg,
                        thalach,
                        exang,
                        oldpeak,
                        slope,
                        ca,
                        thal
                        ]

            # Predicting using the input data passed by the user
            diagnosis = heart_disease_prediction(input_data)

        # Handling exception if the user passes bad values    
        except:
            diagnosis = "You didn't pass the correct input values!!!!"
    
    # Upon successful clicking we will display the diagnosis result
    st.success(diagnosis)





	