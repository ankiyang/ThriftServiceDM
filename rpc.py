#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from thrift.transport import TSocket
from thrift.transport.TTransport import TBufferedTransportFactory
from thrift.protocol.TBinaryProtocol import TBinaryProtocolFactory

from thrift.server.TServer import TSimpleServer


def make_server(service, handler,
                host='localhost', port=9090, unix_socket=None,
                trans_factory=TBufferedTransportFactory(),
                proto_factory=TBinaryProtocolFactory()):

    if unix_socket:
        server_socket = TSocket.TServerSocket(unix_socket=unix_socket)
    elif host and port:
        server_socket = TSocket.TServerSocket(host=host, port=9090)
    else:
        raise ValueError("Either host/port or unix_socket must be provided.")

    processor = service.Processor(handler())

    server = TSimpleServer(processor, server_socket, trans_factory,
                           proto_factory)

    return server


def make_client(service, host="localhost", port=9090, unix_socket=None,
                trans_factory=TBufferedTransportFactory(),
                proto_factory=TBinaryProtocolFactory()):

    socket = TSocket.TSocket(host, port)
    transport = trans_factory.getTransport(socket)
    protocol = proto_factory.getProtocol(transport)
    client = service.Client(protocol)

    transport.open()
    client.log('logile.log')
    print client.multiply(2, 21)
    transport.close()
    pass