# Restaurant Food Review Sentiment Analysis

This is a **Sentiment Analysis** application that determines the sentiment of restaurant food reviews. The app classifies a given review as either **Positive** or **Negative** based on the text input.

## Features

- **Text Input**: Users can enter a restaurant review in a text box.
- **Sentiment Prediction**: The app analyzes the review and predicts if the sentiment is **Positive** or **Negative**.
- **User-Friendly Interface**: Built with **Streamlit**, providing a clean and interactive web interface.

## Technologies Used

- **Python**: The main programming language.
- **Streamlit**: A Python library for building interactive web applications.
- **scikit-learn**: For machine learning models and text vectorization.
- **NLTK**: Natural Language Toolkit for text preprocessing (e.g., stopword removal, stemming).
- **Pickle**: For saving and loading the trained sentiment analysis model.
- **Pandas**: For data manipulation and handling.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tsr94/sentiment-analysis.git
2. Navigate to the project directory:
   ```bash
   cd sentiment-analysis
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - **Windows**:
     ```bash
     .env\Scriptsctivate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   **requirements.txt** should contain:
   ```text
   streamlit
   scikit-learn
   pandas
   nltk
   pillow
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser at `http://localhost:8501`.

3. Enter a restaurant review in the provided text box and click on **Analyze Sentiment** to see whether the review is **Positive** or **Negative**.

## Model Details

The sentiment analysis model was trained using a dataset of restaurant reviews. It uses the following steps for prediction:

1. **Text Preprocessing**: Removal of non-alphabetic characters, converting to lowercase, stopword removal, and stemming.
2. **TF-IDF Vectorization**: The reviews are transformed into numerical features using TF-IDF.
3. **Model**: A machine learning classifier (e.g., Logistic Regression, Naive Bayes) is used to predict sentiment based on the processed text.

## Example

### Input:
```
The food was absolutely amazing! I loved the ambiance and the service was great.
```

### Output:
**Positive 😊**

### Input:
```
The food was terrible, and the service was awful. I will never come back.
```

### Output:
**Negative 😞**

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. Contributions are always welcome!

## License

This project is open-source and available under the MIT License.

## Acknowledgments

- Thanks to **Streamlit** for creating an easy-to-use framework for building web applications.
- Thanks to **scikit-learn** for providing the tools for machine learning.

