import joblib
import streamlit as st
st.write("Hello, World!\n")
# import numpy as np
import pandas as pd

## load trained model
model = joblib.load('model.pkl')

## Streamlit app
st.title("HDB Price Prediction")

## User inputs
town_selected = st.selectbox('Select Town', towns)
flat_type_selected = st.selectbox('Select Flat Type', flat_types)
storey_range_selected = st.selectbox('Select Storey', storey_ranges)
floor_area_selected = st.slider('Select Floor Area (sqm)',
                                min_value=30,
                                max_value=200,
                                value=70)

## Predict button
if st.button('Predict HDB Price'):

    ## Create dict for input features
    # input_data = {
    #     'town': town_selected,
    #     'flat_type': flat_type_selected,
    #     'storey_range': storey_range_selected,
    #     'floor_area_sqm': floor_area_selected
    # }

    ## Convert input data to a DataFrame
    df_input = pd.DataFrame({
        'town': [town_selected],
        'flat_type': [flat_type_selected],
        'storey_range': [storey_range_selected],
        'floor_area_sqm': [floor_area_selected]
    })

    ## Data Processing

    ## Predict
    y_unseen_pred = model.predict(df_input)[0]
    st.success(f"Predicted Price: ${y_unseen_pred:,.2f}")