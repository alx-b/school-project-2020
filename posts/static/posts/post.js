    container = document.querySelector(".post-del-container");
    container.style.display = "none";

    delButton = document.querySelector(".post-delete-button");
    delButton.addEventListener("click", showHTML);

    function showHTML(){
        container.style.display = "grid";
    }
