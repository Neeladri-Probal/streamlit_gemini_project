import streamlit as st
from PIL import Image
from api_calling import note_generator,audio_transcription,quiz_generator
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()
with st.sidebar:
    st.header("Controls")
    images = st.file_uploader(
        "Upload the photos of your note",
        type=['jpg','png','jpeg'],
        accept_multiple_files = True
    )
    pil_img = []
    for i in images:
        pil_img.append(Image.open(i))
    if images:
        if len(images) > 3:
            st.error("Upload at max 3 images")
        else:
            col = st.columns(len(images))
            st.subheader("Uploaded images")
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
    #difficulty
    selected_option = st.selectbox(
        "Enter the difficulty of your quiz",
        ['Easy','Medium','Hard'],
        index = None
    )
    pressed = st.button("Click the button to initiate AI",type="primary")
if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not selected_option:
        st.error("You must select a difficulty")
    if images and selected_option:
        #note

        with st.container(border=True):
            st.subheader("Your note")
            with st.spinner("AI is writing for you"):
                generated_note = note_generator(pil_img)
                st.markdown(note_generator(pil_img))
        #Audio Transcript
        with st.container(border=True):
            generated_note = generated_note.replace("#","")
            generated_note = generated_note.replace("*","")
            generated_note = generated_note.replace("-","")
            generated_note = generated_note.replace("`","")
            with st.spinner("AI is writing for you"):
                a = audio_transcription(generated_note)
                st.audio(a)
        #quiz
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) Difficulty")
            with st.spinner("AI is writing for you"):
                quizzes = quiz_generator(pil_img,selected_option)
                st.markdown(quizzes)