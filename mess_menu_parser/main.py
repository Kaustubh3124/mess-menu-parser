import pandas as pd
import json

# File paths
input_file = "menu.xlsx"  # The provided Excel file
output_file = "output.json"  # The JSON output file

try:
    # Load the Excel file
    df = pd.read_excel(input_file)

    # Remove unnecessary values (e.g., "********") and drop empty cells
    df.replace("********", "", inplace=True)
    df.dropna(inplace=True)

    # Convert the data into a structured dictionary
    menu_dict = {}

    for col in df.columns[1:]:  # Skip the first column if it contains time/index
        day_menu = {
            "Breakfast": list(df.iloc[0, 1:].dropna()),  # Row 1 → Breakfast
            "Lunch": list(df.iloc[1, 1:].dropna()),  # Row 2 → Lunch
            "Dinner": list(df.iloc[2, 1:].dropna())  # Row 3 → Dinner
        }
        menu_dict[col] = day_menu

    # Save the structured data as JSON
    with open(output_file, "w") as json_file:
        json.dump(menu_dict, json_file, indent=4, default=str)


    print(f"✅ JSON file saved successfully as {output_file}")

except FileNotFoundError:
    print(f"❌ Error: {input_file} not found! Please add the Excel file.")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")
