from flask import Flask, url_for, session, Blueprint, redirect


bp = Blueprint('log_out', __name__)

@bp.route('/log_out')
def out():
    session.clear()
    return redirect(url_for('home.home'))