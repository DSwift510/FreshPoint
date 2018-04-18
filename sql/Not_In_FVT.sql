DROP TEMPORARY TABLE IF EXISTS combo;
CREATE TEMPORARY TABLE combo 
SELECT complete_freshpoint.Month_Year, complete_freshpoint.Cases_Sold, complete_freshpoint.Description, complete_freshpoint.ProductID
FROM complete_freshpoint 
WHERE complete_freshpoint.SProductID = 9999
GROUP BY complete_freshpoint.Description; 

SELECT * FROM combo;