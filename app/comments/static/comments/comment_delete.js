container = document.querySelector(".comment-del-container");
deleteForm = document.querySelector(".delete-form");

deleteButton = document.querySelector(".form-delete-button");
cancelButton = document.querySelector(".form-cancel-button");

deleteButton.addEventListener("click", submitForm);
cancelButton.addEventListener("click", hideHTML);

function hideHTML(){
    container.style.display = "none";
}

function submitForm(){
    deleteForm.submit();
}


