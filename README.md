# 🏥 MedLite - AI-Powered Medical Report Summarizer

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![Transformers](https://img.shields.io/badge/Transformers-4.30+-green.svg)](https://huggingface.co/transformers)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Project Overview

**MedLite** is an innovative AI-powered application that transforms complex medical reports into patient-friendly summaries. Using state-of-the-art natural language processing and medical terminology translation, MedLite makes medical information accessible to everyone.

### ✨ Key Features

- **🤖 AI-Powered Summarization**: Uses advanced transformer models (BART/T5) for intelligent text summarization
- **📚 Medical Jargon Translation**: Converts complex medical terms into easy-to-understand language
- **📁 Multiple File Formats**: Supports both PDF and TXT file uploads
- **🏥 Comprehensive Coverage**: Works with reports from all major medical specialties
- **🔍 Key Findings Extraction**: Automatically identifies and highlights important medical findings
- **💾 Export Functionality**: Save summaries for future reference
- **🎨 Beautiful UI**: Modern, responsive Streamlit interface
- **📊 Sample Reports**: 20+ realistic medical reports for testing and demonstration

### 🎯 Supported Medical Specialties

- **Cardiology** - Heart conditions, echocardiograms, stress tests
- **Pulmonology** - Lung conditions, chest X-rays, pulmonary function tests
- **Gastroenterology** - Digestive system, endoscopy, colonoscopy
- **Neurology** - Brain conditions, MRI scans, neurological assessments
- **Endocrinology** - Diabetes, thyroid disorders, hormone conditions
- **Nephrology** - Kidney function, dialysis reports
- **Hematology** - Blood disorders, complete blood counts
- **Radiology** - Imaging studies, CT scans, ultrasounds
- **Obstetrics** - Pregnancy scans, prenatal care
- **Oncology** - Cancer screening, mammograms
- **And many more...**

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- 4GB+ RAM recommended for AI models

### Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd MedLite
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, copy the URL from the terminal

### 🎮 Usage

1. **Upload a Medical Report**
   - Click "Upload Report" in the sidebar
   - Choose a PDF or TXT file containing your medical report
   - Wait for the file to be processed

2. **Generate Summary**
   - Click "🚀 Generate Summary" button
   - Wait for AI processing (may take 30-60 seconds)
   - Review the patient-friendly summary

3. **Save Results**
   - Click "💾 Download Summary" to save the results
   - The summary will be saved in the `outputs/` folder

4. **Explore Sample Reports**
   - Click "Sample Reports" in the sidebar
   - Select from 20+ realistic medical reports
   - Test the AI summarization with different conditions

## 🛠️ Technology Stack

### Backend
- **Python 3.8+** - Core programming language
- **Hugging Face Transformers** - AI model framework
- **PyTorch** - Deep learning backend
- **spaCy** - Natural language processing
- **PDFMiner** - PDF text extraction

### Frontend
- **Streamlit** - Web application framework
- **Custom CSS** - Modern, responsive design
- **Pandas** - Data manipulation and display

### AI Models
- **BART (Bidirectional and Auto-Regressive Transformers)** - Primary summarization model
- **T5 (Text-to-Text Transfer Transformer)** - Fallback model
- **Custom Medical Dictionary** - 100+ medical terms translation

## 📁 Project Structure

```
MedLite/
├── app.py                 # Main Streamlit application
├── summarize.py           # AI summarization engine
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── outputs/              # Generated summaries (auto-created)
└── sample_reports/       # Sample medical reports
    ├── chest_xray.txt
    ├── blood_test.txt
    ├── liver_scan.txt
    ├── heart_echo.txt
    ├── brain_mri.txt
    ├── kidney_function.txt
    ├── thyroid_test.txt
    ├── diabetes_report.txt
    ├── covid_test.txt
    ├── pregnancy_scan.txt
    ├── bone_density.txt
    ├── lung_function.txt
    ├── cardiac_stress.txt
    ├── endoscopy.txt
    ├── colonoscopy.txt
    ├── mammogram.txt
    ├── ultrasound.txt
    ├── ct_scan.txt
    ├── allergy_test.txt
    └── vitamin_panel.txt
```

## 🔧 Configuration

### Model Selection
The application automatically selects the best available model:
1. **BART Large CNN** (preferred) - Best for summarization
2. **T5 Small** (fallback) - Lighter alternative

### Medical Terms Dictionary
The system includes 100+ medical terms with patient-friendly translations:
- Cardiovascular: "myocardial infarction" → "heart attack"
- Respiratory: "pneumonia" → "lung infection"
- Gastrointestinal: "hepatitis" → "liver inflammation"
- And many more...

## 📊 Sample Reports

The project includes 20+ realistic medical reports covering:

| Report Type | Condition | File |
|-------------|-----------|------|
| Chest X-Ray | Pneumonia | `chest_xray.txt` |
| Blood Test | Diabetes & Anemia | `blood_test.txt` |
| Liver Scan | Fatty Liver | `liver_scan.txt` |
| Heart Echo | Hypertension | `heart_echo.txt` |
| Brain MRI | Cognitive Changes | `brain_mri.txt` |
| Kidney Function | Chronic Kidney Disease | `kidney_function.txt` |
| Thyroid Test | Hypothyroidism | `thyroid_test.txt` |
| Diabetes Report | Poor Glycemic Control | `diabetes_report.txt` |
| COVID Test | COVID-19 Infection | `covid_test.txt` |
| Pregnancy Scan | 20-Week Anatomy | `pregnancy_scan.txt` |
| Bone Density | Osteoporosis | `bone_density.txt` |
| Lung Function | COPD | `lung_function.txt` |
| Cardiac Stress | Exercise Test | `cardiac_stress.txt` |
| Endoscopy | Gastritis | `endoscopy.txt` |
| Colonoscopy | Polyp Removal | `colonoscopy.txt` |
| Mammogram | Breast Screening | `mammogram.txt` |
| Ultrasound | Gallstones | `ultrasound.txt` |
| CT Scan | Lung Mass | `ct_scan.txt` |
| Allergy Test | Multiple Allergies | `allergy_test.txt` |
| Vitamin Panel | Multiple Deficiencies | `vitamin_panel.txt` |

## 🎯 Use Cases

### For Patients
- Understand complex medical reports
- Get clear explanations of test results
- Prepare questions for healthcare providers
- Maintain personal health records

### For Healthcare Providers
- Generate patient-friendly summaries
- Improve patient communication
- Save time on report explanations
- Enhance patient education

### For Medical Students
- Learn medical terminology
- Practice report interpretation
- Understand patient communication
- Study various medical conditions

## ⚠️ Important Disclaimers

### Medical Disclaimer
**🚨 CRITICAL: MedLite is for educational and informational purposes only.**

- ❌ **NOT a substitute for professional medical advice**
- ❌ **NOT for self-diagnosis or treatment decisions**
- ❌ **NOT a replacement for healthcare provider consultation**
- ✅ **Always consult qualified healthcare professionals**
- ✅ **Use results to enhance, not replace, medical discussions**

### Technical Limitations
- AI models may not be 100% accurate
- Results should be verified by medical professionals
- Complex medical cases may require human interpretation
- Model performance depends on input quality

### Privacy and Security
- Reports are processed locally on your machine
- No data is sent to external servers
- Generated summaries are saved locally
- Always follow HIPAA guidelines for medical data

## 🔧 Troubleshooting

### Common Issues

**1. Model Loading Errors**
```bash
# Solution: Install PyTorch with CUDA support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**2. Memory Issues**
```bash
# Solution: Use CPU-only models
# The app automatically falls back to lighter models
```

**3. PDF Processing Errors**
```bash
# Solution: Ensure PDF is not password-protected
# Try converting to TXT format first
```

**4. Streamlit Not Starting**
```bash
# Solution: Check if port 8501 is available
streamlit run app.py --server.port 8502
```

### Performance Optimization

- **GPU Acceleration**: Install CUDA-compatible PyTorch for faster processing
- **Memory Management**: Close other applications to free up RAM
- **Model Caching**: Models are cached after first use for faster subsequent runs

## 🤝 Contributing

We welcome contributions to improve MedLite! Here's how you can help:

### Areas for Improvement
- Additional medical terminology translations
- Support for more file formats
- Enhanced AI model accuracy
- New medical specialties
- UI/UX improvements

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hugging Face** for providing excellent transformer models
- **Streamlit** for the amazing web framework
- **Medical professionals** who provided feedback and validation
- **Open source community** for various libraries and tools

## 📞 Support

### Getting Help
- Check the troubleshooting section above
- Review the sample reports for examples
- Test with different file formats
- Ensure all dependencies are installed

### Reporting Issues
- Describe the problem clearly
- Include error messages
- Specify your system configuration
- Provide sample files if possible

---

## 🚀 Ready to Get Started?

1. **Install the dependencies**: `pip install -r requirements.txt`
2. **Run the application**: `streamlit run app.py`
3. **Upload a medical report** or try the sample reports
4. **Generate your first AI summary**!

**Remember**: Always consult with healthcare professionals for medical decisions. MedLite is a tool to help understand medical reports, not to replace professional medical advice.

---

*Made with ❤️ for better healthcare communication*
