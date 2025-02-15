import pandas as pd
import json


input_file = "menu.xlsx"  
output_file = "output.json" 

try:
    
    df = pd.read_excel(input_file)

   
    df.replace("********", "", inplace=True)
    df.dropna(inplace=True)

    
    menu_dict = {}

    for col in df.columns[1:]: 
        day_menu = {
            "Breakfast": list(df.iloc[0, 1:].dropna()), 
            "Lunch": list(df.iloc[1, 1:].dropna()),  
            "Dinner": list(df.iloc[2, 1:].dropna()) 
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
