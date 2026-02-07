import streamlit as st
from engine import SocialSphereEngine

st.set_page_config(page_title="SocialSphere AI", layout="centered")

st.title("📱 SocialSphere Manager")
st.write("Your autonomous agent for viral content.")

# Input fields
topic = st.text_input("What is the topic?", placeholder="e.g. Future of AI")
platform = st.selectbox("Platform", ["LinkedIn", "Twitter/X", "Instagram"])

if st.button("🚀 Generate Content"):
    if topic:
        with st.spinner("Agents are working..."):
            # Initialize engine and run
            engine = SocialSphereEngine()
            crew = engine.create_social_crew(topic, platform)
            result = crew.kickoff()
            
            st.markdown("### Final Draft")
            st.info(result)
    else:
        st.warning("Please enter a topic.")