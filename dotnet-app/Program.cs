
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", (ILogger<Program> logger) =>
{
    
   logger.LogWarning("API execution ended.");
   return new HttpResponseMessage(System.Net.HttpStatusCode.OK);
});

app.Run();
