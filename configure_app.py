# configure_app.py
import configparser
import os

def create_config():
    print("Welcome to the RAG App Configuration!")
    print("Please provide the following details:")

    # Azure App Registration
    client_id = input("Azure Client ID: ")
    client_secret = input("Azure Client Secret: ")
    tenant_id = input("Azure Tenant ID: ")
    user_id = input("Azure User ID: ")

    # Gemini API Key
    google_api_key = input("Google Gemini API Key: ")

    # Create config.cfg
    config = configparser.ConfigParser()
    config['azure'] = {
        'clientId': client_id,
        'clientSecret': client_secret,
        'tenantId': tenant_id,
        'userId': user_id
    }
    config['gemini'] = {
        'google_api_key': google_api_key
    }

    with open('config.cfg', 'w') as configfile:
        config.write(configfile)

    print("Configuration file 'config.cfg' has been created successfully!")

if __name__ == "__main__":
    create_config()