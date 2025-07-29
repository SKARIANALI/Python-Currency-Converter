import tkinter as tk
from tkinter import ttk, messagebox
import requests

class CurrencyConverterApp(tk.Tk):
    """
    A currency converter application with a graphical user interface using Tkinter.
    """
    def __init__(self, api_key):
        super().__init__()
        
        self.api_key = api_key
        self.title("Currency Converter 💰")
        self.geometry("400x280")
        self.resizable(False, False)

        # --- Fetch available currencies for dropdowns ---
        self.currencies = self.get_currencies()
        if not self.currencies:
            messagebox.showerror("API Error", "Could not fetch the currency list.\nPlease check your API key and internet connection.")
            self.destroy()
            return
            
        self.create_widgets()

    def get_currencies(self):
        """Fetches the list of supported currency codes from the API."""
        url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/codes"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data.get('result') == 'success':
                # Return a sorted list of currency codes (e.g., ['AED', 'AFN', ...])
                return sorted([code[0] for code in data.get('supported_codes', [])])
            return []
        except requests.exceptions.RequestException:
            return []

    def create_widgets(self):
        """Creates and places the GUI widgets in the main window."""
        self.configure(bg='#f2f2f2') # Set a background color
        
        # --- Style Configuration ---
        style = ttk.Style(self)
        style.configure('TLabel', background='#f2f2f2', font=('Arial', 11))
        style.configure('TButton', font=('Arial', 11, 'bold'), padding=5)
        style.configure('TEntry', font=('Arial', 11))
        style.configure('TCombobox', font=('Arial', 11))

        # --- Main Frame ---
        main_frame = ttk.Frame(self, padding="20 20 20 20", style='TFrame')
        main_frame.pack(fill="both", expand=True)

        # --- Widget Creation ---
        self.amount_label = ttk.Label(main_frame, text="Amount:")
        self.amount_entry = ttk.Entry(main_frame, width=20)
        self.amount_entry.insert(0, "1.0") # Default amount
        
        self.from_currency_label = ttk.Label(main_frame, text="From Currency:")
        self.from_currency_combo = ttk.Combobox(main_frame, values=self.currencies, width=18, state="readonly")
        self.from_currency_combo.set("USD") # Default 'from' currency
        
        self.to_currency_label = ttk.Label(main_frame, text="To Currency:")
        self.to_currency_combo = ttk.Combobox(main_frame, values=self.currencies, width=18, state="readonly")
        self.to_currency_combo.set("INR") # Default 'to' currency
        
        self.convert_button = ttk.Button(main_frame, text="Convert", command=self.perform_conversion)
        self.result_label = ttk.Label(main_frame, text="", font=('Arial', 12, 'bold'), foreground='#006400')

        # --- Widget Placement (Layout) ---
        self.amount_label.grid(row=0, column=0, padx=5, pady=10, sticky='w')
        self.amount_entry.grid(row=0, column=1, padx=5, pady=10)
        
        self.from_currency_label.grid(row=1, column=0, padx=5, pady=10, sticky='w')
        self.from_currency_combo.grid(row=1, column=1, padx=5, pady=10)
        
        self.to_currency_label.grid(row=2, column=0, padx=5, pady=10, sticky='w')
        self.to_currency_combo.grid(row=2, column=1, padx=5, pady=10)

        self.convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=20)
        self.result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    def perform_conversion(self):
        """Fetches the exchange rate from the API and displays the result."""
        try:
            amount = float(self.amount_entry.get())
            from_curr = self.from_currency_combo.get()
            to_curr = self.to_currency_combo.get()
            
            # Use the more efficient 'pair' conversion endpoint
            url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/pair/{from_curr}/{to_curr}/{amount}"
            response = requests.get(url)
            response.raise_for_status()
            
            data = response.json()
            if data.get('result') == 'success':
                converted_result = data.get('conversion_result')
                result_text = f"{amount} {from_curr} = {converted_result:.2f} {to_curr}"
                self.result_label.config(text=result_text, foreground='#006400')
            else:
                error_type = data.get('error-type', 'Unknown conversion error.')
                messagebox.showerror("Conversion Error", f"Could not perform conversion: {error_type}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for the amount.")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("API Error", f"Failed to connect to the API: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# --- Run the application when the script is executed ---
if __name__ == "__main__":
    # IMPORTANT: Replace 'YOUR_API_KEY' with the key from your ExchangeRate-API account.
    API_KEY = "3d7978c79763ec68d55a3c33"
    app = CurrencyConverterApp(API_KEY)
    app.mainloop()