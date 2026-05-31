from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

def translate():
    try:
        text = input_text.get("1.0", END).strip()

        if text == "":
            messagebox.showwarning("Warning", "Enter some text")
            return

        source = languages[source_lang.get()]
        target = languages[target_lang.get()]

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", END))
    root.update()

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru"
}

root = Tk()
root.title("Language Translation Tool")
root.geometry("700x500")

Label(root, text="Language Translation Tool",
      font=("Arial", 18, "bold")).pack(pady=10)

Label(root, text="Enter Text").pack()

input_text = Text(root, height=6, width=70)
input_text.pack(pady=5)

frame = Frame(root)
frame.pack(pady=10)

source_lang = StringVar(value="English")
target_lang = StringVar(value="Hindi")

Label(frame, text="Source Language").grid(row=0, column=0, padx=10)

ttk.Combobox(
    frame,
    textvariable=source_lang,
    values=list(languages.keys()),
    state="readonly",
    width=15
).grid(row=0, column=1)

Label(frame, text="Target Language").grid(row=0, column=2, padx=10)

ttk.Combobox(
    frame,
    textvariable=target_lang,
    values=list(languages.keys()),
    state="readonly",
    width=15
).grid(row=0, column=3)

Button(
    root,
    text="Translate",
    command=translate,
    width=15
).pack(pady=10)

Label(root, text="Translated Text").pack()

output_text = Text(root, height=6, width=70)
output_text.pack(pady=5)

Button(
    root,
    text="Copy Translation",
    command=copy_text,
    width=15
).pack(pady=10)

root.mainloop()
