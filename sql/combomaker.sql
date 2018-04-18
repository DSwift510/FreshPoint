DROP TEMPORARY TABLE IF EXISTS combo;
CREATE TEMPORARY TABLE combo 
SELECT complete_freshpoint.SProductID,complete_freshpoint.Not_Local, monthname(complete_freshpoint.Month_Year) as Month, complete_freshpoint.Cases_Sold, fruit_vegetable_table.Food, fruit_vegetable_table.January, fruit_vegetable_table.February, fruit_vegetable_table.March, fruit_vegetable_table.April, fruit_vegetable_table.May, fruit_vegetable_table.June, fruit_vegetable_table.July, fruit_vegetable_table.August, fruit_vegetable_table.September, fruit_vegetable_table.October, fruit_vegetable_table.November, fruit_vegetable_table.December
FROM complete_freshpoint 
INNER JOIN fruit_vegetable_table ON complete_freshpoint.SProductID = fruit_vegetable_table.ProductID
WHERE complete_freshpoint.Not_local = 0
ORDER BY fruit_vegetable_table.food;
#GROUP BY Month, fruit_vegetable_table.Food; 

SELECT * FROM combo;