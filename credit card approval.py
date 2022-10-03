import streamlit as st
import pickle
import numpy as np

# loading the trained model
pickle_in = open('~/loan prediction project/trained_model.sav', 'rb') 
classifier = pickle.load(pickle_in)


header = st.beta.container()


@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(input_data):   
 
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
 
    # Making predictions 
    prediction = classifier.predict(input_data_reshaped)
    print(prediction)
  
  	if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred


# this is the main function in which we define our webpage  
def main():       
    
    # giving a title
    st.title('Credit Card Approval App')
      
    # following lines create boxes in which user can enter data required to make prediction 
    YearsEmployed = st.selectbox('Years Employed',min_value = 0, max_value = 30)
    CreditScore = st.number_input("Credit SCore", min_value = 0, max_value = 100)
    Income = st.number_input("Applicants monthly income") 
    Age = st.number_input("Total loan amount", min_value = 20, max_value = 50)
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(YearsEmployed, CreditScore, Income, Age) 
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)
     
if __name__=='__main__': 
    main()