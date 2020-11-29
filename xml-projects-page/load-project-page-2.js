// the function called when loading page
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

// actual loading process
function projectPage(xml) {

    // xml doxument
    var xmlDoc;
    xmlDoc = xml.responseXML;

    // entire html of page
    txt = "";

    // load header of page
    var pageTitle = xmlDoc.getElementsByTagName('page-title')[0].innerHTML
    var date = xmlDoc.getElementsByTagName('date')[0].innerHTML
    txt += '<div class="title"><p style="line-height: 70px;">'+pageTitle+'</p></div><div class="date"><p class="pdate">'+date+'</p></div>';


    // load main part of the page
    blocks = xmlDoc.getElementsByTagName("block");

    // loading the main part of the page
    for (currBlockNum = 0; currBlockNum < blocks.length; currBlockNum++) {
        var currBlockLength = blocks[currBlockNum].children.length // the number of elements in the current block
        var currBlock = blocks[currBlockNum].children // the elements inside the current block

        // looping thru the elements in the block
        for (var blockElementNum = 0; blockElementNum < currBlockLength; blockElementNum++){
            var elementType = currBlock[blockElementNum].tagName // contains the tag name for the element (eg... title, text, image)
            var elementData = currBlock[blockElementNum].innerHTML // contains the inner data for the element

            // appending text to var 'txt' depending on tag name
            if (elementType == 'title'){
                txt += '<div class="block"><div class="text"><h1>'+elementData+'</h1>'
            }
            else if (elementType == 'text'){
                txt += '<p>'+elementData+'</p></div>'
            }
            else if (elementType == 'image'){
                txt += '<div class="img"><img src="'+elementData+'" class="img"></div>'
            }
            else{
                console.log('unknown tag name') // shouldnt ever happen
            }
        }
        
        txt += '</div>' // close out block div

    }

    // finally append the 'txt' variable to the body[class] of the html page
    document.getElementsByClassName("body")[0].innerHTML = txt;
}