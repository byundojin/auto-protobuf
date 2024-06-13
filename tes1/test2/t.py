from grpc_tools import protoc

cmd_arg = ['c:\\workspace\\python labs\\gRPC\\.venv\\Lib\\site-packages\\grpc_tools\\protoc.py',
    '-I.',
    '--python_out=.',
    '--grpc_python_out=.',
    './protos/app1/service1/service1.proto',
    '-IC:\\workspace\\python labs\\gRPC\\.venv\\Lib\\site-packages\\grpc_tools\\_proto']
# cmd_arg = ['c:\\workspace\\python labs\\gRPC\\.venv\\Lib\\site-packages\\grpc_tools\\protoc.py',
#     '-I./service2',
#     '--python_out=.',
#     '--grpc_python_out=.',
#     './protos/app1/service2.proto',
#     '-IC:\\workspace\\python labs\\gRPC\\.venv\\Lib\\site-packages\\grpc_tools\\_proto']
protoc.main(cmd_arg)

"""
1. -I
2. --python_out
3. --grpc_python_out
4. .

2. (-I 미설정시 4.) 기준 pb2 생성 위치
3. (-I 미설정시 4.) 기준 pb2_grpc 생성 위치
4. (현재 터미널 절대경로)에서 protofile 위치


"""