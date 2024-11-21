import streamlit as st

# Create 3 columns
coll, col2, col3 = st.columns(3)

with coll:
    # Column 1: Display header and image of a cat
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    # Column 2: Display header and image of a dog
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    # Column 3: Display header and image of an owl
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
