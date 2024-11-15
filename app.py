import streamlit as st
from utils import detect_language, tell_joke

st.title("Language Detector (with Jokes)")
st.write("")

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("language-impl.png", width=300)  

st.write("")
text = st.text_area("📄 Enter some text:")

if st.button("🔍 Detect Language"):
    if text:
        word_count = len(text.strip().split())
        if word_count < 3:
            st.warning("⚠️ Please enter at least three words for accurate language detection.")
        else:
            language, confidence_values = detect_language(text)
            if language is not None:
                st.success(f"**Detected Language:** {language.name}")

                # Retrieve the joke
                joke = tell_joke(language)

                if joke:
                    # Display the joke header and joke on separate lines
                    st.markdown(f"**Here's a programmer joke in {language.name}:**")
                    st.write(joke)
                    st.write()  # Adds a blank line for spacing
                    st.write("(Detect Language again to get another joke!)")
                else:
                    st.write("No joke available in this language.")

                with st.expander("📊 See More Results"):
                    st.subheader("Top 4 Language Predictions:")
                    for confidence in confidence_values:
                        st.write(f"- {confidence.language.name}: {confidence.value:.2f}")
            else:
                st.error("❌ Could not confidently detect the language.")
    else:
        st.warning("⚠️ Please enter some text.")