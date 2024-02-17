import numpy as np
import pickle
import streamlit as st
import pandas as pd
loaded_model=pickle.load(open(r"C:\\Users\\ocmodels03dev\\Desktop\\sameer\\hd_trained_model1.sav",'rb'))

def disease_prediction(input_data):
  # input_data_as_numpy_array=np.asarray(input_data)
  # input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
  # prediction=loaded_model.predict(input_data_reshaped)
  # print(prediction)
  input_data=(40,'M','ATA',140,289,0,'Normal',172,'N',0,'Up')
  input_data_as_dataframe = pd.DataFrame([input_data],columns=['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS',
       'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope'])
  prediction=loaded_model.predict(input_data_as_dataframe)
  print(prediction)

  if (prediction[0]==1):
    return("The patient has Heart Disease")
  else:
    return("The patient do not have Heart Disease")

def main():
  st.title("Heart Disease Prediction")
  Age=st.number_input('Age')
  Sex=st.selectbox('Sex', ['M','F'])
  ChestPainType=st.selectbox('ChestPainType',['ATA','NAP','ASY','TA'])
  RestingBP=st.number_input('RestingBP')
  Cholesterol=st.number_input('Cholesterol')
  FastingBS=st.text_input('FastingBS')
  RestingECG=st.selectbox('RestingECG',['Normal','ST','LVH'])
  MaxHR=st.number_input('MaxHR')
  ExerciseAngina=st.selectbox('ExerciseAngina',['Y','N'])
  Oldpeak=st.number_input('Oldpeak')
  ST_Slope=st.selectbox('ST_Slope',['Up','Flat','Down'])

  result = ''


  if st.button('Result'):
    result = disease_prediction([Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope])
    st.write(result)
  st.success(result)


if __name__=='__main__':
  main()