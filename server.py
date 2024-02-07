from bottle import route, run, static_file
import psycopg2
import json


#############################################  konek ke db   ####################################################
def query(sql):
    conn = psycopg2.connect("dbname=coba user=postgres password=mukti")
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return data

############################################ rute untuk transfer data ###########################################
@route("/data_mhs")
def data_mhs():
    Getdata = query("select * from t_mahasiswa")
    return json.dumps(Getdata)
@route("/data_fakultas")
def data_fakultas():
    Getdata1 = query("select * from t_fakultas")
    return json.dumps(Getdata1)
@route("/data_jadwal")
def data_jadwal():
    Getdata2 = query("select * from t_jadwal")
    return json.dumps(Getdata2)


############################################ rute untuk halaman #############################################
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


######################################### untuk konek ke booststrap ############################################
@route("/assets/css/<filename:re:.*\.css>")
def sejarah(filename):
    return static_file(filename, root="assets/css")
@route("/assets/js/<filename:re:.*\.js>")
def sejarah(filename):
    return static_file(filename, root="assets/js")

run(host='localhost', port=8080, debug=True)