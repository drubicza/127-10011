import os, sys, time, random, socket, select, datetime, threading
from time import sleep as timeout

def rus(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)


def tes(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)


sys.stdout.write('\x1b]2;POLOSAN TELKOMSEL @Mr.Tr3v!0n Channel Youtube: Tutorial Android\x07')
os.system('clear')
print '\x1b[32;1m    __________________________'
time.sleep(1)
rus('\n\x1b[39;1m     Jangan lupa subscribe \n     channel youtube admin\n     dan aktifkan notifikasi \n     lonceng nya...\n     nama channel nya adalah\n     \x1b[32;1mTutorial Android-ID\n')
print '\x1b[32;1m    __________________________'
print '\x1b[32;1m    __________________________'
time.sleep(1)
rus('\n\x1b[39;1m     Silahkan Setting psiphone \n      nya lalu isikan :\n      \x1b[34;1mHost Adress: \x1b[35;1m127.1.1.8\n      \x1b[34;1mPort: \x1b[35;1m10011\n     \x1b[39;1mSilahkan hidupkan Psiphone nya\n')
print '\x1b[32;1m    __________________________'
print '\n'
time.sleep(5)
lock = threading.RLock()
os.system('cls' if os.name == 'nt' else ' ')

def real_path(file_name):
    return os.path.dirname(os.path.abspath(__file__)) + file_name


def filter_array(array):
    for i in range(len(array)):
        array[i] = array[i].strip()
        if array[i].startswith('#'):
            array[i] = ''

    return [ x for x in array if x ]


def colors(value):
    patterns = {'R1': '\x1b[31;1m',
       'R2': '\x1b[36;2m', 'G1': '\x1b[32;1m',
       'Y1': '\x1b[33;1m', 'P1': '\x1b[35;1m',
       'CC': '\x1b[0m'}
    for code in patterns:
        value = value.replace(('[{}]').format(code), patterns[code])

    return value


def log(value, status='', color=''):
    value = colors(('{value}[CC]').format(time=datetime.datetime.now().strftime(''), value=value, color=color, status=status))
    with lock:
        print value


def log_replace(value, status='[ Rusmana-ID ]', color='[G1]'):
    value = colors(('{}{} ({})        [CC]\r').format(color, status, value))
    with lock:
        sys.stdout.write(value)
        sys.stdout.flush()


class inject(object):

    def __init__(self, inject_host, inject_port):
        super(inject, self).__init__()
        self.inject_host = str(inject_host)
        self.inject_port = int(inject_port)

    def log(self, value, color='[G1]'):
        log(value, color=color)

    def start(self):
        try:
            socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_server.bind((self.inject_host, self.inject_port))
            socket_server.listen(1)
            frontend_domains = open(real_path('/___server__id___.py')).readlines()
            frontend_domains = filter_array(frontend_domains)
            if len(frontend_domains) == 0:
                self.log('___server__id___.py tidk ada', color='[R1]')
                return
            self.log(('').format(self.inject_host, self.inject_port))
            while True:
                socket_client, _ = socket_server.accept()
                socket_client.recv(4096)
                domain_fronting(socket_client, frontend_domains).start()

        except Exception as exception:
            self.log(('').format(self.inject_host, self.inject_port), color='[R1]')


class domain_fronting(threading.Thread):

    def __init__(self, socket_client, frontend_domains):
        super(domain_fronting, self).__init__()
        self.frontend_domains = frontend_domains
        self.socket_tunnel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_client = socket_client
        self.buffer_size = 9999
        self.daemon = True

    def log(self, value, status='FREE INTERNET INDONESIA', color='[G1]'):
        log(value, status=status, color=color)

    def handler(self, socket_tunnel, socket_client, buffer_size):
        sockets = [
         socket_tunnel, socket_client]
        timeout = 0
        while True:
            timeout += 1
            socket_io, _, errors = select.select(sockets, [], sockets, 3)
            if errors:
                break
            if socket_io:
                for sock in socket_io:
                    try:
                        data = sock.recv(buffer_size)
                        if not data:
                            break
                        elif sock is socket_client:
                            socket_tunnel.sendall(data)
                        elif sock is socket_tunnel:
                            socket_client.sendall(data)
                        timeout = 0
                    except:
                        break

            if timeout == 60:
                break

    def run(self):
        try:
            self.proxy_host_port = random.choice(self.frontend_domains).split(':')
            self.proxy_host = self.proxy_host_port[0]
            self.proxy_port = self.proxy_host_port[1] if len(self.proxy_host_port) >= 2 and self.proxy_host_port[1] else '443'
            self.log(('\x1b[39;1m[ \x1b[31;1mBELUM KONEK \x1b[39;1m]\x1b[32;1m@>\x1b[31;1m[ \x1b[35;1mStatus 404 No \x1b[31;1m]').format(self.proxy_host, self.proxy_port))
            self.socket_tunnel.connect((str(self.proxy_host), int(self.proxy_port)))
            self.socket_client.sendall('HTTP/1.1 200 OK\r\n\r\n')
            self.handler(self.socket_tunnel, self.socket_client, self.buffer_size)
            self.socket_client.close()
            self.socket_tunnel.close()
            os.system('clear')
            print '\x1b[31;1m'
            print '\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\x1b[33;1m\xe0\xae\x9c\xdb\xa9\xf0\x9f\x94\xb0\xdb\xa9\xe0\xae\x9c\x1b[31;1m\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac'
            print '\x1b[34;1m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97'
            print '\x1b[34;1m\xe2\x95\x91\x1b[32;1mSCRIPT POLOSAN TELKOMSEL TERBARU 2019\x1b[34;1m\xe2\x95\x91'
            print '\x1b[34;1m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
            print '\x1b[31;1m\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac'
            print ' \x1b[34;1m Author\x1b[31;1m:\x1b[34;1mMr.Tr3v!0n\x1b[31;1m|\x1b[34;1mBlack Coder Crush'
            print '\x1b[36;1m Channel Youtube\x1b[31;1m: \x1b[35;1mTutorial Android-ID'
            print '\x1b[31;1m[ \x1b[39;1mVersion 2.0 \x1b[31;1m] \x1b[31;1m[ \x1b[39;1mQpython New Virsion \x1b[31;1m]'
            print '\x1b[31;1m\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac'
            print '\n\n '
            self.log(('\x1b[39;1m[ \x1b[32;1mSUDAH KONEK \x1b[39;1m]\x1b[32;1m@>\x1b[31;1m[ \x1b[36;1mStatus 200 OK \x1b[31;1m]\n\x1b[39;1mCONNECT [host_port] [protocol][crlf]Host: \nmy.telkomsel.info[crlf]X-Online-Host: \nmy.telkomsel.info[crlf]X-Forward-Host: \nmy.telkomsel.info[crlf]X-Forwarded-For: \nmy.telkomsel.info[crlf]Connection: Keep-Alive[crlf][crlf]').format(self.proxy_host, self.proxy_port), color='[R1]')
        except OSError:
            self.log('Connection error', color='[R1]')


def main():
    print colors(('\n').join([]))
    inject('127.1.1.8', '10011').start()


if __name__ == '__main__':
    main()
