"""
Configuration file for Fake News Detection system
Contains all constants and model parameters
"""

# Model Parameters
MODEL_CONFIG = {
    'n_estimators': 200,
    'max_depth': 20,
    'random_state': 42,
    'n_jobs': -1
}

# Vectorizer Parameters
VECTORIZER_CONFIG = {
    'stop_words': 'english',
    'max_features': 5000,
    'ngram_range': (1, 3),
    'max_df': 0.7
}

# Dataset Configuration
DATASET_CONFIG = {
    'default_csv': 'news.csv',
    'test_size': 0.2,
    'min_text_length': 5
}

# Text Column Keywords
TEXT_COLUMN_KEYWORDS = ['text', 'title', 'content', 'news', 'article', 'headline', 'statement']

# Label Column Keywords
LABEL_COLUMN_KEYWORDS = ['label', 'class', 'fake', 'target', 'category', 'type']

# Server Configuration
SERVER_CONFIG = {
    'host': '0.0.0.0',
    'port': 5000,
    'debug': True
}

# Confidence Thresholds
CONFIDENCE_THRESHOLDS = {
    'very_high': 85,
    'high': 70,
    'moderate': 55
}
