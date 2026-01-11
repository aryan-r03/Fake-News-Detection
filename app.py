"""
Fake News Detector - Main Application
Entry point for the Flask web application
"""

from flask import Flask
from model import FakeNewsDetector
from data_loader import DataLoader
from routes import setup_routes
from config import SERVER_CONFIG, DATASET_CONFIG


def create_app():
    """
    Create and configure the Flask application
    
    Returns:
        Configured Flask app instance
    """
    app = Flask(__name__)
    
    # Initialize the detector
    detector = FakeNewsDetector()
    
    # Load and train the model
    print("\n" + "="*60)
    print("🚀 FAKE NEWS DETECTOR - INITIALIZATION")
    print("="*60)
    print("\n📊 Dataset Requirements:")
    print("   - CSV file name: 'news.csv' (or custom path)")
    print("   - Text column: text/title/content/article/headline")
    print("   - Label column: label/class/fake/target")
    print("   - Labels: 0=Real News, 1=Fake News (or False/True)")
    
    # Load dataset
    df = DataLoader.load_dataset_from_csv(DATASET_CONFIG['default_csv'])
    
    # Train model
    detector.train(df)
    
    # Setup routes
    setup_routes(app, detector)
    
    return app


if __name__ == '__main__':
    print("\n🌐 Server starting on: http://127.0.0.1:{port}".format(
        port=SERVER_CONFIG['port']
    ))
    print("\n💡 Note: If 'news.csv' not found, will use sample data")
    print("="*60 + "\n")
    
    app = create_app()
    app.run(
        debug=SERVER_CONFIG['debug'],
        port=SERVER_CONFIG['port'],
        host=SERVER_CONFIG['host']
    )
