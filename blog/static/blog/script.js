document.addEventListener("DOMContentLoaded", function(){
    if (document.querySelector("#edit_post")){

        const editBtn = document.querySelector("#edit_post");

        editBtn.addEventListener('click', function(){

            const titleElement = document.querySelector("#post_title");
            const postTitle = titleElement.innerHTML;
            titleElement.remove();

            const contentElement = document.querySelector("#post_content");
            const postContent = contentElement.innerHTML;
            contentElement.remove();

            const titleDiv = document.querySelector("#titleDiv");

            const contentDiv = document.querySelector("#contentDiv");

            // Title Element
            let titleInput = document.createElement("input");
            titleInput.className = "form-control";
            titleInput.placeholder = "Title";
            titleInput.name = "newPostTitle";
            titleInput.value = postTitle;
            titleInput.required = true;

            titleDiv.append(titleInput);

            // Textarea Element
            let contentTextarea = document.createElement("textarea");
            contentTextarea.className = "form-control";
            contentTextarea.rows = "10";
            contentTextarea.name = "newPostContent";
            contentTextarea.required = true;
            contentTextarea.value = postContent;

            contentDiv.append(contentTextarea);

            // Submit Element
            let submitBtn = document.querySelector("#submitBtn");
            submitBtn.style.display = "block";
            

    })
    }
})