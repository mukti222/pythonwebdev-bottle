from bottle import route, post, run, static_file, request
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
#### tambahan 1
def query2(sql, param):
    conn = psycopg2.connect("dbname=coba user=postgres password=mukti") # 172.17.0.2 / localhost / 127.0.0.1
    cur = conn.cursor()
    cur.execute(sql, param)
    conn.commit()
    cur.close()
    conn.close()
#### tambahan 1


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
###tambahan 1
################# save edit #####################
@post('/save_mahasiswa')
def save_mahasiswa():
    ###############  ambil data input form  ###################
    id = int(request.forms.get('input_id'))
    nama = request.forms.get('input_nama')
    print(nama)
    nim = request.forms.get('input_nim')
    alamat = request.forms.get('input_alamat')
    tlp = request.forms.get('input_tlp')

    ############### pengecekan isi form
    if nim == "" or nim == None:
        hasil = {'success': False, 'pesan': 'Data gagal diset karena nim masih kosong'}
    elif nama == "" or nama == None:
        hasil = {'success': False, 'pesan': 'Data gagal diset karena nama masih kosong'}
    elif alamat == "" or alamat == None:
        hasil = {'success': False, 'pesan': 'Data gagal diset karena alamat masih kosong'}
    elif tlp == "" or tlp == None:
        hasil = {'success': False, 'pesan': 'Data gagal diset karena tlp masih kosong'}
    else:
        ############ dibawah 0 ############ logika apakah run insert atau update ####
        if id > 0:
            ##########  memakai query psycopg
            query2(
                "UPDATE t_mahasiswa SET nim=%s, nama=%s, alamat=%s, tlp=%s WHERE id=%s;",
                (nim, nama, alamat, tlp, id)
                )
            hasil = {'success': True, 'pesan': 'Data Berhasil Disimpan'}
        else:
            query2(
                "insert into t_mahasiswa(nim, nama, alamat, tlp) values(%s, %s, %s, %s)",
                (nim, nama, alamat, tlp)
                )
            hasil = {'success': True, 'pesan': 'Data Berhasil Disimpan'}
    return json.dumps(hasil)
@post('/save_fakultas')
def save_fakultas():
    ###############  ambil data input form  ###################
    id = int(request.forms.get('input_id'))
    nama_fakultas = request.forms.get('input_nama_fakultas')
    print(nama_fakultas)
    jumlah_mhs = request.forms.get('input_jumlah_mhs')
    jumlah_prodi = request.forms.get('input_jumlah_prodi')

    ############### pengecekan isi form FAKULTAS
    if nama_fakultas == "" or nama_fakultas == None:
        hasil = {'success': False, 'pesan': 'Data gagal diset karena nama_fakultas masih kosong'}
    elif jumlah_mhs == "" or jumlah_mhs == None:
        hasil = {'success': False, 'pesan': 'Data gagal diset karena jumlah_mhs masih kosong'}
    elif jumlah_prodi == "" or jumlah_prodi == None:
        hasil = {'success': False, 'pesan': 'Data gagal diset karena jumlah_prodi masih kosong'}
    else:
        ############ dibawah 0 ############ logika apakah run insert atau update ####
        if id > 0:
            ##########  memakai query psycopg
            query2(
                "UPDATE t_fakultas SET nama_fakultas=%s, jumlah_mhs=%s, jumlah_prodi=%s WHERE id=%s;",
                (nama_fakultas, jumlah_mhs, jumlah_prodi, id)
                )
            hasil = {'success': True, 'pesan': 'Data Berhasil Disimpan'}
        else:
            query2(
                "insert into t_fakultas(nama_fakultas, jumlah_mhs, jumlah_prodi) values(%s, %s, %s)",
                (nama_fakultas, jumlah_mhs, jumlah_prodi)
                )
            hasil = {'success': True, 'pesan': 'Data Berhasil Disimpan'}
    return json.dumps(hasil)
