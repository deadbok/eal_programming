#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# The above lines tell the shell to use python as interpreter when the
# script is called directly, and that this file uses utf-8 encoding,
# because of the country specific letter in my surname.
"""
Name: Juniper communication abstraction class.
Author: Martin Bo Kristensen Grønholdt.
Version: 1.0 (2017-03-07)

Class that encapsulates the finer details of communicating with a Junpier
device using paramiko.
"""

import sys, paramiko, time


class VSRX():
    """
    Class that encapsulates the finer details of communicating with a Junpier
device using paramiko.
    """
    OPERATIONAL = 0
    CONFIGURATION = 1
    SHELL = 3

    def __init__(self):
        """
        Constructor..
        """
        self.channel = None
        self.cli_active = None
        self.mode = None

        self.client = paramiko.SSHClient() # Create SSHClient object
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def startCLI(self):
        self.channel = self.client.invoke_shell()
        self.mode = self.SHELL

        self.channel.send('cli\n')
        # We are now in operational mode
        self.mode = self.OPERATIONAL

        self.getOutput()

    def getOutput(self, wait_interval = 0.1, wait_period = 1):
        """
        Empty the paramiko in buffer.
        """
        ret = ''
        current_wait = 0
        done = False
        while not done:
            if self.channel.recv_ready():
                ret += self.channel.recv(10000).decode()
                current_wait = 0
            else:
                time.sleep(wait_interval)
                current_wait += wait_interval

            if current_wait == wait_period:
                done = True

            if self.mode == self.SHELL:
                if ret.endswith('% '):
                    done = True
            elif self.mode == self.OPERATIONAL:
                if ret.endswith('> '):
                    done = True
            elif self.mode == self.CONFIGURATION:
                if ret.endswith('# '):
                    done = True
        return(ret)

    def connect(self, ip, port='2222', username='root', password='TestTest'):
        self.client.connect(ip, port=port, username=username, password=password)
        self.startCLI()

    def showConfiguration(self):
        ret = ''
        if self.channel is not None:
            self.channel.send('show configuration | no-more\n')
            ret = self.getOutput().split('\n')

        return('\n'.join(ret[1:-1]))

    def close(self):
        if self.channel is not None:
            self.channel.send('exit')
        self.channel.close()


