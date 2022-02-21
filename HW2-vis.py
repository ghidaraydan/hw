from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
import plotly.figure_factory as ff
import chart_studio.plotly as py
from plotly.offline import init_notebook_mode,iplot
import streamlit as st 
import chart_studio.plotly as py
import plotly.graph_objects as go

import plotly.express as px

st.set_page_config(layout="wide")

st.title("Welcome...")
st.markdown("""**Hello**  and **welcome** to my first streamlit application in MSBA325 course!

In this application, I used two datasets. The first is: **graduate admission prediction** to study the factors that increase the chance for graduate studies admission. 
The second is **life expectancy** to see the difference in age expectancy among countries.""")

Graduate_admission= ' [Graduate Admission](https://www.kaggle.com/mohansacharya/graduate-admissions)'
Life_Expectancy=  '  [Life Expectancy](https://www.kaggle.com/amansaxena/lifeexpectancy)'
st.markdown("""These datasets are obtained from kaggle and can be checked using the following links:""")
st.markdown(Graduate_admission,unsafe_allow_html=True)
st.markdown(Life_Expectancy,unsafe_allow_html=True)

st.title("Graduate Admission Prediction")

df = pd.read_csv("https://raw.githubusercontent.com/ghidaraydan/hw/main/Admission_Predict.csv")
st.image("https://866821.smushcdn.com/1939086/wp-content/uploads/graduate-masters-admission.jpg?lossy=1&strip=1&webp=1")

if st.checkbox('Show graduate admission data'):
      st.subheader('Graduate Admission Data')
      st.write(df)

st.title("Choose a Score")
pages_names = ("CGPA","TOEFL Score", "GRE Score")
page=st.radio('Navigation',pages_names)


st.write("Chance of Admit by ", page)
if page == "CGPA" :
 ax=px.scatter(df,x="CGPA",y="Chance of Admit ", color="LOR ", size_max=10, hover_name="Serial No.")
 st.plotly_chart(ax)
if page =="TOEFL Score" :
    ax=px.scatter(df,x="TOEFL Score",y="Chance of Admit ", color="LOR ", size_max=10, hover_name="Serial No.")
    st.plotly_chart(ax)
if page ==  "GRE Score" :
    ax=px.scatter(df,x="GRE Score",y="Chance of Admit ", color="LOR ", size_max=10, hover_name="Serial No.")
    st.plotly_chart(ax)

st.subheader(f'Scatter Plot showing the chance of graduate admission by CGPA and University Rating ')
df["sum of grades"]=df["GRE Score"]+df["TOEFL Score"]+df["CGPA"]
ax1=px.scatter(df,x="CGPA",y="Chance of Admit ", color="LOR ",size="TOEFL Score", size_max=10, hover_name="Serial No.",facet_col="University Rating")
st.plotly_chart(ax1)


st.subheader(f'Animated Scatter Plot showing the correlation between TOEFL Score and GRE  Score ')
ax2=px.scatter(df,x="GRE Score",y="TOEFL Score", color="CGPA", hover_name="Serial No.",animation_frame="LOR ")
st.plotly_chart(ax2)

University_Rating = st.slider('University Rating', 1, 5, 3)
st.subheader(f'Chance of Graduate Admission by University Rating = {University_Rating}')
axx=px.bar(x=df["University Rating"]== University_Rating, y= df["Chance of Admit "])
st.plotly_chart(axx)

st.subheader(f'Histogram showing the chance of admit for graduate by research and sum of grades')
ax3=px.histogram(df,x="sum of grades",y="Chance of Admit ", histfunc="avg",color="Research")
st.plotly_chart(ax3)

st.subheader(f'Box Plot showing the chance of admit for graduate by research')
ax4=px.box(df,x="Research",y="Chance of Admit ",color="Research")
st.plotly_chart(ax4)

st.title("Life Expectancy")
st.image("data:image/png;base64,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")
df1=pd.read_csv("https://raw.githubusercontent.com/ghidaraydan/hw/main/Life_expectancy_dataset.csv",encoding='latin-1')

if st.checkbox('Show Life Expectancy Data'):
    st.subheader('Life Expectancy Data')
    st.write(df1)

import plotly.express as px
st.subheader("3d Scatter Plot Showing the Overall Life by Country and Continent")
fig = px.scatter_3d(df1, x='Country', y='Continent', z='Overall Life',
              color='Continent', size='Overall Life', size_max=15,
               opacity=0.7)
ax=fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
st.plotly_chart(ax)

st.subheader("Sunburst showing the overall life in each country in the continents")
fig=px.sunburst(df1, color="Overall Life", values="Overall Life", path=["Continent","Country"],hover_name="Country")
ax2=fig.update_layout(
    margin = dict(t=25, l=30, r=25, b=30)
)
st.plotly_chart(ax2)

df2=df1.groupby("Continent",as_index=False)[["Overall Life","Male Life", "Female Life"]].mean()


st.subheader("Life Expectancy by Continent")
st.sidebar.checkbox("Show Analysis by Continent", True, key=1)
select = st.sidebar.selectbox('Select a Continent',df2['Continent'])

#get the state selected in the selectbox
state_data = df2[df2['Continent'] == select]
select_status = st.sidebar.radio("Life Expectancty by Continent", ('Overall Life',
'Male Life', 'Female Life',))

def get_total_dataframe(dataset):
    total_dataframe = pd.DataFrame({
    'Status':['Overall Life', 'Male Life', 'Female Life'],
    'Number of cases':(dataset.iloc[0]['Overall Life'],
    dataset.iloc[0]['Male Life'], 
    dataset.iloc[0]['Female Life'])})
    return total_dataframe
state_total = get_total_dataframe(df2)

if st.sidebar.checkbox("Show Analysis by Continent", True, key=2):
    st.markdown("## **Continent level analysis**")
    st.markdown("### Overall Life, Male Life and, Female Life " +
    " in %s " % (select))
    if not st.checkbox('Hide Graph', False, key=1):
        state_total_graph = px.bar(
        state_total, 
        x='Status',
        y='Number of cases',
        labels={'Number of cases':'Number of cases in %s' % (select)},
        color='Status')
        st.plotly_chart(state_total_graph)



st.sidebar.write("**Contact** **Details:**")
st.sidebar.write("Done by: **Ghida** **Raydan**")
st.sidebar.write("email:gmr07@mail.aub.edu")




