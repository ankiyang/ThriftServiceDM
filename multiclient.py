#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
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

from threading import Thread
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import time


def create_client(num):
    print num
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    multiprocessor = TMultiplexedProtocol(protocol, 'FirstHandler')
    client = MyFirstService.Client(multiprocessor)

    # client = MyFirstService.Client(protocol)

    sec_multiprocessor = TMultiplexedProtocol(protocol, 'SecondHandler')
    sec_client = MyFirstService.Client(sec_multiprocessor)

    transport.open()

    # print time.time()
    print client.multiply(num, num)
    # print time.time()
    print sec_client.multiply(num, num)
    # print time.time()

    transport.close()


def main():
    a = int(time.time())
    deal_len = range(1,30)

    pool = ThreadPool(10)
    pool.map(create_client, deal_len)
    pool.close()
    pool.join()

    print "....time:", int(time.time())-a


if __name__ == '__main__':
    main()

