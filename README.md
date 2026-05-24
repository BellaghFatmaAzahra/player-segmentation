# Player Segmentation Dashboard

## Behavioral clustering analysis of 10,000 gamers

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.57-red)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.8-orange)
![UMAP](https://img.shields.io/badge/UMAP-0.5-purple)

---

## Dashboard Preview

![Dashboard Overview](images/dashboard_overview.png)

*Main dashboard interface with filters and key metrics*

---

## Overview

This project performs **unsupervised clustering** on 10,000 player profiles to identify distinct behavioral segments. The analysis helps game publishers understand their audience and tailor content accordingly.

**Key capabilities:**
- K-Means clustering on 7 behavioral features
- UMAP dimensionality reduction for visualization
- Interactive dashboard for segment exploration

---

## Problem Statement

Game publishers need to understand their player base:
- Who are my core players?
- What are the different engagement patterns?
- How to personalize content for each segment?

This analysis answers these questions through data-driven segmentation.

---

## Methodology

### Features Used

| Feature | Description |
|---------|-------------|
| hours_played | Total play time (hours) |
| sessions_per_week | Average weekly sessions |
| avg_session_minutes | Average session duration |
| games_owned | Number of games in library |
| achievements_pct | Achievement completion rate |
| pay_to_win_score | Willingness to pay |
| age | Player age |

### Algorithms

| Step | Method |
|------|--------|
| Preprocessing | StandardScaler |
| Clustering | K-Means (k=5) |
| Visualization | UMAP (n_components=2) |

---

## Results

### Segment Distribution

![Segment Distribution](images/segment_distribution.png)

*Distribution of player segments identified by clustering*

| Segment | Count | Percentage | Avg Hours | Sessions/Week |
|---------|-------|------------|-----------|---------------|
| CASUAL PLAYER | 4,296 | 43.0% | 27h | 8 |
| SOCIAL GAMER | 4,068 | 40.7% | 82h | 21 |
| HARDCORE GAMER | 1,636 | 16.4% | 236h | 34 |

### Play Time Analysis

![Play Time Boxplot](images/playtime_boxplot.png)

*Distribution of play hours across different player segments*

### Segment Characteristics Heatmap

![Heatmap](images/heatmap.png)

*Average behavioral metrics per player segment*

---

## Segment Profiles

### HARDCORE GAMER (16.4%)
- High engagement with 236h average playtime
- 34 sessions per week, 197 min per session
- Core audience for complex games
- **Recommendation**: Depth content, competitive modes, premium monetization

### CASUAL PLAYER (43.0%)
- Light engagement with 27h average playtime
- 8 sessions per week, 46 min per session
- Largest segment, prefers simple mechanics
- **Recommendation**: Short sessions, quick rewards, easy onboarding

### SOCIAL GAMER (40.7%)
- Moderate engagement with 82h average playtime
- 21 sessions per week, 94 min per session
- Values multiplayer and community features
- **Recommendation**: Clans, events, social features, cosmetics

---

## Dashboard Features

| Feature | Description |
|---------|-------------|
| Segment Filter | Filter by player type |
| Time Filter | Minimum play time slider |
| Distribution Chart | Pie chart of segment sizes |
| Box Plot | Play time distribution by segment |
| Heatmap | Average metrics per segment |
| Profiles | Detailed segment descriptions |

---

## Project Structure
