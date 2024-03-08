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
  # SIMPLEX
  c1,c2,c3 = st.columns([1,1,1])
  with c2:
    st.subheader(':red[SIMPLEX]')
  c1,c2 = st.columns([1,1])
  with c1:
    st.button(':film_projector: :red[watch]',key='Wsimplex',use_container_width=True)
  with c2:
    st.button(':lock: :red[download]',key='Bsimplex',disabled=True,use_container_width=True)
  st.divider()
  # B-F-G-S
  c1,c2,c3 = st.columns([1,1,1])
  with c2:
    st.subheader(':red[B-F-G-S]')
  c1,c2 = st.columns([1,1])
  with c1:
    st.button(':film_projector: :red[watch]',key='Wbfgs',use_container_width=True)
  with c2:
    st.button(':lock: :red[download]',key='Bbfgs',disabled=True,use_container_width=True)
  st.divider()
    # GENETIC
  c1,c2,c3 = st.columns([1,1,1])
  with c2:
    st.subheader(':red[GENETIC]')
  c1,c2 = st.columns([1,1])
  with c1:
    st.button(':film_projector: :red[watch]',key='Wgenetic',use_container_width=True)
  with c2:
    st.button(':lock: :red[download]',key='Bgenetic',disabled=True,use_container_width=True)
  st.divider()
    # ADJOINT
  c1,c2,c3 = st.columns([1,1,1])
  with c2:
    st.subheader(':red[ADJOINT]')
  c1,c2 = st.columns([1,1])
  with c1:
    st.button(':film_projector: :red[watch]',key='Wadjoint',use_container_width=True)
  with c2:
    st.button(':lock: :red[download]',key='Badjoint',disabled=True,use_container_width=True)
