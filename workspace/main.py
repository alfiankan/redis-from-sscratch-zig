import socket
import time

def main():
    """
    ini hanyalah contoh untuk mendengarkan koneksi dari redis client
    selebihnya silahkan kerjakan sendiri
    bisa menggunakan bahasa pemograman lain
    tidak ada pembatasan menggunakan stack teknologi yang lain
    ini hanyalah contoh
    namun tcp harus me listen pada port 6379 dan host 0.0.0.0
    """
    HOST = "0.0.0.0" 
    PORT = 6379  

    print("Starting server...")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                print(data)
                if not data:
                    break
                if 'PING' in data.decode():
                    conn.sendall("+PONG\r\n".encode())
                else:
                    conn.sendall("+OK\r\n".encode())


if __name__ == '__main__':
    main()
