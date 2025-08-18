# Daily Task Automator

A Python script to automate common daily tasks such as opening Google Maps, checking the weather, and launching custom web links in your browser.



## 1. Business Understanding

Many people perform repetitive online tasks every day, such as checking locations, weather, or visiting frequently used websites. This project aims to automate these tasks to save time and improve productivity.



## 2. Data Understanding

The “data” in this context is the user input:  
- Addresses or locations (for Google Maps or weather queries)  
- Website names or URLs (for opening custom links)  

Optional: Clipboard content is also used if no input is provided.



## 3. Data Preparation

- User inputs are cleaned using `.strip()` to remove extra spaces.  
- Website names are formatted to include `https://` and `.com` if missing.  
- Clipboard content is retrieved using `pyperclip` if no input is provided.



## 4. Modeling (Logic / Implementation)

- **Google Maps:** Constructs a URL with the address and opens it using `webbrowser`.  
- **Weather:** Constructs a Google search URL for the weather and opens it.  
- **Custom Links:** Splits comma-separated website names, formats them, and opens each in a new tab.


## 5. Evaluation

- The script prompts the user with a clear menu.  
- Validates input (checks if a number 1–4 is entered).  
- Handles empty inputs gracefully using clipboard content.  
- Opens the correct URLs in browser tabs.



## 6. Deployment

- Run locally using Python 3.x:

```bash
python daily_url_opener.py