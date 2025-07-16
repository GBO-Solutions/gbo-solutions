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
  if not st.session_state['show_simplex_text']: #*#
    st.video('./video-0.mp4') #*#
  else:
    if st.button('close',key='close_simplex',help='return to video'):
      st.session_state['show_simplex_text'] = False
      with open('simplex_manual.html', 'r', encoding='utf-8') as file:
        simplex_html = file.read()
      st.markdown(simplex_html, unsafe_allow_html=True)

#    st.markdown('''
#        <div style='height: 650px; overflow-y: auto; background-color: white; padding: 1rem; border: 1px solid #ccc; border-radius: 8px; text-align: justify; color: red; font-size: 16px;'>
#        <h3>Simplex Method – Technical Guide</h3>
#        <h4>1. Introduction</h4>
#        <p>Linear Programming is one of the most important fields in operations research and optimization. Its goal is to determine the optimal solution to a maximization or minimization problem of a linear objective function, subject to linear constraints. It is widely used in areas such as industrial production, resource management, economic analysis, supply chain logistics, and strategic planning.</p>
#        <p>The Simplex algorithm, developed by George Dantzig in 1947, is the fundamental method for solving linear programming problems. It operates by moving from vertex to vertex along the feasible region of solutions, searching for the optimum. Despite its conceptual simplicity, the Simplex method has proven to be highly efficient in practice and is applied in a wide range of contexts—from production planning and transportation optimization to financial portfolio allocation and energy management.</p>
#        <p>The purpose of this manual is twofold: first, to present the theoretical foundations of the Simplex method with clarity and an educational perspective; and second, to support the development and application of a functional computational tool, implemented within the GBO-solutions platform. Through detailed examples and step-by-step explanations, the reader will not only gain a deep understanding of the methodology, but also acquire a complete and reliable means for solving practical linear maximization problems.</p>
#        <h4>2. Theory of Simplex</h4>
#        <h5>2.1. Standard Form of a Linear Programming Problem</h5>
#        <p>Linear programming is a mathematical optimization methodology aimed at determining the best possible value of a linear objective function, given a set of linear constraints. Such problems can be precisely described using systems of equations and inequalities.</p>
#        <p>The general standard form of a linear programming problem is formulated as follows:</p>
#        <p>where,</p>
#        <ul>
#          <li>the variables <b>x<sub>1</sub></b>,<b>x<sub>2</sub></b>,...,<b>x<sub>n</sub></b> are called decision variables,</li>
#          <li>the constants <b>c<sub>j</sub></b> are the coefficients of the objective function,</li>
#          <li>the coefficients aij define the linear constraints of the problem,</li>
#          <li>and <b>b<sub>i</sub></b> represent the right-hand side values of the constraints.</li>
#        </ul>
#        <p>This formulation is well-suited for applying the Simplex method, as it enables a systematic transformation of the problem into tableau format and facilitates organized data processing.</p>
#        <h5>2.2. Conversion to Standard Form</h5>
#        <p>In order for a linear programming problem to be solved using the Simplex method, it must first be expressed in standard form. This form requires that all constraints are written as equalities, and all variables are non-negative.</p>
#        <p>Since most real-world constraints are expressed as inequalities of the form "less than or equal to" (&le), the conversion is performed by introducing slack variables.</p>
#        <p>For example, the constraint:</p>
#        <p>is transformed into the equivalent equation:</p>
#        <p>where <b>s<sub>1</sub></b> is the slack variable, with <b>s<sub>1</sub><b>=0.</p>
#        <p>The same procedure is applied to each constraint of the &le type, adding a different slack variable to each. In this way, the system of inequalities becomes an equivalent system of equations, enabling the construction of the initial Simplex tableau.</p>
#        <p>This transformation preserves the equivalence with the original problem while ensuring that all necessary conditions for the application of the method are met.</p>
#        <h5>2.3. Geometric Interpretation of the Method</h5>
#        <p>The Simplex method can be interpreted geometrically as an algorithmic process for locating the optimal solution with a convex, finite set of points - the so-called feasible region polyhedron. This polyhedron arises as the intersection of the half-spaces defined by the linear constraints of the problem.</p>
#        <p>In problems with two variables, the feasible region corresponds to a convex polygon in the plane. In the general case, the geometric representation extends to higher dimensions, with the feasible region forming a convex multi-dimensional geometric space.</p>
#        <p>A key property of linear programming is that, if an optimal solution exists, it lies at one of the vertices (basic feasible solutions) of the polyhedron. The Simplex method leverages this property and operates by moving from vertex to vertex - along the edges of the polyhedron - aiming to continusly improve the value of the objective function.</p>
#        <p>The process begins at an initial basic feasible solution and, at each step, selects a new vertex that leads to a higher objective value. The algorithm terminates when no further improvement is possible.</p>
#        <p>This geometric perspective provides significant insight into the operation of the Simplex method and explains why solving the problem does not require exhaustive enumeration of all feasible points, but rather a selective traversal of the vertices.</p>
#        <h5>2.4. The Simplex Tableau</h5>
#        <p>The Simplex tableau is the core computational and organizational tool of the method. At each step of the algorithm, the tableau summarixes the current state of the solution and provides all necessary information for determining the variables that will modify the besis, as well as for computing the next basic feasible solution.</p>
#        <p>The general structure of the tableau includes:</p>
#        <ul>
#          <li>the coefficients of the decision variables in the objective function (<b>C<sub>j</sub></b>),</li>
#          <li>the constraint coefficients (matrix A),</li>
#          <li>the right-hand side values of the constraints (b),</li>
#          <li>the basic variables (with their corresponding <b>C<sub>d</sub></b> values),</li>
#          <li>and the computed quantities <b>Z<sub>j</sub></b> and <b>C<sub>j</sub>-Z<sub>j</sub></b>.</li>
#        </ul>
#        <p>Specifically:</p>
#        <ul>
#          <li><b>Z<sub>j</sub></b> represents the contribution of each variable to the overall objective value, based on the current solution.</li>
#          <li><b>C<sub>j</sub>-Z<sub>j</sub></b> expresses the marginal improvement (or reduction) in the objective function if the variable enters the basis. This quantity is also known as the reduced cost.</li>
#        </ul>
#        <p>The tableau allows direct execution of pivot operations using linear algebraic transformations. In each iteration, one variable enters the basis and one leaves, and the tableau is updated accordingly. The process continues until all values of <b>C<sub>j</sub>-Z<sub>j</sub><=0</b>, at which point the optimal solution has been reached.</p>
#        <h5>2.5. Steps of the Simplex Algorithm</h5>
#        <p>The Simplex method follows an iterative procedure in which each step leads to an improved (or at least equivalent) basic solution. The process begins with an initial feasible solution and advances through linear transformations until it terminates.</p>
#        <p>The fundamental steps of the algorithm are as follows:</p>
#        <ul>
#          <li>
#            <p>Optimality check (termination criterion):</p>
#            <p>The values <b>C<sub>j</sub>-Z<sub>j</sub></b> are computed for all non-basic variables.</p>
#            <p>If all values are less than or equal to zero (<b>C<sub>j</sub>-Z<sub>j</sub><=0</b>), the current solution is optimal and the algorithm stops.</p>
#          </li>
#          <li>
#            <p>Selection of entering variable:</p>
#            <p>The variable with the largest positive value of <b>C<sub>j</sub>-Z<sub>j</sub></b> is selected. This variable has the greatest potential to increase the   value of z.</p>
#          </li>
#          <li>
#            <p>Ratio test:</p>
#            <p>For each constraint, the ration <b>b<sub>i</sub>/a<sub>ij</sub></b> is calculated, where <b>a<sub>ij</sub></b> is the coefficient of the entering variable in row i.</p>
#            <p>The row with the smallest non-negative ratio determines the leaving variable.</p>
#          </li>
#          <li>
#            <p>Pivoting - Tableau update:</p>
#            <p>A linear transformation of the tableau is performed so that the entering variable basic and the leaving variable exits the basis.</p>
#          </li>
#        </ul>
#        <p>The tableau is fully updated, and the procedure restarts from step i. The method completes in a finite number of steps and, provided that the problem has a feasible and bounded solution, the algorithm converges to the optimal value of the objective function.</p>
#        <h5>2.6. Termination and Interpretation of the Solution</h5>
#        <p>The Simplex algorithm terminates when all values of <b>C<sub>j</sub>-Z<sub>j</sub></b> are less than or equal to zero. At this point, no non-basic variable can enter the basis and improve the value of the objective function. The current basic solution is therefore considered optimal.</p>
#        <p>The final value of the objective function is obtained directly from the corresponding field in the tableau.</p>
#        <p>The value of the decision variables (<b>x<sub>1</sub></b>,<b>x<sub>2</sub></b>,...,<b>x<sub>n</sub></b>) are determined as follows:</p>
#        <ul>
#          <li>Basic variables take the values of the corresponding right-hand side entries (<b>b</sub>i</sub></b>) in the rows where they appear.</li>
#          <li>Non-basic variables are assigned a value of zero, as they are not included in the basis.</li>
#        </ul>
#        <p>If, during the procedure, a negative or undefined ratio arises in the pivoting step, this indicates that the problem is unbounded, meaning that the objective function can increase indefinitely without violating any constraints.</p>
#        <p>The final solution provides both the optimal value of the objective function and the composition of the solutio, that is, specific values of the variables that achieve it.</p>
#        <h4>3. Numerical Example (Step-by-Step Solution)</h4>
#    </div>
#    ''', unsafe_allow_html=True)

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
    st.button(':red[manuscript]', key='Wsimplex', on_click=lambda: st.session_state.update({'show_simplex_text': True}), use_container_width=True) #*#
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
