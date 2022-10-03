import streamlit as st
import numpy as np
import pickle

st.title('Welcome to my credit Approval Project')

#load the saved model
#loaded_model = pickle.load(open('/Users/chukwuemekaugwu/Desktop/loan prediction project/test.sav', 'rb'))

def prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return "Rejected"
    else:
        return "Approved"

# this is the main function in which we define our webpage  
def main():       

    # giving a title
    st.title('Credit Card Approval App')

    # following lines create boxes in which user can enter data required to make prediction 
    Male = st.selectbox("Male", (0,1))
    Age = st.number_input("Age", min_value = 20, max_value = 50)
    Debt = st.number_input("Debt", min_value = 0, max_value = 100)
    Married = st.selectbox("Marital status", (0,1,2,3))
    EducationLevel = st.number_input("EducationLevel", min_value = 1, max_value = 14)
    Ethnicity = st.number_input("Ethnicity", min_value = 0, max_value = 9)
    YearsEmployed = st.number_input('Years Employed',min_value = 0, max_value = 30)
    PriorDefault = st.selectbox("Defaulted", (0,1))
    Employed = st.selectbox("Employed", (0,1))
    CreditScore = st.number_input("Credit SCore", min_value = 0, max_value = 100)
    Citizen = st.selectbox("Citizen", (0,1,2))
    Income = st.number_input("Applicants monthly income") 
    result =""

    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction([[YearsEmployed, CreditScore, Income, Age]]) 
        st.success('Your loan is {}'.format(result))
        

if __name__=='__main__': 
            main()