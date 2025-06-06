import streamlit as st
#from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport
import pandas as pd
import os



def main():


    

    df = pd.read_csv("src/edu_piv/static/data/data_extractor.csv")
    columnas = ["abrir","max","min","cerrar","cierre_ajustado","volumen","indicador"]
    df_2 = df[columnas]
    profile = ProfileReport(df_2, title="Dashboard Indicador Dolar")
    st.title("Análisis de Datos")
    st.write(profile)
    #profile.to_file("Analysis.html")

    #st_profile_report(profile)


if __name__ == "__main__":
    main()


