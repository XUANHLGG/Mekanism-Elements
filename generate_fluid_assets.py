import os
import json

fluids = [
    "ammonia", "ammonium_nitrate", "beryllium", "bromine", "compressed_air", "helium",
    "hydrogen_cyanide", "superheated_helium", "iodine", "methane", "nitric_acid",
    "nitrogen", "nitrogen_dioxide", "nitric_oxide", "potassium_chloride",
    "potassium_cyanide", "potassium_hydroxide", "potassium_iodide", "strontium",
    "xenon", "yttrium"
]

base_path = "c:/Users/imba/Git/Mekanism-Elements/src/main/resources/assets/mekanismelements"
blockstates_dir = os.path.join(base_path, "blockstates")
models_dir = os.path.join(base_path, "models/block")

os.makedirs(blockstates_dir, exist_ok=True)
os.makedirs(models_dir, exist_ok=True)

for fluid in fluids:
    # Generate Blockstate
    bs_path = os.path.join(blockstates_dir, f"{fluid}.json")
    variants = {}
    # Creating variants for all levels 0-15
    for i in range(16):
        variants[f"level={i}"] = { "model": f"mekanismelements:block/{fluid}" }
    
    bs_content = { "variants": variants }
    
    with open(bs_path, "w") as f:
        json.dump(bs_content, f, indent=2)
    
    # Generate Model
    model_path = os.path.join(models_dir, f"{fluid}.json")
    model_content = {
        "textures": {
            "particle": "mekanism:liquid/liquid"
        }
    }
    
    with open(model_path, "w") as f:
        json.dump(model_content, f, indent=2)

print(f"Generated assets for {len(fluids)} fluids.")
