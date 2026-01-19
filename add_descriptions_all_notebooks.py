import json
import os
from pathlib import Path

# Comprehensive descriptions for each notebook type
notebook_descriptions = {
    "biometric_failure_analysis.ipynb": {
        "descriptions": [
            "**Analysis Insight:** This visualization identifies temporal patterns in biometric capture failures, helping pinpoint peak failure periods and equipment maintenance schedules.",
            "**Analysis Insight:** Geographic distribution of biometric failures reveals regions with infrastructure challenges, guiding targeted equipment upgrades and technical support.",
            "**Analysis Insight:** Age-wise failure analysis shows which demographic groups experience more authentication difficulties, informing operator training and technology improvements.",
            "**Analysis Insight:** The failure rate comparison across states highlights best-performing regions, providing benchmarks and best practices for underperforming areas.",
            "**Analysis Insight:** Trend analysis reveals whether biometric capture quality is improving over time, measuring the effectiveness of technical interventions.",
            "**Analysis Insight:** Correlation analysis between failure rates and enrollment volumes helps optimize resource allocation during peak periods.",
            "**Analysis Insight:** District-level hotspots identify specific localities requiring immediate technical attention and equipment upgrades.",
            "**Analysis Insight:** This breakdown shows the relationship between failure types and environmental factors, guiding infrastructure improvements.",
            "**Analysis Insight:** Success rate distribution across different biometric modalities (fingerprint, iris, photo) informs which technologies work best in various settings.",
            "**Analysis Insight:** The comparative analysis reveals patterns that distinguish systematic issues from random failures, enabling preventive measures."
        ]
    },
    
    "Resource_Allocation_Optimization.ipynb": {
        "descriptions": [
            "**Analysis Insight:** Population distribution analysis reveals where enrollment centers should be concentrated for maximum reach and efficiency.",
            "**Analysis Insight:** Demand forecasting visualizes enrollment trends, helping optimize staff allocation and infrastructure planning for future needs.",
            "**Analysis Insight:** State-wise resource utilization shows efficiency metrics, identifying over-resourced and under-resourced regions for rebalancing.",
            "**Analysis Insight:** This temporal analysis identifies seasonal patterns in enrollment, enabling dynamic resource allocation during peak and off-peak periods.",
            "**Analysis Insight:** District-level demand mapping highlights underserved areas requiring new enrollment centers or mobile units.",
            "**Analysis Insight:** The capacity utilization chart shows how effectively current resources are being used, identifying optimization opportunities.",
            "**Analysis Insight:** Geographic coverage analysis reveals accessibility gaps, guiding strategic placement of new enrollment facilities.",
            "**Analysis Insight:** This efficiency comparison across regions provides benchmarks for improving operational performance in lagging areas.",
            "**Analysis Insight:** Enrollment rate per capita shows which states are successfully reaching their target populations versus those needing intervention.",
            "**Analysis Insight:** Resource allocation recommendations based on population density and current coverage help optimize budget distribution."
        ]
    },
    
    "fraud_detection_analysis.ipynb": {
        "descriptions": [
            "**Analysis Insight:** Anomaly detection patterns reveal unusual enrollment spikes that may indicate fraudulent activity or data entry errors.",
            "**Analysis Insight:** Geographic distribution of suspicious patterns helps target fraud investigation efforts to high-risk regions.",
            "**Analysis Insight:** This temporal analysis identifies time-based fraud patterns, such as unusual activity during specific periods or hours.",
            "**Analysis Insight:** Demographic mismatch analysis flags enrollments with inconsistent age, gender, or location data requiring verification.",
            "**Analysis Insight:** The fraud risk score distribution categorizes enrollments by likelihood of irregularity, prioritizing investigation resources.",
            "**Analysis Insight:** Duplicate detection patterns show potential identity fraud through multiple enrollments with similar biometric data.",
            "**Analysis Insight:** State-wise fraud prevalence comparison reveals regions requiring enhanced security measures and monitoring.",
            "**Analysis Insight:** This network analysis identifies clusters of suspicious enrollments that may indicate organized fraud attempts.",
            "**Analysis Insight:** Behavioral pattern analysis detects unusual operator activity that could signal internal fraud or system manipulation.",
            "**Analysis Insight:** The trend analysis shows whether fraud prevention measures are effectively reducing suspicious activity over time."
        ]
    },
    
    "district_anomaly_detection.ipynb": {
        "descriptions": [
            "**Analysis Insight:** District-level anomaly scores identify localities with unusual enrollment patterns requiring investigation or policy intervention.",
            "**Analysis Insight:** Geographic hotspot mapping visualizes regions with statistically significant deviations from expected enrollment patterns.",
            "**Analysis Insight:** This comparative analysis shows how each district performs relative to state and national averages, highlighting outliers.",
            "**Analysis Insight:** Temporal anomaly detection reveals districts with unusual enrollment volatility or sudden changes in patterns.",
            "**Analysis Insight:** The enrollment ratio analysis identifies districts with disproportionately high or low adoption rates relative to population.",
            "**Analysis Insight:** Multi-dimensional anomaly scoring considers population, geography, and demographics to provide comprehensive outlier detection.",
            "**Analysis Insight:** This clustering analysis groups districts with similar anomaly patterns, enabling targeted policy interventions.",
            "**Analysis Insight:** Contextual analysis compares districts with similar socio-economic profiles to identify meaningful deviations.",
            "**Analysis Insight:** The severity ranking helps prioritize which district anomalies require immediate attention versus routine monitoring.",
            "**Analysis Insight:** Trend comparison shows whether anomalies are persistent issues or temporary fluctuations, guiding intervention strategies."
        ]
    }
}

