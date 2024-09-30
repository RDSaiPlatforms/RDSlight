import re

# A collection of utility functions for basic data processing
def clean_text(text):
    """Remove special characters and unnecessary spaces."""
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize_text(text):
    """Tokenizes the text into words."""
    return text.split()

def preprocess_text(text):
    """Apply a series of cleaning and tokenization steps."""
    cleaned_text = clean_text(text)
    tokens = tokenize_text(cleaned_text)
    return tokens

# Example usage
if __name__ == "__main__":
    sample_text = "I'm feeling really excited about my upcoming exams!"
    cleaned = clean_text(sample_text)
    tokens = tokenize_text(cleaned)
    
    print("Cleaned Text:", cleaned)
    print("Tokens:", tokens)