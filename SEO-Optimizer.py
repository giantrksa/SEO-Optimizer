import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from apps import content_generator, content_review


# Define the home page
def home_page():
    # Libraries
    from PIL import Image

    # Title
    st.title('SEO Optimizer')


    st.write(
        """
        
        SEO copywriting content apps are tools that assist content creators and marketers in producing content that is optimized for search engines. 
        
        These apps are designed to help writers produce high-quality content that is both readable and optimized for search engines.

        There are several benefits to using SEO copywriting content apps. 
        
        First, they help writers to produce content that is optimized for specific keywords and phrases. 
        
        This can help to increase the visibility of the content in search engine results pages (SERPs) and drive more traffic to the website.

        """
    )

    st.subheader('Expectation')
    st.write(
        """
        There are several tools available that utilize generator prompt text and Python libraries to assist in SEO copywriting. 
        
        These tools use natural language processing (NLP) algorithms to analyze the content and provide suggestions for improving its optimization.

        One example of such a tool is GPT-3, a language generation model that uses machine learning to generate human-like text. 
        
        GPT-3 can be used to generate prompts for content creators to follow, such as headlines, subheadings, and opening sentences. 
        
        These prompts are designed to be optimized for specific keywords and phrases, improving the content's visibility in search engine results.
        """
    )

    st.subheader('Future Works')
    st.write(
        """
        We will update soon~~
        """
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.info('**Data Scientist: Gian**')
    with c2:
        st.info('**Conceptor: Feivel**')
    with c3:
        st.info('**GitHub: [@giantrksa](https://github.com/giantrksa/)**')


# Define the pages of our app
PAGES = {
    "Introduction":home_page,
    "SEO Copywriting Tools": content_generator.app,
    "SEO Content Review Tools": content_review.app,
}

# Define the sidebar menu
with st.sidebar:
    st.sidebar.image("seo.png", use_column_width=True, output_format="PNG")
    st.sidebar.title('SEO Optimizer')
    page = option_menu("Features", list(PAGES.keys()))

# Display the selected page
PAGES[page]()
