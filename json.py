import requests
# Define your API key
api_key = "YOUR_API_KEY"

# Define the base URL for the UN Data API
base_url = "http://data.un.org/Handlers/"

# Define a function to fetch data from the API
def fetch_un_data(indicator, country="all", year="2020"):
    url = (
        f"{base_url}{indicator}.ashx?"
        f"DataSet=POP&crID={country}&sDM=YE&sp=0&" 
        f"tid={indicator}TH&thid=1&ts=5&" 
        f"rcID=1&occID=5&returnhtml=false&" 
        f"token={api_key}"
    )
    response = requests.get(url)
    print(response.text)  # Print the response content for debugging
    data = response.json()
    return data
