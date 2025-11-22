import streamlit as st
from PIL import Image
from few_shot import FewShotPosts
from post_generator import generate_post


length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


def main():
    st.set_page_config(layout="wide")

    # ---- TOP TITLE ----
    st.markdown(
        """
        <h1 style="font-size:40px; font-weight:700; text-align:center; margin-bottom:5px;">
            LinkedIn Post Generator
        </h1>
        <p style="text-align:center; font-size:18px; color:#bbbbbb; margin-top:-10px;">
            Create polished, AI-generated LinkedIn posts instantly.
        </p>
        """,
        unsafe_allow_html=True
    )

    # ---- TWO COLUMN LAYOUT ----
    left, right = st.columns([1.1, 1], gap="large")

    # ---------------- LEFT SECTION ----------------
    with left:
        st.markdown("### Generate Your Post")

        col1, col2, col3 = st.columns([1, 1, 1])

        fs = FewShotPosts()
        tags = fs.get_tags()

        with col1:
            selected_tag = st.selectbox("Topic", options=tags)

        with col2:
            selected_length = st.selectbox("Length", options=length_options)

        with col3:
            selected_language = st.selectbox("Language", options=language_options)

        # Button
        if st.button("Generate", use_container_width=True):
            post = generate_post(selected_length, selected_language, selected_tag)
            st.write(post)

    # ---------------- RIGHT SECTION (FULL IMAGE, NO HEADING) ----------------
    with right:
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        collage = Image.open("posts.png")  # your single collage image
        st.image(collage, use_column_width=True)


if __name__ == "__main__":
    main()
