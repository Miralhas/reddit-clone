# Django blog 

## What should a blog have?
 - User Auth.
 - Only authenticated users can create posts.
 - All posts should appear in the index page.
 - When a user click in a post, he will be redirected to that post page.
 - Post pages needs to display the post title, content and have a coment section.
 - Post owners can edit and delete their posts.
 - Post owners can delete comments made in their post.
 - Users can delete their comments
 - Each Post should have a button to up vote / down vote in the index page
 
## Models
 - User 
 - Post
    - owner 
    - date_published 
    - content 
    - title 
    - votes
    - comments

 - Comment
    - fk_user 
    - fk_post
    - text 
    - comment_date