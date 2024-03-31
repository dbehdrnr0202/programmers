-- 코드를 작성해주세요
SELECT E.ID, IFNULL(C.CHILD_COUNT,0) AS CHILD_COUNT
FROM ECOLI_DATA AS E
LEFT JOIN
(
    SELECT PARENT_ID, COUNT(ID) AS CHILD_COUNT
    FROM ECOLI_DATA
    GROUP BY PARENT_ID
) AS C
ON E.ID = C.PARENT_ID