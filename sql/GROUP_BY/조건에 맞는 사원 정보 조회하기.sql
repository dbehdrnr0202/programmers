-- 코드를 작성해주세요
SELECT S.TOTAL_SCORE AS SCORE, 
    E.EMP_NO, 
    E.EMP_NAME, 
    E.POSITION, 
    E.EMAIL
FROM HR_EMPLOYEES E,
    (
        SELECT EMP_NO, SUM(SCORE) AS TOTAL_SCORE
        FROM HR_GRADE G
        WHERE G.YEAR LIKE '2022'
        GROUP BY G.EMP_NO
    ) AS S
WHERE S.EMP_NO = E.EMP_NO
ORDER BY S.TOTAL_SCORE DESC LIMIT 1