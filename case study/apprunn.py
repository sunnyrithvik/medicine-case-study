
import pandas as pd
import streamlit as st

df = pd.read_csv('healthdata.csv')
st.set_page_config(layout="wide")

st.title("User Reviews")
#st.header("This is a header")
#st.subheader("This is a subheader")

#st.write(len(df))
lt = len(df)
link2=df.loc[lt-1].at["Url"]


for i in range(0,lt):

    # st.text_input('Review', df.loc[i].at["Review"])

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('Review Number')
        st.info(i+1)

    with col2:
        st.write('Author Name')
        st.info(df.loc[i].at["Author name"])
        #st.text_input('Author:', df.loc[i].at["Author name"])

    with col3:
        st.write('Date of Review')
        st.info(df.loc[i].at["Date of review"])
        #st.text_input('Date of Review:', df.loc[i].at["Date of review"])

    st.write('Url Link')
    st.markdown(link2)

    st.text('Comment')
    st.info(df.loc[i].at["Comment"])
    #st.text_input('Comment:', df.loc[i].at["Comment"])
    
    st.write(" ")
    st.write(" ")
    st.write(" ")

#st.write('Sentiment:', run_sentiment_analysis(txt))
#link='check out this [link](https://retailscope.africa/)'
#st.markdown(link,unsafe_allow_html=True)

