import socket
import psycopg2


buffer_size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9999))
sock.listen(1)
print('Sock name: {}'.format(sock.getsockname()))


conn = psycopg2.connect(
    database='tracking',
    user='postgres',
    password='************',
    host='127.0.0.1',
    port='5432'
)
print("Database opened successfully")


conn.autocommit = True
cursor = conn.cursor()
# cursor.execute('''DROP TABLE car_data_info'')


while True:
    conn, addr = sock.accept()
    print('Connection address: {}'.format(addr))

    all_data = []

    while True:
        data = conn.recv(buffer_size)
        if not data:
            break

        conn.send(data)
        byte_decode = data.decode('utf-8')
        all_data = byte_decode.split(', ')
        print('Machine data: {}'.format(all_data))
        cursor.execute("INSERT into car_data_info(car_brand, driver, car_number, date, speed, coordinates, "
                       "fuel_condition, run)"
                       "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(all_data[0], all_data[1],
                        all_data[2], all_data[3], all_data[4], all_data[5], all_data[6], all_data[7]))

        print("List has been inserted to CAR table successfully...")

    print('Close')
    conn.close()