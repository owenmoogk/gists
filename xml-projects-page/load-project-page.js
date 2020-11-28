function loadProjectPage() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			projectPage(this);
		}
    };
    xmlhttp.open("GET", "/pagetest.xml", true);
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
    var currBlock, txt; 
    blocks = xmlDoc.getElementsByTagName("block");
    for (currBlockNum = 0; currBlockNum < blocks.length; currBlockNum++) {
        var currBlockLength = blocks[currBlockNum].children.length
        var currBlock = blocks[currBlockNum]
        var title = currBlock.getElementsByTagName('title')[0].innerHTML
        var text = currBlock.getElementsByTagName('text')[0].innerHTML
        var image;
        if (currBlockNum == 3){
            image = currBlock.getElementsByTagName('image')[0].innerHTML
        }
        txt += '<div class="block"><div class="text"><h1>Overview</h1><p>text</p></div><div class="img"><img src="/projects/2702-2019/img/robot.png" alt="Robot" class="img"></div></div>';
    }

    // load links at the bottom
    links = xmlDoc.getElementsByTagName

    document.getElementsByClassName("body")[0].innerHTML = txt;
}