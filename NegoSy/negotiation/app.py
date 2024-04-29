import streamlit as st
import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown
import re
from messages import messages, seller_persona, buyer_persona, to_markdown, model


# Define the chatbot function
def chatbot(prompt, persona):
    if persona == "seller":
        response = f"{seller_persona} {prompt}"
    else:
        response = f"{buyer_persona} {prompt}"
    print(response)
    return response


# Streamlit app
def app():
    st.title("Welcome to NegoSy")
    st.write('<span style="font-size:30px;">Let\'s talk!</span>', unsafe_allow_html=True)

    # persona = st.radio("Select your persona", ["Seller", "Buyer"])

    # if persona == "Seller":
    #     chat_persona = seller_persona
    # else:
    #     chat_persona = buyer_persona

    st.write(f"You are: Buyer")

    user_input = st.text_input("Enter your message")

    if user_input:

        messages.append({'role':'user','parts':user_input})
        response = model.generate_content(messages)
        messages.append({'role':'model',
                 'parts':[response.text]})
        
        # print(messages)
        json_data = messages[len(messages) - 1]
        # print(json_data)
        percent = int(re.search(r'\d+(?=%)', json_data['parts'][0]).group()) if '%' in json_data['parts'][0] else None
        # print(percent)
        
        if percent is not None:
            st.progress(percent)
        else:
            st.warning("No probability of purchase detected in the response.")

    for message in messages:
        if message["role"] == "user":
            st.write(f"**You:** {message['parts']}")
        else:
            st.write(f"**Bot:** {message['parts'][0]}")
    

if __name__ == "__main__":
    app()

