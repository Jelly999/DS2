from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import xml.etree.ElementTree as ET
import time

XML = 'db.xml'

tree = ET.parse(XML)
root = tree.getroot()

# attrib = {}
# element = root.makeelement('topic', attrib)
# root.append(element)

# # adding an element to the seconditem node
# attrib = {'name': 'secondname2'}
# subelement = root[0][0][0].makeelement('name', attrib)
# ET.SubElement(root[0][0][0], 'name', attrib)

# # create a new XML file with the new element
# tree.write(XML)


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    server.register_function(pow)

    # Register a function under a different name
    def adder_function(x, y):
        return x + y
    server.register_function(adder_function, 'add')

    def items():
        return "topic" #['topic', 'subject' ,'timestamp']

    server.register_function(items(), 'items')
    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'mul').
    class MyFuncs:
        def mul(self, x, y):
            return x * y
        def item(self, p_topic, p_text, p_timestamp):
            print(p_topic, p_text, p_timestamp)
            for topic in root.findall('topic'):
                if (p_topic == topic.get('name')):
                    for note in topic.findall('note'):
                        for text in note.findall('text'):
                            if p_text != '' and p_text != text.text:
                                text.text = p_text
                                for timestamp in note.findall('timestamp'):
                                    timestamp.text = p_timestamp
                                tree.write(XML)
                            print(text.text)
                        print(note.get('name'))
                # else:
                #     print("Not found")
                    # create new entry
            return 'not found'
            
            # return 'not found'
            # return root[0][0][0].text #['topic', 'text' ,'timestamp']
    server.register_instance(MyFuncs())



    # Run the server's main loop
    server.serve_forever()