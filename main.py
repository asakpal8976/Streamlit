import streamlit as st
st.write('Hello World')
st.write('Good Morning')
st.balloons()

from sklearn.datasets import load_iris

data = load_iris(as_frame=True).frame
data.head()