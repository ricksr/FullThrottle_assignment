# FullThrottle_assignment

Function endpoint : 
    https://mt19cnvqh4.execute-api.us-east-1.amazonaws.com/prod
    
Database : 
    https://full-throttle-sutirth.herokuapp.com/v1/graphql
    
Db pswd : 
    test

Db design idea :

    there can be two tables :-

    1. Members  ( this contains info specific to a user )
    2. Members Activity ( 
        this table contains MANY activities of any particular user, 
        "id" of the previous table is the foreign key here named as "member_id" )

    Why this should work ?

    we want to create multiple activities for a particular user , 
    so its better to use another table , for storing activities , as per our use case , 
    this design fullfils the reuirement , 
    
    why not single table ?

    if we wish to update "member" related info. not "member activity" , 
    then in a single table , we will end up traversing many rows  increasing overall complexity , 
    solution is to make two different tables , each fullfilling a particular use case .

    What is the relation between both the table ?

    They are associated with a common id ( which is acting as a Foreign key )
    "id" of "member" table ----->  "member_id" of "member_activity_periods" table
    This is one to many relationship .
    

API design :

    1. one can create a member and add details to it -

        endpoint : https://mt19cnvqh4.execute-api.us-east-1.amazonaws.com/prod/id=5&real_name=test1&tz=asia

        Here , we are creating a user in the "members" table ,i.e,
        id = 5, real_name = test1, tz = asia , as per the aarguments passed along with the URL,
        
    2. for a member you can add multiple activites - 

        endpoint : https://mt19cnvqh4.execute-api.us-east-1.amazonaws.com/prod/add-member-activity?id=5&start_time=aug12&end_time=aug14

        Here , for id = 5
        we are inserting its activity , start_time = aug12 and end_time = aug14 ,
        this data is being inserted into "members_activity_periods" table , 
        assuming that the id already exists , if not , then create the id using the first API .

    3. view user details using its "id" - 

        endpoint : https://mt19cnvqh4.execute-api.us-east-1.amazonaws.com/prod/get-users?id=4
        
        id = 4 is the arguement , which ie being queried to fetch the details related to that particular user



