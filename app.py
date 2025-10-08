"""
MedLite - AI-Powered Medical Report Summarizer
Streamlit Web Application

A user-friendly interface for uploading medical reports and generating
patient-friendly summaries using AI.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import os
import io
try:
    from pdfminer.high_level import extract_text
except ImportError:
    def extract_text(pdf_file):
        return "PDF processing not available. Please convert to TXT format."
try:
    from summarize import summarize_report
except ImportError:
    from summarize_simple import summarize_report
import warnings
warnings.filterwarnings("ignore")

# Page configuration
st.set_page_config(
    page_title="MedLite - AI Medical Report Summarizer",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #A23B72;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        margin: 1rem 0;
    }
    .warning-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        margin: 1rem 0;
    }
    .stButton > button {
        background-color: #2E86AB;
        color: white;
        border-radius: 0.5rem;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #1e5f7a;
    }
</style>
""", unsafe_allow_html=True)

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF file."""
    try:
        text = extract_text(pdf_file)
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {str(e)}")
        return None

def save_summary_to_file(summary_data, filename):
    """Save summary to output file."""
    try:
        os.makedirs("outputs", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"outputs/summary_{timestamp}_{filename}.txt"
        
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write("MEDLITE - AI-POWERED MEDICAL REPORT SUMMARY\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Original file: {filename}\n\n")
            f.write("PATIENT-FRIENDLY SUMMARY:\n")
            f.write("-" * 30 + "\n")
            f.write(summary_data['patient_friendly'] + "\n\n")
            f.write("KEY FINDINGS:\n")
            f.write("-" * 15 + "\n")
            for i, finding in enumerate(summary_data['key_findings'], 1):
                f.write(f"{i}. {finding}\n")
            f.write("\nTECHNICAL SUMMARY:\n")
            f.write("-" * 20 + "\n")
            f.write(summary_data['summary'])
        
        return output_filename
    except Exception as e:
        st.error(f"Error saving file: {str(e)}")
        return None

def main():
    """Main Streamlit application."""
    
    # Header
    st.markdown('<h1 class="main-header">🏥 MedLite</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #A23B72;">AI-Powered Medical Report Summarizer</h2>', unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("📋 Navigation")
    page = st.sidebar.selectbox("Choose a page:", ["Upload Report", "Sample Reports", "About"])
    
    if page == "Upload Report":
        upload_page()
    elif page == "Sample Reports":
        sample_reports_page()
    else:
        about_page()

def upload_page():
    """Main upload and processing page."""
    
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("""
    **Welcome to MedLite!** 
    
    Upload your medical report (PDF or TXT) and get an AI-generated, patient-friendly summary.
    Our AI will translate complex medical jargon into easy-to-understand language.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # File upload section
    st.markdown('<div class="sub-header">📁 Upload Medical Report</div>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Choose a medical report file",
        type=['pdf', 'txt'],
        help="Upload a PDF or TXT file containing your medical report"
    )
    
    if uploaded_file is not None:
        # Display file information
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        st.info(f"📊 File size: {uploaded_file.size} bytes")
        
        # Extract text based on file type
        if uploaded_file.type == "application/pdf":
            with st.spinner("Extracting text from PDF..."):
                text_content = extract_text_from_pdf(uploaded_file)
        else:  # TXT file
            text_content = str(uploaded_file.read(), "utf-8")
        
        if text_content:
            # Display original report
            with st.expander("📄 View Original Report", expanded=False):
                st.text_area("Original Report Content:", text_content, height=300)
            
            # Processing section
            st.markdown('<div class="sub-header">🤖 AI Processing</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            
            with col1:
                if st.button("🚀 Generate Summary", type="primary"):
                    with st.spinner("AI is analyzing your medical report..."):
                        # Generate summary
                        summary_result = summarize_report(text_content)
                        
                        # Display results
                        st.markdown('<div class="success-box">', unsafe_allow_html=True)
                        st.markdown("### ✅ Summary Generated Successfully!")
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        # Patient-friendly summary
                        st.markdown("### 👤 Patient-Friendly Summary")
                        st.markdown('<div class="info-box">', unsafe_allow_html=True)
                        st.write(summary_result['patient_friendly'])
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                        # Key findings
                        if summary_result['key_findings']:
                            st.markdown("### 🔍 Key Findings")
                            for i, finding in enumerate(summary_result['key_findings'], 1):
                                st.write(f"**{i}.** {finding}")
                        
                        # Technical summary (collapsible)
                        with st.expander("🔬 Technical Summary (For Healthcare Providers)"):
                            st.write(summary_result['summary'])
                        
                        # Save functionality
                        st.markdown("### 💾 Save Summary")
                        if st.button("💾 Download Summary"):
                            output_file = save_summary_to_file(summary_result, uploaded_file.name)
                            if output_file:
                                st.success(f"✅ Summary saved to: {output_file}")
                                
                                # Provide download link
                                with open(output_file, 'rb') as f:
                                    st.download_button(
                                        label="📥 Download Summary File",
                                        data=f.read(),
                                        file_name=f"summary_{uploaded_file.name}.txt",
                                        mime="text/plain"
                                    )
            
            with col2:
                st.markdown("### 📊 Report Statistics")
                word_count = len(text_content.split())
                char_count = len(text_content)
                st.metric("Word Count", word_count)
                st.metric("Character Count", char_count)
                st.metric("Estimated Reading Time", f"{word_count // 200 + 1} minutes")

def sample_reports_page():
    """Page showing sample medical reports."""
    
    st.markdown('<div class="sub-header">📋 Sample Medical Reports</div>', unsafe_allow_html=True)
    
    st.markdown("""
    Explore our collection of sample medical reports covering various conditions.
    Click on any report to see how MedLite processes different types of medical documents.
    """)
    
    # Sample reports list
    sample_reports = [
        "chest_xray.txt", "blood_test.txt", "liver_scan.txt", "heart_echo.txt",
        "brain_mri.txt", "kidney_function.txt", "thyroid_test.txt", "diabetes_report.txt",
        "covid_test.txt", "pregnancy_scan.txt", "bone_density.txt", "lung_function.txt",
        "cardiac_stress.txt", "endoscopy.txt", "colonoscopy.txt", "mammogram.txt",
        "ultrasound.txt", "ct_scan.txt", "allergy_test.txt", "vitamin_panel.txt"
    ]
    
    selected_report = st.selectbox("Select a sample report:", sample_reports)
    
    if st.button("📖 Load Sample Report"):
        sample_path = f"sample_reports/{selected_report}"
        if os.path.exists(sample_path):
            with open(sample_path, 'r', encoding='utf-8') as f:
                sample_content = f.read()
            
            st.markdown("### 📄 Sample Report Content")
            st.text_area("Report:", sample_content, height=200)
            
            if st.button("🤖 Generate Summary for Sample"):
                with st.spinner("Processing sample report..."):
                    summary_result = summarize_report(sample_content)
                    
                    st.markdown("### 👤 Patient-Friendly Summary")
                    st.markdown('<div class="info-box">', unsafe_allow_html=True)
                    st.write(summary_result['patient_friendly'])
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    if summary_result['key_findings']:
                        st.markdown("### 🔍 Key Findings")
                        for i, finding in enumerate(summary_result['key_findings'], 1):
                            st.write(f"**{i}.** {finding}")
        else:
            st.warning("Sample report file not found. Please ensure the sample_reports directory contains the files.")

def about_page():
    """About page with project information."""
    
    st.markdown('<div class="sub-header">ℹ️ About MedLite</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ## 🏥 MedLite - AI-Powered Medical Report Summarizer
    
    MedLite is an innovative AI application designed to make medical reports more accessible 
    to patients by translating complex medical jargon into easy-to-understand language.
    
    ### ✨ Key Features
    
    - **AI-Powered Summarization**: Uses state-of-the-art transformer models (BART/T5)
    - **Medical Jargon Translation**: Converts complex terms to patient-friendly language
    - **Multiple File Formats**: Supports PDF and TXT files
    - **Comprehensive Coverage**: Works with reports from all major medical specialties
    - **Key Findings Extraction**: Identifies and highlights important medical findings
    - **Export Functionality**: Save summaries for future reference
    
    ### 🧠 Technology Stack
    
    - **Frontend**: Streamlit for user-friendly web interface
    - **AI Models**: Hugging Face Transformers (BART, T5)
    - **Text Processing**: spaCy, PDFMiner, FuzzyWuzzy
    - **Backend**: Python 3.8+
    
    ### 🎯 Supported Medical Specialties
    
    - Cardiology (Heart conditions)
    - Pulmonology (Lung conditions)
    - Gastroenterology (Digestive system)
    - Neurology (Brain and nervous system)
    - Endocrinology (Hormone disorders)
    - Nephrology (Kidney conditions)
    - Hematology (Blood disorders)
    - Radiology (Imaging studies)
    - And many more...
    
    ### ⚠️ Important Disclaimer
    
    **MedLite is for educational and informational purposes only.**
    
    - This tool is NOT a substitute for professional medical advice
    - Always consult with qualified healthcare providers for medical decisions
    - The AI-generated summaries should not be used for self-diagnosis
    - Results may not be 100% accurate and should be verified by medical professionals
    
    ### 🚀 Getting Started
    
    1. Upload your medical report (PDF or TXT)
    2. Click "Generate Summary" to process with AI
    3. Review the patient-friendly summary
    4. Save the summary for your records
    5. Always discuss results with your healthcare provider
    
    ### 📞 Support
    
    For technical support or questions about MedLite, please contact your healthcare provider
    or IT support team.
    """)
    
    st.markdown('<div class="warning-box">', unsafe_allow_html=True)
    st.markdown("""
    **⚠️ Medical Disclaimer**: This application is designed to assist in understanding medical reports 
    but should never replace professional medical consultation. Always seek advice from qualified 
    healthcare professionals for medical decisions.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()