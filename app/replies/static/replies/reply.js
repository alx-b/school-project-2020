let containerR = document.querySelectorAll(".reply-del-container");

for (x of containerR){
    x.style.display = "none";
    console.log(x);
}


let containersR = Array.from(containerR);


let replyDeleteButton = document.querySelectorAll(".reply-delete-button");
let replyDeleteButtons = Array.from(replyDeleteButton);

for (some of replyDeleteButtons){
    some.addEventListener("click", showReplyHTML);
}


let replyCancelButton = document.querySelectorAll(".reply-form-cancel-button");
let replyCancelButtons = Array.from(replyCancelButton);


for (x of replyCancelButtons){
    x.addEventListener("click", hideReplyHTML);
}


function hideReplyHTML(event){
    idx = replyCancelButtons.indexOf(event.currentTarget);
    console.log("HIDE?");
    containersR[idx].style.display = "none";
}

function showReplyHTML(event){
    currentIndex = replyDeleteButtons.indexOf(event.currentTarget);
    console.log(currentIndex);
    containersR[currentIndex].style.display = "grid";
}
