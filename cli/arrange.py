import requests
import random

def prompt_user():
    # Prompt user for hardiness zone
    hardiness_zone = input("Enter your hardiness zone: ")

    # Prompt user for desired color palette
    color_palette = input("Enter your desired color palette (comma-separated): ").split(',')

    # Prompt user for sun exposure
    sun_exposure = input("Enter your sun exposure (full shade, part shade, full sun): ")

    varieties = input("Enter how many plant vatieties your arrangement should contain: ")

    return hardiness_zone, color_palette, sun_exposure, varieties

def get_plants(api_key, page=1, cycle="annual", sunlight="full_sun", indoor=0, palette=[], varieties=5):
    url = f"https://perenual.com/api/species-list?key={api_key}&page={page}&cycle={cycle}&sunlight={sunlight}&indoor={indoor}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4XX and 5XX status codes
        json = response.json()


        data_array = json.get("data", [])
        if not isinstance(data_array, list):
            print("Error: 'data' field is not a list.")
            return []

        random_entries = random.sample(data_array, min(varieties, len(data_array)))
        common_names = [entry.get("common_name", "") for entry in random_entries]
        return [name for name in common_names if name]

    except requests.RequestException as e:
        print("Error fetching plant list:", e)
        return None
    
    
# TODO: Key is stored in plain text right now. It really should not be. Should be stored in a vault and get
#       built into container that runs this as an env var
def get_key():
    try:
        with open("secrets/key", "r") as file:
            key = file.read().strip()
            return key
    except FileNotFoundError:
        print("Error: The key file was not found.")
        return None

def main():
    print("Welcome to the Plant Arrangment Program!")
    hardiness_zone, color_palette, sun_exposure, varieties = prompt_user()
    print("\nYou entered the following:")
    print("Hardiness Zone:", hardiness_zone)
    print("Desired Color Palette:", color_palette)
    print("Sun Exposure:", sun_exposure)
    print("Number of plant varieties:", varieties)

    key = get_key()
    plant_list = get_plants(key, hardiness_zone, sunlight=sun_exposure, palette=color_palette, varieties=varieties)

    print(f"You should plant {plant_list}!")

if __name__ == "__main__":
    main()
