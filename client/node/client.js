const PROTO_PATH ="../proto/notes.proto";

const grpc = require("grpc");
const protoLoader = require("@grpc/proto-loader");
let packageDefinition = protoLoader.loadSync(
    PROTO_PATH,{
        keepCase:true,
        longs:String,
        enums:String,
        arrays:true
    });

const NoteSerivers = grpc.loadPackageDefinition(packageDefinition).NoteService
const client = new NoteSerivers("localhost:8082",grpc.credentials.createInsecure())

module.exports = client;

