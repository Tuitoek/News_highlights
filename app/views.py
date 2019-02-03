from flask import render_template
from app import app

# Views
@app.route('/')
def sources():

    '''
    View root page function that returns the sources page and its data
    '''
    return render_template('sources.html')
