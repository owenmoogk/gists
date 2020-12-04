function funcClick(){
    let x = document.getElementById("mypara"); // accessing the paragraph, assigning it to x
    x.innerHTML = "Helloworld! From Javascript";
}

function date() {
    let x = document.getElementById("header");
    x.innerHTML = Date();
}

function classremove(y){
    let x = document.getElementsByClassName(y);
    for (var i = 0; i< x.length; i++){
        x[i].style.display = "none";
    }
}

function giveborder(id){
    let x = document.getElementById(id);
}