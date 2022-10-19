import socket
import schedule


host = '127.0.0.1'
port = 9999
buffer_size = 1024

data_car = 'MERCEDES-2312, Evgeniy_Smirnov, 770099, 28102022, 48, 2596262, 6, 2330'
# data_car = 'VOLVO-075, Ivan Petrov, 84325, 30102022, 70, 625658, 8, 2285'
byte_encode = data_car.encode()


def time():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(byte_encode)
        data = s.recv(buffer_size)
    print('-' * 90)
    print('Received data: {}'.format(data))


def main():
    schedule.every(2).seconds.do(time)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()





