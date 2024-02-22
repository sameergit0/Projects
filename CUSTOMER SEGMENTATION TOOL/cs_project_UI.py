import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open("C:/Users/ocmodels03dev/Desktop/CUSTOMER SEGMENTATION TOOL/cs_trained_model.sav",'rb'))

def cs_result(input_data):
  input_data_as_numpy_array=np.asarray(input_data)
  input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
  prediction=loaded_model.predict(input_data_reshaped)
  print(prediction)

  if (prediction[0]==0):
    return 'The data is from cluster 0'
  elif (prediction[0]==1):
    return 'The data is from cluster 1'
  elif (prediction[0]==2):
    return 'The data is from cluster 2'
  else:
    return 'The data is from cluster 3'

def main():
  st.title("CUSTOMER SEGMENTATION TOOL")
  col_0 = st.number_input("column_0")
  col_1 = st.number_input("column_1")
  col_2 = st.number_input("column_2")
  col_3 = st.number_input("column_3")
  col_4 = st.number_input("column_4")
  col_5 = st.number_input("column_5")
  col_6 = st.number_input("column_6")
  col_7 = st.number_input("column_7")
  col_8 = st.number_input("column_8")
  col_9 = st.number_input("column_9")
  col_10 = st.number_input("column_10")
  col_11 = st.number_input("column_11")
  col_12 = st.number_input("column_12")
  col_13 = st.number_input("column_13")
  col_14 = st.number_input("column_14")
  col_15 = st.number_input("column_15")

  output = ''

  if st.button('output'):
    output = cs_result([col_0,col_1,col_2,col_3,col_4,col_5,col_6,col_7,col_8,col_9,col_10,col_11,col_12,col_13,col_14,col_15,])
    st.write(output)
  st.success(output)


if __name__=='__main__':
  main()