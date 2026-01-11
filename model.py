"""
Fake News Detection Model
Contains the main detector class with training and prediction capabilities
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from text_processor import TextProcessor
from config import MODEL_CONFIG, VECTORIZER_CONFIG, DATASET_CONFIG, CONFIDENCE_THRESHOLDS


class FakeNewsDetector:
    """Main class for fake news detection using Random Forest and TF-IDF"""
    
    def __init__(self):
        """Initialize the detector with model and vectorizer"""
        self.model = RandomForestClassifier(**MODEL_CONFIG)
        self.vectorizer = TfidfVectorizer(**VECTORIZER_CONFIG)
        self.accuracy = 0
        self.text_processor = TextProcessor()

    def train(self, df):
        """
        Train the fake news detection model
        
        Args:
            df: pandas.DataFrame with 'text' and 'label' columns
            
        Returns:
            Model accuracy score
        """
        print("\n" + "="*60)
        print("TRAINING FAKE NEWS DETECTION MODEL")
        print("="*60)

        # Clean data
        df = df.dropna()
        df['text'] = df['text'].apply(self.text_processor.preprocess_text)
        df = df[df['text'].str.len() > DATASET_CONFIG['min_text_length']]

        X = df['text']
        y = df['label']

        print(f"\nDataset: {len(df)} samples")
        print(f"Fake: {(y==1).sum()} ({(y==1).sum()/len(y)*100:.1f}%)")
        print(f"Real: {(y==0).sum()} ({(y==0).sum()/len(y)*100:.1f}%)")

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, 
            test_size=DATASET_CONFIG['test_size'], 
            random_state=MODEL_CONFIG['random_state'], 
            stratify=y
        )

        # Vectorize text
        print(f"\nVectorizing text...")
        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)

        # Train model
        print("Training Random Forest...")
        self.model.fit(X_train_vec, y_train)

        # Evaluate
        y_pred = self.model.predict(X_test_vec)
        self.accuracy = accuracy_score(y_test, y_pred)

        print(f"\n{'='*60}")
        print(f"MODEL ACCURACY: {self.accuracy*100:.2f}%")
        print("="*60)

        return self.accuracy

    def predict(self, text):
        """
        Predict if news text is fake or real
        
        Args:
            text: News text to analyze
            
        Returns:
            Dictionary with prediction results
        """
        try:
            processed = self.text_processor.preprocess_text(text)
            
            if not self.text_processor.is_valid_text(processed):
                return {'error': 'Please provide valid text'}

            # Vectorize and predict
            text_vec = self.vectorizer.transform([processed])
            prediction = self.model.predict(text_vec)[0]
            probs = self.model.predict_proba(text_vec)[0]

            # Calculate metrics
            confidence = max(probs) * 100
            fake_prob = probs[1] * 100
            real_prob = probs[0] * 100

            # Determine credibility level
            if confidence >= CONFIDENCE_THRESHOLDS['very_high']:
                credibility = "Very High Confidence"
            elif confidence >= CONFIDENCE_THRESHOLDS['high']:
                credibility = "High Confidence"
            elif confidence >= CONFIDENCE_THRESHOLDS['moderate']:
                credibility = "Moderate Confidence"
            else:
                credibility = "Low Confidence"

            # Prepare result
            result = {
                'is_fake': bool(prediction == 1),
                'result': 'LIKELY FAKE NEWS ⚠️' if prediction == 1 else 'LIKELY REAL NEWS ✅',
                'confidence': f'{confidence:.1f}',
                'credibility': credibility,
                'fake_probability': f'{fake_prob:.1f}',
                'real_probability': f'{real_prob:.1f}',
                'word_count': len(text.split())
            }

            return result

        except Exception as e:
            return {'error': f'Prediction error: {str(e)}'}

    def get_accuracy(self):
        """
        Get the current model accuracy
        
        Returns:
            Accuracy as percentage string
        """
        return f"{self.accuracy*100:.2f}"
