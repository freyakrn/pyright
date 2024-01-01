import mysql.connector
import matplotlib as plt

def connectionDatabase() :
    connector = mysql.connector.connect(
            host="localhost",
            user="root",
            port = 3307,
            password="",
            database="uty"
        )
    if connector.is_connected :
        print("Database terkoneksi")
        return connector
    else :
        print("Database gagal terkoneksi")
        return False
    
def insertData(nim, nama, mtk, ipa, agama) :
    try :
        conn = connectionDatabase()
        cursor = conn.cursor()
        sql = "INSERT INTO nilai (nim, nama, mtk, ipa, agama) VALUES (%s, %s, %s, %s, %s)"
        data = (nim, nama, mtk, ipa, agama)
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil ditambah")
    except mysql.connector.Error as error :
        print("Terjadi kesalahan : ", error)
    finally :
        if conn.is_connected :
            cursor.close()
            conn.close()

def selectData(inputUser) :
    try :
        conn = connectionDatabase()
        cursor = conn.cursor()
        sql = "SELECT agama, ipa, mtk FROM nilai WHERE nim = %s"
        search = (inputUser,)
        cursor.execute(sql, search)
        result = cursor.fetchall()
        if result :
            print("Data ditemukan!")
            for i in result :
                matkul = ["agama", "ipa", "mtk"]
                hasil = i
                plt.bar(matkul, hasil)
                plt.show()
        else :
            print("Data tidak ditemukan")
    except mysql.connector.Error as error :
        print("Terjadi kesalahan : ", error)
    finally :
        if conn.is_connected :
            cursor.close()
            conn.close()

def updateData(nama, mtk, agama, ipa, nim) :
    try :
        conn = connectionDatabase()
        cursor = conn.cursor()
        sql = "UPDATE nilai SET nama = %s, mtk = %s, agama = %s, ipa = %s WHERE nim = %s"
        data = (nama, mtk, agama, ipa, nim)
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil diubah")
    except mysql.connector.Error as error :
        print("Terjadi kesalahan : ", error)
    finally :
        if conn.is_connected :
            cursor.close()
            conn.close()

def deleteData(nim) :
    try :
        conn = connectionDatabase()
        cursor = conn.cursor()
        sql = "DELETE FROM nilai WHERE nim = %s"
        data = (nim,)
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil dihapus")
    except mysql.connector.Error as error :
        print("Terjadi kesalahan : ", error)
    finally :
        if conn.is_connected :
            cursor.close()
            conn.close()

def mainMenu() :
    print("====================")
    print("===== WELCOME! =====")
    print("====================")
    print("1. Show visualisation")
    print("2. Input data")
    print("3. Edit data")
    print("4. Delete data")
    print("5. Exit")

while True :
    mainMenu()
    pilih = int(input("Input your choice of menu [1-5] : "))
    if pilih == 1 :
        nim = int(input("Input the NIM of the college students : "))
        selectData(nim)
    elif pilih == 2 :
        inputanNim = int(input("Input your NIM : "))
        inputanNama = input("Input your name : ")
        inputanMtk = int(input("Input your MTK score : "))
        inputanIpa = int(input("Input your IPA score : "))
        inputanAgama = int(input("Input your Agama score : "))
        insertData(inputanNim, inputanNama, inputanMtk, inputanIpa, inputanAgama)
    elif pilih == 3 :
        editNama = input("Input your new name : ")
        editMtk = int(input("Input your new MTK score : "))
        editAgama = int(input("Input your new Agama score : "))
        editIpa = int(input("Input your new IPA score : "))
        yourNim = int(input("Input your nim so that we know who to edit : "))
        updateData(editNama, editMtk, editAgama, editIpa, yourNim)
    elif pilih == 4 :
        selectedNim = int(input("Input the NIM of the college student you want to delete : "))
        deleteData(selectedNim)
    elif pilih == 5 :
        print("You have been successfully logged out!")
        break
