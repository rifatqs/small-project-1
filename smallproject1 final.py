import psycopg2

def pilihan():

    print (" ")
    print ("                    SMALL PROJECT 1                  ")
    print ("masukan angka 1 untuk user melihat invoiceid melakukan pembayaran awal tahun")
    print ("masukan angka 2 untuk user melihat invoiceid melakukan pembayaran akhir tahun")
    print ("masukan angka 3 untuk user melihat invoiceid yb belum melakukan pembayaran")
    print ("masukan angka 0 untuk keluar app")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    angka = input ("masukan angka =  ")
    try:
        connection = psycopg2.connect(user="postgres", 
                                    password="postgres",
                                    host="localhost",
                                    port="5432",
                                    database="small_project1")
        cursor = connection.cursor()
  
  
        if(angka == '1'):
            a = 'SELECT invoiceID FROM awal_tahun'
            cursor.execute(a)
            awal_tahun = cursor.fetchall()
            for x in (awal_tahun):
                print('Terima kasih telah melakukan pembayaran pada invoice ' + x[0] + " Anda berhak mendapatkan diskon awal tahun sebesar 10%")
    
        elif(angka == '2'):
            b = 'SELECT invoiceID FROM akhir_tahun'
            cursor.execute(b)
            akhir_tahun = cursor.fetchall()
            for x in (akhir_tahun):
                print('Terima kasih telah melakukan pembayaran pada invoice ' + x[0] + " Anda berhak mendapatkan diskon akhir tahun sebesar 20%")
    
        elif(angka == '3'):
            c = 'SELECT invoiceID FROM belum_bayar'
            cursor.execute(c)
            belum_bayar = cursor.fetchall()
            for x in (belum_bayar):
                print('yuk segera bayar tagihan invoice ' + x[0] + " dan dapatkan diskon sebesar 15%")

        elif(angka == '0'):
                exit()

        else:
            print("angka yg anda masukan salah, pilih lagi")
            pilihan() 

    except (Exception, psycopg2.Error) as error:
            print("Failed connect", error)


if __name__ == "__main__":
    while True:
        pilihan()
