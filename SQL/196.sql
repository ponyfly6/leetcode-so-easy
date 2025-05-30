delete from Person
where Id not in (
    select min(Id)
    from Person
    group by Email
);