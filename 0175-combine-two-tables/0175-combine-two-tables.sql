/* Write your PL/SQL query statement below */
SELECT firstName, lastName, city, state
FROM Person left join Address on Person.personId = Address.personId