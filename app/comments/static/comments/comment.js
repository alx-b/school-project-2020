    container = document.querySelector(".comment-del-container");
    container.style.display = "none";

    delButton = document.querySelector(".comment-delete-button");
    delButton.addEventListener("click", showHTML);

    function showHTML(){
        container.style.display = "grid";
    }
