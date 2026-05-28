import streamlit as st
import google.generativeai as genai
import base64

# ==========================================
# CONFIGURATION & SETUP
# ==========================================
st.set_page_config(
    page_title="LUNA - Laptop Matchmaker",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return "" 

img_base64 = get_base64_of_bin_file('bh.jpg')

# ==========================================
# MODERN CSS INJECTION (PREMIUM UI UPGRADE)
# ==========================================
st.markdown(f"""
<style>
/* Background setup */
[data-testid="stAppViewContainer"] {{
    background-image: linear-gradient(rgba(10, 10, 15, 0.85), rgba(10, 10, 15, 0.98)), url("data:image/jpeg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Custom Sleek Scrollbar */
::-webkit-scrollbar {{
    width: 6px;
}}
::-webkit-scrollbar-track {{
    background: transparent;
}}
::-webkit-scrollbar-thumb {{
    background: rgba(124, 58, 237, 0.4); 
    border-radius: 10px;
}}
::-webkit-scrollbar-thumb:hover {{
    background: rgba(124, 58, 237, 0.8); 
}}

/* Disable Streamlit's default screen dimming/blurring during reruns */
*[data-stale="true"] {{
    opacity: 1 !important;
    filter: none !important;
    transition: none !important;
}}

/* Sidebar Styling */
[data-testid="stSidebar"] {{
    background-color: rgba(15, 15, 20, 0.7) !important;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255, 255, 255, 0.05);
}}

/* Transparent header */
[data-testid="stHeader"] {{
    background: transparent;
}}

/* Main app text color */
.stApp {{
    color: #e0e0e0;
}}

/* --- THE FIX: Make the Streamlit container holding the logo STICKY --- */
div.element-container:has(.glass-header-wrapper) {{
    position: sticky;
    top: 20px;
    z-index: 999;
}}

/* Glassmorphism Header Box with Glowing Edges (CIRCULAR) */
.glass-header-wrapper {{
    position: relative;
    width: 120px;  
    height: 120px; 
    margin: 0 auto 1rem auto; 
    border-radius: 50%; 
    padding: 2px; 
    background: linear-gradient(45deg, #ff007f, #7c3aed, #00d2ff, #3a7bd5, #ff007f);
    background-size: 400% 400%;
    animation: glowAnimation 10s ease-in-out infinite;
    /* Ultra-smooth, silky fluid transition for thinking */
    transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}}

.glass-header-wrapper::after {{
    content: "";
    position: absolute;
    top: -5px; left: -5px; right: -5px; bottom: -5px;
    background: inherit;
    border-radius: 50%; 
    filter: blur(20px);
    opacity: 0.7;
    z-index: -1;
    animation: glowAnimation 10s ease-in-out infinite;
    /* Ultra-smooth transition for the glow */
    transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}}

.glass-header {{
    background: rgba(10, 10, 15, 0.95); 
    border-radius: 50%; 
    width: 100%;
    height: 100%;
    box-sizing: border-box; 
    position: relative;
    z-index: 1; 
    /* Added backdrop blur so scrolling text underneath looks frosted */
    backdrop-filter: blur(30px);
    -webkit-backdrop-filter: blur(30px);
    /* Ultra-smooth transition for the inner box */
    transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}}

@keyframes glowAnimation {{
    0% {{ background-position: 0% 50%; }}
    50% {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}

/* Creative Gradient Title */
.creative-title {{
    background: linear-gradient(45deg, #a78bfa, #f472b6, #a78bfa);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3.8rem; /* Default size, overridden inline for the circle */
    font-weight: 900;
    margin-bottom: 0.5rem;
    letter-spacing: -2px;
    display: flex;
    align-items: center;
    justify-content: center;
    animation: gradientShift 6s ease infinite;
    text-shadow: 0px 4px 15px rgba(124, 58, 237, 0.3);
}}

@keyframes gradientShift {{
    0% {{ background-position: 0% 50%; }}
    50% {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}

/* Smooth slide-in animation for chat bubbles */
@keyframes slideIn {{
    from {{ opacity: 0; transform: translateY(20px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

/* PREMIUM User Chat Bubble (With Gradient & Tail) */
div[data-testid="stChatMessage"][data-baseweb="block"]:has(div[data-testid="stChatMessageAvatarUser"]) {{
    animation: slideIn 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) forwards;
    background: linear-gradient(135deg, rgba(124, 58, 237, 0.2), rgba(236, 72, 153, 0.05));
    border-radius: 20px 20px 0px 20px; /* Tail pointing right */
    padding: 15px 25px;
    margin-left: auto;
    margin-bottom: 25px;
    border: 1px solid rgba(124, 58, 237, 0.3);
    backdrop-filter: blur(12px);
    max-width: 75%;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
    font-size: 1.05rem;
    color: #ffffff;
}}

/* PREMIUM Assistant Chat Bubble (Glass & Glow) */
div[data-testid="stChatMessage"][data-baseweb="block"]:has(div[data-testid="stChatMessageAvatarAssistant"]) {{
    animation: slideIn 0.4s cubic-bezier(0.25, 0.8, 0.25, 1) forwards;
    background-color: rgba(20, 20, 25, 0.5);
    border-radius: 20px 20px 20px 0px; /* Tail pointing left */
    padding: 18px 25px;
    margin-bottom: 25px;
    border: 1px solid rgba(255, 255, 255, 0.03);
    border-left: 4px solid #7c3aed; /* Neon Purple Accent */
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2), -5px 0 20px rgba(124, 58, 237, 0.15);
    font-size: 1.05rem;
    line-height: 1.6;
}}

/* PREMIUM Chat Input Box (Outer Wrapper) */
[data-testid="stChatInput"] {{
    background-color: rgba(15, 15, 20, 0.8) !important;
    border: 1px solid rgba(124, 58, 237, 0.3) !important;
    border-radius: 30px !important;
    backdrop-filter: blur(15px);
    padding: 5px 10px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
    transition: all 0.3s ease-in-out;
}}

/* Chat Input Glow on Focus */
[data-testid="stChatInput"]:focus-within {{
    border-color: #ec4899 !important;
    box-shadow: 0 0 25px rgba(236, 72, 153, 0.3), 0 10px 40px rgba(0, 0, 0, 0.5);
    transform: translateY(-2px);
}}

/* Aggressively Nuke All Inner Backgrounds & Borders */
[data-testid="stChatInput"] div {{
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
}}

[data-testid="stChatInput"] textarea {{
    background-color: transparent !important;
    color: white !important;
    border: none !important;
    box-shadow: none !important;
}}

/* Make the send button match the premium vibe */
[data-testid="stChatInput"] button {{
    background-color: transparent !important;
    color: #ec4899 !important; 
    transition: transform 0.2s ease;
}}

[data-testid="stChatInput"] button:hover {{
    transform: scale(1.1);
    color: #7c3aed !important;
}}

/* Sidebar History Interactive Cards */
.history-card {{
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 12px 15px;
    margin-bottom: 12px;
    font-size: 0.9rem;
    color: #a0a0a0;
    transition: all 0.3s ease;
    cursor: default;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}}

.history-card:hover {{
    background: rgba(124, 58, 237, 0.1);
    border-color: rgba(124, 58, 237, 0.4);
    color: #ffffff;
    transform: translateX(5px); /* Slides right on hover */
    box-shadow: 0 4px 15px rgba(124, 58, 237, 0.2);
}}

/* Premium Button Styling */
div.stButton > button {{
    width: 100%;
    border-radius: 12px;
    background-color: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: white;
    font-weight: 600;
    transition: all 0.3s ease;
    padding: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}}

div.stButton > button:hover {{
    background-color: rgba(124, 58, 237, 0.8);
    border-color: #7c3aed;
    color: white;
    box-shadow: 0 0 20px rgba(124, 58, 237, 0.5);
    transform: translateY(-2px);
}}
</style>
""", unsafe_allow_html=True)

# Dynamic CSS Placeholder for animations
# We will inject and delete CSS here depending on whether LUNA is thinking
thinking_animation_placeholder = st.empty()

# ==========================================
# INITIALIZATION
# ==========================================

# Replace with your actual Gemini API key
GEMINI_API_KEY = "ENTER YOUR GEMINI API KEY HERE"
genai.configure(api_key=GEMINI_API_KEY)

# Default welcome message
welcome_msg = {"role": "assistant", "content": "Hey there! 👋 I'm LUNA, your personal tech matchmaker. What kind of laptop vibe are we looking for today?"}

if "messages" not in st.session_state:
    st.session_state.messages = [welcome_msg]

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("## ⚙️ Dashboard")
    
    if st.button("➕ New Conversation"):
        st.session_state.messages = [welcome_msg]
        st.rerun()
        
    st.markdown("---")
    st.markdown("### 📜 Session History")
    
    user_queries = [msg["content"] for msg in st.session_state.messages if msg["role"] == "user"]
    
    if not user_queries:
        st.caption("No queries yet. Start chatting!")
    else:
        for i, query in enumerate(reversed(user_queries[-5:])): 
            # Replaced st.caption with custom interactive history cards
            st.markdown(f'<div class="history-card">💭 {query[:35]}...</div>', unsafe_allow_html=True)
            
        st.write("") 
        
        if st.button("🗑️ Clear History", type="primary"):
            st.session_state.messages = [welcome_msg]
            st.rerun()

# ==========================================
# MAIN USER INTERFACE
# ==========================================

# Changed the <h1> tag inside the circle to a <div> tag to remove the hover clip mark
# 1. The Logo Block (This one will stick to the top when you scroll)
st.markdown(f"""
<div class="glass-header-wrapper">
    <div class="glass-header" style="display: flex; flex-direction: column; align-items: center; justify-content: center; box-sizing: border-box;">
        <div class="creative-title" style="margin: 0; padding: 0; width: 100%; text-align: center; line-height: 1; font-size: 2.2rem;">
            L U N A
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 2. The Text Block (This one will scroll away normally)
st.markdown(f"""
<p style="color: #c4c4c4; font-size: 1.15rem; margin: 0.5rem 0 3rem 0; padding: 0; font-weight: 400; text-align: center; letter-spacing: 0.5px; line-height: 1.4;">
    Your Personalized Laptop Matchmaker
</p>
""", unsafe_allow_html=True)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================
# HANDLE USER INPUT
# ==========================================
if user_prompt := st.chat_input("E.g., Find me a beautifully designed laptop under ₹80000..."):
    
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # UPDATED: We removed the local dataset! LUNA now relies completely on the web.
    system_instruction = """
    You are LUNA, an incredibly creative, enthusiastic, and style-conscious tech expert. 
    Your goal is to recommend the best laptops to the user by searching the live internet for the newest and most relevant models.
    Don't just list specs—paint a picture of why this laptop fits their vibe, workflow, and lifestyle.
    Use formatting creatively (emojis, bolding, styled bullet points) to make the text pop.
    Always mention the exact Price in Rupees (₹) based on current online data.
    
    CRITICAL RULE FOR LINKS: NEVER make up, guess, or predict URLs. 
    If you do not have the exact, verified working URL from your search results, DO NOT provide a link. 
    Instead, just tell the user where to look (e.g., "You can find this on Amazon or the official HP website").
    """

    with st.chat_message("assistant"):
        
        # Trigger the "Super Cool" Pulsing Glow exactly when processing starts
        thinking_animation_placeholder.markdown("""
        <style>
        .glass-header-wrapper {
            transform: scale(1.15) !important;
            box-shadow: 0 0 30px rgba(236, 72, 153, 0.7), 0 0 60px rgba(124, 58, 237, 0.9) !important;
        }
        .glass-header-wrapper::after {
            filter: blur(40px) !important;
            opacity: 1 !important;
            animation: glowAnimation 1.5s linear infinite !important; /* Sped up animation */
        }
        .glass-header {
            box-shadow: inset 0 0 25px rgba(124, 58, 237, 0.6) !important;
        }
        </style>
        """, unsafe_allow_html=True)

        try:
            # Initialize Gemini with GOOGLE SEARCH enabled!
            model = genai.GenerativeModel(
                model_name="gemini-2.5-flash", 
                system_instruction=system_instruction,
                tools=[genai.protos.Tool(google_search=genai.protos.Tool.GoogleSearch())] # <--- The official Tool Object!
            )
            
            # Format history for Gemini
            gemini_history = []
            for msg in st.session_state.messages[-6:]: 
                role = "model" if msg["role"] == "assistant" else "user"
                gemini_history.append({"role": role, "parts": [msg["content"]]})

            # Stream response
            response = model.generate_content(
                gemini_history,
                stream=True,
                generation_config=genai.GenerationConfig(
                    temperature=0.85,
                )
            )

            def stream_response():
                for chunk in response:
                    if chunk.text:
                        yield chunk.text
            
            ai_response = st.write_stream(stream_response())
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            
        except Exception as e:
            st.error(f"Oops! The AI encountered an error: {e}")
            
        finally:
            # Delete the temporary CSS the moment she finishes, snapping her back to normal
            thinking_animation_placeholder.empty()