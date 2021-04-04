import xmlrpc.client
import datetime

s = xmlrpc.client.ServerProxy('http://localhost:8000')
# print(s.pow(2,3))  # Returns 2**3 = 8
# print(s.add(2,3))  # Returns 5
# print(s.mul(5,2))  # Returns 5*2 = 10
# print(s.system.listMethods())
datenow = datetime.datetime.now()
while (True):
    topic = (input("Topic: "))
    if topic == '0':
        break
    text = input("Text: ")
    timestamp = datetime.datetime.now
    timestamp = timestamp.strftime("%d%M%Y %H:%M")
    print(s.item(topic, text, timestamp))