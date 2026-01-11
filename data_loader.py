"""
Data loading and dataset creation utilities
Handles CSV loading, column detection, and fallback dataset creation
"""

import pandas as pd
import os
from config import TEXT_COLUMN_KEYWORDS, LABEL_COLUMN_KEYWORDS


class DataLoader:
    """Handles loading and preparing datasets for training"""
    
    @staticmethod
    def load_dataset_from_csv(csv_path='news.csv'):
        """
        Load dataset from CSV file with automatic column detection
        
        Args:
            csv_path: Path to the CSV file
            
        Returns:
            pandas.DataFrame with 'text' and 'label' columns
        """
        try:
            if os.path.exists(csv_path):
                print(f"Loading dataset from {csv_path}...")
                df = pd.read_csv(csv_path)
                print(f"✓ Loaded {len(df)} rows")

                text_col = DataLoader._find_column(df, TEXT_COLUMN_KEYWORDS)
                label_col = DataLoader._find_column(df, LABEL_COLUMN_KEYWORDS)

                if text_col and label_col:
                    print(f"✓ Found columns - Text: '{text_col}', Label: '{label_col}'")
                    df = df[[text_col, label_col]].copy()
                    df.columns = ['text', 'label']

                    unique_labels = df['label'].unique()
                    print(f"✓ Unique labels found: {unique_labels}")

                    if len(unique_labels) == 2:
                        sorted_labels = sorted(unique_labels)
                        label_map = {sorted_labels[0]: 0, sorted_labels[1]: 1}
                        df['label'] = df['label'].map(label_map)
                        print(f"✓ Mapped labels: {sorted_labels[0]}→0 (Real), {sorted_labels[1]}→1 (Fake)")

                    return df
                else:
                    print(f"✗ Could not identify text/label columns")
                    print(f"   Available columns: {df.columns.tolist()}")
                    return DataLoader.create_fallback_dataset()
            else:
                print(f"✗ File '{csv_path}' not found")
                return DataLoader.create_fallback_dataset()

        except Exception as e:
            print(f"✗ Error loading CSV: {e}")
            return DataLoader.create_fallback_dataset()

    @staticmethod
    def _find_column(df, keywords):
        """
        Find column matching keywords
        
        Args:
            df: pandas.DataFrame
            keywords: List of keywords to search for
            
        Returns:
            Column name if found, None otherwise
        """
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in keywords):
                return col
        return None

    @staticmethod
    def create_fallback_dataset():
        """
        Create a fallback sample dataset for testing
        
        Returns:
            pandas.DataFrame with sample fake and real news
        """
        print("\n⚠️  Creating fallback sample dataset...")
        print("   For better accuracy, provide 'news.csv' with columns:")
        print("   - Text column: 'text', 'title', 'content', etc.")
        print("   - Label column: 'label', 'class', 'fake', etc.")
        print("   - Labels should be 0/1 or False/True (0=Real, 1=Fake)\n")

        fake_news = [
            "BREAKING: Scientists discover miracle cure doctors don't want you to know",
            "SHOCKING: Government admits aliens exist living among us for years",
            "You won't believe what celebrity did doctors hate this weird trick",
            "URGENT: New world order plan exposed they don't want you knowing",
            "Miracle weight loss secret pharmaceutical companies hiding from public",
            "BREAKING NEWS: President caught in massive scandal impeachment imminent",
            "Scientists SHOCKED by discovery everything we knew was wrong",
            "Simple trick will make you rich overnight billionaires hate it",
            "ALERT: Dangerous vaccine side effects hidden by mainstream media",
            "Celebrity dies in suspicious circumstances truth finally revealed"
        ] * 50

        real_news = [
            "City council approves new infrastructure development plan for downtown",
            "University researchers publish findings on renewable energy efficiency",
            "Stock market closes with moderate gains following Federal Reserve decision",
            "Technology company reports quarterly earnings meeting analyst expectations",
            "State legislature debates new education funding bill in committee",
            "International summit concludes with joint statement on climate cooperation",
            "Healthcare providers report steady increase in vaccination rates",
            "Transportation department announces scheduled highway maintenance project",
            "Scientific journal publishes research on new pharmaceutical treatment",
            "Economic data shows moderate employment growth in manufacturing sector"
        ] * 50

        df = pd.DataFrame({
            'text': fake_news + real_news,
            'label': [1] * len(fake_news) + [0] * len(real_news)
        })

        return df.sample(frac=1, random_state=42).reset_index(drop=True)
