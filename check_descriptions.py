import json

# Check if descriptions were added
notebooks = [
    "biometric_failure_analysis.ipynb",
    "Resource_Allocation_Optimization.ipynb", 
    "fraud_detection_analysis.ipynb",
    "district_anomaly_detection.ipynb"
]

print("Checking if descriptions were added...\n")

for nb_name in notebooks:
    original_file = nb_name
    described_file = nb_name.replace('.ipynb', '_with_descriptions.ipynb')
    
    try:
        with open(original_file, 'r', encoding='utf-8') as f:
            nb_orig = json.load(f)
        
        with open(described_file, 'r', encoding='utf-8') as f:
            nb_desc = json.load(f)
        
        orig_cells = len(nb_orig['cells'])
        desc_cells = len(nb_desc['cells'])
        
        # Count markdown cells with "Analysis Insight"
        desc_count = sum(1 for cell in nb_desc['cells'] 
                        if cell['cell_type'] == 'markdown' 
                        and 'Analysis Insight' in ''.join(cell['source']))
        
        print(f"{nb_name}:")
        print(f"  Original cells: {orig_cells}")
        print(f"  With descriptions: {desc_cells}")
        print(f"  Description cells added: {desc_count}")
        print()
        
    except Exception as e:
        print(f"Error checking {nb_name}: {e}\n")
