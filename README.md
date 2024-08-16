**IFRS Research Assistant**

The IFRS Research Assistant is a Streamlit application designed to assist users in researching International Financial Reporting Standards (IFRS). Users can input their IFRS-related queries, and the app fetches detailed responses from the Perplexity AI API. The app also generates a downloadable Word document containing the response.

**Key Features**

-**User Authentication**: Secure login with username, password, and a user-provided Perplexity API key.

-**IFRS-Specific Query Handling**: Filters and processes only IFRS-related queries.

-**Interactive Display**: Responses are displayed with a typing effect for enhanced user experience.

-**Downloadable Reports**: Generates a Word document of the query response for easy download.

-**Secure API Management**: Users provide their own API key, ensuring no keys are hardcoded or exposed.

**How to Use**
**Login**: Enter the credentials (default username: IFRSUser1, password: Password) and your Perplexity API key.

**Enter Query**: Submit an IFRS-related query to receive a detailed response.

**Download**: Download the generated response as a Word document.

**Reference**: For detailed IFRS standards, visit IFRS Standards.

**Installation and Deployment**
Clone the repository and install dependencies using pip install -r requirements.txt.
Run the app locally with streamlit run IFRS.py.
