select
cc.id,
cc.name,
cc.email,
roles.description,
ca.description as claim_description
FROM  

users cc INNER JOIN roles ON cc.role_id = roles.id
INNER JOIN user_claims uc on cc.id  = uc.user_id 
INNER join claims ca on ca.id = uc.claim_id 