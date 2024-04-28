import cv2
import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd

# Function to update DataFrame and display data
def update_data():
    # Here you would update your DataFrame with new data
    # For demonstration, let's create a dummy DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [85, 70, 60, 45]  # Example scores, you can replace this with your actual data
    }
    df = pd.DataFrame(data)

    # Clear previous data labels
    for label in data_labels:
        label.destroy()
    data_labels.clear()

    # Update label text with DataFrame
    for i, row in df.iterrows():
        text = f"{row['Name']}, Age: {row['Age']}, Score: {row['Score']}"
        label = tk.Label(root, text=text, justify=tk.LEFT)
        label.pack(side=tk.BOTTOM, anchor=tk.W)
        data_labels.append(label)
        # Change background color based on score value
        score = row['Score']
        if score >= 70:
            label.configure(bg='lightgreen')
        elif 50 <= score < 70:
            label.configure(bg='yellow')
        else:
            label.configure(bg='red')

    # Schedule next update after 5 seconds
    root.after(5000, update_data)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Function to update webcam frame
def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        panel.img = img
        panel.config(image=img)
        panel.after(10, update_frame)

# Create a Tkinter window
root = tk.Tk()
root.title("Webcam and DataFrame Display")

# Create a panel to display webcam feed
panel = tk.Label(root)
panel.pack()

# Start updating webcam feed
update_frame()

# List to keep track of data labels
data_labels = []

# Start updating data automatically
update_data()

# Start the Tkinter event loop
root.mainloop()

# Release the webcam
cap.release()
