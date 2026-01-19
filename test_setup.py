#!/usr/bin/env python3
"""Test script to verify UIDAI dashboard components"""

import os
import sys

def check_file_exists(filepath, description):
    """Check if file exists"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description} NOT FOUND: {filepath}")
        return False

def main():
    print("=" * 60)
    print("UIDAI Dashboard Component Verification")
    print("=" * 60)
    
    all_good = True
    
    # Check data files
    print("\n📊 Data Files:")
    all_good &= check_file_exists("data/biometric.csv", "Biometric data")
    all_good &= check_file_exists("data/demographic.csv", "Demographic data")
    all_good &= check_file_exists("data/enrollment.csv", "Enrollment data")
    
    # Check notebooks
    print("\n📓 Jupyter Notebooks:")
    all_good &= check_file_exists("biometric_failure_analysis.ipynb", "Biometric analysis")
    all_good &= check_file_exists("Resource_Allocation_Optimization.ipynb", "Resource optimization")
    all_good &= check_file_exists("fraud_detection_analysis.ipynb", "Fraud detection")
    all_good &= check_file_exists("Rural_Urban_Adoption_Analysis.ipynb", "Rural/Urban analysis")
    all_good &= check_file_exists("district_anomaly_detection.ipynb", "District hotspots")
    
    # Check dashboard files
    print("\n🖥️ Dashboard Files:")
    all_good &= check_file_exists("enhanced_streamlit_dashboard.py", "Main dashboard")
    all_good &= check_file_exists("biometric_analysis_enhanced.py", "Enhanced analysis")
    
    # Check documentation
    print("\n📚 Documentation:")
    all_good &= check_file_exists("README.md", "README")
    all_good &= check_file_exists("IMPLEMENTATION_SUMMARY.md", "Implementation summary")
    
    # Test imports
    print("\n🔧 Testing Imports:")
    try:
        import streamlit
        print("✅ Streamlit installed")
    except ImportError:
        print("❌ Streamlit NOT installed - run: pip install streamlit")
        all_good = False
    
    try:
        import pandas
        print("✅ Pandas installed")
    except ImportError:
        print("❌ Pandas NOT installed - run: pip install pandas")
        all_good = False
    
    try:
        import plotly
        print("✅ Plotly installed")
    except ImportError:
        print("❌ Plotly NOT installed - run: pip install plotly")
        all_good = False
    
    # Test biometric analyzer
    print("\n🧪 Testing Biometric Analyzer:")
    try:
        from biometric_analysis_enhanced import BiometricAnalyzer
        analyzer = BiometricAnalyzer()
        summary = analyzer.get_failure_summary()
        print(f"✅ Biometric analyzer working - {summary['total_records']} records loaded")
    except Exception as e:
        print(f"❌ Biometric analyzer error: {e}")
        all_good = False
    
    # Final status
    print("\n" + "=" * 60)
    if all_good:
        print("✅ ALL CHECKS PASSED!")
        print("\n🚀 Ready to run:")
        print("   streamlit run enhanced_streamlit_dashboard.py")
    else:
        print("⚠️ SOME CHECKS FAILED - Please review above")
    print("=" * 60)
    
    return 0 if all_good else 1

if __name__ == "__main__":
    sys.exit(main())
