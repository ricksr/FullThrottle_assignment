# FullThrottle_assignment

<b>Function endpoint :</b> 
    https://mt19cnvqh4.execute-api.us-east-1.amazonaws.com/prod
    
<b>Database :</b> 
    https://full-throttle-sutirth.herokuapp.com/v1/graphql
    
<b>Db pswd :</b> 
    test

<h3>Db design idea :</h3>

    #there can be two tables :-

    1. Members  ( this contains info specific to a user )
        Link :
            https://full-throttle-sutirth.herokuapp.com/console/data/schema/public/tables/members/browse
            
    2. Members Activity ( 
        this table contains multiple activities of any particular user, 
        "id" of the previous table is the foreign key here named as "member_id" )
        Link:
            https://full-throttle-sutirth.herokuapp.com/console/data/schema/public/tables/members_activity_periods/browse

    #Why this should work ?

        we want to create multiple activities for a particular user , 
        so its better to use another table , for storing activities , as per our use case , 
        this design fullfils the reuirement , 
    
    #why not single table ?

        if we wish to update "member" related info. not "member activity" , 
        then in a single table , we will end up traversing many rows  increasing overall complexity , 
        solution is to make two different tables , each fullfilling a particular use case .

    #What is the relation between both the table ?

        They are associated with a common id ( which is acting as a Foreign key )
        "id" of "member" table ----->  "member_id" of "member_activity_periods" table
        This is one to many relationship .
    

<h3>API design :</h3>

    1. one can create a member and add details to it -
         
        endpoint : https://mt19cnvqh4.execute-api.us-east-1.amazonaws.com/prod/add-member?id=5&real_name=test1&tz=asia
        
        Here , we are creating a user in the "members" table ,i.e,
        id = 5, real_name = test1, tz = asia , as per the aarguments passed along with the URL and "/add-member",
        
    2. for a member you can add multiple activites - 

        endpoint : https://mt19cnvqh4.execute-api.us-east-1.amazonaws.com/prod/add-member-activity?id=5&start_time=aug12&end_time=aug14

        Here , for id = 5
        we are inserting its activity , start_time = aug12 and end_time = aug14 ,
        this data is being inserted into "members_activity_periods" table , 
        here , along with the URL , "/add-member-activity" this is the endpoint for activites
        assuming that the id already exists , if not , then create the id using the first API .

    3. view user details using its "id" - 

        endpoint : https://mt19cnvqh4.execute-api.us-east-1.amazonaws.com/prod/get-users?id=4
        
        id = 4 is the arguement , which is being queried to fetch the details related to that particular user
        Here , "/get-users" is the endpoint
        

To Summarise :

endpoints :

Base url + /add-member ,(args = id , real_name, tz),

base url + /add-member-activity ,(args = id, start_time, end_time),

base url + /get-users ,(args = id)


