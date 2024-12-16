import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Save the complete HTML content to a file
        with open('website_content.html', 'w', encoding='utf-8') as file:
            file.write(str(soup))
        
        print("Website content has been successfully extracted and saved to 'website_content.html'.")
    else:
        print("Failed to retrieve the web page.")

# Example usage
url = "https://aminutewithmary.com/"  # Enter the URL for desired website
scrape_website(url)
