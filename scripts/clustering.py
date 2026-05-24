import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import umap
import warnings
warnings.filterwarnings('ignore')

print("Chargement des donnees...")
df = pd.read_csv('data/player_behavior.csv')
print(f"Donnees chargees: {len(df)} lignes")

features = ['hours_played', 'sessions_per_week', 'avg_session_minutes', 
            'games_owned', 'achievements_pct', 'pay_to_win_score', 'age']

df_features = df[features].copy()

print("Normalisation des donnees...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_features)

print("Application de K-Means (5 clusters)...")
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

print("\n=== PROFILS JOUEURS ===")
cluster_profiles = {}

for cluster_id in range(5):
    cluster_data = df[df['cluster'] == cluster_id]
    print(f"\n--- CLUSTER {cluster_id} ({len(cluster_data)} joueurs) ---")
    print(f"  Heures: {cluster_data['hours_played'].mean():.0f}h")
    print(f"  Sessions/semaine: {cluster_data['sessions_per_week'].mean():.0f}")
    print(f"  Duree session: {cluster_data['avg_session_minutes'].mean():.0f}min")
    print(f"  Jeux: {cluster_data['games_owned'].mean():.0f}")
    print(f"  Achievements: {cluster_data['achievements_pct'].mean():.1f}%")
    
    avg_hours = cluster_data['hours_played'].mean()
    avg_sessions = cluster_data['sessions_per_week'].mean()
    
    if avg_hours > 200 and avg_sessions > 30:
        profile = "HARDCORE GAMER"
    elif avg_hours > 150:
        profile = "COMPETITIVE PAYER"
    elif avg_hours < 50 and avg_sessions < 10:
        profile = "CASUAL PLAYER"
    elif avg_sessions > 15:
        profile = "SOCIAL GAMER"
    else:
        profile = "EXPLORER"
    
    cluster_profiles[cluster_id] = profile
    print(f"  >>> {profile}")

df['profile'] = df['cluster'].map(cluster_profiles)

print("\nGeneration UMAP...")
reducer = umap.UMAP(random_state=42, n_components=2)
X_umap = reducer.fit_transform(X_scaled)
df['umap_x'] = X_umap[:, 0]
df['umap_y'] = X_umap[:, 1]

# Sauvegarder dans outputs
import os
os.makedirs('outputs', exist_ok=True)
df.to_csv('outputs/player_clusters.csv', index=False)
print("\nFichier sauvegarde: outputs/player_clusters.csv")

print("\n=== DISTRIBUTION FINALE ===")
print(df['profile'].value_counts())