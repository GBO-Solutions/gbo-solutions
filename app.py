import streamlit as st

st.set_page_config(layout='wide')
c1,c2 = st.columns([1,5])
with c1:
  st.image('./logo.png')
with c2:
  st.title(':red[The immediate enemy of the good is the better and its existential enemy is the optimum...]')
st.header('',divider='red')
st.title('')

col1,col2 = st.columns([2,1])
with col1:
  st.video('./video-0.mp4')
  st.divider()
with col2:
  c1,c2,c3 = st.columns([1,1,1])
  with c2:
    st.subheader(':red[SIMPLEX]')
#  c1,c2 = st.columns([1,1])
#  with c1:
#    st.button(':film_projector: :red[watch]',key='simplex1',on_click=video_select,use_container_width=True)
#  with c2:
#    st.button(':lock: :red[download]',key='simplex2',disabled=True,use_container_width=True)
#  
