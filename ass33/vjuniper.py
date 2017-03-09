"""
Name: Junpier configuration snatcher
Author: Martin Bo Kristensen Grønholdt, Rickie Ljungberg, Kasper Soelberg.
Version: 1.0 (2017-03-09)

Class that encapsulates the finer details of communicating with a Junpier
device using paramiko.
"""

import sys, paramiko, time


class VJuniper():
    """
    Class that encapsulates the finer details of communicating with a Junpier
    device using paramiko.
    """
    # Constant used to tell that the Juniper device is in operational mode.
    OPERATIONAL = 0
    # Constant used to tell that the Juniper device is in configuration mode.
    CONFIGURATION = 1
    # Constant used to tell that the Juniper device is in shall mode.
    SHELL = 2

    def __init__(self):
        """
        Constructor..
        """
        # Used for the channel that is opened using paramiko.
        self.__channel = None
        # Used to keep track of the mode that the Juniper device is in.
        self.__mode = None

        # Create the paramiko SSH client object.
        self.__client = paramiko.SSHClient()
        # Allow unknown hosts to be added to the host keys
        self.__client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def __getOutput(self, wait_interval=0.1, wait_period=1):
        """
        Empty the paramiko in buffer and return the contents.

        :param wait_interval: The interval beetween checking for new output.
        :param wait_period: The maximum amount of time that this method is
                            allowed to wait for output.
        :return: The output of the Juniper device as a string.
        """
        # Start of with an empty return value.
        ret = ''
        # We haven't done any waiting yet.
        current_wait = 0
        # We are not done.
        done = False

        # Instead of waiting blindly crossing our fingers that it it is enough,
        # this code block tries to be smarter.
        # It uses the fact that whenever the Juniper device is done running a
        # command, it will show a prompt. The prompt is different in each mode
        # which is why we keep track of the mode in other places. This will
        # loop until the maximum amount of time allowed, has passed, checking
        # at wait_interval periods for the prompt at the end of the output.
        #
        # To things will break this:
        #  * Always run commands using no-more to make sure that the Juniper
        #    device will not wait for a keypress that will never happen.
        # * There is a possiblity that the end of the ouput from the router
        #   could be the start of a comment, a hashtag followed by a space,
        #   which is handled as a prompt in configuration mode. To fix this
        #   a regular expression including the user@hostname part would be
        #   better.
        while not done:
            # Is there any new output?
            if self.__channel.recv_ready():
                # Add it to our return variable.
                ret += self.__channel.recv(10000).decode()
                # Reset the wait period.
                current_wait = 0
            else:
                # No new output, wait some more.
                time.sleep(wait_interval)
                current_wait += wait_interval

            # Have we reached the time out?
            if current_wait == wait_period:
                done = True

            # Check for a prompt which indicates the end of the output, and
            # get out if we find one..
            if self.__mode == self.SHELL:
                if ret.endswith('% '):
                    done = True
            elif self.__mode == self.OPERATIONAL:
                if ret.endswith('> '):
                    done = True
            elif self.__mode == self.CONFIGURATION:
                if ret.endswith('# '):
                    done = True
        # Return the output.
        return (ret)

    def startCLI(self):
        """
        Start the CLI on the Juniper device, entering operational mode.
        """
        # Invoke a shell on the Juniper device.
        self.__channel = self.__client.invoke_shell()
        # The Juniper device is now in shell mode.
        self.__mode = self.SHELL

        # Enter the cli.
        self.__channel.send('cli\n')
        # We are now in operational mode
        self.__mode = self.OPERATIONAL

        # Empty the paramiko input buffer, and discard the data.
        self.__getOutput()

    def connect(self, ip, port='22', username='root', password='TestTest'):
        """
        Connect to a Junpier device using paramiko SSH, and start the cli.

        :param ip: IP address of the Juniper device.
        :param port: The port that SSH is listening on.
        :param username: The user name used to log in to the Juniper device,
        :param password: The password used to log in to the Juniper device,
        """
        # Use paramiko to connect.
        self.__client.connect(ip, port=port, username=username,
                              password=password, timeout=10)
        # Start the cli.
        self.startCLI()

    def showConfiguration(self):
        """
        Run the show configuration command on the Juniper device and return
        the output.

        :return: The Juniper device configuration.
        """
        # Start of with an empty return value,
        ret = ['', '', '']
        # Check that we have a connection.
        if self.__channel is not None:
            # Send the show configuration command.
            self.__channel.send('show configuration | no-more\n')
            # Get the output from the Juniper device, make a list by splitting
            # the string at each new line..
            ret = self.__getOutput().split('\n')

        # Return the list as a string, but remove the first and last line,
        # which is the command that we ran, at the top line, and the prompt at
        # the last line.
        return ('\n'.join(ret[1:-1]))

    def close(self):
        """
        Close the connection to the Juniper device.
        """
        # If the channel is open, exit the cli for good measure.
        if self.__channel is not None:
            self.__channel.send('exit')
        # Close the connection.
        self.__channel.close()
