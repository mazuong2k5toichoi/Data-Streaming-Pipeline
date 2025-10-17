connect-cassandra:
	docker exec -it cassandra  cqlsh -u cassandra -p  cassandra localhost 9042
spark-submit:
	spark-submit --master spark://localhost:7077 \
    --packages com.datastax.spark:spark-cassandra-connector_2.12:3.4.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4 \
    spark_stream.py
check-kafka:
	nc -zv localhost 9092
restart-kafka:
	docker-compose restart broker
resubmit-spark:
	spark-submit --master spark://localhost:7077 \
	--packages com.datastax.spark:spark-cassandra-connector_2.12:3.5.4,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4 \
	spark_stream.py
up:
	docker-compose up -d
down:
	docker-compose down
pull:
	docker-compose pull
