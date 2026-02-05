import os
import json

def fix_recipe(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error decoding {file_path}")
        return

    changed = False

    # Fix item_input
    if "item_input" in data:
        item_input = data["item_input"]
        if "ingredient" in item_input:
            ing = item_input["ingredient"]
            if "id" in ing:
                ing["item"] = ing.pop("id")
                changed = True
        # Sometimes item_input itself might be the ingredient if it's not wrapped? 
        # But Adsorption/Radiation seem to strictly use "ingredient" sub-object.
        # Check standard Mekanism ItemStackIngredient structure.
    
    # Fix fluid_input (Adsorption)
    if "fluid_input" in data:
        fluid_input = data["fluid_input"]
        if "id" in fluid_input:
            fluid_input["fluid"] = fluid_input.pop("id")
            changed = True
    
    # Fix chemical_input (Radiation)
    if "chemical_input" in data:
        chem_input = data["chemical_input"]
        if "id" in chem_input:
            # Mekanism 1.21 uses "chemical" for pure chemical inputs
            chem_input["chemical"] = chem_input.pop("id")
            changed = True
            
    # Check for gas_input (Old format? or just different naming?)
    # RadiationIrradiatorRecipeSerializer might allow 'gas_input' alias? 
    # Let's assume keys in JSON are correct ('chemical_input') but inner 'id' is wrong.

    if changed:
        print(f"Fixing {file_path}")
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)

def main():
    root_dir = r"c:\Users\imba\Git\Mekanism-Elements\src\main\resources\data\mekanismelements\recipes"
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".json"):
                fix_recipe(os.path.join(subdir, file))

if __name__ == "__main__":
    main()
