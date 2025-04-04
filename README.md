# SimpliVity-Python

A python class for SimpliVity RestAPI.  

The master branch contains the most recent SimpliVity Python class (v4.0), that is tested with OmniStack versions:
- 4.1.0
- 4.0.1
- 4.0

The SimpliVity Python class v4.0 offers you the capability to run RestAPI calls with a full list of optional parameters. The parameters must be provided as an array of key-value pairs, where the key is the parameter name.  The following example shows the GetVM call where you display the optional_fields and limit output entries: 

###  x = svt.GetVM({'show_optional_fields':'true','limit':limit})

Take a look at the HPE Developer website to get a current list of SimpliVity RestAPI call parameters: https://developer.hpe.com/api/simplivity/ 

If you do have SimpliVity cluster with the following OmniStack versions:
- 3.7.10
- 3.7.9
- 3.7.8

then please use the branch v3.0: https://github.com/tbeha/SimpliVity-Python/blob/v3.0/README.md
