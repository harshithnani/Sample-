import streamlit as st
import pandas as pd
import base64
import openpyxl

# Function to process data with Algorithm 1
def process_algorithm_1(df):
    # Your processing logic for Algorithm 1
    # For example, you can add a new column 'Processed_Algorithm_1'
    df['Processed_Algorithm_1'] = df['Column1'] * 2
    df['extra'] = df['Processed_Algorithm_1'] * 3  # Adding 'extra' column
    return df

# Function to process data with Algorithm 2
def process_algorithm_2(df):
    # Your processing logic for Algorithm 2
    # For example, you can add a new column 'Processed_Algorithm_2'
    df['Processed_Algorithm_2'] = df['Column1'] + df['Column2']
    df['extra'] = df['Processed_Algorithm_2'] + 5  # Adding 'extra' column
    return df

# Function to handle parse errors and invalid file formats
def handle_errors():
    st.error("Invalid file format. Please upload a valid Excel file.")

# Main Streamlit app
def main():
    st.set_page_config(page_title="Excel Processing App", page_icon="📊")

    # Sidebar for selecting processing algorithm
    algorithm_choice = st.sidebar.radio("Select Processing Algorithm", ["Algorithm 1", "Algorithm 2"])

    # Upload Excel file
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            # Read the Excel file
            df = pd.read_excel(uploaded_file)
        except pd.errors.ParserError:
            handle_errors()
            return

        st.subheader("Original Data")
        st.write(df)

        # Process data based on the selected algorithm
        if algorithm_choice == "Algorithm 1":
            df_processed = process_algorithm_1(df)
        else:
            df_processed = process_algorithm_2(df)

        st.subheader("Processed Data")
        st.write(df_processed)

        # Download processed data as Excel file
        csv_data = df_processed.to_excel(index=False, header=True, encoding='utf-8-sig')
        b64 = base64.b64encode(csv_data.encode()).decode()
        href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="processed_data.xlsx">Download Processed Data</a>'
        st.markdown(href, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
