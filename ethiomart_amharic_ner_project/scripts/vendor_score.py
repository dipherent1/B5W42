"""Vendor scoring script. Reads a CSV of messages with vendor/channel metadata and NER-extracted prices/views.
Produces a vendor scorecard CSV summarizing Avg Views/Post, Posts/Week, Avg Price, Lending Score.
"""
import pandas as pd
import numpy as np

def compute_scores(df):
    # df must have: channel, timestamp (ISO), views (int), price (float)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    out = []
    for channel, g in df.groupby('channel'):
        posts = len(g)
        weeks = (g['timestamp'].max() - g['timestamp'].min()).days / 7
        weeks = weeks if weeks>0 else 1/7
        posts_per_week = posts / weeks
        avg_views = g['views'].mean() if 'views' in g.columns else 0
        avg_price = g['price'].mean() if 'price' in g.columns else np.nan
        # simple lending score (example weights) normalize components
        score = (avg_views * 0.5) + (posts_per_week * 10 * 0.5)  # scale posts_per_week to similar magnitude
        out.append({'channel':channel, 'posts':posts, 'posts_per_week':posts_per_week, 'avg_views':avg_views, 'avg_price':avg_price, 'lending_score':score})
    return pd.DataFrame(out)

if __name__ == '__main__':
    # example usage
    df = pd.read_csv('data/sample_messages_with_views.csv') if os.path.exists('data/sample_messages_with_views.csv') else pd.DataFrame()
    if df.empty:
        print('No sample data with views found. Run NER and enrich messages with views/price first.')
    else:
        print(compute_scores(df))
