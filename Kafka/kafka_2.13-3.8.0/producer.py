from kafka import KafkaProducer
import json

# Since Kafka produces and consumes messages in raw bytes,
# you need to encode our JSON messages and serialize them into bytes. 
# For the value_serializer argument, you will define a lambda function to take a Python dict/list object and serialize it into bytes.
producer = KafkaProducer(value_serializer = lambda v: json.dumps(v).encode('utf-8'))

# The first argument specifies the topic bankbranch to be sent and the second argument represents the message value in a Python dict format and will be serialized into bytes.
producer.send("bankbranch",{'atmid':1, 'transid':100})
producer.send("bankbranch",{'atmid':2, 'transid':101})


producer.flush()
producer.close()

# In the above code, the producer is sending across two messages through this code. These messages will be received by the consumer.