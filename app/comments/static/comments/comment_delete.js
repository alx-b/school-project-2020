//containerComment = document.querySelector(".comment-del-container");

deleteCommentForm = document.querySelector(".comment-delete-form");
deleteCommentButton = document.querySelector(".comment-form-delete-button");

//cancelCommentButton = document.querySelector(".comment-form-cancel-button");


deleteCommentButton.addEventListener("click", submitCommentForm);

//function hideCommentHTML(event){
//    console.log("HIDE?");
//    containerComments[event.currentTarget].style.display = "none";
//}

function submitCommentForm(){
    deleteCommentForm.submit();
}


