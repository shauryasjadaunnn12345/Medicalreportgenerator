from transformers import pipeline

# Load a Hugging Face medical AI model
medical_ai = pipeline("text-classification", model="medicalai/ClinicalBERT")

def diagnose(symptoms):
    """Call Hugging Face model for diagnosis"""
    try:
        response = medical_ai(symptoms)
        return response[0]["label"] if response else "No diagnosis available"
    except Exception as e:
        return f"Error: {str(e)}"

