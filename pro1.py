import numpy as np

crop_water_requirements = {
    "rice": 20000,      # kg/ha
    "wheat": 6000,      # kg/ha
    "corn": 8000,       # kg/ha
    "soybeans": 7000,   # kg/ha
    "sugarcane": 25000  # kg/ha
}

def select_field():
    fields = [
        {"name": "North Farm", "coords": (28.7, 77.1), "size": 1.2},
        {"name": "East Farm", "coords": (28.8, 77.3), "size": 2.5},
        {"name": "South Farm", "coords": (28.6, 77.2), "size": 3.8},
        {"name": "West Farm", "coords": (28.5, 77.0), "size": 0.9}
    ]
    print("Select your field location:")
    for idx, field in enumerate(fields, 1):
        print(f"{idx}. {field['name']} (Lat: {field['coords'][0]}, Lon: {field['coords'][1]}) - Size: {field['size']} ha")
    print(f"{len(fields)+1}. Set a custom farm location")
    while True:
        try:
            choice = int(input("Enter the number of your field location: "))
            if 1 <= choice <= len(fields):
                return fields[choice - 1]
            elif choice == len(fields) + 1:
                lat = float(input("Enter latitude: "))
                lon = float(input("Enter longitude: "))
                size = float(input("Enter field size in hectares: "))
                return {"name": "Custom Farm", "coords": (lat, lon), "size": size}
            else:
                print("Invalid selection. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("=== AI Crop Water System ===")
    field = select_field()
    crop = input("Enter crop name (e.g., rice, wheat, corn): ").strip().lower()
    crop_req = crop_water_requirements.get(crop, 5000)
    irrigation_volume = crop_req * field["size"]
    print(f"\nIrrigation volume required for {crop.capitalize()} on {field['size']} ha: {irrigation_volume:.2f} kg")

    total_quota = np.random.uniform(500, 1500)
    allocated = min(irrigation_volume, total_quota / 4)
    deficit = irrigation_volume - allocated
    print("\n--- Recommendation ---")
    print(f"Field: {field['name']} ({field['size']} ha)")
    print(f"Crop: {crop.capitalize()}")
    print(f"Requested Volume: {irrigation_volume:.2f} kg")
    print(f"Allocated Volume: {allocated:.2f} kg")
    if deficit > 0.01:
        print(f"Deficit: {deficit:.2f} kg. Suggest buying water from neighbors.")
    elif allocated > irrigation_volume:
        print(f"Surplus: {allocated - irrigation_volume:.2f} kg. Suggest selling water to neighbors.")
    else:
        print("Needs met. No trading required.")

if __name__ == "__main__":
    main()
