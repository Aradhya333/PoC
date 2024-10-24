import streamlit as st
import openai
import requests
import os

def main():
    st.title("Azure OpenAI GPT-4o Connectivity Test") 
    
    # Azure OpenAI connection details
    # Store your API key in an environment variable for better security
    azure_openai_key = os.getenv(" 22ec84421ec24230a3638d1b51e3a7dc")  # Ensure you set this in your environment
    azure_openai_endpoint = "https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"  # Replace with your actual endpoint URL
    
    # Button to initiate the connection and request
    if st.button("Connect and Get Response"):
        
        if azure_openai_key and azure_openai_endpoint:
            try:
                # Setting up headers for the API request
                headers = {
                    "Content-Type": "application/json",
                    "api-key":" 22ec84421ec24230a3638d1b51e3a7dc"  # Use the environment variable for the API key
                }
                
                # Data to be sent to Azure OpenAI
                data = {
                    "messages": [{"role": "user", "content": "Hello, Azure OpenAI!"}],
                    "max_tokens": 50
                }
                
                # Making the POST request to the Azure OpenAI endpoint
                response = requests.post(azure_openai_endpoint, headers=headers, json=data)
                
                # Check if the request was successful
                if response.status_code == 200:
                    result = response.json()
                    st.success(result["choices"][0]["message"]["content"].strip())
                else:
                    st.error(f"Failed to connect or retrieve response: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Failed to connect or retrieve response: {str(e)}")
        else:
            st.warning("Please enter all the required details.")

if __name__ == "__main__":
    main()
