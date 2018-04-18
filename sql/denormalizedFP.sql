drop temporary table if exists cf;
create temporary table cf
SELECT monthname(Month_Year) as MY, Cases_Sold, SProductID 
FROM complete_freshpoint 
WHERE SProductID != 9999 AND complete_freshpoint.Not_local = 1;

select MY, Cases_sold, SProductID from cf GROUP BY SProductID, Cases_Sold, MY;

drop temporary table if exists cbo3;
create temporary table cbo3
Select * from cf 
inner join fruit_vegetable_table on cf.SProductID = fruit_vegetable_table.ProductID
#INNER JOIN fruit_vegetable_table ON complete_freshpoint.SProductID = fruit_vegetable_table.ProductID
GROUP BY fruit_vegetable_table.Food, cf.SProductID, cf.MY, cf.Cases_Sold; 

select * from cbo3 GROUP BY Food, SProductID, MY;