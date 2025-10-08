#!/usr/bin/env python3
"""
Test script for MedLite - AI-Powered Medical Report Summarizer
"""

import os
import sys

def test_imports():
    """Test if all required modules can be imported."""
    print("Testing imports...")
    
    try:
        import streamlit as st
        print("✅ Streamlit imported successfully")
    except ImportError as e:
        print(f"❌ Streamlit import failed: {e}")
        return False
    
    try:
        from summarize_simple import summarize_report
        print("✅ Simple summarizer imported successfully")
    except ImportError as e:
        print(f"❌ Simple summarizer import failed: {e}")
        return False
    
    return True

def test_summarizer():
    """Test the summarizer with sample text."""
    print("\nTesting summarizer...")
    
    try:
        from summarize_simple import summarize_report
        
        sample_text = """
        PATIENT: John Doe
        DOB: 01/01/1980
        DATE: 12/15/2023
        
        CHEST X-RAY REPORT
        
        CLINICAL HISTORY: Patient presents with acute onset of dyspnea and chest pain.
        
        FINDINGS:
        The chest X-ray demonstrates bilateral lower lobe consolidation consistent with pneumonia.
        The cardiac silhouette is within normal limits. No evidence of pneumothorax or pleural effusion.
        
        IMPRESSION:
        1. Bilateral lower lobe pneumonia
        2. No acute cardiopulmonary abnormalities
        3. Recommend follow-up chest X-ray in 2 weeks
        """
        
        result = summarize_report(sample_text)
        
        print("✅ Summarizer test successful!")
        print(f"📝 Patient-friendly summary: {result['patient_friendly'][:100]}...")
        print(f"🔍 Key findings: {len(result['key_findings'])} findings extracted")
        
        return True
        
    except Exception as e:
        print(f"❌ Summarizer test failed: {e}")
        return False

def test_sample_reports():
    """Test if sample reports exist."""
    print("\nTesting sample reports...")
    
    sample_dir = "sample_reports"
    if not os.path.exists(sample_dir):
        print(f"❌ Sample reports directory not found: {sample_dir}")
        return False
    
    sample_files = os.listdir(sample_dir)
    print(f"✅ Found {len(sample_files)} sample reports")
    
    # Test reading a sample report
    try:
        with open(os.path.join(sample_dir, "chest_xray.txt"), 'r') as f:
            content = f.read()
        print(f"✅ Successfully read sample report (length: {len(content)} characters)")
        return True
    except Exception as e:
        print(f"❌ Failed to read sample report: {e}")
        return False

def main():
    """Run all tests."""
    print("🏥 MedLite - AI-Powered Medical Report Summarizer")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_summarizer,
        test_sample_reports
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! MedLite is ready to run.")
        print("\nTo start the application, run:")
        print("  streamlit run app.py")
        print("\nOr:")
        print("  python3 -m streamlit run app.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
