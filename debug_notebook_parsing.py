import json
import os
import re

NOTEBOOK_MAP = {
    "biometric_failure_analysis.ipynb": {"name": "🔍 Biometric Failure Analysis", "analyst": "Paras"},
    "Resource_Allocation_Optimization.ipynb": {"name": "📈 Resource Allocation Optimization", "analyst": "Sriyansh Sharma"},
    "fraud_detection_analysis.ipynb": {"name": "🚨 Fraud Detection", "analyst": "Anurag Rai"},
    "Rural_Urban_Adoption_Analysis.ipynb": {"name": "🏘️ Rural vs Urban Adoption", "analyst": "Shivansh "},
    "district_anomaly_detection.ipynb": {"name": "📍 District-level Hotspots", "analyst": "Kartikeya Gupta"}
}

def parse_notebook(notebook_path):
    """Parse notebook and extract sections with plots"""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        sections = []
        current_section = None
        
        for cell in nb.get('cells', []):
            if cell['cell_type'] == 'markdown':
                content = ''.join(cell['source'])
                headings = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
                if headings:
                    if current_section and current_section['plots']:
                        sections.append(current_section)
                    current_section = {'heading': headings[0], 'plots': [], 'text': content}
                elif current_section:
                    current_section['text'] += '\n' + content
            
            elif cell['cell_type'] == 'code' and current_section:
                if 'outputs' in cell:
                    for output in cell['outputs']:
                        if output.get('output_type') in ['display_data', 'execute_result']:
                            if 'data' in output:
                                plot_data = output['data']
                                if 'image/png' in plot_data or 'text/html' in plot_data:
                                    current_section['plots'].append(plot_data)
        
        if current_section and current_section['plots']:
            sections.append(current_section)
        
        return sections
    except Exception as e:
        print(f"Error parsing notebook: {e}")
        return []

# Check each notebook
for filename, info in NOTEBOOK_MAP.items():
    if os.path.exists(filename):
        print(f"\n{'='*80}")
        print(f"Notebook: {info['name']}")
        print(f"File: {filename}")
        print(f"Analyst: {info['analyst']}")
        print(f"{'='*80}")
        
        sections = parse_notebook(filename)
        
        if not sections:
            print("⚠️ NO SECTIONS WITH PLOTS FOUND!")
            print("\nDebugging info:")
            
            # Check if notebook has any content
            with open(filename, 'r', encoding='utf-8') as f:
                nb = json.load(f)
            
            cells = nb.get('cells', [])
            markdown_cells = [c for c in cells if c['cell_type'] == 'markdown']
            code_cells = [c for c in cells if c['cell_type'] == 'code']
            
            print(f"  - Total cells: {len(cells)}")
            print(f"  - Markdown cells: {len(markdown_cells)}")
            print(f"  - Code cells: {len(code_cells)}")
            
            # Check for headings
            headings = []
            for cell in markdown_cells:
                content = ''.join(cell['source'])
                found_headings = re.findall(r'^#+\s+(.+)$', content, re.MULTILINE)
                headings.extend(found_headings)
            
            print(f"  - Headings found: {len(headings)}")
            if headings:
                print("    First few headings:")
                for h in headings[:5]:
                    print(f"      • {h}")
            
            # Check for outputs
            cells_with_outputs = [c for c in code_cells if c.get('outputs')]
            print(f"  - Code cells with outputs: {len(cells_with_outputs)}")
            
            # Check for plot outputs
            plot_outputs = 0
            for cell in code_cells:
                for output in cell.get('outputs', []):
                    if output.get('output_type') in ['display_data', 'execute_result']:
                        if 'data' in output:
                            plot_data = output['data']
                            if 'image/png' in plot_data or 'text/html' in plot_data:
                                plot_outputs += 1
            
            print(f"  - Plot outputs found: {plot_outputs}")
        else:
            print(f"✅ Found {len(sections)} sections with plots")
            for i, section in enumerate(sections, 1):
                print(f"\n  {i}. {section['heading']}")
                print(f"     Plots: {len(section['plots'])}")
    else:
        print(f"\n❌ File not found: {filename}")

print("\n" + "="*80)
