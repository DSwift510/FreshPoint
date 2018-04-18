drop temporary table if exists cf;
create temporary table cf
SELECT monthname(Month_Year) as MY, Cases_Sold, SProductID
FROM complete_freshpoint 
WHERE SProductID != 9999 AND complete_freshpoint.Not_local = 1;

select MY, Cases_sold, SProductID from cf;

drop temporary table if exists cl;
create temporary table cl
SELECT monthname(Month_Year) as MY, Cases_Sold, SProductID, Not_local  
FROM complete_freshpoint 
WHERE SProductID != 9999 AND complete_freshpoint.Not_local = 0;

select MY, Cases_sold, SProductID, Not_local from cl;

drop table if exists goodl;
create table goodl
Select * from cl 
inner join fruit_vegetable_table on cl.SProductID = fruit_vegetable_table.ProductID
#INNER JOIN fruit_vegetable_table ON complete_freshpoint.SProductID = fruit_vegetable_table.ProductID
GROUP BY fruit_vegetable_table.Food, cl.SProductID, cl.MY, cl.Cases_Sold; 

select MY, Not_local, Cases_Sold, Food, January, February, March, April, May, June, July, August, September, October, November, December from goodl GROUP BY Food, SProductID, MY;

drop table if exists goodmap;
create table goodmap
Select * from cf 
inner join fruit_vegetable_table on cf.SProductID = fruit_vegetable_table.ProductID
#INNER JOIN fruit_vegetable_table ON complete_freshpoint.SProductID = fruit_vegetable_table.ProductID
GROUP BY fruit_vegetable_table.Food, cf.SProductID, cf.MY, cf.Cases_Sold; 

select MY, Cases_Sold, Food, January, February, March, April, May, June, July, August, September, October, November, December from goodmap GROUP BY Food, SProductID, MY;