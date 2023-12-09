from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)

debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/story')
def story():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    generatedStory = stories.story.generate({"place":place, "noun": noun, "verb": verb, "adjective":adjective, "plural_noun": plural_noun})
    return render_template("story.html",generatedStory = generatedStory)