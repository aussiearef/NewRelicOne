
using System.Data.SqlClient;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () =>
{
    const string DbConnectionStringBuilder = "Server=localhost,1433;Initial Catalog=NewRelic;;User Id=sa;Password=Asd123)_";
   using var con = new SqlConnection(connectionString:DbConnectionStringBuilder);
   using var cmd = con.CreateCommand();
   cmd.CommandType=System.Data.CommandType.Text;
   cmd.CommandText="select * from testdata";
   con.Open();

   var reader = cmd.ExecuteReader();
   while (reader.Read())
   {
      var rnd = new Random((int)DateTime.Now.Ticks).Next(10);
      Console.WriteLine($"Waiting for {10*rnd} milli-seconds");
      Thread.Sleep(10* rnd);
   }
   con.Close();

   Console.WriteLine("API execution ended.");
   return new HttpResponseMessage(System.Net.HttpStatusCode.OK);
});

app.Run();
