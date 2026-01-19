import os
import shutil

# List of successfully described notebooks
notebooks_to_update = [
    "Resource_Allocation_Optimization.ipynb",
    "fraud_detection_analysis.ipynb",
    "district_anomaly_detection.ipynb",
    "Rural_Urban_Adoption_Analysis.ipynb"
]

print("Applying descriptions to original notebooks...\n")

for notebook in notebooks_to_update:
    described_version = notebook.replace('.ipynb', '_with_descriptions.ipynb')
    
    if os.path.exists(described_version) and os.path.exists(notebook):
        # Only update if backup doesn't already exist
        backup_name = notebook.replace('.ipynb', '_backup.ipynb')
        if not os.path.exists(backup_name):
            shutil.copy2(notebook, backup_name)
            print(f"Backed up: {notebook} -> {backup_name}")
        
        # Replace original with described version
        shutil.copy2(described_version, notebook)
        print(f"Updated: {notebook} with descriptions\n")
    else:
        print(f"Skipping {notebook} - missing files\n")

print("\n" + "="*60)
print("DONE!")
print("="*60)
print("The following notebooks now have descriptions:")
for nb in notebooks_to_update:
    if os.path.exists(nb):
        print(f"  - {nb}")
