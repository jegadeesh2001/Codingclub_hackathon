
import streamlit as st
import pandas as pd
import numpy as np

import streamlit.components.v1 as components

def rec():
    st.header("Recommending Safer cities to User")

    fromcity = st.text_input("Enter source City").upper()

    destcity=st.text_input("Enter destination City").upper()
    if len(fromcity)!=0 and len(destcity)!=0 :
        df = pd.read_csv('CrimeIndex.csv')
        try:
            src_val = df.loc[df['DISTRICT'].values == fromcity]['Crime Index'].values[0]
            dest_val = df.loc[df['DISTRICT'].values == destcity]['Crime Index'].values[0]
            st.write(f"Crime rate of {fromcity} is {src_val}")
            st.write(f"Crime rate of {destcity} is {dest_val}")

            if src_val < dest_val:
                st.write(f"We don't recommend travelling to {destcity} as it is dangerous!")
            else:
                st.write(f"We recommend travelling ro {destcity} as it is safer!")
        except:
            st.write('Please enter source and destination from the cities in the given dataset')


def pred():
    st.header("Predicting Crimes for a District in a particular Year")
    dist=st.text_input("Enter the District Name").upper()
    year = int(st.selectbox(
     'Enter the year for forecasting',
     ('2015', '2016', '2017','2018','2019','2020','2021','2022')))

    f_year=year-2000-1



    if len(dist)!=0 and year!=None:
        df=pd.read_csv('prediction.csv')
        try:
            res_df = df.loc[df['DISTRICT'].values == dist]
            # ans=res_df.iloc[f_year]
            st.write(res_df.iloc[[f_year], :])


        except:
            st.write("Please choose City from the dataset")









def main():
    st.title("ANALYSIS OF CRIMES IN INDIA (Team AJS)")
    menu=["Dashboard","Recommender System",'Time Series Forecasting']
    choice = st.sidebar.selectbox("Options", menu)
    if choice=="Dashboard":
        st.header("Exploratory Data Analysis ")
        html_temp = """<div class='tableauPlaceholder' id='viz1651922181940' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;NE&#47;NEW_DASH&#47;YearWiseReport&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='NEW_DASH&#47;YearWiseReport' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;NE&#47;NEW_DASH&#47;YearWiseReport&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1651922181940');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, width=1130, height=700)
    if choice=="Recommender System":
        rec()
    if choice=="Time Series Forecasting":
        pred()


if __name__=="__main__":
    main()