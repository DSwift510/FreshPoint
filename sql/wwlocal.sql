# update warrenwilson.wwlocal, ufoods.fruit_vegetable_table set wwlocal.productid = fruit_vegetable_table.ProductID, wwlocal.foodtype = fruit_vegetable_table.Food
# WHERE LOCATE(Food, wwlocal.fpitem) 

drop temporary table if exists wwheatmap1;
create /*temporary*/ table wwheatmap1 
SELECT month as MY, cases, productid as PID, foodtype 
FROM wwlocal 
WHERE productid != '' AND 100miles = 1 or 250miles = 1 or 500miles = 1;

select MY, cases, PID, foodtype from wwheatmap1 where PID != '';

drop temporary table if exists wwheatmap2;
create /*temporary*/ table wwheatmap2
Select * from wwheatmap1 
inner join ufoods.fruit_vegetable_table on warrenwilson.wwheatmap1.PID = fruit_vegetable_table.ProductID
#INNER JOIN fruit_vegetable_table ON complete_freshpoint.SProductID = fruit_vegetable_table.ProductID
GROUP BY fruit_vegetable_table.Food, wwheatmap1.PID, wwheatmap1.MY, wwheatmap1.cases; 

select * from wwheatmap2 GROUP BY Food, productid, MY; /*MY, cases, Food, January, February, March, April, May, June, July, August, September, October, November, December*/