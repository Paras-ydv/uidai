import json
import os

# Specific descriptions for biometric failure analysis
biometric_descriptions = [
    "**Analysis Insight:** This visualization identifies temporal patterns in biometric capture failures, helping pinpoint peak failure periods and equipment maintenance schedules.",
    "**Analysis Insight:** Geographic distribution of biometric failures reveals regions with infrastructure challenges, guiding targeted equipment upgrades and technical support.",
    "**Analysis Insight:** The failure rate comparison across states highlights best-performing regions, providing benchmarks and best practices for underperforming areas.",
    "**Analysis Insight:** Age-wise failure analysis shows which demographic groups experience more authentication difficulties, informing operator training and technology improvements.",
    "**Analysis Insight:** This breakdown shows the relationship between failure types and environmental factors, guiding infrastructure improvements.",
    "**Analysis Insight:** Trend analysis reveals whether biometric capture quality is improving over time, measuring the effectiveness of technical interventions.",
    "**Analysis Insight:** Correlation analysis between failure rates and enrollment volumes helps optimize resource allocation during peak periods.",
    "**Analysis Insight:** District-level hotspots identify specific localities requiring immediate technical attention and equipment upgrades."
]

def add_descriptions_to_biometric():
    """Add descriptions to biometric failure analysis notebook"""
    
    notebook_path = 'biometric_failure_analysis.ipynb'
    
    if not os.path.exists(notebook_path):
        print(f"Error: {notebook_path} not found")
        return
    
    # Load notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    new_cells = []
    desc_index = 0
    added_count = 0
    
    for i, cell in enumerate(nb['cells']):
        new_cells.append(cell)
        
        # Check if this is a code cell with plot output
        if cell['cell_type'] == 'code':
            # Check if it has image output (PNG)
            has_plot = False
            if 'outputs' in cell:
                for output in cell.get('outputs', []):
                    if 'data' in output and 'image/png' in output.get('data', {}):
                        has_plot = True
                        break
            
            # Add description after code cells with plots
            if has_plot and desc_index < len(biometric_descriptions):
                desc_cell = {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [f"\n{biometric_descriptions[desc_index]}\n"]
                }
                new_cells.append(desc_cell)
                desc_index += 1
                added_count += 1
                print(f"Added description {desc_index} after cell {i}")
    
    # Update notebook
    nb['cells'] = new_cells
    
    # Save with _with_descriptions suffix
    output_path = 'biometric_failure_analysis_with_descriptions.ipynb'
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2, ensure_ascii=False)
    
    print(f"\nSuccessfully added {added_count} descriptions to {output_path}")
    return output_path, added_count

if __name__ == "__main__":
    print("Adding descriptions to biometric failure analysis notebook...\n")
    add_descriptions_to_biometric()
