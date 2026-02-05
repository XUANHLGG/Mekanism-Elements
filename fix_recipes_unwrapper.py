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
        # Unwrap 'ingredient' if present
        if "ingredient" in item_input:
            print(f"Unwrapping item_input in {file_path}")
            # Move contents of ingredient up
            ing_content = item_input.pop("ingredient")
            item_input.update(ing_content)
            changed = True
        
        # Now fix id -> item
        if "id" in item_input:
            item_input["item"] = item_input.pop("id")
            changed = True
    
    # Fix fluid_input (Adsorption)
    if "fluid_input" in data:
        fluid_input = data["fluid_input"]
        # Unwrap 'ingredient' if present (check just in case)
        if "ingredient" in fluid_input:
            print(f"Unwrapping fluid_input in {file_path}")
            ing_content = fluid_input.pop("ingredient")
            fluid_input.update(ing_content)
            changed = True

        if "id" in fluid_input:
            fluid_input["fluid"] = fluid_input.pop("id")
            changed = True
    
    # Fix chemical_input (Radiation)
    if "chemical_input" in data:
        chem_input = data["chemical_input"]
        # Unwrap 'ingredient' if present
        if "ingredient" in chem_input:
            print(f"Unwrapping chemical_input in {file_path}")
            ing_content = chem_input.pop("ingredient")
            chem_input.update(ing_content)
            changed = True

        if "id" in chem_input:
            chem_input["chemical"] = chem_input.pop("id")
            changed = True
            
        if "gas" in chem_input:
            chem_input["chemical"] = chem_input.pop("gas")
            changed = True

    # Fix output (ChemicalStack)
    if "output" in data:
        output = data["output"]
        # Convert legacy types to 'id'
        for legacy_key in ["slurry", "gas", "infuse_type", "pigment", "chemical"]:
            if legacy_key in output:
                print(f"Fixing output {legacy_key} -> id in {file_path}")
                output["id"] = output.pop(legacy_key)
                changed = True
        
        # Remove chemicalType if present (legacy)
        if "chemicalType" in output:
             output.pop("chemicalType")
             changed = True

    if changed:
        print(f"Saving {file_path}")
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
