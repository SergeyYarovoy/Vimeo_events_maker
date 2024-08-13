# Usage: 
# python create_live_events.py --user_token <your_user_token> --user_id <your_user_id> --count <number_of_events>


import requests
import argparse

def create_live_event(user_token, user_id, event_number):
    api_url = f"https://api.vimeo.com/users/{user_id}/live_events"
    headers = {
        "Authorization": f"Bearer {user_token}",
        "Content-Type": "application/json"
    }
    event_number_formatted = f"{event_number:04}"
    data = {
        "stream_title": f"New Live Event {event_number_formatted}",
        "title": f"New Live Event {event_number_formatted}",
        "automatically_title_stream": "false",
        "stream_description": f"This is live event number {event_number_formatted} created via API.",
        "privacy": {
            "view": "unlisted"
        }
    }

    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code == 200:
        print("Live event created successfully.")
    else:
        print(f"Failed to create live event. HTTP Status: {response.status_code}")

def main():
    parser = argparse.ArgumentParser(description="Create Vimeo live events via API.")
    parser.add_argument('--user_token', required=True, help="Your Vimeo user token.")
    parser.add_argument('--user_id', required=True, help="Your Vimeo user ID.")
    parser.add_argument('--count', type=int, default=100, help="Number of live events to create. Default is 100.")
    
    args = parser.parse_args()

    for i in range(1, args.count + 1):
        print(f"Creating live event {i:04}...")
        create_live_event(args.user_token, args.user_id, i)

if __name__ == "__main__":
    main()

