def update_data(data):
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