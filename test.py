from SimpliVityClass import *

url="https://10.0.40.15/api/"
svtuser="behat@demo.local"
svtpassword="We95sms!!"


try:    
    svt = SimpliVity(url)
    svt.connect(svtuser,svtpassword)

    # response = svt.GetCertificate()
    response = svt.GetHost()
    for x in response['hosts']:
        print(x['name'], x['model'], x['id'])
        print(svt.GetHostId(x['name']))
        result = svt.GetHostMetrics(x['name'],timerange='3600',resolution='Minute')
        result = svt.GetHostHardware(x['name'])
    response = svt.GetVM()
    for x in response['virtual_machines']:
        print(x['name'], x['state'], x['datastore_name'], x['id'])
        print( svt.GetVMId(x['name']) )
        result = svt.GetVMMetric(x['name'],timerange='3600',resolution='Minute')
        if x['state'] == 'ALIVE':
            print(svt.GetVMLastBackup(x['name']))

    response = svt.GetDataStore()
    for x in response['datastores']:
        print(x['name'], x['id'])
        print(svt.GetDataStoreId(x['name']))

    response = svt.GetPolicy()
    for x in response['policies']:
        print(x['name'], x['id'] )
        print(x['rules'])
        print( svt.GetPolicyId(x['name']))

    response = svt.GetCluster()
    for x in svt.GetClusterThroughput():
        print(x['date'], x['source_omnistack_cluster_name'], '->', x['destination_omnistack_cluster_name'], x['throughput']  )

    for x in response['omnistack_clusters']:
        print(x['name'], x['id'])
        result = svt.GetClusterId(x['name'])
        result = svt.GetClusterMetric(x['name'])

except SvtError as e:
    print("SvtError")
    print(e.expression)
    print(e.status)
    print(e.message)
