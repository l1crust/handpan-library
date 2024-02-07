import csv
import os


def youtube_id_to_url(videoId):
	if videoId.isalnum():
		return "http://www.youtube.com/embed/" + videoId
	else:  return ""

def save_youtube_to_csv(videoId, scale, notes, tags, filename='data/music_data.csv'):
	save_to_csv(youtube_id_to_url(videoId), scale, notes, tags, filename=filename)

def save_to_csv(url, scale, notes, tags, filename='data/music_data.csv'):
	if url != "" and scale != "":
	    with open(filename, mode='a', newline='') as file:
	        writer = csv.writer(file)
	        writer.writerow([url, scale, notes, tags])
	else:
		print("error")

def get_scales_from_folder(folder="data"):
    scales = set()
    files = os.listdir(folder)
    for file in files:
        filename = folder + "/" + file
        if os.path.isfile(filename):
            scale = get_scales_from_csv(filename=filename)
            scales.update(scale)

    orderedScales = sorted(list(scales))
    return orderedScales

def get_scales_from_csv(filename='music_data.csv'):
    scales = set()
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            scales.add(row[1])  # Assuming scale is stored in the second column
    orderedScales = sorted(list(scales))
    return orderedScales


def get_entries_for_scale(scale, folder='data'):
    entries = []
    files = os.listdir(folder)
    for file in files:
        filename = folder + "/" + file
        if os.path.isfile(filename):
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[1] == scale:  # Check if the scale matches
                        entries.append({
                            'link': row[0],
                            'scale': row[1],
                            'notes': row[2],
                            'tags': row[3]
                        })
    return entries