def add_descriptions_to_notebook(notebook_path, descriptions):
    """Add descriptions after code cells in a notebook"""
    
    # Load notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    new_cells = []
    desc_index = 0
    added_count = 0
    
    for i, cell in enumerate(nb['cells']):
        new_cells.append(cell)
        
        # Add description after code cells (assuming they might have plots)
        if cell['cell_type'] == 'code':
            # Check if the code cell has substantial content (not just imports or comments)
            source = ''.join(cell.get('source', []))
            
            # Skip if it's just imports, comments, or very short code
            if (len(source.strip()) > 50 and 
                desc_index < len(descriptions) and
                not source.strip().startswith('import') and
                not source.strip().startswith('#') and
                not source.strip().startswith('from')):
                
                # Create description cell
                desc_cell = {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [f"\n{descriptions[desc_index]}\n"]
                }
                new_cells.append(desc_cell)
                desc_index += 1
                added_count += 1
    
    # Update notebook
    nb['cells'] = new_cells
    
    # Save with _with_descriptions suffix
    base_name = Path(notebook_path).stem
    output_path = f"{base_name}_with_descriptions.ipynb"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=2, ensure_ascii=False)
    
    return output_path, added_count

def main():
    print("Adding descriptions to all notebooks...\n")
    
    results = []
    
    for notebook_file, config in notebook_descriptions.items():
        if os.path.exists(notebook_file):
            print(f"Processing: {notebook_file}")
            output_file, count = add_descriptions_to_notebook(
                notebook_file, 
                config['descriptions']
            )
            results.append({
                'original': notebook_file,
                'output': output_file,
                'descriptions_added': count
            })
            print(f"   Added {count} descriptions -> {output_file}\n")
        else:
            print(f"   Not found: {notebook_file}\n")
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    for result in results:
        print(f"\n{result['original']}")
        print(f"   - Descriptions added: {result['descriptions_added']}")
        print(f"   - Output file: {result['output']}")
    
    print("\n" + "="*60)
    print("NEXT STEPS:")
    print("="*60)
    print("1. Review each *_with_descriptions.ipynb file")
    print("2. Adjust descriptions as needed")
    print("3. Backup original files")
    print("4. Replace originals with described versions:")
    print("\n   For each notebook, run:")
    print("   Copy-Item '<notebook>_with_descriptions.ipynb' '<notebook>.ipynb' -Force")
    print("\n5. The dashboard will automatically pick up the changes!")

if __name__ == "__main__":
    main()
