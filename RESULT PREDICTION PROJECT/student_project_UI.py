import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open("C:/Users/ocmodels03dev/Desktop/RESULT PREDICTION PROJECT/stu_trained_model.sav",'rb'))

def result_prediction(input_data):
  input_data_as_numpy_array=np.asarray(input_data)
  input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
  prediction=loaded_model.predict(input_data_reshaped)
  print(prediction)

  if (prediction[0]==1):
    return("The student Passes the test")
  else:
    return("The student Fails the test")


def main():
  st.title("Result Prediction")
  # Student_ID=st.number_input('Student_ID')
  Previous_Exam_Score=st.number_input('Previous_Exam_Score')
  Subject1_Score=st.number_input('Subject1_Score')
  Subject2_Score=st.number_input('Subject2_Score')
  Attendance=st.number_input('Attendance')
  Study_Hours=st.number_input('Study_Hours')
  Participation=st.number_input('Participation')
  Homework_Completion=st.number_input('Homework_Completion')
  st.text('Teacher_Feedback:\nPositive:1\nNegative:0')
  Teacher_Feedback=st.number_input('Teacher_Feedback')
  st.text('Family_Support:\nHigh:0\nMedium:2\nLow:1')
  Family_Support=st.number_input('Family_Support')
  st.text('Socioeconomic_Background\nGood:1\nModerate:1')
  Socioeconomic_Background=st.number_input('Socioeconomic_Background')

  result = ''

  if st.button('Result'):
    result = result_prediction([Previous_Exam_Score, Subject1_Score, Subject2_Score,Attendance, Study_Hours, Participation, Homework_Completion,Teacher_Feedback, Family_Support, Socioeconomic_Background])
    st.write(result)
  st.success(result)


if __name__=='__main__':
  main()