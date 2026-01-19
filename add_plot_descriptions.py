import json
import copy

# Load the notebook
with open('Rural_Urban_Adoption_Analysis.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Descriptions for each major section's plots
plot_descriptions = {
    "Data Overview": [
        "**Analysis Insight:** This visualization shows the distribution of rural and urban areas in the dataset, providing a baseline understanding of the geographic composition of Aadhaar enrollments.",
        "**Analysis Insight:** The demographic breakdown reveals the age-wise distribution of enrollments across rural and urban areas, highlighting which age groups have higher adoption rates.",
        "**Analysis Insight:** This comparison chart identifies states with the highest enrollment counts, allowing policymakers to understand regional adoption patterns."
    ],
    "Rural vs Urban Analysis - Enrollment Data": [
        "**Analysis Insight:** This chart compares total enrollments between rural and urban areas, revealing the urban-rural divide in Aadhaar adoption and helping identify underserved regions.",
        "**Analysis Insight:** Age-wise enrollment distribution shows which demographic groups are being reached effectively in both rural and urban areas, guiding targeted outreach programs.",
        "**Analysis Insight:** State-wise comparison highlights geographic disparities in rural vs urban adoption, enabling resource allocation to states with lower rural enrollment."
    ],
    "State-wise Rural vs Urban Analysis": [
        "**Analysis Insight:** The top states comparison reveals which regions have successfully implemented Aadhaar in both rural and urban areas, providing best practices for other states.",
        "**Analysis Insight:** This detailed breakdown shows the enrollment gap between rural and urban areas for each leading state, identifying where intervention is most needed.",
        "**Analysis Insight:** District-level analysis within top states pinpoints specific localities with enrollment challenges, enabling micro-level policy interventions.",
        "**Analysis Insight:** The proportional view illustrates the relative success of rural enrollment compared to urban areas, accounting for population differences."
    ],
    "Demographic Data Analysis": [
        "**Analysis Insight:** Demographic enrollment patterns by area type show how different population segments are accessing Aadhaar services in rural vs urban settings.",
        "**Analysis Insight:** Age-wise demographic distribution reveals which age groups face barriers to enrollment in rural areas compared to urban centers.",
        "**Analysis Insight:** This cross-sectional analysis helps identify demographic groups requiring targeted awareness and enrollment campaigns."
    ],
    "Biometric Authentication Analysis": [
        "**Analysis Insight:** Biometric capture success rates indicate infrastructure quality and accessibility differences between rural and urban enrollment centers.",
        "**Analysis Insight:** Age-wise authentication patterns reveal whether certain demographics face more challenges with biometric technology in rural areas.",
        "**Analysis Insight:** Geographic distribution of biometric failures helps identify areas needing equipment upgrades or operator training."
    ],
    "Digital Divide Analysis": [
        "**Analysis Insight:** The digital divide index quantifies the gap in Aadhaar adoption between rural and urban areas, providing a single metric for policy evaluation."
    ],
    "Time-Series Analysis": [
        "**Analysis Insight:** Enrollment trends over time reveal whether the rural-urban gap is narrowing or widening, indicating the effectiveness of government initiatives to improve rural access."
    ]
}

# Create a new cells list
new_cells = []
current_section = None

for i, cell in enumerate(nb['cells']):
    new_cells.append(cell)
    
    # Check if this is a markdown cell with a heading
    if cell['cell_type'] == 'markdown':
        content = ''.join(cell['source'])
        # Extract section names
        for section_name in plot_descriptions.keys():
            if section_name.lower() in content.lower():
                current_section = section_name
                break
    
    # Check if this is a code cell with output (a plot)
    if cell['cell_type'] == 'code' and current_section:
        has_image = False
        if 'outputs' in cell and cell['outputs']:
            for output in cell['outputs']:
                if output.get('output_type') in ['display_data', 'execute_result']:
                    if 'data' in output and 'image/png' in output['data']:
                        has_image = True
                        break
        
        # If this code cell has an image output, add a description cell after it
        if has_image and current_section in plot_descriptions:
            descriptions = plot_descriptions[current_section]
            if descriptions:
                desc_text = descriptions.pop(0)  # Take the first available description
                
                # Create a new markdown cell with the description
                desc_cell = {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        f"\n{desc_text}\n"
                    ]
                }
                new_cells.append(desc_cell)
                print(f"Added description after cell {i} in section '{current_section}'")

# Update the notebook with new cells
nb['cells'] = new_cells

# Save the updated notebook
output_file = 'Rural_Urban_Adoption_Analysis_with_descriptions.ipynb'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print(f"\n✅ Updated notebook saved as: {output_file}")
print(f"📊 Total cells: {len(new_cells)}")
print("\n💡 Review the notebook and adjust descriptions as needed, then rename it to replace the original.")
