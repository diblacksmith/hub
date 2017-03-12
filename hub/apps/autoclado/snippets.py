#coding:utf-8

#fetcher
def f(cursor):
    return lambda x: cursor.execute(x).fetchall()


#duplas de cadeia
"""
SELECT
    (SELECT palavra FROM palavras WHERE id = primaria_id),
    (SELECT palavra FROM palavras WHERE id = secundaria_id)
FROM cadeia_palavras
"""

#duplas especificas de cadeia
"""
SELECT
    (SELECT palavra FROM palavras WHERE id = primaria_id),
    (SELECT palavra FROM palavras WHERE id = secundaria_id)
FROM cadeia_palavras p
WHERE secundaria_id = (SELECT id FROM palavras WHERE palavra = 'fazer' OR palavra = 'tomar')
"""

#contagem de possiveis palavras
"""
SELECT
    (SELECT palavra FROM palavras WHERE id = secundaria_id),
    COUNT(secundaria_id) as num FROM cadeia_palavras
WHERE primaria_id = (SELECT id FROM palavras WHERE palavra = 'abre')
GROUP BY secundaria_id
ORDER BY num DESC
LIMIT 3
"""
