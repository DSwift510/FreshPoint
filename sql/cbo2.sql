drop temporary table if exists cf;
create temporary table cf
SELECT monthname(Month_Year) as MY, Cases_Sold, SProductID 
FROM complete_freshpoint 
WHERE SProductID != 9999 AND complete_freshpoint.100miles = 1 or complete_freshpoint.500miles = 1;

select MY, Cases_sold, SProductID from cf;

drop temporary table if exists cbo;
create temporary table cbo
Select * from cf 
inner join fruit_vegetable_table on cf.SProductID = fruit_vegetable_table.ProductID
#INNER JOIN fruit_vegetable_table ON complete_freshpoint.SProductID = fruit_vegetable_table.ProductID
GROUP BY fruit_vegetable_table.Food, cf.SProductID, cf.MY, cf.Cases_Sold; 

select MY, Cases_Sold, Food/*, /*January, February, March, April, May, June, July, August, September, October, November, December*/ from cbo GROUP BY Food, SProductID, MY;