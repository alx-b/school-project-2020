someContainer = document.querySelector(".post-del-container");
delForm = document.querySelector(".del-form");

deleteButton = document.querySelector(".delete-button");
cancelButton = document.querySelector(".cancel-button");

deleteButton.addEventListener("click", submitForm);
cancelButton.addEventListener("click", hideHTML);

function hideHTML(){
    someContainer.style.display = "none";
}

function submitForm(){
    delForm.submit();
}


