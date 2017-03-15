# Feedback #

A solid and documented solution. Very good technical solution and a nice GUI
layout. Relatively nice user manual. Efficiently solved.

General:
    * Explain why you use Qt?
    * Please tell what Python version you use?

* Use case diagram
    * Is “save configuration to local file” a use case?
* A specification list. I.e. write a list with the program features.
    * "Fetching Juniper configuration" should be "Fetching router configuration"
* A network diagram
    * OK. A few words on the test environment please!
* A block diagram possibly combined with the network diagram.
    * OK, but what OS are you on? Show the files being handled.
* A class diagram with description.
    * All diagrams needs 3 lines of explanation as a minimum.
* A user manual.
    * Very nice screen shots.
* Source code with comments and a description.
    * Put this a s part of the report. It is two big and important to be a
      program comment.
      
      
      

    # Instead of waiting blindly crossing our fingers that it it is enough,
    # this code block tries to be smarter.
    # It uses the fact that whenever the Juniper device is done running a
    # command, it will show a prompt. The prompt is different in each mode
    # which is why we keep track of the mode in other places. This will
    # loop until the maximum amount of time allowed, has passed, checking
    # at wait_interval periods for the prompt at the end of the output.
    #
    # To things will break this:
    # * Always run commands using no-more to make sure that the Juniper
    # device will not wait for a keypress that will never happen.
    # * There is a possiblity that the end of the ouput from the router
    # could be the start of a comment, a hashtag followed by a space,
    # which is handled as a prompt in configuration mode. To fix this
    # a regula