@post('/save_jadwal')
def save_jadwal():
    ###############  ambil data input form  ###################
    id = int(request.forms.get('input_id'))
    kode_matkul = request.forms.get('input_kode_matkul')
    print(kode_matkul)
    nama_matkul = request.forms.get('input_nama_matkul')
    kode_dosen = request.forms.get('input_kode_dosen')
    nama_dosen = request.forms.get('input_nama_dosen')

    ############### pengecekan isi form FAKULTAS
    if kode_matkul == "" or kode_matkul == None:
        hasil = {'success': False, 'pesan': 'Data gagal diset karena kode_matkul masih kosong'}
    elif nama_matkul == "" or nama_matkul == None:
        hasil = {'success': False, 'pesan': 'Data gagal diset karena nama_matkul masih kosong'}
    elif kode_dosen == "" or kode_dosen == None:
        hasil = {'success': False, 'pesan': 'Data gagal diset karena kode_dosen masih kosong'}
    elif nama_dosen == "" or nama_dosen == None:
        hasil = {'success': False, 'pesan': 'Data gagal diset karena nama_dosen masih kosong'}
    else:
        ############ dibawah 0 ############ logika apakah run insert atau update ####
        if id > 0:
            ##########  memakai query psycopg
            query2(
                "UPDATE t_jadwal SET kode_matkul=%s, nama_matkul=%s, kode_dosen=%s, nama_dosen=%s WHERE id=%s;",
                (kode_matkul, nama_matkul, kode_dosen, nama_dosen, id)
                )
            hasil = {'success': True, 'pesan': 'Data Berhasil Disimpan'}
        else:
            query2(
                "insert into t_jadwal(kode_matkul, nama_matkul, kode_dosen, nama_dosen) values(%s, %s, %s, %s)",
                (kode_matkul, nama_matkul, kode_dosen, nama_dosen)
                )
            hasil = {'success': True, 'pesan': 'Data Berhasil Disimpan'}
    return json.dumps(hasil)

##################  hapus   ######################
@post('/hapus_mahasiswa')
def hapus_mahasiswa():
    id = int(request.forms.get('id'))
    nim = request.forms.get('nim')
    nama = request.forms.get('nama')
    if nim == "" or nim == None:
        hasil = {'success': False, 'pesan': 'Data gagal dihapus karena nim masih kosong'}
    elif nama == "" or nama == None:
        hasil = {'success': False, 'pesan': 'Data gagal dihapus karena nama masih kosong'}
    else:
        query2("delete from t_mahasiswa where id=%(int)s", {'int': id})
        hasil = {'success': True, 'pesan': 'Data ('+nama+') Berhasil Dihapus'}
    return json.dumps(hasil)
@post('/hapus_fakultas')
def hapus_fakultas():
    id = int(request.forms.get('id'))
    nama_fakultas = request.forms.get('nama_fakultas')
    # nama = request.forms.get('nama')
    if nama_fakultas == "" or nama_fakultas == None:
        hasil = {'success': False, 'pesan': 'Data gagal dihapus karena fakultas masih kosong'}
    # elif nama == "" or nama == None:
    #     hasil = {'success': False, 'pesan': 'Data gagal dihapus karena nama masih kosong'}
    else:
        query2("delete from t_fakultas where id=%(int)s", {'int': id})
        hasil = {'success': True, 'pesan': 'Data ('+nama_fakultas+') Berhasil Dihapus'}
    return json.dumps(hasil)
@post('/hapus_jadwal')
def hapus_jadwal():
    id = int(request.forms.get('id'))
    kode_matkul = request.forms.get('kode_matkul')
    # nama = request.forms.get('nama')
    if kode_matkul == "" or kode_matkul == None:
        hasil = {'success': False, 'pesan': 'Data gagal dihapus karena kode_matkul masih kosong'}
    # elif nama == "" or nama == None:
    #     hasil = {'success': False, 'pesan': 'Data gagal dihapus karena nama masih kosong'}
    else:
        query2("delete from t_jadwal where id=%(int)s", {'int': id})
        hasil = {'success': True, 'pesan': 'Data ('+kode_matkul+') Berhasil Dihapus'}
    return json.dumps(hasil)
###tambahan 1
# kode_matkul
# nama_matkul
# kode_dosen
# nama_dosen

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