    containerP = document.querySelector(".post-del-container");
    delButton = document.querySelector(".post-delete-button");

    if (containerP && delButton){
        containerP.style.display = "none";
        delButton.addEventListener("click", showPostHTML);
    }


    function showPostHTML(){
        containerP.style.display = "grid";
    }
