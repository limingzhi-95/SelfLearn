from ProtocolBuffer.protocol_obj.addressbook_pb2 import AddressBook, Person
persion = Person()

persion.id = 123
persion.name = 'leo'
persion.email = '123@123.com'
phone = persion.phones.add()
phone.number = "123-321"
phone.type = Person.Home

