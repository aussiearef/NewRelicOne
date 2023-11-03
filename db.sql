
CREATE TABLE [dbo].[TestData](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Message] [varchar](100) NOT NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[TestData] ADD PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO

insert into TestData ([Message]) VALUES ('Hello World')