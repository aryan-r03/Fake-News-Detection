"""
HTML templates for the web interface
Contains the complete frontend HTML/CSS/JavaScript
"""

def get_index_template():
    """Return the main index.html template as a string"""
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔍 Fake News Detector - AI-Powered News Verification</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
        }

        .header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }

        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .main-grid {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 30px;
            margin-bottom: 30px;
        }

        .card {
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }

        .section-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #333;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .section-title span {
            font-size: 1.8rem;
        }

        textarea {
            width: 100%;
            min-height: 200px;
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            font-size: 1rem;
            font-family: inherit;
            resize: vertical;
            transition: border-color 0.3s;
        }

        textarea:focus {
            outline: none;
            border-color: #667eea;
        }

        .char-counter {
            text-align: right;
            color: #666;
            font-size: 0.9rem;
            margin-top: 5px;
        }

        .analyze-btn {
            width: 100%;
            padding: 18px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 12px;
            font-size: 1.1rem;
            font-weight: 700;
            cursor: pointer;
            margin-top: 20px;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        .analyze-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        }

        .analyze-btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }

        .loading {
            display: none;
            text-align: center;
            padding: 40px;
        }

        .loading.show {
            display: block;
        }

        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #667eea;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            animation: spin 1s linear infinite;
            margin: 0 auto 20px;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .stats-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 20px;
        }

        .stat-value {
            font-size: 2.5rem;
            font-weight: 900;
            margin-bottom: 5px;
        }

        .stat-label {
            font-size: 1rem;
            opacity: 0.9;
        }

        .info-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 15px;
            border-left: 5px solid #667eea;
        }

        .info-card h3 {
            color: #333;
            margin-bottom: 15px;
            font-size: 1.2rem;
        }

        .info-item {
            padding: 8px 0;
            color: #555;
            font-size: 0.95rem;
        }

        .info-item strong {
            color: #667eea;
        }

        .results-card {
            display: none;
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }

        .results-card.show {
            display: block;
        }

        .results-card.fake {
            border-left: 8px solid #e74c3c;
        }

        .results-card.real {
            border-left: 8px solid #27ae60;
        }

        .result-header {
            display: flex;
            align-items: center;
            gap: 20px;
            margin-bottom: 30px;
        }

        .result-icon {
            font-size: 4rem;
        }

        .result-title h2 {
            font-size: 2rem;
            color: #333;
            margin-bottom: 10px;
        }

        .credibility-badge {
            display: inline-block;
            padding: 5px 15px;
            background: #667eea;
            color: white;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
        }

        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }

        .metric-box {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
        }

        .metric-label {
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 10px;
        }

        .metric-value {
            font-size: 2rem;
            font-weight: 900;
            color: #667eea;
        }

        .sample-buttons {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            margin-bottom: 20px;
        }

        .sample-btn {
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            background: white;
            cursor: pointer;
            font-size: 0.9rem;
            font-weight: 600;
            transition: all 0.3s;
        }

        .sample-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .sample-btn.fake {
            border-color: #e74c3c;
            color: #e74c3c;
        }

        .sample-btn.fake:hover {
            background: #e74c3c;
            color: white;
        }

        .sample-btn.real {
            border-color: #27ae60;
            color: #27ae60;
        }

        .sample-btn.real:hover {
            background: #27ae60;
            color: white;
        }

        @media (max-width: 968px) {
            .main-grid {
                grid-template-columns: 1fr;
            }

            .header h1 {
                font-size: 2rem;
            }

            .sample-buttons {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔍 Fake News Detector</h1>
            <p>Advanced AI-Powered News Verification System</p>
        </div>

        <div class="main-grid">
            <div class="card">
                <div class="sample-buttons">
                    <button class="sample-btn fake" onclick="loadSample('fake1')">
                        ⚠️ Fake News Sample 1
                    </button>
                    <button class="sample-btn fake" onclick="loadSample('fake2')">
                        ⚠️ Fake News Sample 2
                    </button>
                    <button class="sample-btn real" onclick="loadSample('real1')">
                        ✅ Real News Sample 1
                    </button>
                    <button class="sample-btn real" onclick="loadSample('real2')">
                        ✅ Real News Sample 2
                    </button>
                </div>

                <form id="newsForm">
                    <div class="section-title">
                        <span>📰</span>
                        Enter News Content
                    </div>
                    <textarea 
                        id="newsText" 
                        placeholder="Paste news article, headline, or content here to verify authenticity..."
                        required
                        maxlength="5000"
                    ></textarea>
                    <div class="char-counter">
                        <span id="charCount">0</span> / 5000 characters
                    </div>

                    <button type="submit" class="analyze-btn" id="analyzeBtn">
                        🔬 Analyze News Authenticity
                    </button>
                </form>

                <div class="loading" id="loading">
                    <div class="spinner"></div>
                    <p style="color: #666; font-weight: 600;">Analyzing content...</p>
                </div>
            </div>

            <!-- Stats Sidebar -->
            <div>
                <div class="stats-card">
                    <div class="stat-value" id="modelAccuracy">--</div>
                    <div class="stat-label">Model Accuracy</div>
                </div>

                <div class="stats-card">
                    <div class="stat-value">5000</div>
                    <div class="stat-label">TF-IDF Features</div>
                </div>

                <div class="info-card">
                    <h3>🧠 Model Details</h3>
                    <div class="info-item">
                        <strong>Algorithm:</strong> Random Forest
                    </div>
                    <div class="info-item">
                        <strong>Trees:</strong> 200
                    </div>
                    <div class="info-item">
                        <strong>N-grams:</strong> 1-3
                    </div>
                    <div class="info-item">
                        <strong>Processing:</strong> Advanced NLP
                    </div>
                </div>
            </div>
        </div>

        <!-- Results -->
        <div class="results-card" id="resultsCard">
            <div class="result-header">
                <div class="result-icon" id="resultIcon">⚠️</div>
                <div class="result-title">
                    <h2 id="resultTitle">Analysis Complete</h2>
                    <span class="credibility-badge" id="credibilityBadge">--</span>
                </div>
            </div>

            <div class="metrics-grid">
                <div class="metric-box">
                    <div class="metric-label">Confidence</div>
                    <div class="metric-value" id="confidenceScore">--</div>
                </div>
                <div class="metric-box">
                    <div class="metric-label">Fake Probability</div>
                    <div class="metric-value" id="fakeProb">--</div>
                </div>
                <div class="metric-box">
                    <div class="metric-label">Real Probability</div>
                    <div class="metric-value" id="realProb">--</div>
                </div>
                <div class="metric-box">
                    <div class="metric-label">Word Count</div>
                    <div class="metric-value" id="wordCount">--</div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const form = document.getElementById('newsForm');
        const newsText = document.getElementById('newsText');
        const charCount = document.getElementById('charCount');
        const loading = document.getElementById('loading');
        const resultsCard = document.getElementById('resultsCard');
        const analyzeBtn = document.getElementById('analyzeBtn');

        const samples = {
            fake1: "BREAKING NEWS: Scientists discover miracle cure that doctors don't want you to know about! This one weird trick will change your life forever. Government trying to hide shocking truth!",
            fake2: "UNBELIEVABLE: Billionaire reveals secret to get rich overnight! Pharmaceutical companies hate this natural remedy. Mainstream media refuses to report this massive conspiracy!",
            real1: "The city council approved a new infrastructure development plan during Tuesday's meeting. The $50 million project will focus on improving public transportation over the next two years.",
            real2: "Researchers published their findings on renewable energy efficiency in the Journal of Applied Physics. The peer-reviewed study demonstrates improvements in solar panel performance."
        };

        newsText.addEventListener('input', function() {
            charCount.textContent = this.value.length;
        });

        function loadSample(type) {
            newsText.value = samples[type];
            charCount.textContent = samples[type].length;
            newsText.focus();
        }

        fetch('/api/stats')
            .then(res => res.json())
            .then(stats => {
                document.getElementById('modelAccuracy').textContent = stats.accuracy + '%';
            })
            .catch(() => {
                document.getElementById('modelAccuracy').textContent = 'N/A';
            });

        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const text = newsText.value.trim();
            if (text.length < 10) {
                alert('⚠️ Please enter at least 10 characters');
                return;
            }

            analyzeBtn.disabled = true;
            loading.classList.add('show');
            resultsCard.classList.remove('show');

            try {
                const response = await fetch('/api/analyze', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ text: text })
                });

                const data = await response.json();

                if (data.success) {
                    displayResult(data.result);
                } else {
                    alert('❌ Error: ' + (data.error || 'Unknown error'));
                }
            } catch (error) {
                alert('❌ Error: ' + error.message);
            } finally {
                analyzeBtn.disabled = false;
                loading.classList.remove('show');
            }
        });

        function displayResult(result) {
            const isFake = result.is_fake;
            
            resultsCard.className = 'results-card ' + (isFake ? 'fake' : 'real') + ' show';
            document.getElementById('resultIcon').textContent = isFake ? '⚠️' : '✅';
            document.getElementById('resultTitle').textContent = result.result;
            document.getElementById('credibilityBadge').textContent = result.credibility;
            document.getElementById('confidenceScore').textContent = result.confidence + '%';
            document.getElementById('fakeProb').textContent = result.fake_probability + '%';
            document.getElementById('realProb').textContent = result.real_probability + '%';
            document.getElementById('wordCount').textContent = result.word_count;

            setTimeout(() => {
                resultsCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 100);
        }
    </script>
</body>
</html>
"""
