import streamlit as st

if 'show_simplex_text' not in st.session_state: #*#
  st.session_state['show_simplex_text'] = False #*#
  
#page_bg_img = """"
#<style>
#   [data-testid = "stAppViewContainer"] {background-color: #4fff30;}
#</style>
#"""
#st.markdown(page_bg_img)

st.set_page_config(layout='wide')
c1,c2 = st.columns([5,1])
with c1:
  st.header(':red[*The prime rival of Good is Better, and its arch rival is Optimum...*]')
  st.header('',divider='red')
with c2:
  st.image('./logo.png')
st.title('')

col1,col2 = st.columns([2,1])
with col1:
  #st.video('./video-0.mp4')
  if not st.session_state['show_simplex_text']: #*#
    st.video('./video-0.mp4') #*#
  else: #*#
    close_col,_ = st.columns([0.1,0.9])
    with close_col:
      if st.button('close',key='close_simplex',help='return to video'):
        st.session_state['show_simplex_text'] = False
    st.title(':red[Simplex]')
    #st.header(':red[1. Introduction]')
    ##st.subheader('Simplex')
    #st.write(':red[Linear Programming is one of the most important fields in operations research and optimization. Its goal is to determine the optimal solution to a maximization or minimization problem of a linear objective function, subject to linear constraints. It is widely used in areas such as industrial production, resource management, economic analysis, supply chain logistics, and strategic planning.]')
    #st.write(':red[The Simplex algorithm, developed by George Dantzig in 1947, is the fundamental method for solving linear programming problems. It operates by moving from vertex to vertex along the feasible region of solutions, searching for the optimum. Despite its conceptual simplicity, the Simplex method has proven to be highly efficient in practice and is applied in a wide range of contexts—from production planning and transportation optimization to financial portfolio allocation and energy management.]')
    #st.write(':red[The purpose of this manual is twofold: first, to present the theoretical foundations of the Simplex method with clarity and an educational perspective; and second, to support the development and application of a functional computational tool, implemented within the GBO-solutions platform. Through detailed examples and step-by-step explanations, the reader will not only gain a deep understanding of the methodology, but also acquire a complete and reliable means for solving practical linear maximization problems.]')
    #st.header(':red[2. Theory of Simplex]')
    #st.subheader(':red[2.1. Standard Form of a Linear Programming Problem]')
    #st.write(':red[Linear programming is a mathematical optimization methodology aimed at determining the best possible value of a linear objective function, given a set of linear constraints. Such problems can be precisely described using systems of equations and inequalities.]')
    #st.write(':red[The general standard form of a linear programming problem is formulated as follows:]')
    #st.write(':red[where,]')
    #st.write(':red[* the variables x_1,x2,...,xn are called decision variables,]')
    #st.latex(r':red[\text{the variables } x_1]')
    #st.write(':red[* the constants cj are the coefficients of the objective function,]')
    #st.write(':red[* the coefficients aij define the linear constraints of the problem,]')
    #st.write(':red[* and bi represent the right-hand side values of the constraints.]')
    #st.write(':red[This formulation is well-suited for applying the Simplex method, as it enables a systematic transformation of the problem into tableau format and facilitates organized data processing.]')
    #st.text('-----')
    st.markdown( #*#
        """
        <div style='text-align: justify; color: red; font-size: 16px;'>

    The variables <b>x<sub>1</sub></b>, <b>x<sub>2</sub></b>, and <b>x<sub>3</sub></b> represent the decision parameters of the system. 
    Their values determine the optimal configuration in the optimization model being evaluated.

    <ul>
      <li><b>x<sub>1</sub></b>: Represents the amount of resource A allocated.</li>
      <li><b>x<sub>2</sub></b>: Corresponds to the production rate of unit B.</li>
      <li><b>x<sub>3</sub></b>: Indicates the transportation cost for region C.</li>
    </ul>

    The goal is to minimize the total cost function under the given constraints while ensuring system feasibility.

    </div>
        """, unsafe_allow_html=True
    ) #*#

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
#########################
    #st.button(':film_projector: :red[watch] :hammer_and_wrench:',key='Wsimplex',disabled=True,use_container_width=True)
    st.button(':film_projector: :red[watch] :hammer_and_wrench:', key='Wsimplex', on_click=lambda: st.session_state.update({'show_simplex_text': True}), use_container_width=True) #*#
#    if st.button('e-manual', key='Msimplex', use_container_width=True):
#      st.switch_page('simplex.py')
#########################
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
