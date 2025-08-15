# importing dependencies 
import streamlit as st
import numpy as np
import pandas as pd
import pickle

# importing dataframe and ml pipeline
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Set pages configurations 
st.set_page_config(
    page_title="Startup's Profit Prediction Model",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Title 
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Startup's Profit Prediction Model 💼</h1>", unsafe_allow_html=True)

st.write("### Enter the details below to predict your startup's profit:")

# Input features for end users 
col1, col2 = st.columns(2)

with col1:
    RandDSpend = st.number_input('💡 R&D Spend', min_value=0.0, step=1000.0)

with col2:
    admincost = st.number_input('🏢 Administration Cost', min_value=0.0, step=1000.0)

col3, col4 = st.columns(2)

with col3:
    ad = st.number_input('📢 Marketing Spend', min_value=0.0, step=1000.0)

with col4:
    state = st.selectbox('📍 State', df['State'].unique())

# Prediction button
if st.button('🎯 Predict Profit'):
    # Create input dataframe (model expects one-hot encoded state internally)
    input_df = pd.DataFrame([[RandDSpend, admincost, ad, state]],
                            columns=['R&D Spend', 'Administration', 'Marketing Spend', 'State'])
    
    # Prediction
    result = pipe.predict(input_df)[0]

    # Output with style
    st.markdown(f"""
        <div style="padding:15px; background-color:#f0f9ff; border-radius:10px; border: 2px solid #4CAF50; text-align:center;">
            <h3 style="color:#4CAF50;">💰 Predicted Profit: <b>${result:,.2f}</b></h3>
        </div>
    """, unsafe_allow_html=True)
