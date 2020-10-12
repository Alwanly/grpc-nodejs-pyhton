import grpc
  
import notes_pb2 as notes_pb2
import notes_pb2_grpc as notes_pb2_grpc


class Note(object):
    def __init__(self,id,todo):
        self.id = id
        self.todo = todo 

class NotesClient(object):
    
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 8082
        self.channel = grpc.insecure_channel("localhost:8082")                
        self.stub = notes_pb2_grpc.NoteServiceStub(self.channel)
    
    def get_notes(self):
        message = notes_pb2.Empty()    
        return self.stub.GetAll(message)  

    def get_note_by_id(self,data):
        message = notes_pb2.NoteById(id=data.id)  
        return self.stub.Get(message)

    def add_note(self,data):
        message = notes_pb2.Note(todo=data.todo)
        return self.stub.Insert(message)

    def delete_note(self,data):
        message = notes_pb2.NoteById(id=data.id)
        return self.stub.Delete(message)

    def edit_note(self,data):
        message = notes_pb2.Note(id=data.id,todo=data.todo)
        return self.stub.Update(message)
           
if __name__=='__main__':
    client = NotesClient()
    data = Note(0,"Bangun")
    result = client.add_note(data)
    print(result)
