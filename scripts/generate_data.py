import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

print("Generation du dataset de joueurs...")
n_players = 10000

profiles = []
for i in range(n_players):
    player_type = np.random.choice(['hardcore', 'casual', 'competitive', 'social', 'explorer'], 
                                    p=[0.15, 0.40, 0.15, 0.20, 0.10])
    
    if player_type == 'hardcore':
        hours_played = np.random.gamma(2, 100)
        sessions_per_week = np.random.randint(20, 50)
        avg_session_min = np.random.randint(120, 300)
        genres = 'RPG,Action,Strategy'
        pay_to_win = np.random.choice([0,1], p=[0.3, 0.7])
        age = np.random.randint(18, 35)
        
    elif player_type == 'casual':
        hours_played = np.random.gamma(1, 20)
        sessions_per_week = np.random.randint(3, 12)
        avg_session_min = np.random.randint(20, 60)
        genres = 'Puzzle,Casual,Simulation'
        pay_to_win = np.random.choice([0,1], p=[0.8, 0.2])
        age = np.random.randint(25, 55)
        
    elif player_type == 'competitive':
        hours_played = np.random.gamma(2, 80)
        sessions_per_week = np.random.randint(15, 40)
        avg_session_min = np.random.randint(60, 180)
        genres = 'FPS,MOBA,Fighting'
        pay_to_win = np.random.choice([0,1], p=[0.5, 0.5])
        age = np.random.randint(16, 30)
        
    elif player_type == 'social':
        hours_played = np.random.gamma(1.5, 40)
        sessions_per_week = np.random.randint(10, 30)
        avg_session_min = np.random.randint(45, 120)
        genres = 'MMO,Sports,Party'
        pay_to_win = np.random.choice([0,1], p=[0.6, 0.4])
        age = np.random.randint(20, 40)
        
    else:
        hours_played = np.random.gamma(1.8, 50)
        sessions_per_week = np.random.randint(8, 25)
        avg_session_min = np.random.randint(30, 150)
        genres = 'Adventure,Indie,OpenWorld'
        pay_to_win = np.random.choice([0,1], p=[0.7, 0.3])
        age = np.random.randint(18, 45)
    
    profiles.append({
        'player_id': i,
        'age': age,
        'hours_played': round(hours_played, 1),
        'sessions_per_week': sessions_per_week,
        'avg_session_minutes': avg_session_min,
        'games_owned': np.random.randint(5, 200),
        'achievements_pct': round(np.random.uniform(10, 95), 1),
        'pay_to_win_score': pay_to_win,
        'player_type_true': player_type,
        'genres': genres
    })

df = pd.DataFrame(profiles)
df.to_csv('data/player_behavior.csv', index=False)
print(f"Dataset genere: {len(df)} joueurs")
print("\nDistribution reelle des profils:")
print(df['player_type_true'].value_counts())
print("\nApercu des donnees:")
print(df.head())