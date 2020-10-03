import sys
import time

from lib.driverservice_pb2 import *
from lib.driverservice_pb2_grpc import *

if __name__ == "__main__":

    hostName, portNumber = sys.argv[1], sys.argv[2]

    driverNumber = sys.argv[3]

    channel = grpc.insecure_channel('{}:{}'.format(hostName, portNumber))
    stub = DriverServiceStub(channel)
    user = User(uid=driverNumber, name="Driver-{}".format(driverNumber),
                email="random-driver{}@uber.com".format(driverNumber), lastlogin=12345678)
    res = stub.StoreUserLogin(user)
    print('logged in succesfully')

    lat = input('Enter lat')
    lng = input('Enter lng')

    locationRequest = LocationRequest(uid=driverNumber, lat=float(lat), lng=float(lng), timestamp=12345678)
    while True:
        stub.UpdateLocation(locationRequest)
        time.sleep(5)
