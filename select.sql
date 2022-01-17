SELECT cc.id, cc.name, cc.email, roles.description, ca.description AS claim_description
    FROM  users cc 
    INNER JOIN roles ON cc.role_id = roles.id
    INNER JOIN user_claims uc on cc.id  = uc.user_id 
    INNER join claims ca ON ca.id = uc.claim_id
WHERE cc.id = 1 -- Insira aqui o Id do usuário que você quer consultar