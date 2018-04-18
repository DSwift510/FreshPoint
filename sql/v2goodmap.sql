drop temporary table if exists fpnlocal;
create temporary table fpnlocal
SELECT monthname(Month_Year) as MY, Cases_Sold, SProductID
FROM ufoods.complete_freshpoint 
WHERE SProductID != 9999 AND complete_freshpoint.Not_local = 1;

select MY, Cases_sold, SProductID from fpnlocal;

drop temporary table if exists fplocal;
create temporary table fplocal
SELECT monthname(Month_Year) as MY, Cases_Sold, SProductID, Not_local  
FROM ufoods.complete_freshpoint 
WHERE SProductID != 9999 AND complete_freshpoint.Not_local = 0;

select MY, Cases_sold, SProductID, Not_local from fplocal;

drop temporary table if exists goodluck;
create temporary table goodluck
Select * from fplocal 
inner join ufoods.fruit_vegetable_table on fplocal.SProductID = fruit_vegetable_table.ProductID
#INNER JOIN fruit_vegetable_table ON complete_freshpoint.SProductID = fruit_vegetable_table.ProductID
GROUP BY fruit_vegetable_table.Food, fplocal.SProductID, fplocal.MY, fplocal.Cases_Sold; 

select MY, Not_local, Cases_Sold, Food, January, February, March, April, May, June, July, August, September, October, November, December from goodluck GROUP BY Food, SProductID, MY;

drop temporary table if exists goodmapper;
create temporary table goodmapper
Select * from fpnlocal 
inner join ufoods.fruit_vegetable_table on fpnlocal.SProductID = fruit_vegetable_table.ProductID
#INNER JOIN fruit_vegetable_table ON complete_freshpoint.SProductID = fruit_vegetable_table.ProductID
GROUP BY fruit_vegetable_table.Food, fpnlocal.SProductID, fpnlocal.MY, fpnlocal.Cases_Sold; 

select MY, Cases_Sold, Food, January, February, March, April, May, June, July, August, September, October, November, December from goodmapper GROUP BY Food, SProductID, MY;