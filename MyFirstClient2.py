import sys, glob

# add path with Apache Thrift compiler generated files
sys.path.append('gen-py')
# add path where built Apache Thrift libraries are
sys.path.insert(0, glob.glob('thrift-0.10.0/lib/py/build/lib.*')[0])

from first import MyFirstService
from first.ttypes import *
from first.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport 
from thrift.protocol import TBinaryProtocol
from thrift.protocol.TMultiplexedProtocol import TMultiplexedProtocol


if __name__ == '__main__':

    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # multiprocessor = TMultiplexedProtocol(protocol, '1_handler')
    # client = MyFirstService.Client(multiprocessor)

    # client = MyFirstService.Client(protocol)

    sec_multiprocessor =  TMultiplexedProtocol(protocol, 'SecondHandler')
    sec_client = MyFirstService.Client(sec_multiprocessor)


    transport.open()

    # print client.multiply(2,2)
    print sec_client.multiply(2,2)

    transport.close()



