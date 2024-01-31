from bottle import route, run, static_file


#rute"
@route("/")
def home():
    return static_file("home.html", root="halaman/")


@route("/mahasiswa")
def mahasiswa():
    return static_file("mahasiswa.html", root="halaman/")
@route("/fakultas")
def fakultas():
    return static_file("fakultas.html", root="halaman/")
@route("/jadwal")
def jadwal():
    return static_file("jadwal.html", root="halaman/")


#untuk konek ke booststrap
@route("/assets/css/<filename:re:.*\.css>")
def sejarah(filename):
    return static_file(filename, root="assets/css")
@route("/assets/js/<filename:re:.*\.js>")
def sejarah(filename):
    return static_file(filename, root="assets/js")

run(host='localhost', port=8080, debug=True)