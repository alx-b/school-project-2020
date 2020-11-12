containerPost = document.querySelector(".post-del-container");
deletePostForm = document.querySelector(".delete-form");

deletePostButton = document.querySelector(".form-delete-button");
cancelPostButton = document.querySelector(".form-cancel-button");

deletePostButton.addEventListener("click", submitForm);
cancelPostButton.addEventListener("click", hidePostHTML);

function hidePostHTML(){
    containerPost.style.display = "none";
}

function submitForm(){
    deletePostForm.submit();
}


