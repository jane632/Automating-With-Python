# Necessary libraries to automate daily tasks
import webbrowser
from urllib.parse import quote_plus
import pyperclip

def google_maps(address):
    query = quote_plus(address)
    link = f"https://www.google.com/maps/search/?api=1&query={query}"
    webbrowser.open(link)
    print(f"Opened Google Maps for: {address}")

def weather_today(address):
    link = 'https://www.google.com/search?q=weather+' + quote_plus(address)
    webbrowser.open(link)
    print(f"Opened Weather for: {address}")

def open_daily_url():
    links = input('Enter the app(s) you want to open (comma separated): ')
    link_list = [url.strip() for url in links.split(',') if url.strip()]
    for link in link_list:
        if not link.startswith('http'):
            link = 'https://' + link + '.com'
        webbrowser.open_new_tab(link)
    print('All app links opened in browser tabs.')

def get_address():
    address = input("Enter the address/location: ").strip()
    if not address:
        clipboard = pyperclip.paste()
        if clipboard:
            print("No address entered. Using clipboard content.")
            address = clipboard
        else:
            print("No address provided and clipboard is empty. Exiting.")
            exit(1)
    return address

if __name__ == "__main__":
    while True:
        print('\nChoose a task:')
        print('1. Open Google Maps')
        print('2. Check the weather')
        print('3. Open custom app links')
        print('4. Exit')

        option = input('Enter number 1-4: ').strip()

        if option == "1":
            address = get_address()
            google_maps(address)

        elif option == "2":
            address = get_address()
            weather_today(address)

        elif option == "3":
            open_daily_url()

        elif option == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print('Invalid choice. Please enter a number between 1-4.')
