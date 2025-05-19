import pandas as pd
import json


old_config = pd.read_json("config_old.json")
new_config = pd.read_json("config_new.json")

merged_config = pd.merge(old_config, new_config, on="key", how="inner", suffixes=("_old", "_new"))

changed = merged_config[
    (merged_config["value_old"] != merged_config["value_new"])
]

print(changed.shape)