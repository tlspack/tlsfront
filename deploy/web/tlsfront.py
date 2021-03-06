import os
import aiohttp, json
from aiohttp import web
import asyncio
import json

gstats = {}

_gstats = {"testrail-sslfront": {"192.168.125.65": [{"appSessStructNotAvail": 0, "socketBindIpv4": 3, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 1, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 1, "socketReuseSetFail": 0, "sslAcceptSuccess": 0, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 0, "sslConnInit": 0, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 0, "sslConnInitRate": 0, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 0, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 0, "tcpActiveConns": 0, "tcpConnInit": 0, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 0, "tcpConnInitProgress": 0, "tcpConnInitRate": 0, "tcpConnInitSuccess": 0, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 0, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 1, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 0, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 0, "tlsfrontThroughput": 0}, {"appSessStructNotAvail": 0, "socketBindIpv4": 3, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 1, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 1, "socketReuseSetFail": 0, "sslAcceptSuccess": 0, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 0, "sslConnInit": 0, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 0, "sslConnInitRate": 0, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 0, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 0, "tcpActiveConns": 0, "tcpConnInit": 0, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 0, "tcpConnInitProgress": 0, "tcpConnInitRate": 0, "tcpConnInitSuccess": 0, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 0, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 1, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 0, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 0, "tlsfrontThroughput": 0}, {"appSessStructNotAvail": 0, "socketBindIpv4": 3, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 1, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 1, "socketReuseSetFail": 0, "sslAcceptSuccess": 0, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 0, "sslConnInit": 0, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 0, "sslConnInitRate": 0, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 0, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 0, "tcpActiveConns": 0, "tcpConnInit": 0, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 0, "tcpConnInitProgress": 0, "tcpConnInitRate": 0, "tcpConnInitSuccess": 0, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 0, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 1, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 0, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 0, "tlsfrontThroughput": 0}], "sum": [{"appSessStructNotAvail": 0, "socketBindIpv4": 2751, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 917, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 917, "socketReuseSetFail": 0, "sslAcceptSuccess": 0, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 0, "sslConnInit": 0, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 0, "sslConnInitRate": 0, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 0, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 0, "tcpActiveConns": 0, "tcpConnInit": 0, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 0, "tcpConnInitProgress": 0, "tcpConnInitRate": 0, "tcpConnInitSuccess": 0, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 0, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 917, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 0, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 0, "tlsfrontThroughput": 0}, {"appSessStructNotAvail": 0, "socketBindIpv4": 2757, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 919, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 919, "socketReuseSetFail": 0, "sslAcceptSuccess": 0, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 0, "sslConnInit": 0, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 0, "sslConnInitRate": 0, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 0, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 0, "tcpActiveConns": 0, "tcpConnInit": 0, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 0, "tcpConnInitProgress": 0, "tcpConnInitRate": 0, "tcpConnInitSuccess": 0, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 0, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 919, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 0, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 0, "tlsfrontThroughput": 0}, {"appSessStructNotAvail": 0, "socketBindIpv4": 2763, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 921, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 921, "socketReuseSetFail": 0, "sslAcceptSuccess": 0, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 0, "sslConnInit": 0, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 0, "sslConnInitRate": 0, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 0, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 0, "tcpActiveConns": 0, "tcpConnInit": 0, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 0, "tcpConnInitProgress": 0, "tcpConnInitRate": 0, "tcpConnInitSuccess": 0, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 0, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 921, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 0, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 0, "tlsfrontThroughput": 0}], "192.168.17.249": [{"appSessStructNotAvail": 0, "socketBindIpv4": 3, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 1, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 1, "socketReuseSetFail": 0, "sslAcceptSuccess": 0, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 0, "sslConnInit": 0, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 0, "sslConnInitRate": 0, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 0, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 0, "tcpActiveConns": 0, "tcpConnInit": 0, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 0, "tcpConnInitProgress": 0, "tcpConnInitRate": 0, "tcpConnInitSuccess": 0, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 0, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 1, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 0, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 0, "tlsfrontThroughput": 0}, {"appSessStructNotAvail": 0, "socketBindIpv4": 3, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 1, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 1, "socketReuseSetFail": 0, "sslAcceptSuccess": 0, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 0, "sslConnInit": 0, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 0, "sslConnInitRate": 0, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 0, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 0, "tcpActiveConns": 0, "tcpConnInit": 0, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 0, "tcpConnInitProgress": 0, "tcpConnInitRate": 0, "tcpConnInitSuccess": 0, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 0, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 1, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 0, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 0, "tlsfrontThroughput": 0}, {"appSessStructNotAvail": 0, "socketBindIpv4": 3, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 1, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 1, "socketReuseSetFail": 0, "sslAcceptSuccess": 0, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 0, "sslConnInit": 0, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 0, "sslConnInitRate": 0, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 0, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 0, "tcpActiveConns": 0, "tcpConnInit": 0, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 0, "tcpConnInitProgress": 0, "tcpConnInitRate": 0, "tcpConnInitSuccess": 0, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 0, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 1, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 0, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 0, "tlsfrontThroughput": 0}]}, "tcpserver-sslfront": {"192.168.125.68": [{"appSessStructNotAvail": 0, "socketBindIpv4": 1615, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 1613, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 3225, "socketReuseSetFail": 0, "sslAcceptSuccess": 1612, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 10, "sslConnInit": 1612, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 1612, "sslConnInitRate": 10, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 1612, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 10, "tcpActiveConns": 0, "tcpConnInit": 1612, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 0, "tcpConnInitProgress": 0, "tcpConnInitRate": 10, "tcpConnInitSuccess": 1612, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 10, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 1, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 0, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 1612, "tlsfrontThroughput": 32768000}, {"appSessStructNotAvail": 0, "socketBindIpv4": 1625, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 1623, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 3245, "socketReuseSetFail": 0, "sslAcceptSuccess": 1622, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 10, "sslConnInit": 1622, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 1622, "sslConnInitRate": 10, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 1622, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 10, "tcpActiveConns": 0, "tcpConnInit": 1622, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 0, "tcpConnInitProgress": 0, "tcpConnInitRate": 10, "tcpConnInitSuccess": 1622, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 10, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 1, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 0, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 1622, "tlsfrontThroughput": 32309248}, {"appSessStructNotAvail": 0, "socketBindIpv4": 1635, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 1633, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 3265, "socketReuseSetFail": 0, "sslAcceptSuccess": 1632, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 10, "sslConnInit": 1632, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 1632, "sslConnInitRate": 10, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 1632, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 10, "tcpActiveConns": 0, "tcpConnInit": 1632, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 0, "tcpConnInitProgress": 0, "tcpConnInitRate": 10, "tcpConnInitSuccess": 1632, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 10, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 1, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 0, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 1632, "tlsfrontThroughput": 32374784}], "sum": [{"appSessStructNotAvail": 0, "socketBindIpv4": 131421, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 130963, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 261697, "socketReuseSetFail": 0, "sslAcceptSuccess": 130734, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 1612, "sslConnInit": 130734, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 130734, "sslConnInitRate": 1612, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 130734, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 1612, "tcpActiveConns": 2, "tcpConnInit": 130734, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 1, "tcpConnInitProgress": 0, "tcpConnInitRate": 1612, "tcpConnInitSuccess": 130734, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 1612, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 229, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 1, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 130734, "tlsfrontThroughput": 5256839168}, {"appSessStructNotAvail": 0, "socketBindIpv4": 133046, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 132586, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 264942, "socketReuseSetFail": 0, "sslAcceptSuccess": 132356, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 1622, "sslConnInit": 132356, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 132356, "sslConnInitRate": 1622, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 132356, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 1622, "tcpActiveConns": 2, "tcpConnInit": 132356, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 1, "tcpConnInitProgress": 0, "tcpConnInitRate": 1622, "tcpConnInitSuccess": 132356, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 1622, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 230, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 1, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 132356, "tlsfrontThroughput": 5289148416}, {"appSessStructNotAvail": 0, "socketBindIpv4": 134681, "socketBindIpv4Fail": 0, "socketBindIpv6": 0, "socketBindIpv6Fail": 0, "socketConnectEstablishFail": 0, "socketConnectEstablishFail2": 0, "socketCreate": 134219, "socketCreateFail": 0, "socketIpTransparentSet": 0, "socketIpTransparentSetFail": 0, "socketLingerSet": 0, "socketLingerSetFail": 0, "socketListenFail": 0, "socketReuseSet": 268207, "socketReuseSetFail": 0, "sslAcceptSuccess": 133988, "sslAcceptSuccessInSec": 0, "sslAcceptSuccessRate": 1632, "sslConnInit": 133988, "sslConnInitFail": 0, "sslConnInitInSec": 0, "sslConnInitProgress": 133988, "sslConnInitRate": 1632, "sslConnInitSuccess": 0, "sslConnInitSuccessInSec": 0, "sslConnInitSuccessRate": 0, "tcpAcceptFail": 0, "tcpAcceptSuccess": 133988, "tcpAcceptSuccessInSec": 0, "tcpAcceptSuccessRate": 1632, "tcpActiveConns": 2, "tcpConnInit": 133988, "tcpConnInitFail": 0, "tcpConnInitFailImmediateEaddrNotAvail": 0, "tcpConnInitFailImmediateOther": 0, "tcpConnInitInSec": 0, "tcpConnInitInUse": 1, "tcpConnInitProgress": 0, "tcpConnInitRate": 1632, "tcpConnInitSuccess": 133988, "tcpConnInitSuccessInSec": 0, "tcpConnInitSuccessRate": 1632, "tcpConnStructNotAvail": 0, "tcpGetSockNameFail": 0, "tcpInitServerFail": 0, "tcpListenStart": 231, "tcpListenStartFail": 0, "tcpListenStop": 0, "tcpListenStructNotAvail": 0, "tcpLocalPortAssignFail": 0, "tcpPollRegUnregFail": 0, "tcpReadFail": 0, "tcpWriteFail": 0, "tcpWriteReturnsZero": 0, "tlsfrontActSessions": 1, "tlsfrontBytesInSec": 0, "tlsfrontSessions": 133988, "tlsfrontThroughput": 5321523200}]}}

