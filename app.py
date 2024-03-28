import streamlit as st

st.set_page_config(layout='wide')
c1,c2 = st.columns([1,5])
with c1:
  st.image('./logo.png')
with c2:
#  st.title(':red[The prime rival of Good is Better, and its arch rival is Optimum...]')
  st.title(r':red[The prime rival of Good is Better,]\n:red[and its arch rival is Optimum...]')
st.header('',divider='red')
st.title('')

col1,col2 = st.columns([2,1])
with col1:
  st.video('./video-0.mp4')
  st.header('',divider='red')
  c1,c2,c3,c4,c5,c6,c7 = st.columns([3,1,1,4,1,1,4])
  with c1:
    st.image('./qr.png')
  with c3:
    st.image('./email.png')
    st.image('./linkedin.png')
    st.image('./ytube.png')
  with c4:
    st.write(':red[gbosolut]'+':red[@gmail.com]')
    st.write('')
    st.write(':red[gbo-solutions]')
    st.write('')
    st.write(':red[@GBO-Solutions]')
  with c6:
    st.image('x.png')
    st.image('instagram.png')
    st.image('tiktok.png')
  with c7:
    st.write(':red[@gbo_solut]')
    st.write('')
    st.write(':red[@gbo_solutions]')
    st.write('')
    st.write(':red[@gbo_solut]')
with col2:
  # SIMPLEX
  c1,c2,c3 = st.columns([5,4,5])
  with c2:
    st.subheader(':red[SIMPLEX]')
  c1,c2 = st.columns([1,1])
  with c1:
    st.button(':film_projector: :red[watch] :hammer_and_wrench:',key='Wsimplex',disabled=True,use_container_width=True)
  with c2:
    with open('GBOsimplex.zip','rb') as f_zip:
      st.download_button(label=':red[download]',data=f_zip,file_name='GBOsimplex.zip',mime='application/zip',key='Bsimplex',disabled=False,use_container_width=True)
  st.divider()
  # B-F-G-S
  c1,c2,c3 = st.columns([5,4,5])
  with c2:
    st.subheader(':red[B-F-G-S]')
  c1,c2 = st.columns([1,1])
  with c1:
    st.button(':film_projector: :red[watch] :hammer_and_wrench:',key='Wbfgs',disabled=True,use_container_width=True)
  with c2:
    with open('GBObfgs.zip','rb') as f_zip:
      st.download_button(label=':red[download]',data=f_zip,file_name='GBObfgs.zip',mime='application/zip',key='Bbfgs',disabled=False,use_container_width=True)
  st.divider()
    # GENETIC
  c1,c2,c3 = st.columns([5,4,5])
  with c2:
    st.subheader(':red[GENETIC]')
  c1,c2 = st.columns([1,1])
  with c1:
    st.button(':film_projector: :red[watch] :hammer_and_wrench:',key='Wgenetic',disabled=True,use_container_width=True)
  with c2:
    with open('GBOgenetic.zip','rb') as f_zip:
      st.download_button(label=':red[download]',data=f_zip,file_name='GBOgenetic.zip',mime='application/zip',key='Bgenetic',disabled=False,use_container_width=True)
  st.divider()
    # ADJOINT
  c1,c2,c3 = st.columns([5,4,5])
  with c2:
    st.subheader(':red[ADJOINT]')
  c1,c2 = st.columns([1,1])
  with c1:
    st.button(':film_projector: :red[watch] :hammer_and_wrench:',key='Wadjoint',disabled=True,use_container_width=True)
  with c2:
    st.button(':lock: :red[download] :hammer_and_wrench:',key='Badjoint',disabled=True,use_container_width=True)
