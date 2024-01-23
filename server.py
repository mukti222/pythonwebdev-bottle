# menentukan alamat = route 
# pip install bottle
from bottle import route, run, static_file

@route("/")
def home():
    return static_file("home.html", root= "halaman/page") #diarahkan ke folder halaman/page/home.html

@route("/sejarah")
def sejarah():
    return static_file("sejarah.html", root= "halaman/page")

@route("/tentang")
def tentang():
    return "Ini adalah halaman tentang"

@route("/tentang/visimisi")
def visimisi():
    return "ini adalah halaman tentang visimisi"

@route("/info")
def info():
    return "Ini adalah halaman info"

@route("/info/berita")
def info():
    return "Ini adalah halaman info berita"

@route("/info/pengumuman")
def info():
    return "Ini adalah halaman info pengumuman"

# menjalankan server
run(host="localhost", port=8080, debug=True)