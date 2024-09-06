
import streamlit as st
import plotly.express as px
import pandas as pd
from analyze_data import train_and_evaluate_bert, detect_anomalies
from config import CLEANED_DATA_FILE

def visualize_results(df):
    fig = px.scatter_matrix(df, dimensions=df.columns, title="Analysis Results")
    st.plotly_chart(fig)

def main():
    st.title("Advanced Apollo 11 Data Analysis")
    if st.button('Run Advanced Analysis'):
        model = train_and_evaluate_bert()
        st.write("Advanced model trained successfully!")
        df = pd.DataFrame(model.layers[-1].output)
        visualize_results(df)

    if st.button('Show Data'):
        data = pd.read_csv(CLEANED_DATA_FILE)
        st.write(data.head())

if __name__ == "__main__":
    main()
