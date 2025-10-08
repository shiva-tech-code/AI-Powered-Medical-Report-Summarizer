#!/bin/bash

# MedLite - AI-Powered Medical Report Summarizer
# Startup script

echo "🏥 MedLite - AI-Powered Medical Report Summarizer"
echo "=================================================="

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ app.py not found. Please run this script from the MedLite directory"
    exit 1
fi

# Check if Streamlit is installed
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo "❌ Streamlit is not installed. Installing..."
    pip3 install streamlit pandas numpy
fi

echo "✅ All dependencies are ready!"
echo ""
echo "🚀 Starting MedLite..."
echo "📱 The app will open in your browser at: http://localhost:8501"
echo "⏹️  Press Ctrl+C to stop the application"
echo ""

# Start the application
python3 -m streamlit run app.py --server.port 8501
