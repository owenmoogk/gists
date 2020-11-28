function loadProjectPage(xmlPage) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			projectPage(this);
		}
    };
    xmlhttp.open("GET", xmlPage, true);
    xmlhttp.send();
}
function projectPage(xml) {

    var xmlDoc;
    xmlDoc = xml.responseXML; // xml doxument

    txt = ""; // entire html of page

    // load header of page
    var pageTitle = xmlDoc.getElementsByTagName('page-title')[0].innerHTML
    var date = xmlDoc.getElementsByTagName('date')[0].innerHTML
    txt += '<div class="title"><p style="line-height: 70px;">'+pageTitle+'</p></div><div class="date"><p class="pdate">'+date+'</p></div>';


    // load main part of the page
    blocks = xmlDoc.getElementsByTagName("block");
    for (currBlockNum = 0; currBlockNum < blocks.length; currBlockNum++) {
        var currBlockLength = blocks[currBlockNum].children.length
        var currBlock = blocks[currBlockNum]
        var title = currBlock.getElementsByTagName('title')[0].innerHTML
        var text = currBlock.getElementsByTagName('text')[0].innerHTML
        var image;
        txt += '<div class="block"><div class="text"><h1>'+title+'</h1><p>'+text+'</p></div>';
        if (currBlockLength == 3){
            image = currBlock.getElementsByTagName('image')[0].innerHTML
            txt += '<div class="img"><img src="'+image+'" class="img"></div>'
        }
        txt += '</div>'
    }

    // load links at the bottom
    links = xmlDoc.getElementsByTagName('link')
    txt += '<div class="block"><div class="text"><h1>Resources</h1><p><ul>'
    for (currLinkNum = 0; currLinkNum < links.length; currLinkNum++) {
        var currLink = links[currLinkNum]
        console.log(currLink)
        var linkText = currLink.getElementsByTagName('link-text')[0].innerHTML
        var src = currLink.getElementsByTagName('src')[0].innerHTML
        txt += '<li><a href="'+src+'" class="blinks" target="_blank">'+linkText+'</a></li>';
    }
    txt += '</ul></p></div></div>'

    document.getElementsByClassName("body")[0].innerHTML = txt;
}