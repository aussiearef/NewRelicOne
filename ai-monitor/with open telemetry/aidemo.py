# RUN 'pip install -r requirements.txt' first, to install the libraries.

import os
from fastapi import FastAPI
from openai import OpenAI

# 1. Import OpenTelemetry Core Trace & Resource Components
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource

# 2. Import OpenTelemetry Core Metrics Components
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter

# 3. Import Framework Instrumentation Wrappers
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor

# 4. Initialize Shared Resource Attributes (Pulls service name from terminal env)
resource = Resource.create()

# 5. Configure and Register the Trace Provider (HTTP Protobuf)
tracer_provider = TracerProvider(resource=resource)
trace_processor = BatchSpanProcessor(OTLPSpanExporter())
tracer_provider.add_span_processor(trace_processor)
trace.set_tracer_provider(tracer_provider)

# 6. Configure and Register the Meter Provider (HTTP Protobuf)
metric_reader = PeriodicExportingMetricReader(OTLPMetricExporter())
meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
metrics.set_meter_provider(meter_provider)

# 7. Instrument OpenAI SDK before framework startup
OpenAIInstrumentor().instrument()

app = FastAPI(title="OpenTelemetry AI Monitoring Demo")

# 8. Instrument FastAPI to capture inbound HTTP requests and performance metrics
FastAPIInstrumentor.instrument_app(app)

@app.get("/chat")
def run_openai_demo(prompt: str = "Explain metrics, logs, and traces in one sentence."):
    print(f"Received request with prompt: {prompt}")
    
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    response = client.chat.completions.create(
        model="gpt-5.4-nano",
        messages=[{"role": "user", "content": prompt}],
        max_completion_tokens=150,
        temperature=0.7
    )
    
    return {
        "status": "success",
        "model": "gpt-5.4-nano",
        "response": response.choices[0].message.content.strip()
    }