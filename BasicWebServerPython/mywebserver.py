"""
Author: Thanakit Yuenyongphisit

"""

import socket


class Myserver:

    def __init__(self, ip, port, dict_type=None):
        # Table of type
        if not dict_type:  # default
            dict_type = {'html': 'text/html', 'htm': 'text/html', 'gif': 'image/gif', 'jpeg': 'image/jpeg','png': 'image/png'}
        self.dict_type = dict_type

        # Set socket
        self.server_socket = socket.socket(
            socket.AF_INET,  # set protocol family to 'Internet' (INET)
            socket.SOCK_STREAM,  # set socket type to 'stream' (i.e. TCP)
            proto=0  # set the default protocol (for TCP it's IP)
        )

        self.set(ip, port, 10)
        print("Server started http://%s:%s" % self.server_socket.getsockname())

    def set(self, ip, port, backlog):  # ip, port, number of queue
        self.server_socket.bind((ip, port))  # Bind to ip and port
        self.server_socket.listen(backlog)  # Set Number of queue server can handle

    def get_file_bytes_from_req_dir_with_type(self, file):
        try:
            #
            if not file or file == 'mypage.html':  # no req file so we open html
                temp_file = open('mypage.html', 'rb')
                content = self.dict_type['html']
            else:  # file req file
                temp_file = open(file, 'rb')
                content = self.dict_type[file.split('.')[-1]]  # if key not found will throw exception

            result = temp_file.read()
            temp_file.close()
            return result, content

        except Exception as e:
            print(e)
            return None, None

    @staticmethod
    def get_method_version_req_dir(req: str):  # Use to get each value of req method, req_dir
        req_arr = req.split(" ")
        method = req_arr[0]
        try:
            req_dir = req_arr[1].lstrip("/").split("?")[0]
            version = req_arr[2].split('\r\n')[0]
        except Exception as e:
            print(req)
            raise e

        return method, version, req_dir

    @staticmethod
    def header_generate(*args):
        header = ""
        for each in args:
            header += each
            header += "\r\n"

        # end of header
        header += '\r\n'
        return header

    def get_request(self):
        client_sock, client_addr = self.server_socket.accept()
        print("Connected by:", client_addr[0], client_addr[1])

        # Waiting for request
        req = client_sock.recv(1024).decode()

        # get method and directory of file
        method, version, req_dir = self.get_method_version_req_dir(req)

        # get the response bytes code and content_type
        response, content_type = self.get_file_bytes_from_req_dir_with_type(req_dir)

        # Normal case
        if response:
            # Prepare header and response, encoding
            # In this assignedment fixed to be HTTP/1.0 so i override the version
            version = "HTTP/1.0"
            if content_type == 'text/html':  # Case html
                header = self.header_generate(version + ' 200 OK', 'content-Type: ' + content_type + "; TIS-620")
                response = response.decode()
                response = response.encode('TIS-620')  # encode html file

            else:  # Case other data
                header = self.header_generate(version + ' 200 OK', 'content-Type: ' + content_type + "; UTF-8")
                # no need to decode and encode on other type file

            header = header.encode('UTF-8')
            # Send header
            client_sock.sendall(header)
            # Send body
            client_sock.sendall(response)
        # error case
        else:

            header = self.header_generate(version + ' 404 Not Found', 'content-Type: ' + 'text/html' + "; UTF-8")
            header = header.encode('UTF-8')

            client_sock.sendall(header)
            response = '<html><body><h1>404 Not found</h1></body></html>'.encode('UTF-8')
            client_sock.sendall(response)
        # close connection
        client_sock.close()

    def run(self):
        while True:
            try:
                self.get_request()
            except Exception as e:
                print(e)


if __name__ == "__main__":  # invoke only when called by it self
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    x = Myserver(ip_address, 5000)
    x.run()
