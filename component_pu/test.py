import clr
clr.AddReference("ActUtlTypeLib")

from ActUtlTypeLib import ActUtlType

test = ActUtlType()

test.ActLogicalStationNumber = 5
test.Open()

test.WriteDeviceBlock("M0",3,1)

return_value = 6000
return_array= 0
ret2 = list()
for value in range(500):
    device = "D{0}".format(value)
    
    ret2.append(test.GetDevice(device,return_array)[1])


print(ret2)

test.SetDevice("D1",return_value)

test.Close()