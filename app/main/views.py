from flask import render_template,redirect ,url_for, abort
from . import main
from flask_login import login_required
from ..models import  User,Pitches
from .forms import UpdateProfile,PitchesForm
from .. import db


# Views
@main.route('/')
@login_required
def index():
    pitches = Pitches.query.all()
    name= pitches[1].u_name
    return render_template('index.html', pitches= pitches, name= name)


@main.route('/user/<uname>',methods = ['GET','POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    userid = user.id
    use = user.username
    form = PitchesForm()
    p = Pitches(pitch= form.pitch.data, upvote= 0, downvote= 0 , u_name= use)
    db.session.add(p)
    db.session.commit()
    pitches = Pitches.query.filter_by( u_name = use).all()
    
    
    if user is None:
        abort(404)
    

    return render_template("profile/profile.html", user = user, pitches= pitches, form = form)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)