import socketserver

serverName = "localhost"
serverPort = 80
# url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
url = "https://media.tenor.com/wa4aIHG-dT0AAAAC/eating-cake.gif"


class RedirectRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Receive data from the client (if needed)
        # data = self.request.recv(1024)

        # Send the redirect response to the client
        response = f"HTTP/1.1 302 Found\nLocation: {url}\n\n"
        self.request.sendall(response.encode("utf-8"))


if __name__ == "__main__":
    with socketserver.TCPServer((serverName, serverPort), RedirectRequestHandler) as server:
        server.serve_forever()
