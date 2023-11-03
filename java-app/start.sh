mvn clean package
cd ./target

# To run the app with no instrumentation:
# java -jar app-1.0-SNAPSHOT.jar

# To run the app with instrumentation:
 java -javaagent:./newrelic/newrelic.jar -jar app-1.0-SNAPSHOT.jar

