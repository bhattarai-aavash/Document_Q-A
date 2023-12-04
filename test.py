import streamlit as st
import os
import tempfile
from inference import model, button_model
from PIL import Image
from pdf2image import convert_from_bytes
import io


def save_uploaded_image(uploaded_file):
    folder_path = 'files'
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, uploaded_file.name)
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    return file_path


def pdf_to_images(pdf_bytes, output_path):
    images = convert_from_bytes(pdf_bytes)
    for idx, image in enumerate(images):
        image.save(os.path.join(output_path, f"output_image_{idx}.png"), "PNG")
    return images


def inference_main():
    st.title("Image Upload App")
    st.write("Upload an image or PDF and write a question.")

    # File uploader
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        file_extension = uploaded_file.name.split('.')[-1]
        file_name = uploaded_file.name
        if file_extension == "pdf":
            pdf_bytes = uploaded_file.read()
            images = pdf_to_images(pdf_bytes, "files")
            img_path = 'files/output_image_0.png'

        else:
            img_path = save_uploaded_image(uploaded_file)

        st.image(img_path, caption="Uploaded Image", use_column_width=True)
        
        if st.button("Invoice"):
            answer = button_model(img_path, "What is the Invoice no?")
            st.write("Invoice", answer)

        if st.button("Due date"):
            answer = button_model(img_path, "What is the Due date?")
            st.write("Due Date", answer)

        if st.button("Total"):
            answer = button_model(img_path, "What is the Grand Total?")
            st.write("Total", answer)

        # Text box for question
        with st.sidebar:
            question = st.text_input("Enter your question below")
            if st.button("Submit"):
                # Process the question
                if question:
                    st.write("Question:", question)
                    answers, length_of_answer = model(img_path, question)
                    st.write("Length:", length_of_answer)
                    for answer in answers:
                        st.write("Answer:", answer)


if __name__ == "__main__":
    inference_main()
