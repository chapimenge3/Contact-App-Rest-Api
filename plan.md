# Feature of the Project 
    - User have to signup to use the System 
    - After signup user can create contact , edit , delete, view  
    - Homepage will show all his contact ( using pagination max 50 contact per page )
    - Contact page will show single saved contact details 
    - User can edit their profile information
    - User can delete their account and exit from our system  

# Model 
    - User 
        - name (first and last ) *req
        - phone number *req
        - email *req
        - BOD 
        - active 
        - profilePic
        - SocialMedias
    - Conact 
        - name *req
        - phone *req
        - email *req
        - Campany(Model ) foreignkey
        - address(Model) foreignkey
        - website 
        - Social Medias(Model) MTM
        - Note
        - image

    - Campany
        - title 
        - CampanyName
        - website

    - Adress 
        - Country
        - state  
        - City 
        - street
        - PO BOX
        - Zipcode
        - Homenumber

    - Social Media
        - nameOfSocailMedia
        - urlOfProfile
        - iconOfSocialMedia