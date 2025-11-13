<form method="POST" action="/submit">
  <input type="text" name="name" placeholder="Full name">
  <input type="text" name="country" placeholder="Country of origin">
  <input type="number" name="age" placeholder="Age">
  <button type="submit">Register</button>
</form>
import json
import os
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    country = request.form['country']
    age = request.form['age']

    # Check if file exists
    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            data = json.load(file)
    else:
        data = []

    # Add the new registration
    data.append({'name': name, 'country': country, 'age': age})

    # Save all registrations back to the file
    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    return redirect(url_for('index'))
