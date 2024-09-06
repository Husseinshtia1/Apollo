
# Apollo 11 Data Analysis - High-Level Advanced Version

## Overview
This project provides a high-level advanced analysis of Apollo 11 mission data using cutting-edge AI techniques such as BERT for text analysis and Autoencoders for anomaly detection.

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run the data download**:
   ```
   python download_data.py
   ```

4. **Clean and prepare the data**:
   ```
   python extract_text.py
   ```

5. **Train the advanced AI model**:
   ```
   python analyze_data.py
   ```

6. **Start the Streamlit app**:
   ```
   streamlit run app.py
   ```

## Files
- `config.py`: Configuration settings for the project.
- `download_data.py`: Script to download mission data.
- `extract_text.py`: Script to clean and extract text from PDFs.
- `analyze_data.py`: Advanced AI models for analyzing the data.
- `app.py`: Streamlit app for running and visualizing the advanced analysis.
- `requirements.txt`: List of Python dependencies.
