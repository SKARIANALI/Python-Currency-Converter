import requests

def currency_converter():
    """
    A simple command-line currency converter that uses an API for real-time rates.
    """
    # --- Configuration ---
    # IMPORTANT: Replace 'YOUR_API_KEY' with the key from your ExchangeRate-API account.
    api_key = '3d7978c79763ec68d55a3c33'
    
    # --- User Input ---
    base_currency = input("Enter the three-letter code for the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the three-letter code for the target currency (e.g., INR): ").upper()
    
    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Error: The amount must be a valid number.")
        return

    # --- API Call ---
    # Construct the URL for the API request
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    
    try:
        # Send the GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # This will raise an error for bad responses (4xx or 5xx)
        
        # Parse the JSON response into a Python dictionary
        data = response.json()
        
        # --- Data Processing and Calculation ---
        if data.get('result') == 'success':
            conversion_rates = data.get('conversion_rates')
            
            # Check if the target currency is in the retrieved rates
            if target_currency in conversion_rates:
                rate = conversion_rates[target_currency]
                converted_amount = amount * rate
                
                # Display the final result, formatted to two decimal places
                print(f"\n✅ Converted Amount:")
                print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
            else:
                print(f"Error: The target currency '{target_currency}' was not found in the available rates.")
        else:
            # Handle API-specific errors, like an invalid API key or unsupported currency code
            error_type = data.get('error-type', 'An unknown error occurred.')
            print(f"API Error: {error_type}")

    except requests.exceptions.RequestException as e:
        # Handle network-related errors (e.g., no internet connection)
        print(f"Error connecting to the currency service: {e}")
    except KeyError:
        # Handle cases where the expected data isn't in the response
        print("Error: Could not parse the API response. Please check your base currency code.")

# --- Run the converter when the script is executed ---
if __name__ == "__main__":
    currency_converter()