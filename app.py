import streamlit as st
from transformers import pipeline
import pandas as pd
import random

# Set Page Config for that "Aesthetic" feel
st.set_page_config(page_title="VibeCheck AI", page_icon="🎭", layout="centered")

# Custom CSS for the "Onion Pink" and Modern vibe
st.markdown("""
    <style>
    .main { background-color: #fff5f6; }
    .stButton>button { background-color: #ff91a4; color: white; border-radius: 20px; }
    </style>
    """, unsafe_allow_status_code=True)

@st.cache_resource
def load_model():
    # Loading the emotion classifier (DistilBERT)
    return pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

classifier = load_model()

st.title("🎭 VibeCheck AI: Aura & Ghosting Risk")
st.write("### Paste a bio, caption, or message to reveal the true vibe.")

user_text = st.text_area("Enter Text Here...", placeholder="e.g., 'Building my future in Data Science. ✨'", height=150)

if st.button("ANALYZE VIBE"):
    if user_text:
        results = classifier(user_text)
        emotion = results[0]['label']
        
        # --- Aura & Personality Logic ---
        aura_data = {
            "joy": {"aura": "Golden Yellow", "hex": "#FFD700", "vibe": "The Radiant Visionary"},
            "anger": {"aura": "Crimson Red", "hex": "#DC143C", "vibe": "The Fierce Competitor"},
            "fear": {"aura": "Electric Blue", "hex": "#7DF9FF", "vibe": "The Strategic Analyst"},
            "sadness": {"aura": "Deep Indigo", "hex": "#4B0082", "vibe": "The Deep Thinker"},
            "love": {"aura": "Onion Pink", "hex": "#FF91A4", "vibe": "The Empath"},
            "surprise": {"aura": "Neon Orange", "hex": "#FF5F1F", "vibe": "The Out-of-the-Box Innovator"}
        }
        
        vibe_info = aura_data.get(emotion, {"aura": "Grey", "hex": "#808080", "vibe": "The Mystery"})
        
        # --- Red/Green Flags ---
        red_flags = ["private", "know me", "don't care", "...", "alone", "ghost"]
        green_flags = ["learner", "goal", "thankful", "create", "explore", "connect"]
        
        found_red = [w for w in red_flags if w in user_text.lower()]
        found_green = [w for w in green_flags if w in user_text.lower()]
        
        # --- Ghosting Risk Score ---
        ghost_risk = random.randint(10, 40) if emotion in ["joy", "love"] else random.randint(60, 95)
        if len(user_text) < 15: ghost_risk += 10
        ghost_risk = min(ghost_risk, 100) # Cap at 100%

        # --- Display Results ---
        st.divider()
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Predicted Aura", vibe_info['aura'])
            st.markdown(f"<div style='width: 100px; height: 100px; background-color: {vibe_info['hex']}; border-radius: 50%; margin: auto;'></div>", unsafe_allow_html=True)
            st.write(f"**Vibe Type:** {vibe_info['vibe']}")

        with col2:
            st.metric("Ghosting Risk", f"{ghost_risk}%")
            st.progress(ghost_risk / 100)
            if ghost_risk > 70:
                st.warning("⚠️ High chance of 'Seen' and no reply.")
            else:
                st.success("✅ Likely a consistent replier.")

        # Flag Summary
        st.write("---")
        st.write(f"🍀 **Green Flags:** {len(found_green)} | 🚩 **Red Flags:** {len(found_red)}")
        if found_red:
            st.write(f"*Detected Red Flags:* {', '.join(found_red)}")
            
        st.balloons()
    else:
        st.error("Please enter some text first!")
