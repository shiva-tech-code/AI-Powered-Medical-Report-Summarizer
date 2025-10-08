"""
MedLite - Simplified Medical Report Summarizer
Fallback version without heavy AI dependencies
"""

import re
from typing import Dict, List

class SimpleMedicalReportSummarizer:
    """
    Simplified medical report summarizer that uses rule-based text processing
    and medical jargon translation without requiring heavy AI models.
    """
    
    def __init__(self):
        """Initialize the simple summarizer."""
        print("Using simplified medical report summarizer")
        
        # Medical jargon to patient-friendly terms dictionary
        self.medical_terms = {
            # Cardiovascular terms
            "myocardial infarction": "heart attack",
            "coronary artery disease": "heart disease",
            "hypertension": "high blood pressure",
            "hypotension": "low blood pressure",
            "tachycardia": "fast heart rate",
            "bradycardia": "slow heart rate",
            "arrhythmia": "irregular heartbeat",
            "angina": "chest pain",
            "atherosclerosis": "hardening of arteries",
            "cardiomyopathy": "heart muscle disease",
            
            # Respiratory terms
            "pneumonia": "lung infection",
            "bronchitis": "inflammation of airways",
            "asthma": "breathing condition",
            "COPD": "chronic lung disease",
            "dyspnea": "shortness of breath",
            "tachypnea": "rapid breathing",
            "hypoxia": "low oxygen levels",
            "pulmonary edema": "fluid in lungs",
            
            # Gastrointestinal terms
            "gastroenteritis": "stomach flu",
            "hepatitis": "liver inflammation",
            "cirrhosis": "liver scarring",
            "cholecystitis": "gallbladder inflammation",
            "pancreatitis": "pancreas inflammation",
            "gastritis": "stomach inflammation",
            "ulcer": "sore in stomach/intestine",
            "GERD": "acid reflux",
            
            # Neurological terms
            "cerebrovascular accident": "stroke",
            "transient ischemic attack": "mini-stroke",
            "migraine": "severe headache",
            "epilepsy": "seizure disorder",
            "dementia": "memory loss condition",
            "Alzheimer's disease": "memory disease",
            "Parkinson's disease": "movement disorder",
            "multiple sclerosis": "nervous system disease",
            
            # Endocrine terms
            "diabetes mellitus": "diabetes",
            "hyperglycemia": "high blood sugar",
            "hypoglycemia": "low blood sugar",
            "hyperthyroidism": "overactive thyroid",
            "hypothyroidism": "underactive thyroid",
            "diabetic ketoacidosis": "diabetes complication",
            
            # Kidney terms
            "acute kidney injury": "sudden kidney damage",
            "chronic kidney disease": "long-term kidney disease",
            "nephritis": "kidney inflammation",
            "renal failure": "kidney failure",
            "dialysis": "kidney treatment",
            
            # Blood terms
            "anemia": "low red blood cells",
            "leukemia": "blood cancer",
            "thrombosis": "blood clot",
            "hemorrhage": "bleeding",
            "coagulopathy": "bleeding disorder",
            
            # General medical terms
            "malignancy": "cancer",
            "benign": "non-cancerous",
            "acute": "sudden onset",
            "chronic": "long-term",
            "inflammation": "swelling",
            "infection": "germ invasion",
            "fracture": "broken bone",
            "contusion": "bruise",
            "laceration": "cut",
            "abrasion": "scrape",
            "edema": "swelling",
            "fever": "high temperature",
            "nausea": "feeling sick",
            "vomiting": "throwing up",
            "diarrhea": "loose stools",
            "constipation": "hard stools",
            "fatigue": "tiredness",
            "malaise": "general feeling of illness"
        }
    
    def clean_text(self, text: str) -> str:
        """Clean and preprocess the medical report text."""
        # Remove extra whitespace and normalize
        text = re.sub(r'\s+', ' ', text.strip())
        
        # Remove common report headers/footers
        text = re.sub(r'^(Patient Name|DOB|Date|Report|Physician|Doctor).*?\n', '', text, flags=re.MULTILINE | re.IGNORECASE)
        
        # Remove excessive punctuation
        text = re.sub(r'[^\w\s.,!?;:-]', '', text)
        
        # Remove numbers that are likely IDs or codes
        text = re.sub(r'\b\d{6,}\b', '', text)
        
        return text
    
    def translate_medical_jargon(self, text: str) -> str:
        """Replace medical jargon with patient-friendly terms."""
        text_lower = text.lower()
        
        for medical_term, patient_term in self.medical_terms.items():
            # Case-insensitive replacement
            pattern = re.compile(re.escape(medical_term), re.IGNORECASE)
            text = pattern.sub(patient_term, text)
        
        return text
    
    def extract_key_findings(self, text: str) -> List[str]:
        """Extract key medical findings from the report."""
        # Common patterns for medical findings
        finding_patterns = [
            r'(?:finding|result|shows?|reveals?|indicates?|demonstrates?)[:\s]+([^.!?]+)',
            r'(?:diagnosis|impression)[:\s]+([^.!?]+)',
            r'(?:abnormal|normal|positive|negative|elevated|reduced)[:\s]+([^.!?]+)',
        ]
        
        findings = []
        for pattern in finding_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            findings.extend([match.strip() for match in matches if len(match.strip()) > 10])
        
        return findings[:5]  # Return top 5 findings
    
    def create_simple_summary(self, text: str) -> str:
        """Create a simple summary using rule-based extraction."""
        # Extract key sections
        sections = []
        
        # Look for common medical report sections
        if "impression" in text.lower():
            impression_match = re.search(r'impression[:\s]+([^.!?]+)', text, re.IGNORECASE)
            if impression_match:
                sections.append(f"Main findings: {impression_match.group(1).strip()}")
        
        if "diagnosis" in text.lower():
            diagnosis_match = re.search(r'diagnosis[:\s]+([^.!?]+)', text, re.IGNORECASE)
            if diagnosis_match:
                sections.append(f"Diagnosis: {diagnosis_match.group(1).strip()}")
        
        # Extract abnormal values
        abnormal_matches = re.findall(r'([^.!?]*(?:elevated|low|high|abnormal|positive|negative)[^.!?]*)', text, re.IGNORECASE)
        if abnormal_matches:
            sections.append(f"Key results: {'; '.join(abnormal_matches[:3])}")
        
        # If no specific sections found, create a general summary
        if not sections:
            # Take first few sentences
            sentences = re.split(r'[.!?]+', text)
            sections = [s.strip() for s in sentences[:3] if len(s.strip()) > 20]
        
        return ". ".join(sections) + "."
    
    def summarize_report(self, text: str) -> Dict[str, str]:
        """Generate a patient-friendly summary of the medical report."""
        try:
            # Clean the input text
            cleaned_text = self.clean_text(text)
            
            if len(cleaned_text) < 50:
                return {
                    "summary": "The report is too short to generate a meaningful summary.",
                    "key_findings": ["Report length insufficient for analysis"],
                    "patient_friendly": "Please provide a longer medical report for analysis."
                }
            
            # Create simple summary
            raw_summary = self.create_simple_summary(cleaned_text)
            
            # Translate medical jargon to patient-friendly terms
            patient_friendly_summary = self.translate_medical_jargon(raw_summary)
            
            # Extract key findings
            key_findings = self.extract_key_findings(cleaned_text)
            patient_friendly_findings = [self.translate_medical_jargon(finding) for finding in key_findings]
            
            return {
                "summary": raw_summary,
                "patient_friendly": patient_friendly_summary,
                "key_findings": patient_friendly_findings
            }
            
        except Exception as e:
            return {
                "summary": f"Error generating summary: {str(e)}",
                "patient_friendly": "Unable to process the medical report. Please try again.",
                "key_findings": ["Processing error occurred"]
            }

