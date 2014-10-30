#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file VoiceService.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>

import socket

# This module's spesification
# <rtc-template block="module_spec">
voiceservice_spec = ["implementation_id", "VoiceService",
                 "type_name",         "VoiceService",
                 "description",       "ModuleDescription",
                 "version",           "1.0.0",
                 "vendor",            "Wu Chih-En",
                 "category",          "Voice",
                 "activity_type",     "STATIC",
                 "max_instance",      "1",
                 "language",          "Python",
                 "lang_type",         "SCRIPT",
                 "conf.default.android_host", "192.168.0.100",
                 "conf.default.android_port", "5000",
                 "conf.default.buffersize", "4096",
                 "conf.__widget__.android_host", "text",
                 "conf.__widget__.android_port", "text",
                 "conf.__widget__.buffersize", "text",
                 ""]
# </rtc-template>

##
# @class VoiceService
# @brief ModuleDescription
#
#
class VoiceService(OpenRTM_aist.DataFlowComponentBase):

    ##
    # @brief constructor
    # @param manager Maneger Object
    #
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        self._d_tts = RTC.TimedString(RTC.Time(0,0),0)
        """
        """
        self._ttsIn = OpenRTM_aist.InPort("tts", self._d_tts)
        self._d_enable = RTC.TimedBoolean(RTC.Time(0,0),0)
        """
        """
        self._enableIn = OpenRTM_aist.InPort("enable", self._d_enable)
        self._d_speech = RTC.TimedString(RTC.Time(0,0),0)
        """
        """
        self._speechOut = OpenRTM_aist.OutPort("speech", self._d_speech)





        # initialize of configuration-data.
        # <rtc-template block="init_conf_param">
        """

         - Name:  android_host
         - DefaultValue: 192.168.0.100
        """
        self._android_host = ['192.168.0.100']
        """

         - Name:  android_port
         - DefaultValue: 5000
        """
        self._android_port = [5000]
        """

         - Name:  buffersize
         - DefaultValue: 4096
        """
        self._buffersize = [4096]

        # </rtc-template>



    ##
    #
    # The initialize action (on CREATED->ALIVE transition)
    # formaer rtc_init_entry()
    #
    # @return RTC::ReturnCode_t
    #
    #
    def onInitialize(self):
        # Bind variables and configuration variable
        self.bindParameter("android_host", self._android_host, "192.168.0.100")
        self.bindParameter("android_port", self._android_port, "5000")
        self.bindParameter("buffersize", self._buffersize, "4096")

        # Set InPort buffers
        self.addInPort("tts",self._ttsIn)
        self.addInPort("enable",self._enableIn)

        # Set OutPort buffers
        self.addOutPort("speech",self._speechOut)

        # Set service provider to Ports

        # Set service consumers to Ports

        # Set CORBA Service Ports

        return RTC.RTC_OK

    #       ##
    #       #
    #       # The finalize action (on ALIVE->END transition)
    #       # formaer rtc_exiting_entry()
    #       #
    #       # @return RTC::ReturnCode_t
    #
    #       #
    #def onFinalize(self, ec_id):
    #
    #       return RTC.RTC_OK

    #       ##
    #       #
    #       # The startup action when ExecutionContext startup
    #       # former rtc_starting_entry()
    #       #
    #       # @param ec_id target ExecutionContext Id
    #       #
    #       # @return RTC::ReturnCode_t
    #       #
    #       #
    #def onStartup(self, ec_id):
    #
    #       return RTC.RTC_OK

    #       ##
    #       #
    #       # The shutdown action when ExecutionContext stop
    #       # former rtc_stopping_entry()
    #       #
    #       # @param ec_id target ExecutionContext Id
    #       #
    #       # @return RTC::ReturnCode_t
    #       #
    #       #
    #def onShutdown(self, ec_id):
    #
    #       return RTC.RTC_OK

        ##
        #
        # The activated action (Active state entry action)
        # former rtc_active_entry()
        #
        # @param ec_id target ExecutionContext Id
        #
        # @return RTC::ReturnCode_t
        #
        #
    def onActivated(self, ec_id):

        return RTC.RTC_OK

        ##
        #
        # The deactivated action (Active state exit action)
        # former rtc_active_exit()
        #
        # @param ec_id target ExecutionContext Id
        #
        # @return RTC::ReturnCode_t
        #
        #
    def onDeactivated(self, ec_id):

        return RTC.RTC_OK

        ##
        #
        # The execution action that is invoked periodically
        # former rtc_active_do()
        #
        # @param ec_id target ExecutionContext Id
        #
        # @return RTC::ReturnCode_t
        #
        #
    def onExecute(self, ec_id):
        mode = raw_input('Select Mode >>> ')

        # If not input then start recognition
        if mode == '':
            sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
            sock.connect( ( self._android_host[0], self._android_port[0] ) )

            print( "Android: %s :%d" )%( self._android_host[0], self._android_port[0] )

            sock.send( 'recognize' )
            data = sock.recv(self._buffersize[0])

            print( "Speech Recognition Result: %s" ) %( data )
            self._d_speech.data = data
            OpenRTM_aist.setTimestamp(self._d_speech)
            self._speechOut.write()

        # Else start speech
        else:
            sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
            sock.connect( ( self._android_host[0], self._android_port[0] ) )

            print( "Android: %s :%d" )%( self._android_host[0], self._android_port[0] )

            sock.send( self._d_tts.data )

            print( "Text to Speech: %s" ) %( self._d_tts.data )

        return RTC.RTC_OK

    #       ##
    #       #
    #       # The aborting action when main logic error occurred.
    #       # former rtc_aborting_entry()
    #       #
    #       # @param ec_id target ExecutionContext Id
    #       #
    #       # @return RTC::ReturnCode_t
    #       #
    #       #
    #def onAborting(self, ec_id):
    #
    #       return RTC.RTC_OK

    #       ##
    #       #
    #       # The error action in ERROR state
    #       # former rtc_error_do()
    #       #
    #       # @param ec_id target ExecutionContext Id
    #       #
    #       # @return RTC::ReturnCode_t
    #       #
    #       #
    #def onError(self, ec_id):
    #
    #       return RTC.RTC_OK

    #       ##
    #       #
    #       # The reset action that is invoked resetting
    #       # This is same but different the former rtc_init_entry()
    #       #
    #       # @param ec_id target ExecutionContext Id
    #       #
    #       # @return RTC::ReturnCode_t
    #       #
    #       #
    #def onReset(self, ec_id):
    #
    #       return RTC.RTC_OK

    #       ##
    #       #
    #       # The state update action that is invoked after onExecute() action
    #       # no corresponding operation exists in OpenRTm-aist-0.2.0
    #       #
    #       # @param ec_id target ExecutionContext Id
    #       #
    #       # @return RTC::ReturnCode_t
    #       #

    #       #
    #def onStateUpdate(self, ec_id):
    #
    #       return RTC.RTC_OK

    #       ##
    #       #
    #       # The action that is invoked when execution context's rate is changed
    #       # no corresponding operation exists in OpenRTm-aist-0.2.0
    #       #
    #       # @param ec_id target ExecutionContext Id
    #       #
    #       # @return RTC::ReturnCode_t
    #       #
    #       #
    #def onRateChanged(self, ec_id):
    #
    #       return RTC.RTC_OK




def VoiceServiceInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=voiceservice_spec)
    manager.registerFactory(profile,
                            VoiceService,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    VoiceServiceInit(manager)

    # Create a component
    comp = manager.createComponent("VoiceService")

def main():
    mgr = OpenRTM_aist.Manager.init(sys.argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()
