from flask import Blueprint, render_template, request, flash
from flask_login import current_user, login_required
from .models import db, Note

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if note:
            new_note = Note(data=note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note has been created", category='success')

    return render_template('home.html', user = current_user)
