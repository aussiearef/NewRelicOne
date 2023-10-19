mvn clean package
cd ./target
#java -jar app-1.0-SNAPSHOT.jar

java -javaagent:./newrelic/newrelic.jar -jar app-1.0-SNAPSHOT.jar
