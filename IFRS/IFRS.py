import streamlit as st
import requests
from docx import Document
from io import BytesIO
import time

# Expanded list of IFRS-related keywords and phrases
IFRS_KEYWORDS = [
     "IFRS", "financial statements", "revenue recognition", "lease", "asset",
    "liability", "equity", "financial instrument", "impairment", "fair value",
    "consolidation", "subsidiary", "cash flow", "income statement", "balance sheet",
    "taxation", "deferred tax", "depreciation", "amortization", "goodwill", "provision",
    "acquisition", "business combination", "disclosure", "hedge accounting", "intangible assets",
    "investment property", "joint venture", "minority interest", "non-controlling interest",
    "operating segment", "other comprehensive income", "retained earnings", "share capital",
    "statement of changes in equity", "stock compensation", "conceptual framework", "IAS", "Interim", "Interpretation"
    "Funds", "Rehabilitation", "Liabilities", "Economies"
]

# Function to create a Word document with the actual content
def create_word_doc(query, content):
    doc = Document()
    
    # Adding heading and sections based on the content provided
    doc.add_heading(query, level=1)
    
    doc.add_heading('Generated Content', level=2)
    doc.add_paragraph(content)
    
    # Saving to a bytes buffer
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    
    return buffer

# Function to simulate typing effect
def type_text(text, speed=0.009):
    placeholder = st.empty()  # Create an empty placeholder that we will update
    typed_text = ""

    for char in text:
        typed_text += char
        placeholder.markdown(f"<p style='font-family:monospace; font-size:16px'>{typed_text}</p>", unsafe_allow_html=True)
        time.sleep(speed)

# Function to check if the query is IFRS related
def is_ifrs_related(query):
    for keyword in IFRS_KEYWORDS:
        if keyword.lower() in query.lower():
            return True
    return False

# Streamlit sidebar for login and API key input
st.sidebar.title("Login")
username_input = st.sidebar.text_input("Username")
password_input = st.sidebar.text_input("Password", type="password")
api_key_input = st.sidebar.text_input("Perplexity API Key", type="password")
login_button = st.sidebar.button("Login")

# Session state to keep track of login status and API key
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'api_key' not in st.session_state:
    st.session_state.api_key = None

if login_button:
    if username_input == "IFRSUser1" and password_input == "Password":
        st.session_state.logged_in = True
        st.session_state.api_key = api_key_input
        st.sidebar.success("Login successful!")
    else:
        st.sidebar.error("Invalid username, password, or API key.")

# Main content
if st.session_state.logged_in:
    if st.session_state.api_key:
        st.title("IFRS Research Assistant")
        st.write("Author: **Vikram Lingam**")
        st.write("GitHub Repo: [https://github.com/vikramlingam](https://github.com/vikramlingam)")
        st.write("Enter your IFRS-related query to get detailed research insights.")

        # User input for IFRS query
        query = st.text_input("Enter your query:", "")

        if st.button("Search"):
            if query:
                # Check if the query is related to IFRS
                if is_ifrs_related(query):
                    # Prepare the API request
                    url = "https://api.perplexity.ai/chat/completions"
                    payload = {
                        "model": "llama-3.1-sonar-small-128k-online",
                        "messages": [
                            {
                                "role": "system",
                                "content": "Be precise and concise."
                            },
                            {
                                "role": "user",
                                "content": query
                            }
                        ]
                    }
                    headers = {
                        "accept": "application/json",
                        "content-type": "application/json",
                        "Authorization": f"Bearer {st.session_state.api_key}"
                    }
                    
                    response = requests.post(url, json=payload, headers=headers)

                    if response.status_code == 200:
                        results = response.json()
                        content = results['choices'][0]['message']['content'] if 'choices' in results and len(results['choices']) > 0 else "Not Available"
                        
                        # Display the typing effect
                        st.write("### Results:")
                        type_text(content)
                        
                        # Create Word document with the full content
                        buffer = create_word_doc(query, content)
                        st.download_button(label="Download as Word Document", data=buffer, file_name=f"{query}.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
                    
                    else:
                        st.write(f"Error: {response.status_code}")
                        st.write(f"Response: {response.content}")
                else:
                    # If the query is not IFRS-related
                    st.write("Out of IFRS context.")
            else:
                st.write("Please enter a query.")
        
        # Adding a footer with IFRS standards link
        st.write("---")
        st.write("For detailed information about IFRS standards, visit [IFRS Standards](https://www.ifrs.org/issued-standards/list-of-standards/).")
    else:
        st.write("Please enter your Perplexity API key in the sidebar to proceed.")
else:
    st.write("Please log in to use the IFRS Research Assistant.")
