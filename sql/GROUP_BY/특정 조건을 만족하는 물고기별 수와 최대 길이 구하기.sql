-- 코드를 작성해주세요
SELECT COUNT(F.ID) AS FISH_COUNT, MAX(F.LENGTH) AS MAX_LENGTH, F.FISH_TYPE
FROM 
    (
        SELECT FISH_TYPE, AVG(CASE 
                              WHEN LENGTH IS NULL
                              THEN 10 
                              ELSE LENGTH 
                              END) AS AVG_LENGTH
        FROM FISH_INFO
        GROUP BY FISH_TYPE
    )
   AS A, FISH_INFO AS F
WHERE A.FISH_TYPE=F.FISH_TYPE
AND A.AVG_LENGTH>=33
GROUP BY F.FISH_TYPE
ORDER BY F.FISH_TYPE