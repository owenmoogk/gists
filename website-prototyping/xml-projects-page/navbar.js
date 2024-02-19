function loadMenuItems() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			menuItems(this);
		}
    };
    xmlhttp.open("GET", "/menu-items.xml", true);
    xmlhttp.send();
}
function menuItems(xml) {
    var titles, links, i, xmlDoc; 
    
    // text that is appended to elements
    var txt = ''
    var modalTxt = ''

    // xml variables
    xmlDoc = xml.responseXML;
    titles = xmlDoc.getElementsByTagName("title");
    links = xmlDoc.getElementsByTagName('link');
    
    // loading text variables
    for (i = 0; i < titles.length; i++) { 
        txt += '<a href = '+links[i].childNodes[0].nodeValue+' class = "navlinks">'+titles[i].childNodes[0].nodeValue+'</a>';
        modalTxt += '<a href = '+links[i].childNodes[0].nodeValue+' class = "navlinks">'+titles[i].childNodes[0].nodeValue+'</a>';
    }
    modalTxt += '<p class="close" onClick="modalClose()">&times</p>'
    // text with modal contains the text with the modal html. this is so we can also import text into the modal
    txt = txt+'<div id="nav-button"><img class="nav-img" src="/img/open-nav-button.png"></div>'
    txt += '<div id="myModal" class="modal"><div class="modal-content"><p class="modal-text">Some text in the Modal..</p></div></div>'

    // side nav
    document.getElementById('nav').innerHTML = txt

    // modal text
    var modal = document.getElementById("myModal");
    var modalText = document.getElementsByClassName("modal-text")[0];
    var button = document.getElementById("nav-button");
    modalText.innerHTML = modalTxt
    button.onclick = function() {
        modalOpen()
    }
    window.onclick = function(event) {
        if (event.target == modal) {
            modalClose()
        }
    }
}
function modalClose(){
    var modal = document.getElementById("myModal");
    var body = document.getElementsByTagName('body')[0];
    modal.style.display = "none";
    body.classList.remove("overlay");
}
function modalOpen(){
    var modal = document.getElementById("myModal");
    var body = document.getElementsByTagName('body')[0];
    modal.style.display = "flex";
    body.classList.add("overlay");
}