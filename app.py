import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Data Eng. with Kasra", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/VancouverRS.png")
img_lottie_animation = Image.open("images/CanadaPG.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Kasra :wave:")
    st.title("A Data Engineer From Vancouver, Canada")
    st.write(
        "I am passionate about finding ways to bring new insight to your data in more efficient and effective ways."
    )
    st.write("[Learn More >](https://www.Github.com/kasraheidarinezhad.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About me:")
        st.write("##")
        st.write(
            """ Kasra Heidarinezhad has achieved Bachelor and Master's degree in Computer Engineering from the I. Azad University. He is an accomplished Data engineer, having developed effective solutions to challenging data-related problems. His expertise includes Big Data, Machine Learning, and Predictive Analytics, and he is well-versed in various programming languages and software tools which aid in the analysis and engineering of data. Kasra has been involved in data-driven projects in the financial services, retail, gas-oil, and energy industries. He has a comprehensive knowledge of the data lifecycle, from acquisition, cleaning, and analysis to visualization. Additionally, Kasra is highly capable of designing data pipelines, data warehouses, and machine learning models.
                \\
                Phone: (604) 442-3332\\
                Email:  Kasra.Heidarinezhad@gmail.com
            """
        )
        st.write("[Linkedin >](https://www.Linkedin.com/kasra-heidarinezhad)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Sample Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Data Analysis of Canada Immigration Information")
        st.write(
            """
            Datasets belong to Immigration, Refugees and Citizenship Canada. It is the department of the Government of Canada with responsibility for matters dealing with immigration to Canada, refugees, and Canadian citizenship. The department was established in 1994 following a reorganization.
            """
        )
        st.markdown("[Link coming soon!...](https://www.google.com)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("An EDA Case Study: Real Estate in Metro Vancouver, BC, Canada")
        st.write(
            """
            In this project, we have scraped, prepared, and analyzed the housing prices in British Columbia. We have also done some visualizations in the real estate market and proposed some ML methods for predicting housing prices.
            """
        )
        st.markdown("[Link coming soon!...](https://www.google.com)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/Kasra.Heidarinezhad@GMAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
