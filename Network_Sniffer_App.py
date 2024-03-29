# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Basic_Packet_Sniffer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread, Event
import socket
import struct
import textwrap


class Ui_Basic_Packet_Sniffer(object):
    def setupUi(self, Basic_Packet_Sniffer):
        Basic_Packet_Sniffer.setObjectName("Basic_Packet_Sniffer")
        Basic_Packet_Sniffer.resize(748, 443)
        Basic_Packet_Sniffer.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        Basic_Packet_Sniffer.setAccessibleName("")
        self.verticalLayoutWidget = QtWidgets.QWidget(Basic_Packet_Sniffer)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(570, 20, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ButtonStart = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ButtonStart.setObjectName("ButtonStart")
        self.verticalLayout.addWidget(self.ButtonStart)
        self.ButtonStop = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ButtonStop.setObjectName("ButtonStop")
        self.verticalLayout.addWidget(self.ButtonStop)
        self.tableWidget = QtWidgets.QTableWidget(Basic_Packet_Sniffer)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 721, 321))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(20)
#        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)



        self.numRow=0
        self.retranslateUi(Basic_Packet_Sniffer)
        QtCore.QMetaObject.connectSlotsByName(Basic_Packet_Sniffer)

    def retranslateUi(self, Basic_Packet_Sniffer):
        _translate = QtCore.QCoreApplication.translate
        Basic_Packet_Sniffer.setWindowTitle(_translate("Basic_Packet_Sniffer", "Basic Packet Sniffer"))
        self.ButtonStart.setText(_translate("Basic_Packet_Sniffer", "Start"))
        self.ButtonStop.setText(_translate("Basic_Packet_Sniffer", "Stop"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Basic_Packet_Sniffer", "Dest MAC"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Basic_Packet_Sniffer", "Src MAC"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Basic_Packet_Sniffer", "Protocol"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Basic_Packet_Sniffer", "IPv4 Version"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Basic_Packet_Sniffer", "IPv4 Header Length"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Basic_Packet_Sniffer", "IPv4 TTL"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Basic_Packet_Sniffer", "IPv4 Protocol"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Basic_Packet_Sniffer", "Dest IP"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Basic_Packet_Sniffer", "Src IP"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Basic_Packet_Sniffer", "Dest Port"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Basic_Packet_Sniffer", "Src Port"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Basic_Packet_Sniffer", "Sequence"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Basic_Packet_Sniffer", "Acknowledgment"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Basic_Packet_Sniffer", "Flags[URG]"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Basic_Packet_Sniffer", "Flags[ACK]"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Basic_Packet_Sniffer", "Flags[PSH]"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Basic_Packet_Sniffer", "Flags[RST]"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("Basic_Packet_Sniffer", "Flags[SYN]"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("Basic_Packet_Sniffer", "Flags[FIN]"))        
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("Basic_Packet_Sniffer", "DATA"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def  add_table_item(self, Basic_Packet_Sniffer,data):
        _translate = QtCore.QCoreApplication.translate
        self.tableWidget.setRowCount(self.numRow+1)

        for i in range(20):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(self.numRow, i, item)
        for j in range (20):
                item = self.tableWidget.item(self.numRow, j)
                item.setText(_translate("Basic_Packet_Sniffer", str(data[j]) ))            
        self.numRow +=1



def get_mac_addr(mac_raw):
    byte_str = map('{:02x}'.format, mac_raw)
    mac_addr = ':'.join(byte_str).upper()
    return mac_addr


def format_multi_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])

def ethernet_head(raw_data):

    dest, src, prototype = struct.unpack('! 6s 6s H', raw_data[:14])

    dest_mac = get_mac_addr(dest)
    src_mac = get_mac_addr(src)
    proto = socket.htons(prototype)
    data = raw_data[14:]
    return dest_mac, src_mac, proto, data 

def http(raw_data):
    try:
        data = raw_data.decode('utf-8')
    except:
        data = raw_data
    return data

def icmp_head(raw_data):
    packet_type, code, checksum = struct.unpack('! B B H', raw_data[:4])
    data = raw_data[4:]
    return packet_type, code, checksum, data 

def ipv4_head(raw_data):
    version_header_length = raw_data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', raw_data[:20])
    src = get_ip(src)
    target = get_ip(target)
    data = raw_data[header_length:]
    return version_header_length, version, header_length, ttl, proto, src, target, data

def get_ip(addr):
    return '.'.join(map(str, addr))

def tcp_head( raw_data):
    (src_port, dest_port, sequence, acknowledgment, offset_reserved_flags) = struct.unpack(
        '! H H L L H', raw_data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1
    data = raw_data[offset:]
    return src_port, dest_port, sequence, acknowledgment, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data

def udp_head(raw_data):
    src_port, dest_port, size = struct.unpack('! H H 2x H', raw_data[:8])
    data = raw_data[8:]
    return src_port, dest_port, size, data



def main(ui,Basic_Packet_Sniffer,event: Event):
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    data =[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
    while True:
        raw_data, addr = s.recvfrom(65535)
        eth = ethernet_head(raw_data)
#        print('\nEthernet Frame:')
#        print('Destination: {}, Source: {}, Protocol: {}'.format(eth[0], eth[1], eth[2]))
        data[0],data[1],data[2]=eth[0], eth[1], eth[2]
        if eth[2] == 8:
            ipv4 = ipv4_head(eth[3])
#            print('\t -' + 'IPv4 Packet:')
#            print('\t\t -' + 'Version: {}, Header Length: {}, TTL: {},'.format(ipv4[1], ipv4[2], ipv4[3]))
#            print('\t\t -' + 'Protocol: {}, Source: {}, Target: {}'.format(ipv4[4], ipv4[5], ipv4[6]))
            data[3],data[4],data[5],data[6],data[7],data[8]=ipv4[1], ipv4[2], ipv4[3],ipv4[4], ipv4[6], ipv4[5]
            # TCP
            if ipv4[4] == 6:
                tcp = tcp_head(ipv4[7])
#                print('\t -' + 'TCP Segment:')
#                print('\t\t -' + 'Source Port: {}, Destination Port: {}'.format(tcp[0], tcp[1]))
#                print('\t\t -' + 'Sequence: {}, Acknowledgment: {}'.format(tcp[2], tcp[3]))
#                print('\t\t -' + 'Flags:')
#                print('\t\t\t -' + 'URG: {}, ACK: {}, PSH: {}'.format(tcp[4], tcp[5], tcp[6]))
#                print('\t\t\t -' + 'RST: {}, SYN: {}, FIN:{}'.format(tcp[7], tcp[8], tcp[9]))
                data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18]=tcp[0], tcp[1],tcp[2], tcp[3],tcp[4], tcp[5], tcp[6],tcp[7], tcp[8], tcp[9]
                if len(tcp[10]) > 0:

                    # HTTP
                    data[19]=tcp[10]
                    #if tcp[0] == 80 or tcp[1] == 80:
#                        print('\t\t -' + 'HTTP Data:')
 #                       try:
 #                           http = http(tcp[10])
 #                           http_info = str(http[10]).split('\n')
 #                           for line in http_info:
 #                               print('\t\t\t' + str(line))
 #                       except:
 #                           print(format_multi_line('\t\t\t', tcp[10]))
 #                   else:
 #                       print('\t\t -' + 'TCP Data:')
 #                       print(format_multi_line('\t\t\t', tcp[10]))


            # ICMP
            elif ipv4[4] == 1:
                icmp = icmp_head(ipv4[7])
               # print('\t -' + 'ICMP Packet:')
               # print('\t\t -' + 'Type: {}, Code: {}, Checksum: {},'.format(icmp[0], icmp[1], icmp[2]))
               # print('\t\t -' + 'ICMP Data:')
               # print(format_multi_line('\t\t\t', icmp[3]))
                data[19]= "TCMP packet :'type':{},code:{},Checksum: {} ICMP Data: \t\t\t {}".format(icmp[0], icmp[1], icmp[2],icmp[3])
            elif ipv4[4] == 17:
                udp = udp_head(ipv4[7])
               # print('\t -' + 'UDP Segment:')
               # print('\t\t -' + 'Source Port: {}, Destination Port: {}, Length: {}'.format(udp[0], udp[1], udp[2]))
                data[9],data[10] = udp[0], udp[1]

        # Other IPv4
            else:
                #print('\t -' + 'Other IPv4 Data:')
                #print(format_multi_line('\t\t', ipv4[7]))
                data[19]="Other IPv4 Data: \t\t\t {}".format(ipv4[7])

        else:
            #print('Ethernet Data:')
            #print(format_multi_line('\t', eth[3]))
            data[19] ="Ethernet DATA : {}".format (eth[3])
        ui.add_table_item(Basic_Packet_Sniffer,data)
        if event.is_set():
            print('The thread was stopped prematurely.')
            break


        
if __name__ == "__main__":
    import sys
    data=["3C:F8:62:32:60:5E", "48:EE:0C:15:51:8E","8","4","20","241","6","35.174.210.7","192.168.1.40""443","33616" , 4243330590, 4155262881," 0",1, 1,0,0, 0,'data']
    event = Event()
    app = QtWidgets.QApplication(sys.argv)
    Basic_Packet_Sniffer = QtWidgets.QDialog()
    ui = Ui_Basic_Packet_Sniffer()
    ui.setupUi(Basic_Packet_Sniffer)
#    ui.add_table_item(Basic_Packet_Sniffer,data)
#    ui.add_table_item(Basic_Packet_Sniffer,data)
    sniff = Thread(target=main,args=(ui,Basic_Packet_Sniffer,event))
    ui.ButtonStart.clicked.connect(sniff.start)
    ui.ButtonStop.clicked.connect(event.set )
    Basic_Packet_Sniffer.show()
    sys.exit(app.exec_())
    
