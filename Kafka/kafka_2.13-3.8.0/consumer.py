from kafka import KafkaConsumer

# In the previous step, you published two JSON messages. Now, you can use the KafkaConsumer class to consume the messages.


consumer = KafkaConsumer('bankbranch', group_id =  None, bootstrap_servers = ['localhost:9092'],
                        auto_offset_reset = 'earliest')

print("hello")
print(consumer)

# Once the consumer is created, it will receive all available messages from the topic bankbranch. Then, you can iterate and print them with the following code snippet:
for msg in consumer:
    print(msg.value.decode("utf-8"))
    
    
# The above consuming message operation is equivalent to using kafka-console-consumer.sh --topic in Kafka CLI client.