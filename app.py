import streamlit as st
from doc_querry import inference_main
# Define your page functions
def page_home():
    st.title("Here are some ways to prompt this model")
    
    st.markdown("Example")
    st.markdown("-Right way to ask question -  What is the invoice no ? ")
    st.markdown("-Wrong way to ask question - invoice no ?")




# Create a dictionary of page names and corresponding functions
pages = {
    "Home": page_home,
    
    "Document Question Answer": inference_main
}

# Create a sidebar with page selection
st.sidebar.title("Navigation")
page_selection = st.sidebar.radio("Go to", tuple(pages.keys()))

# Invoke the selected page function
pages[page_selection]()