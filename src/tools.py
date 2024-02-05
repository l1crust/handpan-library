import re
import requests 
import time
from requests.exceptions import ConnectionError

proxies = {
   'http': 'http://localhost:8080',
   'https': 'http://localhost:8080',
}


def get_scale_videos(scale):
	url = "https://web.archive.org/web/20201019042409/https://sites.google.com/site/handpanscales/home/" + scale

	try: 
		r = requests.get(url, allow_redirects=True)
	except ConnectionError:
		print("connection refused. Waiting 30 s")
		time.sleep(30)
		return get_scale_videos(scale)

	video_ids = re.findall(r'youtube\.com\/embed\/([\w-]+)', r.text)
	return video_ids


def get_scale_list():
	return  ['blues', 'caspian', 'celtic-minor', 'chad-gayo', 'chandhra', 'da-xiong-diao', 'dad', 'daxala', 'debac', 'deshvara', 'devarangi', 'dominant-7th', 'dorian', 'double-phrygian', 'ebbtide', 'egyptian', 'el-dorado', 'elion', 'elysian', 'emmanuel', 'equinox', 'fifth-mode', 'free-integral', 'genus', 'geyahajjajji', 'golden-gate', 'goonkali', 'gopikatilaka', 'gowleeswari', 'harmonic-minor', 'harmonic-niner', 'hijaz--hitzaz', 'hijazkiar-hitzazkiar', 'hiperaeolian', 'hira-joshi', 'hokkaido', 'honchishi', 'hungarian-major', 'huzam', 'hyboreal', 'insen', 'integral', 'inuit', 'ionian', 'ionian-pentatonic', 'iwato', 'jiao', 'jibuk', 'kaffa', 'kambhoji', 'kapijingla', 'kedaram', 'khyberi', 'kiavara', 'king-island', 'klezmera', 'kokin-joshi', 'konundrum', 'kourd-atar', 'kumari', 'kumo', 'kurd', 'la-sirena', 'lalabye', 'lalanta', 'limoncello', 'locrian', 'longloy', 'lydian', 'magic-hour', 'mahara', 'melog-selisir', 'migration', 'minor-pentatonic', 'mixo', 'mixolydian', 'mixophonic', 'mondhra', 'monsoon', 'mysorean', 'nihavend', 'noh', 'north-sea', 'olimpia', 'olympos', 'onoleo', 'overtone', 'oxalis', 'paradise', 'paradiso', 'pentatonic-blues', 'phrygian', 'purvi', 'pygmalion', 'pygmy', 'pyramid', 'raga-dejani', 'raga-desh', 'raga-desh-1', 'raga-desya-todi', 'raja', 'riverrun', 'riviera', 'rufinus', 'ruga', 'russian-major', 'sabye', 'sahara', 'saharian', 'saladin', 'saudade', 'shakti', 'shang', 'shang-diao', 'shiraz', 'silverado', 'peanut-butter', 'spyner', 'subvoyage', 'suddha', 'sundown', 'synthesis', 'talaysai', 'tharsi', 'ujo', 'ursa-minor', 'wadi-rum', 'xiao-xiong-diao', 'yshasavita', 'yu-shan-diao', 'banshiki-cho', 'zheng', 'zhi-diao', 'zokuso']
	# html = open("temp.html", "r").read()
	# scales = re.findall(r'<a href="\/web\/20201019042442\/https:\/\/sites\.google\.com\/site\/handpanscales\/home\/([\w-]+)', html)
	# return scales

def convert_to_csv():
	entries = open("temp.csv", "r").readlines()
	for l in entries:
		scale = l.split(";")[0]
		vidId = l.split(";")[1].strip('\n')
		print("http://www.youtube.com/embed/{},{},,".format(vidId,scale))

#get_scale_videos("konundrum")
# scales = get_scale_list()
# print(scales)
# for scale in scales:
# 	videoId = get_scale_videos(scale)
# 	for v in videoId:
# 		print("{};{}".format(scale, v))
convert_to_csv()