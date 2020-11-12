    containerP = document.querySelector(".post-del-container");
    containerP.style.display = "none";

    delButton = document.querySelector(".post-delete-button");
    delButton.addEventListener("click", showPostHTML);

    function showPostHTML(){
        containerP.style.display = "grid";
    }
