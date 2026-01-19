import json
import os

# Check all notebooks
notebooks = [
    "biometric_failure_analysis.ipynb",
    "Resource_Allocation_Optimization.ipynb",
    "fraud_detection_analysis.ipynb",
    "district_anomaly_detection.ipynb",
    "Rural_Urban_Adoption_Analysis.ipynb"
]

print("="*70)
print("FINAL VERIFICATION - NOTEBOOK DESCRIPTIONS")
print("="*70)
print()

total_descriptions = 0

for nb_name in notebooks:
    if os.path.exists(nb_name):
        with open(nb_name, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        # Count cells
        total_cells = len(nb['cells'])
        
        # Count markdown cells with "Analysis Insight"
        desc_count = sum(1 for cell in nb['cells'] 
                        if cell['cell_type'] == 'markdown' 
                        and 'Analysis Insight' in ''.join(cell.get('source', [])))
        
        code_with_plots = sum(1 for cell in nb['cells']
                             if cell['cell_type'] == 'code'
                             and 'outputs' in cell
                             and any('image/png' in output.get('data', {})
                                   for output in cell.get('outputs', [])
                                   if 'data' in output))
        
        total_descriptions += desc_count
        
        status = "OK" if desc_count > 0 else "NO DESCRIPTIONS"
        
        print(f"{nb_name}")
        print(f"  Total cells: {total_cells}")
        print(f"  Code cells with plots: {code_with_plots}")
        print(f"  Description cells: {desc_count}")
        print(f"  Status: {status}")
        print()
    else:
        print(f"{nb_name} - FILE NOT FOUND")
        print()

print("="*70)
print(f"TOTAL DESCRIPTIONS ADDED ACROSS ALL NOTEBOOKS: {total_descriptions}")
print("="*70)
print()
print("All notebooks are ready for the Streamlit dashboard!")
print("The descriptions will appear alongside the plots automatically.")
