import struct

HEADER_SIZE = 15

class Header:
    def __init__(self, src_port, dst_port, seq_num, ack_num, data_len, syn, ack, fin, new_port):
        self.src_port = src_port
        self.dst_port = dst_port
        self.seq_num = seq_num
        self.ack_num = ack_num
        self.data_len = data_len
        self.syn = syn
        self.ack = ack
        self.fin = fin
        self.new_port = new_port


    def serialize(self):
        # '!HHLLHB' es un string que usamos para formatear
        # '> es para especificar que utilizaremos big endian,
        # H significa que es un unsigned short (2 bytes)
        # L significa que es un unsigned long (4 bytes)
        # B significa que es un unsigned char (1 byte)
        # El orden en el que se pasan los argumentos es el orden en el que se empaquetarán
        flags = (self.syn << 3) | (self.ack << 2) | (self.fin << 1) | self.new_port
        return struct.pack('>HHLLHB', self.src_port, self.dst_port, self.seq_num, self.ack_num, self.data_len, flags)

    @classmethod
    def deserialize(cls, data):
        src_port, dst_port, seq_num, ack_num, data_len, flags = struct.unpack('>HHLLHB', data)
        syn = bool(flags & 0b1000)
        ack = bool(flags & 0b0100)
        fin = bool(flags & 0b0010)
        new_port = bool(flags & 0b0001)
        return cls(src_port, dst_port, seq_num, ack_num, data_len, syn, ack, fin, new_port)