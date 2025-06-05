import streamlit as st
from streamlit_pandas_profiling import st_profile_report
#import ydata-profiling
from ydata_profiling import ProfileReport
import pandas as pd
import os



def main():


    

    df = pd.read_csv("src/edu_piv/static/data/data_extractor.csv")
    profile = ProfileReport(df, title="Dashboard Indicador Dolar")

    st_profile_report(profile)


if __name__ == "__main__":
    main()


