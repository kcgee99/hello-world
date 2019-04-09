# hello-world
just another repository



USE MSSQLTipsDemo
GO
CREATE TABLE ID_Test
(
ID INT IDENTITY (1,1) PRIMARY KEY,
EmpName nvarchar(50)
)

CREATE TABLE SecondID_Test
(
ID INT IDENTITY (10,1) PRIMARY KEY,
CourName nvarchar(50)
)
