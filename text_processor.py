"""
Text preprocessing utilities
Handles text cleaning and normalization
"""

import re
import warnings

warnings.filterwarnings('ignore')

try:
    import nltk
    nltk.data.find('stopwords')
except:
    import nltk
    nltk.download('stopwords', quiet=True)


class TextProcessor:
    """Handles text preprocessing and cleaning operations"""
    
    @staticmethod
    def preprocess_text(text):
        """
        Clean and preprocess text for analysis
        
        Args:
            text: Raw text string
            
        Returns:
            Cleaned and normalized text string
        """
        if not isinstance(text, str):
            return ""
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text)
        
        # Remove mentions and hashtags
        text = re.sub(r'@\w+|#\w+', '', text)
        
        # Remove special characters, keep only letters, spaces, and periods
        text = re.sub(r'[^a-zA-Z\s\.]', '', text)
        
        # Normalize whitespace
        text = ' '.join(text.split())
        
        return text
    
    @staticmethod
    def is_valid_text(text, min_length=5):
        """
        Check if text is valid for processing
        
        Args:
            text: Text to validate
            min_length: Minimum required length
            
        Returns:
            Boolean indicating validity
        """
        if not text or not isinstance(text, str):
            return False
        return len(text.strip()) >= min_length
