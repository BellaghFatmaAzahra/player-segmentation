import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Player Segmentation Dashboard", layout="wide")

# Custom CSS pour style professionnel (fond blanc, texte noir)
st.markdown("""
<style>
    /* Fond blanc principal */
    .stApp {
        background-color: #ffffff;
    }
    
    /* Titres en noir */
    h1, h2, h3, h4, h5, h6, .stMarkdown, label, .stSelectbox label {
        color: #1a1a2e !important;
    }
    
    h1 {
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: #1a1a2e !important;
        border-bottom: 3px solid #2563eb;
        padding-bottom: 0.5rem;
        display: inline-block;
    }
    
    h2, h3 {
        font-weight: 600 !important;
        color: #1f2937 !important;
    }
    
    /* Cartes métriques */
    [data-testid="stMetricValue"] {
        color: #1e293b !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #64748b !important;
        font-size: 0.75rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
    }
    
    [data-testid="stMetricDelta"] {
        color: #10b981 !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f8fafc !important;
        border-right: 1px solid #e2e8f0 !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown, 
    [data-testid="stSidebar"] label {
        color: #1e293b !important;
    }
    
    /* Expander et cartes */
    .streamlit-expanderHeader {
        background-color: #f8fafc !important;
        color: #1e293b !important;
        border-radius: 8px !important;
        border: 1px solid #e2e8f0 !important;
    }
    
    /* Messages */
    .stAlert {
        background-color: #f0fdf4 !important;
        color: #166534 !important;
    }
    
    hr {
        border-color: #e2e8f0 !important;
        margin: 1rem 0 !important;
    }
    
    /* Captions */
    .stCaption {
        color: #64748b !important;
    }
</style>
""", unsafe_allow_html=True)

try:
    df = pd.read_csv('outputs/player_clusters.csv')
    df['profile'] = df['profile'].fillna('Unknown')
    
    # Sidebar
    with st.sidebar:
        st.markdown("## Filters")
        st.markdown("---")
        
        profiles = st.multiselect(
            "Player Segments",
            options=sorted(df['profile'].unique()),
            default=sorted(df['profile'].unique())
        )
        
        st.markdown("---")
        
        min_hours = st.slider("Minimum Play Time (hours)", 0, 500, 0)
        
        st.markdown("---")
        st.caption("Segmentation v1.0 | K-Means + UMAP")
    
    filtered_df = df[df['profile'].isin(profiles)]
    filtered_df = filtered_df[filtered_df['hours_played'] >= min_hours]
    
    # Header
    st.title("Player Segmentation Dashboard")
    st.caption("Behavioral clustering analysis of 10,000 players | K-Means + UMAP")
    st.markdown("---")
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Players", f"{len(filtered_df):,}")
    with col2:
        st.metric("Avg Play Time", f"{filtered_df['hours_played'].mean():.0f} hrs")
    with col3:
        st.metric("Avg Sessions/Week", f"{filtered_df['sessions_per_week'].mean():.0f}")
    with col4:
        st.metric("Avg Games Owned", f"{filtered_df['games_owned'].mean():.0f}")
    
    st.markdown("---")
    
    # Row 1: Two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Segment Distribution")
        dist_data = filtered_df['profile'].value_counts().reset_index()
        dist_data.columns = ['Segment', 'Count']
        fig1 = px.pie(dist_data, values='Count', names='Segment', 
                      hole=0.4, 
                      color_discrete_sequence=['#2563eb', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6'])
        fig1.update_layout(
            plot_bgcolor='white', 
            paper_bgcolor='white',
            font_color='#1e293b',
            font_family='Arial',
            showlegend=True,
            legend_title_text=''
        )
        fig1.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.subheader("Play Time Distribution")
        fig2 = px.box(filtered_df, x='profile', y='hours_played', color='profile',
                      color_discrete_sequence=['#2563eb', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6'])
        fig2.update_layout(
            plot_bgcolor='white', 
            paper_bgcolor='white',
            font_color='#1e293b',
            xaxis_title='',
            yaxis_title='Hours Played',
            showlegend=False
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("---")
    
    # Row 2: Heatmap
    st.subheader("Segment Characteristics")
    
    stats = filtered_df.groupby('profile')[['hours_played', 'sessions_per_week', 
                                              'avg_session_minutes', 'games_owned', 
                                              'achievements_pct']].mean().round(1)
    
    stats.columns = ['Play Time', 'Sessions/Week', 'Session (min)', 'Games', 'Achiev (%)']
    
    fig3 = px.imshow(stats.T, text_auto='.1f', aspect='auto',
                     color_continuous_scale='Blues',
                     title='Average Metrics by Segment')
    fig3.update_layout(
        plot_bgcolor='white', 
        paper_bgcolor='white',
        font_color='#1e293b',
        height=400,
        xaxis_title='Segment',
        yaxis_title='Metric'
    )
    st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown("---")
    
    # Row 3: Segment descriptions
    st.subheader("Segment Profiles")
    
    descriptions = {
        "HARDCORE GAMER": "High engagement. Core audience for complex games. High playtime and frequent sessions.",
        "CASUAL PLAYER": "Light engagement. Prefers short sessions and simple mechanics. Largest segment.",
        "SOCIAL GAMER": "Plays for interaction. Values multiplayer features and community.",
        "EXPLORER": "Enjoys discovery. High achievement rate across diverse genres.",
        "COMPETITIVE PAYER": "Focus on winning. Willing to pay for advantages."
    }
    
    cols = st.columns(len([s for s in descriptions.keys() if s in profiles]) or 1)
    
    for idx, segment in enumerate([s for s in descriptions.keys() if s in profiles]):
        col_idx = idx % len(cols)
        with cols[col_idx]:
            count = len(filtered_df[filtered_df['profile'] == segment])
            pct = count / len(filtered_df) * 100 if len(filtered_df) > 0 else 0
            st.markdown(f"**{segment}**")
            st.caption(f"{count:,} players ({pct:.1f}%)")
            st.caption(descriptions.get(segment, ""))
            st.markdown("---")

except FileNotFoundError:
    st.error("Data file not found. Run 'python scripts/clustering.py' first.")
    
except Exception as e:
    st.error(f"Error: {e}")