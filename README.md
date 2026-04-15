🎭 VibeCheck AI: Aura & Behavioral Analysis
Decoding Social Patterns with Transformers and NLP
🎯 The Vision
In an era of curated social media, what people say is often different from the "vibe" they project. I built VibeCheck AI to bridge the gap between text and intent. This project doesn't just analyze sentiment; it predicts Aura Personalities and evaluates social metrics like Ghosting Risk and Behavioral Flags using state-of-the-art Deep Learning.

🚀 The "Out of the Box" Features
Aura Identification: Maps linguistic patterns to specific color archetypes (e.g., Onion Pink for Empaths, Crimson for Competitors).

Ghosting Risk Algorithm: A custom-weighted probability score that predicts communication consistency based on emotional distance and text length.

Pattern Matching: Detects "Red" and "Green" flags by analyzing keywords and emotional spikes within bios and captions.

🧠 Technical Deep Dive
Model: Powered by a pre-trained DistilBERT (Transformer) model specialized in emotion classification.

Optimization: Utilizes st.cache_resource for efficient model loading and memory management on Streamlit Cloud.

NLP Pipeline: Implements a multi-stage analysis: Emotion Extraction -> Keyword Pattern Matching -> Probabilistic Risk Calculation.

🛠️ Tech Stack
Transformers (HuggingFace): For high-accuracy emotion detection.

PyTorch: The underlying engine for tensor computations.

Streamlit: To create a sleek, "Aesthetic" user interface.

Pandas: For structuring behavioral data outputs.
