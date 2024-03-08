import streamlit as st

st.set_page_config(layout='wide')
c1,c2 = st.columns([1,5])
with c1:
  st.image('./logo.png')
with c2:
  st.title(':red[The immediate enemy of the good is the better and its existential enemy is the optimum...]')
st.header('',divider='red')
st.title('')