stats_ticks = 60

async def index_handle(request):
    return web.FileResponse('public/index.html')

async def api_get_deployments(request):
    return web.json_response(list(gstats.keys()))

async def api_get_stats(request):
    return web.json_response(gstats)

async def api_get_tlsfront_stats(request):
    results = {}
    for k in gstats.keys():
        if k.startswith('sslfront') \
            or k.endswith('sslfront') \
            or k.startswith('tlsfront') \
            or k.endswith('tlsfront'):
            results[k] = gstats[k]
    return web.json_response(results)

app = web.Application()

app.add_routes([web.static('/build', 'public/build')])
app.add_routes([web.static('/assets', 'public/assets')])

app.add_routes([web.route('get'
                            , '/api/deployments'
                            , api_get_deployments)])

app.add_routes([web.route('get'
                            , '/api/stats'
                            , api_get_stats)])

app.add_routes([web.route('get'
                            , '/api/tlsfront_stats'
                            , api_get_tlsfront_stats)])

app.add_routes([web.route('get', '/{tail:.*}', index_handle)])

class StatsListener:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        message = data.decode()
        stats = json.loads(message)
        appId = stats['appId']
        podIp = stats['podIp']
        del stats['appId']
        del stats['podIp']

        if not gstats.get(appId):
            gstats[appId] = {}
        if not gstats[appId].get(podIp):
            gstats[appId][podIp] = []

        gstats[appId][podIp].append(stats)
        if len(gstats[appId][podIp]) > stats_ticks:
            gstats[appId][podIp].pop(0)


        gstats[appId]['sum'] = [] 

        for i in range (stats_ticks):
            sum_stats = {}
            for _, podTickList in gstats[appId].items():
                if i < len(podTickList):
                    podStats = podTickList[i]
                    for k in podStats.keys():
                        if sum_stats.get(k):
                            sum_stats[k] = sum_stats[k] + podStats[k]
                        else:
                            sum_stats[k] = podStats[k]
            gstats[appId]['sum'].append(sum_stats)

def main ():
    global stats_ticks

    cfg_file = '/configs/config.json'
    with open(cfg_file) as f:
        cfg = json.loads(f.read())

    stats_ticks = cfg['stats_ticks']

    loop = asyncio.get_event_loop()
    runner = aiohttp.web.AppRunner(app)
    loop.run_until_complete(runner.setup())
    site = aiohttp.web.TCPSite(runner
                , host=cfg['webui_ip']
                , port=cfg['webui_port']
                , reuse_port=True)
    loop.run_until_complete(site.start())

    listen = loop.create_datagram_endpoint(StatsListener
                    , local_addr=(cfg['webui_ip']
                                    , cfg['stats_port'])
                    , reuse_port=True)

    loop.run_until_complete(listen)

    loop.run_forever()
    # web.run_app(app, port=8888)

if __name__ == '__main__':
    print ('http://localhost:8888')
    main()

