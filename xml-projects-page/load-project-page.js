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
    var currBlock, txt, xmlDoc; 
    xmlDoc = xml.responseXML;
    txt = "";
    blocks = xmlDoc.getElementsByTagName("block");
    for (currBlockNum = 0; currBlockNum < blocks.length; currBlockNum++) {
        var currBlockLength = blocks[currBlockNum].children.length
        var currBlock = blocks[currBlockNum]
        var title = currBlock.getElementsByTagName('title')[0].innerHTML
        var text = currBlock.getElementsByTagName('text')[0].innerHTML
        var image
        if (currBlockNum == 3){
            image = currBlock.getElementsByTagName('text')[0].innerHTML
        }
        var linkLocations = []
        var continueLoop = true
        while (continueLoop){
            linkLocations.push(text.search('~~'))
            text = text.replace('~~','')
            console.log(linkLocations)
            if (!text.includes('~~')){
                continueLoop = false
            }
        }

        txt += '<a href = '+links[i].childNodes[0].nodeValue+' class = "navlinks">'+titles[i].childNodes[0].nodeValue+'</a>';
    }
    document.getElementById("main").innerHTML = txt;
}