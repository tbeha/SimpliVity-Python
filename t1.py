import getpass
from SimpliVityClass import *                

### Main ###########################################################################

if __name__ == "__main__":
    
    """ Create the SimpliVity Rest API Object"""
    
    svtuser = input("Username: ")
    svtpassword = getpass.getpass()
    ovc = input("OVC: ")
    url="https://"+ovc+"/api/"         
    svt = SimpliVity(url)
    svt.Connect(svtuser,svtpassword)

    try:
        lim = input("Limit: ")
        offset = input("Offset: ")
        dxo = int(offset)*int(lim)
        x = svt.GetVM({'show_optional_fields':'true','limit':lim,'offset':str(dxo)})
        print(x)
        last = x['offset']+x['limit']
        print(last)
        x = svt.GetVM({'show_optional_fields':'true','limit':lim,'offset':str(last)})
        print(x)      
   
    except KeyError:
        print("KeyError")
        print(str(e.expression))
        print(str(e.status))
        print(str(e.message))
        pass                         
    except SvtError as e:
        if e.status == 401:
            try:
                print("Open Connection to SimpliVity")
                svt.Connect(svtuser,svtpassword)
                print("Connection to SimpliVity is open")
            except SvtError as e:
                print("Failed to open a conection to SimplVity")
                print(str(e.expression))
                print(str(e.status))
                print(str(e.message))
                print("close SimpliVity connection")
                exit(-200)
        elif e.status == 555:
            print('SvtError:')
            print(str(e.expression))
            print(str(e.status))
            print(str(e.message))                          
        else:
            print('Unhandeled SvtError:')
            print(str(e.expression))
            print(str(e.status))
            print(str(e.message))
            print("close SimpliVity connection")
            exit(-200)
    except Exception as ex:
            print(ex)
            print('Exception')
            print(str(ex))
            pass