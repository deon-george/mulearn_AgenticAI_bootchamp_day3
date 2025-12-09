import os
import time

try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

def call_llm(prompt: str) -> str:
    """
    Calls the Gemini API if GEMINI_API_KEY is set and package is installed.
    Otherwise returns deterministic mock responses.
    """
    api_key = os.getenv("AIzaSyBenCzUBeB2pZLYEQKr5VeexyyWETRp52w")
    
    if api_key and HAS_GENAI:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error calling Gemini API: {e}")
            print("Falling back to mock response...")
    elif not HAS_GENAI and api_key:
        print("GEMINI_API_KEY found but 'google-generativeai' not installed.")
        print("Please run: pip install google-generativeai")
        print("Falling back to mock response...")
    
    # Mock Response Logic (Fallback)
    print(f"DEBUG: Using Mock LLM for prompt beginning: {prompt[:50]}...")
    time.sleep(0.5) 
    
    if "Planner Agent" in prompt:
        if "notebook" in prompt.lower() or "csv" in prompt.lower():
            return """1. Load the CSV file using pandas.
2. Perform basic data cleaning.
3. Calculate summary statistics.
4. Generate visualizations using matplotlib.
5. Save the analysis."""
        else:
            return """1. Define the API endpoints (e.g., /health, /info).
2. Choose a framework (Flask).
3. Implement the main application logic.
4. Add error handling.
5. Write the server startup code."""
    
    elif "Research Agent" in prompt:
        if "csv" in prompt.lower() or "pandas" in prompt.lower():
             return """- Recommended Library: Pandas for data manipulation, Matplotlib for plotting.
- Architecture: Jupyter notebook or linear script.
- Edge Case: Handle missing values and malformed CSVs.
- Best Practice: Use relative paths for data files."""
        else:
            return """- Recommended Library: Flask for simplicity.
- Architecture: MVC pattern is overkill here, single file is fine.
- Edge Case: Handle 404s and 500s gracefully.
- Best Practice: Use environment variables for configuration."""
    
    elif "Coding Agent" in prompt:
        if "Flask" in prompt and "CSV" not in prompt:
            return """from flask import Flask, jsonify
import platform

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def get_system_info():
    return jsonify({
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version()
    })

if __name__ == '__main__':
    app.run(debug=True)"""
        else: # CSV mode
            return """import pandas as pd
import matplotlib.pyplot as plt

def analyze_csv(file_path):
    df = pd.read_csv(file_path)
    print("Statistics:")
    print(df.describe())
    
    df.plot(kind='bar')
    plt.show()

# Example usage
# analyze_csv('data.csv')"""

    elif "Evaluation Agent" in prompt:
        return """1. Code looks clean.
2. Imports are correct.
3. No obvious security issues found."""

    return "Unknown prompt type."

