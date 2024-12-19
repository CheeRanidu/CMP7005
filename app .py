import streamlit as st
import pandas as pd


# Set the title of the app
st.title("EDA App: Dataset Analysis")

# Sidebar to upload the dataset
st.sidebar.header("Upload Your Dataset")
uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv", "xlsx"])

# If a file is uploaded
if uploaded_file is not None:
    # Read the dataset
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Display the raw dataset
    st.subheader("Dataset Preview")
    st.write(df.head())

    # Display dataset info
    st.subheader("Dataset Information")
    st.write("Shape of the dataset:", df.shape)
    st.write("Columns:", df.columns.tolist())
    st.write("Data Types:", df.dtypes)
    st.write("Summary Statistics:")
    st.write(df.describe())

    # Data Visualization
    st.subheader("Visualizations")

    # Correlation Heatmap
    st.write("Correlation Heatmap")
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    st.pyplot(plt)

    # Histogram for Numeric Columns
    st.write("Distribution of Numeric Columns")
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    column = st.selectbox("Choose a column for histogram", numeric_columns)
    plt.figure(figsize=(8, 4))
    sns.histplot(df[column], kde=True, bins=30)
    st.pyplot(plt)

    # Scatter Plot
    st.write("Scatter Plot")
    x_axis = st.selectbox("Choose X-axis", numeric_columns)
    y_axis = st.selectbox("Choose Y-axis", numeric_columns)
    plt.figure(figsize=(8, 4))
    sns.scatterplot(data=df, x=x_axis, y=y_axis)
    st.pyplot(plt)

else:
    st.write("Please upload a dataset to begin the analysis.")

