from flask import Flask, session, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = 'supersecretkey'

EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

@app.route('/')
def home():
    return "Welcome to the Home Page!"
def index():
    return render_template('contact_form.html')

@app.route('/about')
def about():
    return "This is the About Page."

@app.route('/contact')
def contact():
    return "Contact us at: info@example.com."

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirmation = request.form['confirmation']
    dob = request.form['Date of Birth']
    gender = request.form['gender']
    nationality = request.form['nationality']
    message = request.form['message']
    emergency_contact = request.form['emergency_contact']
    number_of_dependants = request.form['number_of_dependants']
    phone_number = request.form['phone_number']
    assistance_needed = request.form['assistance_needed']
    address = request.form['address']

    # Store values in session so we can repopulate them
    session['name'] = name
    session['last_name'] = last_name
    session['email'] = email
    session['message'] = message
    session['password'] = password
    session['gender'] = gender
    session['nationality'] = nationality
    session['emergency_contact'] = emergency_contact
    session['Date of Birth'] = dob
    session['number_of_dependants'] = number_of_dependants
    session['phone_number'] = phone_number
    session['assistance_needed'] = assistance_needed
    session['address'] = address
    session['confirmation'] = confirmation


    if __name__ == ('__main__'):
        app.run(debug=True)
        return redirect(url_for('index'))

    if not name or not email or not message or not password:
        flash('All fields are required to be filled out in order to continue')
        return redirect(url_for('index'))

    if last_name == ('__main__')
        app.run(debug=True)
        return redirect(url_for('index'))

    elif last_name = integer:
        flash('You cannot submit a last name with numerical values')
        return redirect(url_for('index'))

    if dob < 0 or age > 100:
        flash('Age must be between 0 and 200!')
        return redirect(url_for('index'))

    if len(message) < 10: flash('Message must be at least 10 characters.')
        return render_template('contact_form.html')

    if confirmation != password:
        flash('Password confirmation required!')
        return render_template('contact_form.html')

    if nationality not in ['A', 'B', 'C', 'D', 'E', 'F']:
        flash('Please enter a valid nationality.')
            return render_template('contact_form.html')

    if emergency_contact not in ['Y', 'N']:
        flash('Please enter a valid emergency contact.')
        return render_template('contact_form.html')

    if gender not in ['M', 'F']:
        flash('Please enter a valid gender.')
        return render_template('contact_form.html')

    if number_of_dependants <= 0:
        flash('Please enter a valid number of dependants.')
        return render_template('contact_form.html')

    if phone_number == '' or phone_number != integers:
        flash('Please enter a valid phone number.')
        return render_template('contact_form.html')

    if address == '':
        flash('Please enter a valid address.')
        return render_template('admin_form.html')

    def submit_form():
        name = request.form['name']
        country = request.form['country']
        age = request.form['age']

        if os.path.exists('registration-json'):
            with open('registration-json', 'r') as json_file:
                data = json.load(json_file)
        else:
            data = {}

    if address does not have 0=<100len(address):
        flash('Please enter a valid address.')
        return render_template('admin_form.html')

    if assistance_needed != 'food', 'shelter', or 'educatoin':
        flash('Please enter a valid assistance needed.')
        return render_template('contact_form.html')

    elif assistance_needed == 'other':
        flash('Please enter a valid assistance needed.')
        return render_template('contact_form.html')

    if

    else:
        flash("Thank you for registering!")
        return redirect(url_for('index'))


        return render_template('contact_form.html', name=name, email=email, message=message)
            session.pop('name', None)
            session.pop('email', None)
            session.pop('message', None)
            flash(f'Thank you, {name}. Your message has been submitted successfully!')
            return redirect(url_for('index'))

#if name.strip() == "":
 #  flash("Name cannot be empty.")
  # return render_template('register.html')
   #saved_name = name
   #saved_country = country
   #saved_age = age
   #saved_password = password
   #saved_gender = gender
   #saved_messsage = message

   # if password != request.form['password']:
    #    flash('Passwords do not match.')
     #   return redirect(url_for('index'))

import json
import os
@app.route('/submit', methods=['POST'])

    # Add the new registration
    data.append({'name': name, 'country': country, 'age': age})

    # Save all registrations back to the file
    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    return redirect(url_for('index'))
@app.route('/view')
def view_registrations():
    with open('registrations.json', 'r') as file:
        data = json.load(file)
    return render_template('view.html', registrations=data)





#return render_template('contact_form.html')