from flask import Flask, render_template, request

app = Flask(__name__)

# Store notes in a list (temporary storage)
notes = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if note and note.strip():  # Ensure the note is not empty or whitespace
            notes.append(note.strip())  # Append cleaned note to the list
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
