from bin.rcon.connection import Connection
from bin.rcon.packet import Packet, PacketType


class Console():
    def __init__(self, host, password, port):
        self._conn = Connection(host, port)
        self._id = 0
        self._login(password)

    def _get_id(self):
        self._id += 1
        return self._id

    def _login(self, password):
        req = Packet(
            id=self._get_id(),
            type=PacketType.SERVERDATA_AUTH,
            body=password
        )
        self._conn.send_packet(req)
        res = self._conn.recv_packet()
        res.print()

    def command(self, command):
        req = Packet(
            id=self._get_id(),
            type=PacketType.SERVERDATA_EXECCOMMAND,
            body=command
        )
        self._conn.send_packet(req)
        res = self._conn.recv_packet()
        #res.print()
        return res.print()


        
        
        
    def close(self):
        self._conn.close()
