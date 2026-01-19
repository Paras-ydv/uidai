import os
import shutil
from pathlib import Path

# List of notebooks to update
notebooks_to_update = [
    "biometric_failure_analysis.ipynb",
    "Resource_Allocation_Optimization.ipynb",
    "fraud_detection_analysis.ipynb",
    "district_anomaly_detection.ipynb",
    "Rural_Urban_Adoption_Analysis.ipynb"
]

print("📝 Applying descriptions to original notebooks...\n")

for notebook in notebooks_to_update:
    described_version = notebook.replace('.ipynb', '_with_descriptions.ipynb')
    
    if os.path.exists(described_version):
        # Create backup of original
        backup_name = notebook.replace('.ipynb', '_backup.ipynb')
        if os.path.exists(notebook):
            shutil.copy2(notebook, backup_name)
            print(f"✅ Backed up: {notebook} → {backup_name}")
        
        # Replace original with described version
        shutil.copy2(described_version, notebook)
        print(f"✅ Updated: {notebook} with descriptions")
        print()
    else:
        print(f"⚠️  Described version not found: {described_version}")
        print()

print("\n" + "="*60)
print("✨ All notebooks have been updated with descriptions!")
print("="*60)
print("\nBackup files (*_backup.ipynb) have been created for safety.")
print("The Streamlit dashboard will now show the descriptions for each plot.")
