import requests
import time

# Function to display the emoji banner
def display_emoji_banner():
    print("""
    🌟✨🌟✨🌟✨🌟✨🌟✨
       🌟   BY RIDI   🌟
    🌟✨🌟✨🌟✨🌟✨🌟✨
    """)
    time.sleep(2)

# Function to read tokens from datas.txt
def read_tokens(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Define request functions
def send_clicks(auth_token):
    url = 'https://crystalton.ru/api/clicks'
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en',
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json;charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
    }
    data = {"clicks": 100}
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Clicks Response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error sending clicks: {e}")

def send_ad(auth_token):
    url = 'https://crystalton.ru/api/ads'
    headers = {
        'accept': 'application/json',
        'accept-language': 'en',
        'authorization': f'Bearer {auth_token}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    try:
        # Switching to GET request based on error analysis
        response = requests.get(url, headers=headers)
        if response.status_code == 405:
            print("The POST method is not supported for this route. Try using GET.")
        print(f"Ad Response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error sending ad: {e}")

def send_spin(auth_token):
    url = 'https://crystalton.ru/api/fortune_wheel/spin'
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en',
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json;charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 404:
            print("Spin endpoint not found. Verify the route.")
        print(f"Spin Response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error sending spin: {e}")

# Main execution loop
def main():
    display_emoji_banner()  # Display the banner at the start
    tokens = read_tokens("datas.txt")
    if not tokens:
        print("No tokens found in datas.txt")
        return

    while True:
        for token in tokens:
            # Send 100 clicks every 6 minutes
            print("Sending clicks...")
            send_clicks(token)
            
            # Send 1 ad, then 1 spin with 2 seconds delay between them
            for _ in range(1):  # Updated to avoid infinite loop
                print("Sending ad...")
                send_ad(token)
                time.sleep(2)
                print("Sending spin...")
                send_spin(token)
                time.sleep(2)
            time.sleep(360)  # Wait 6 minutes before next iteration

# Run the script
if __name__ == "__main__":
    main()
