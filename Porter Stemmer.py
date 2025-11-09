import tkinter as tk
from tkinter import scrolledtext
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk

# הורדת המשאבים הנדרשים
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

# יצירת ה-Stemmer
stemmer = PorterStemmer()

def stem_text():
    text = input_box.get("1.0", tk.END).strip()
    output_box.delete("1.0", tk.END)

    if not text:
        output_box.insert(tk.END, "Insert Text❗ ")
        return

    words = word_tokenize(text)
    lines = []
    for word in words:
        if word.isalpha():
            stemmed = stemmer.stem(word)
            lines.append(f"{word:15} → {stemmed}")

    output_box.insert(tk.END, "\n".join(lines))

root = tk.Tk()
root.title("Porter Stemmer")

tk.Label(root, text="Insert Text :").pack(anchor="w", padx=10, pady=(10, 0))
input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=8, font=("Consolas", 11))
input_box.pack(padx=10, pady=5)

tk.Button(root, text="Apply Stemming", command=stem_text).pack(pady=5)

tk.Label(root, text="Output:").pack(anchor="w", padx=10, pady=(10, 0))
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10, font=("Consolas", 11))
output_box.pack(padx=10, pady=(0, 10))

root.mainloop()
