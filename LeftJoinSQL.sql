SELECT p.firstName, p.secondName, p.city, p.state FROM Person p 
LEFT JOIN Address a ON p.personId = a.personId

the left join table ensures that all the rows from the left table will be provided even tho there are no matches from the 
right table