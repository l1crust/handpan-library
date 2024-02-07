from flask import Flask, render_template, request
from store import save_youtube_to_csv, save_to_csv, get_scales_from_folder, get_entries_for_scale


app = Flask(__name__)

@app.route('/')
def index():
	scales = get_scales_from_folder()
	return render_template('index.html', scales=scales)

@app.route('/manage', methods=['GET', 'POST'])
def manage():
    if request.method == 'POST':
        # Handle the form data here
        link = request.form.get('link')
        scale = request.form.get('scales')
        notes = request.form.get('notes')
        tags = request.form.get('tags')

        # Do something with the form data (e.g., save to a database)
        # For now, let's just print them
        print(f"Link: {link}, Scale: {scale}, Notes: {notes}, Tags: {tags}")
        save_youtube_to_csv(link, scale, notes, tags)

    return render_template('manage.html')


@app.route('/scale/<scale>')
def scale_entries(scale):
    entries = get_entries_for_scale(scale)
    return render_template('scale_entries.html', scale=scale, entries=entries)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)