def summarize_report(text: str) -> Dict[str, str]:
    """
    Main function to summarize a medical report using simplified processing.
    
    Args:
        text (str): Medical report text
        
    Returns:
        Dict[str, str]: Summary results
    """
    summarizer = SimpleMedicalReportSummarizer()
    return summarizer.summarize_report(text)

# Example usage
if __name__ == "__main__":
    # Test with sample text
    sample_text = """
    PATIENT: John Doe
    DOB: 01/01/1980
    DATE: 12/15/2023
    
    CHEST X-RAY REPORT
    
    CLINICAL HISTORY: Patient presents with acute onset of dyspnea and chest pain.
    
    FINDINGS:
    The chest X-ray demonstrates bilateral lower lobe consolidation consistent with pneumonia.
    The cardiac silhouette is within normal limits. No evidence of pneumothorax or pleural effusion.
    The bony structures are unremarkable.
    
    IMPRESSION:
    1. Bilateral lower lobe pneumonia
    2. No acute cardiopulmonary abnormalities
    3. Recommend follow-up chest X-ray in 2 weeks
    
    Dr. Smith, Radiologist
    """
    
    result = summarize_report(sample_text)
    print("Original Summary:", result["summary"])
    print("\nPatient-Friendly Summary:", result["patient_friendly"])
    print("\nKey Findings:", result["key_findings"])
