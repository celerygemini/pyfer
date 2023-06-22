import tkinter as tk
import sys
sys.path.insert(0, '/pyfer/pyfer')
import pyfer


def scramble_button_click(scramble=True):
    input_string = input_text.get()
    key = key_entry.get()
    pm = pyfer.Machine(key)

    if scramble:
        output_string = pm.scramble(input_string)
    else:
        output_string = pm.unscramble(input_string)

    output_text.configure(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output_string)
    output_text.configure(state="disabled")

# window
window = tk.Tk()
window.title("Pyfer")

# input string
input_label = tk.Label(window, text="Input:")
input_label.grid(row=0, column=0, padx=10, pady=10)

input_text = tk.Entry(window,width=50)
input_text.grid(row=0, column=1, padx=10, pady=10)

# input key
key_label = tk.Label(window, text="Key:")
key_label.grid(row=1, column=0, padx=10, pady=10)

key_entry = tk.Entry(window,width=50)
key_entry.grid(row=1, column=1, padx=10, pady=10)

# buttons
scramble_button = tk.Button(window, text="Scramble", command=lambda: scramble_button_click(True))
scramble_button.grid(row=2, column=0, padx=10, pady=10)

unscramble_button = tk.Button(window, text="Unscramble", command=lambda: scramble_button_click(False))
unscramble_button.grid(row=3, column=0, padx=10, pady=10)

# output
output_label = tk.Label(window, text="Output:")
output_label.grid(row=4, column=0, padx=10, pady=10)

output_text = tk.Text(window, height=4, width=70)
output_text.grid(row=4, column=1, padx=10, pady=10)
output_text.configure(state="disabled")

# Start the Tkinter event loop
window.mainloop()