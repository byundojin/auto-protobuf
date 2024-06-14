# kody protobuilder

## Protobuilder

Kody에서 제작한 Proto file 간편 buildder입니다.

## 사용

proto파일 디렉토리는 다음과 같이 구성합니다.

```
protos
└application
    └service
        └proto
```

protos의 전체 proto file을 빌드합니다.

```
python -m protobulder.bulid
```

빌드 후

```
protos
└application
    └service
        ├proto.proto
        ├proto_pb2.py
        └proto_pb2_grpc.py
```

## 옵션

kody-protobuilder는 다음과 같은 옵션을 제공합니다.

### app

특정 app만 build합니다.
중복하여 사용이 가능합니다.

```
--app=<application_name>
-a=<application_name>
```

### service

특정 service만 build합니다.
중복하여 사용이 가능합니다.

```
--service=<application_name>.<service_name>
-s=<application_name>.<service_name>
```

### proto

특정 proto만 build합니다.
중복하여 사용이 가능합니다.

```
--proto=<application_name>.<service_name>.<proro_name>
-p=<application_name>.<service_name>.<proro_name>
```

<proto_name>은 확장자를 표기하여도 상관없습니다.

옵션으로 선택된 모든 파일이 build됩니다.
