import streamlit as st

import pandas as pd
import numpy as np
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import altair as alt





def main():
    st.title("Data Visualization On Education")
    st.markdown("""___""")
    st.image("5120.jpeg")
    st.markdown("""___""")
    st.header("Dataset")
    df = pd.read_csv("StudentsPerformance.csv")
    

    st.dataframe(df.head())



    fig = px.pie(df,'gender', title="Pie chart of gender")
    st.plotly_chart(fig)

    count = Counter(df['race/ethnicity'])
    data = pd.DataFrame({'Ethnicity group':count.keys(), 'Number of students':count.values()})
    fig = px.bar(data, 'Ethnicity group', 'Number of students', title="Race/Ethnicity")
    st.plotly_chart(fig)


    fig = px.scatter(df, 'math score', 'reading score',color="gender", title="Math and Reading score")
    st.plotly_chart(fig)



    clist = ["reading score", "math score","writing score"]

    parents = st.multiselect("Select education", clist, default="math score")
    data = df[parents]
    st.line_chart(data)






    





    
    

    




    




if __name__ == '__main__':
    main()
