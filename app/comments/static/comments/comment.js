let containerC = document.querySelectorAll(".comment-del-container");
for (x of containerC){
    x.style.display = "none";
    console.log(x)
}

let containers = Array.from(containerC);


let delCommentButton = document.querySelectorAll(".comment-delete-button");

let delCommentButtons = Array.from(delCommentButton);

for (some of delCommentButtons){
    some.addEventListener("click", showCommentHTML);
}

let cancelCommentButton = document.querySelectorAll(".comment-form-cancel-button");

let cancelCommentButtons = Array.from(cancelCommentButton);

for (x of cancelCommentButtons){
    x.addEventListener("click", hideCommentHTML);
}


function hideCommentHTML(event){
    idx = cancelCommentButtons.indexOf(event.currentTarget);
    console.log("HIDE?");
    containers[idx].style.display = "none";
}

function showCommentHTML(event){
    currentIndex = delCommentButtons.indexOf(event.currentTarget);
    console.log(currentIndex);
    containers[currentIndex].style.display = "grid";
}
