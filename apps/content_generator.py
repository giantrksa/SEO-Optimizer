import openai
import streamlit as st

def app():
    def chat_gpt_request(prompt, model="text-davinci-002", tokens=250, temperature=0.7, top_p=0.9):
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=tokens,
            n=1,
            stop=None,
            temperature=temperature,
            top_p=top_p
        )
        return response.choices[0].text.strip()

    # Set your OpenAI API key here
    openai.api_key = "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"

    st.title("Content Generator")

    # Input text for theme of content
    theme = st.text_input("Enter the theme of the content you want to generate:")

    # Generate button
    if st.button("Generate"):
        if theme:
            prompt = f"Write a short content based on the theme: {theme}"
            generated_content = chat_gpt_request(prompt)
            st.write(generated_content)
        else:
            st.warning("Please enter a theme to generate content.")
