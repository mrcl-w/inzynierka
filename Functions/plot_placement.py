import matplotlib.pyplot as plt
import seaborn as sns

def plot_song_billboard_placement(song_title, song_artist, data):
    song_data = data[(data['Normalized Title'] == song_title) & (data['Artist'] == song_artist)]
    if not song_data.empty:
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='Date', y='Rank', data=song_data)
        plt.gca().invert_yaxis()  # Invert y-axis to show rank 1 at the top
        plt.title(f'Billboard Placement Over Time for "{song_title.title()}"')
        plt.xlabel('Date')
        plt.ylabel('Rank')
        plt.xticks(rotation=45)
        plt.grid()
        plt.show()
    else:
        print(f'No data found for the song "{song_title}".')