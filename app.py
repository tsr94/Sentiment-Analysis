import streamlit as st
import pickle
import pandas as pd
import re
import nltk==3.6.2
from nltk.corpus import stopwords
import streamlit as st
from nltk.stem.porter import PorterStemmer ## for all words like love loved loving -> love
from PIL import Image
nltk.download('stopwords')
# Set the title of the app

# Load images for styling
header_image = Image.open("img_2.png")  # Replace with your header image path
footer_image = Image.open("img.png")        # Replace with your footer image path

# Set the page configuration
st.set_page_config(
    page_title="Restaurant Food Review Analysis",
    page_icon="🍔",
    layout="centered",
    initial_sidebar_state="collapsed"
)




st.title("Restaurant food Review Analysis")
st.image(header_image, use_container_width=True)# Display the header image
# Add a description
st.write("""
This application allows you to analyze the sentiment of a review. 
Enter your review in the textbox below, and the sentiment (Positive or Negative) will be displayed.
""")
with open("sentiment_model.pkl", "rb") as f:
    tf, classifier = pickle.load(f)

# Input textbox with a larger font for the label
st.markdown(
    """
    <h3 style="font-size:24px; color: white;">Enter your review</h3>
    """,
    unsafe_allow_html=True,
)
# Input textbox for user review
review = st.text_area("", placeholder="Type your review here...")
def predict_sentiments(sample_review):
    sample_review = re.sub('[^^a-zA-Z]',' ',sample_review)
    sample_review = sample_review.lower()
    sample_review_words = sample_review.split()
    sample_review_words = [word for word in sample_review_words if not word in set(stopwords.words('english'))]
    ps = PorterStemmer()
    final_review = [ps.stem(word) for word in sample_review_words]
    final_review = " ".join(final_review)

    temp = tf.transform([final_review]).toarray()
    return classifier.predict(temp)

# Button to analyze sentiment
# Button to analyze sentiment
if st.button("Analyze Sentiment"):
    if not review.strip():
        st.error("Please enter a valid review.")
    else:
        # Predict sentiment
        pred = predict_sentiments(review)

        # Display sentiment result
        if pred:
            sentiment = "Positive 😊"
            st.success(f"This is a **{sentiment}** review.")
        else:
            sentiment = "Negative 😞"
            st.error(f"This is a **{sentiment}** review.")

st.image(footer_image, use_container_width=True)
# Footer
st.write("---")
st.caption("Developed by TSR")

