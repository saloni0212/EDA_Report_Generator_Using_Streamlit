import streamlit as st
import pandas as pd 
import numpy as np 
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#Web app title
st.markdown('''
# **The EDA App**
This is the **EDA App** created in streamlit using the **pandas-profiling** library ''')

# Upload the CSV data
with st.sidebar.header('1.Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
    [Example CSV input file] """)


# Pandas Profiling Report
if uploaded_file is not None:
  @st.cache_data
  def load_csv():
    csv = pd.read_csv(uploaded_file)
    return csv
  df = load_csv()
  pr = ProfileReport(df, explorative=True)
  st.header('**Input DataFrame**')
  st.write(df)
  st.write('---')
  st.header('**Pandas Profiling Report**')
  st_profile_report(pr)
else:
  st.info('Awaiting for CSV file to be uploaded')
  if st.button('Press to use example dataset'):
    #Example data
    @st.cache_data
    def load_data():
      a = pd.DataFrame(
        np.random.rand(100, 5),
        columns = ['a', 'b', 'c', 'd', 'e']
      )
      return a
    df = load_data()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)

# header = st.container()

# with header:
#   st.write("HURRAY! WE DEPLOYED AND APP")

#Web App Title

#Web app title
