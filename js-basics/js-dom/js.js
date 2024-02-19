let x = document.getElementById("7");
x.href = "https://www.2702rebels.com"
x.style.textDecoration = "none"
x.style.color = "blue";


let y = document.getElementById("2");
y.innerHTML = "yo yo yo";

let z = document.getElementById("1");
z.style.color = "red";

let special = false;

function allGreen(){
    let a = document.getElementsByTagName("p");
    for (let i=0;i<a.length;i++){
        a[i].innerHTML = "get haha lmao";
    }
    let b = document.getElementById("7");
    b.innerHTML = "get HAHA lmao";
    special = true;
}


let o = "hi";
function attention(id){
    let p = document.getElementById(id);
    y = p.innerHTML;
    if (special = true){
        p.innerHTML = "wow u boiiiiiiii";
    }
    else{
        p.innerHTML = "yaaaaaaaaaaaaay"
    }
}

function noAttention(id){
    let p = document.getElementById(id);
    p.innerHTML = y;
}