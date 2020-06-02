# SimpliVity-Python

A python class for SimpliVity RestAPI.  

The master branch contains the most recent SimpliVity Python class (v4.0), that is tested with OmniStack versions:
- 4.0.1
- 4.0

The SimpliVity Python class v4.0 offers you the capability to run RestAPI calls with a full list of optional parameters. The parameters must be provided as an array of key-value pairs, where the key is the parameter name.  The following example shows the GetVM call where you display the optional_fields and set a limit to the number of output entries: 

###  x = svt.GetVM({'show_optional_fields':'true','limit':limit})

If you do have SimpliVity cluster with the following OmniStack versions:
- 3.7.10
- 3.7.9
- 3.7.8

then please use the branch v3.0: https://github.com/tbeha/SimpliVity-Python/blob/v3.0/README.md

Docker images with Python and the SimpliVity RestAPI class installed are available at DockerHub (https://hub.docker.com/):
- tb1378/svtcentpy  (CentOS, https://hub.docker.com/repository/docker/tb1378/svtcentpy)
- tb1378/svtupupy   (Ubuntu, https://hub.docker.com/repository/docker/tb1378/svtubupy)
