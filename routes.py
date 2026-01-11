"""
Flask routes and API endpoints
Handles web requests and responses
"""

from flask import Flask, request, jsonify
from templates import get_index_template


def setup_routes(app, detector):
    """
    Setup all Flask routes for the application
    
    Args:
        app: Flask application instance
        detector: FakeNewsDetector instance
    """
    
    @app.route('/')
    def index():
        """Serve the main web interface"""
        return get_index_template()

    @app.route('/api/analyze', methods=['POST'])
    def analyze():
        """
        Analyze news text for authenticity
        
        Expected JSON body:
            {
                "text": "news content to analyze"
            }
            
        Returns:
            JSON with analysis results
        """
        try:
            data = request.get_json()
            text = data.get('text', '')
            
            if not text or len(text.strip()) < 10:
                return jsonify({
                    'success': False,
                    'error': 'Please provide at least 10 characters of text'
                })
            
            # Get prediction from detector
            result = detector.predict(text)
            
            if 'error' in result:
                return jsonify({
                    'success': False,
                    'error': result['error']
                })
            
            return jsonify({
                'success': True,
                'result': result
            })
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': f'Server error: {str(e)}'
            })

    @app.route('/api/stats')
    def stats():
        """
        Get model statistics
        
        Returns:
            JSON with model accuracy
        """
        return jsonify({
            'accuracy': detector.get_accuracy()
        })

    return app
