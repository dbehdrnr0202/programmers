-- 코드를 작성해주세요
SELECT COUNT(ID) AS COUNT
FROM ECOLI_DATA
WHERE GENOTYPE & 5
AND NOT GENOTYPE & 2