import numpy as np
import pickle
import streamlit as st
loaded_model=pickle.load(open("C:/Users/ocmodels03dev/Desktop/ROCK VS MINE PREDICTION PROJECT/rm_trained_model.sav",'rb'))

def rock_mine_prediction(input_data):
  input_data_as_numpy_array=np.asarray(input_data)
  input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
  prediction=loaded_model.predict(input_data_reshaped)
  print(prediction)

  if (prediction[0]=='R'):
    return("The object is rock")
  else:
    return("The object is mine")


def main():
  st.title("Rock vs Mine prediction")
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
  col_16 = st.number_input("column_16")
  col_17 = st.number_input("column_17")
  col_18 = st.number_input("column_18")
  col_19 = st.number_input("column_19")
  col_20 = st.number_input("column_20")
  col_21 = st.number_input("column_21")
  col_22 = st.number_input("column_22")
  col_23 = st.number_input("column_23")
  col_24 = st.number_input("column_24")
  col_25 = st.number_input("column_25")
  col_26 = st.number_input("column_26")
  col_27 = st.number_input("column_27")
  col_28 = st.number_input("column_28")
  col_29 = st.number_input("column_29")
  col_30 = st.number_input("column_30")
  col_31 = st.number_input("column_31")
  col_32 = st.number_input("column_32")
  col_33 = st.number_input("column_33")
  col_34 = st.number_input("column_34")
  col_35 = st.number_input("column_35")
  col_36 = st.number_input("column_36")
  col_37 = st.number_input("column_37")
  col_38 = st.number_input("column_38")
  col_39 = st.number_input("column_39")
  col_40 = st.number_input("column_40")
  col_41 = st.number_input("column_41")
  col_42 = st.number_input("column_42")
  col_43 = st.number_input("column_43")
  col_44 = st.number_input("column_44")
  col_45 = st.number_input("column_45")
  col_46 = st.number_input("column_46")
  col_47 = st.number_input("column_47")
  col_48 = st.number_input("column_48")
  col_49 = st.number_input("column_49")
  col_50 = st.number_input("column_50")
  col_51 = st.number_input("column_51")
  col_52 = st.number_input("column_52")
  col_53 = st.number_input("column_53")
  col_54 = st.number_input("column_54")
  col_55 = st.number_input("column_55")
  col_56 = st.number_input("column_56")
  col_57 = st.number_input("column_57")
  col_58 = st.number_input("column_58")
  col_59 = st.number_input("column_59")

  output = ''

  if st.button('output'):
    output = rock_mine_prediction([col_0,col_1,col_2,col_3,col_4,col_5,col_6,col_7,col_8,col_9,col_10,col_11,col_12,col_13,col_14,col_15,
                                   col_16,col_17,col_18,col_19,col_20,col_21,col_22,col_23,col_24,col_25,col_26,col_27,col_28,col_29,col_30,
                                   col_31,col_32,col_33,col_34,col_35,col_36,col_37,col_38,col_39,col_40,col_41,col_42,col_43,col_44,col_45,
                                   col_46,col_47,col_48,col_49,col_50,col_51,col_52,col_53,col_54,col_55,col_56,col_57,col_58,col_59])
    st.write(output)
  st.success(output)


if __name__=='__main__':
  main()