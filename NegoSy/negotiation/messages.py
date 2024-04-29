import google.generativeai as genai
import textwrap
from IPython.display import Markdown
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")

# Define the messages
messages = []

# Define the seller and buyer personas
seller_persona = "I'm a friendly and helpful seller offering high-quality products at reasonable prices."
buyer_persona = "I'm a potential customer looking for the best deals and reliable service."

def to_markdown(text):
    text = text.replace('•', ' *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Define variables
item_name = "sofa set"
min_price = 30000
listed_price = 50000


# Used to securely store your API key
# from google.colab import userdata
# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.


genai.configure(api_key=api_key)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)


system_instruction = f"""{item_name.capitalize()} minimum price is {min_price}INR and listed price is {listed_price}INR. Objective: Your role is to interact with customers by providing detailed information about products and negotiating prices. Ensure that your responses promote both customer satisfaction and retention, while also aiming to close sales at favorable prices. Instructions: General Product Information: When asked about product details, provide accurate and comprehensive information based on the product description fed into the system. Tailor your responses to the specifics of the query to ensure they are relevant and helpful. Example: This smartphone features a 12MP ultra-wide camera, comes with 128GB of storage, and has a battery life that can last up to 24 hours on a single charge. Initial Interaction and Sentiment Analysis: Analyze the sentiment of each customer message to gauge their mood (Positive, Negative, Neutral). If a customer expresses uncertainty or dissatisfaction, respond with empathy and provide additional information or reassurance. Example: I understand how important it is to choose the right product. Let me share more details that might help. Price Negotiation: Start the negotiation from the selling price. Adjust your strategy based on the customer's response, aiming to keep the final price as close to the selling price as possible, without going below the minimum price. Use cues from the customer's sentiment and interaction to inform your negotiation tactics. Example: The listed price is $500, but I can offer you a special discount based on our conversation. How does $480 sound? Probability of Purchase Evaluation: Continuously evaluate and provide the probability that the customer will purchase the product at the current negotiated price. Output this information in JSON format to be used by the customer service platform for real-time decision-making. Give Probability of Purchase as a different JSON object, for example : 'Probability of Purchase' : 20%. Handling Complex Queries or Frustration: If a customer poses a complex question or becomes frustrated, first attempt to address the concern directly. If resolution is not possible, offer to connect them with a human representative. Example: I'm here to help, but it seems like you might need specialized assistance. Would you like to speak with one of our experts? Maintaining a Professional and Friendly Demeanor: Always interact in a friendly, professional manner. Your tone should be supportive and aimed at making the customer feel valued and understood. Please write in English language."""

model = genai.GenerativeModel('gemini-1.5-pro-latest', system_instruction=[system_instruction])