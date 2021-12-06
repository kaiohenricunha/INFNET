- Para desenvolver e organizar a aplicação utilizei o VS Code e o versionamento de código com git. O TP8 e o TP9 estão contidos nos arquivos server.py e client.py. Todos os outros TPs estão em suas respectivas pastas, assim como num único jupyter notebook chamado kaio_henrique_PB_TP8.ipynb.

- O relatório final está disponível no arquivo: kaio_henrique_PB_TP9.pdf


- The application starts by importing the necessary modules.

- Then, I have the server variable to be able to use socket functions.

- The arguments passed to socket() specify the address family and socket type. AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport our messages in the network. The values passed to bind() depend on the address family of the socket.

- the HOST variable 

- The Python function socket.gethostname() returns the host name of the current system under which the Python interpreter is executed.

- HP is a variable to make it easier to pass both the HOST and the PORT to some functions.

- Larger socket buffers allow your members to distribute data and events more quickly, but they also take memory away from other things.

- When a socket has both an IP address and a port number it is said to be 'bound to a port', or 'bound to an address'. A bound socket can receive data because it has a complete address. The process of allocating a port number to a socket is called 'binding'.

- The accept() call is used by a server to accept a connection request from a client

- Where does the client and addr come from?

- from client.py

- the get_file() start by getting the directory info and, then iterates through the files in the directory checking if the objects found are actual files.

- If it's a file, it then proceeds to get the size, path, creation time, etc