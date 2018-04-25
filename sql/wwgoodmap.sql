drop temporary table if exists wwnlocal;
create temporary table wwnlocal
SELECT Month as MY, Cases, productid, Local
FROM warrenwilson.wwlocal 
WHERE productid != '' AND Local = 0;

select MY, Cases, productid, Local from wwnlocal;

drop temporary table if exists wwlocal;
create temporary table wwlocal
SELECT Month as MY, Cases, productid, Local  
FROM warrenwilson.wwlocal 
WHERE productid != '' AND local = 1;

select MY, Cases, productid, Local from wwlocal;

