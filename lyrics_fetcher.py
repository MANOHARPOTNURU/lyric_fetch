import tkinter as tk
from tkinter import messagebox, scrolledtext
import lyricsgenius

GENIUS_API_TOKEN = "qMZxObVlJVhdPivaICMr1TmQ5xN1CWOlZ-gYMRbNxV_J2fXKP_DqfJNLtse-L0gu"

genius = lyricsgenius.Genius(GENIUS_API_TOKEN, timeout=15, retries=3)

def fetch_lyrics():
    title = title_entry.get()
    artist = artist_entry.get()

    if not title or not artist:
        messagebox.showwarning("Please enter both song title and artist name.")
        return

    try:
        song = genius.search_song(title, artist)
        if song:
            lyrics_display.delete(1.0, tk.END)
            lyrics_display.insert(tk.END, f"🎵 {song.title} by {song.artist}\n\n{song.lyrics}")
        else:
            lyrics_display.delete(1.0, tk.END)
            lyrics_display.insert(tk.END, "Lyrics not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch lyrics:\n{e}")


root = tk.Tk()
root.title("Lyrics Finder")
root.geometry("600x600")
root.resizable(False, False)

tk.Label(root, text="Song Title:", font=('Arial', 12)).pack(pady=5)
title_entry = tk.Entry(root, width=40, font=('Arial', 12))
title_entry.pack(pady=5)

tk.Label(root, text="Artist Name:", font=('Arial', 12)).pack(pady=5)
artist_entry = tk.Entry(root, width=40, font=('Arial', 12))
artist_entry.pack(pady=5)


tk.Button(root, text="Get Lyrics", font=('Arial', 12), command=fetch_lyrics, bg='lightblue').pack(pady=10)

lyrics_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=('Courier', 10))
lyrics_display.pack(padx=10, pady=10)


root.mainloop()
