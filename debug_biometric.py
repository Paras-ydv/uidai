import json

# Check the biometric notebook structure
with open('biometric_failure_analysis.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}\n")

code_cells = [c for c in nb['cells'] if c['cell_type'] == 'code']
print(f"Total code cells: {len(code_cells)}\n")

print("Code cell analysis (first 10):")
for i, cell in enumerate(code_cells[:10]):
    source = ''.join(cell.get('source', []))
    char_count = len(source.strip())
    starts_with = source.strip()[:50] if source.strip() else "(empty)"
    print(f"  Cell {i}: {char_count} chars - Starts with: {starts_with}...")
