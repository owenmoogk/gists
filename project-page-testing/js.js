function loadXML() {
    // make new http request, its a js thing
    var xmlhttp = new XMLHttpRequest();

    // GET, file location and name, and some other propertie i forget
    xmlhttp.open("GET", "/xmlfile.xml", true);
    xmlhttp.send();

    // when there is a change in the request's state, itll check all is green and run the table loading function
    xmlhttp.onreadystatechange = function () {
        // all green
        if (this.readyState == 4 && this.status == 200) {
            loadEntries(this);
        }
        // cant find the xml
        if (this.status == 404) {
            console.log("couldn't find the xml file")
        }
    }
}

// function that loops through the data and spins it into the html. required the "this" from the request made above
function loadEntries(xml) {
    var file = xml.responseXML;
    var loaded = "";
    var pulledData = file.getElementsByTagName("entry");

    // loops through all <resource>'s and addes them to the great table varible
    for (i = 0; i < pulledData.length; i++) {
        var image = "";
        var title = "";
        var type = "";
        var date = "";
        var description = "";

        // put the things into their varibles
        image = "<div class=\"image_div\"><img class=\"image\" src=\"" + pulledData[i].getElementsByTagName("image")[0].childNodes[0].nodeValue + "\"></div>";
        title = "<p class=\"title\">" + pulledData[i].getElementsByTagName("title")[0].childNodes[0].nodeValue + "</p>";
        type = "<div class=\"type_date\"><p class=\"TypeClass\">" + pulledData[i].getElementsByTagName("type")[0].childNodes[0].nodeValue.toUpperCase() + "</p><p>&nbsp · &nbsp</p>";
        date = "<p class=\"date\">" + pulledData[i].getElementsByTagName("date")[0].childNodes[0].nodeValue+"</p></div>";
        description = "<p class=\"description\">" + pulledData[i].getElementsByTagName("description")[0].childNodes[0].nodeValue + "</p>";

        // put it all together
        loaded += "<div class='entry'>" + image + "<div class=\"text_div\">" + title + type + date + description + "</div></div>";
    }
    document.getElementById("projectsGoHere").innerHTML += loaded;

    // putting the click detections here as some may need the loaded xml first

    // for when buttons are clicked
    var buttons = document.getElementsByClassName("btn");

    for (var i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener("click", function () {
            var current = document.getElementsByClassName("active");
            current[0].className = current[0].className.replace(" active", "");
            this.className += " active";

            // based on what class is in the span, itll filter by that type by calling the  filterProjects function
            if (this.classList.contains("sort_all")) {
                filterProjects("all");
            }
            else if (this.classList.contains("sort_cad")) {
                filterProjects("cad");
            }
            else if (this.classList.contains("sort_coding")) {
                filterProjects("coding");
            }
            else if (this.classList.contains("sort_mechanical")) {
                filterProjects("mechanical");
            }
            else if (this.classList.contains("sort_webdev")) {
                filterProjects("webdev");
            }

        });
    }

}

// function that filters by the type of entry
function filterProjects(filterBy) {

    // pulls all entries
    var entries = document.getElementsByClassName("entry");

    // loops thru them all
    for (var i = 0; i < entries.length; i++) {

        // if we're filtering by "all" we need to show all
        if (filterBy == "all") {
            entries[i].style.display = "";
        }

        // if we're filtering anything else, then ...
        else {
            // gets the p element holding the type
            var type = entries[i].getElementsByClassName("TypeClass")[0];

            // if it matchs what we are filtering by it stays
            if (type.innerHTML.toString().toLowerCase() == filterBy) {
                entries[i].style.display = "";
            }
            // else it will just be gone
            else {
                entries[i].style.display = "none";
            }
        }
    }
}

function sortProjects() {

    // pulls the value we're soring by
    var sortValue = document.getElementById("mySort").value;

    var sortBy; // old what we're soring by
    var order; // hold sort order

    // based on the value of sort, we can make an order and sortby
    if (sortValue == "alpha-desc") {
        sortBy = "alpha";
        order = "asc";
    }
    else if (sortValue == "alpha-asc") {
        sortBy = "alpha";
        order = "desc";
    }
    else if (sortValue == 'date'){
        location.reload();
    }

    // some varibles we'll need
    var entries = document.getElementsByClassName("entry"); // pulls all entries
    var switching = true; // shows that we're still running through the entries
    var shouldSwitch; // this var will hold whether or not a switch between two rows needs to be made
    var entryNum; // will store what entry number we're at
    var currentEntry; // will hold the current entry plain "text"
    var nextEntry; // will hold the next entry plain "text"

    while (switching) {
        // set it that there is no switching done, this may be changed later
        switching = false;
        console.log('loopoing')
        // run through all the entries, except last, as at that point we wont be able to compare it to the next
        for (entryNum = 0; entryNum < entries.length - 1; entryNum++) {
            // state that there is need for switching at the moment
            shouldSwitch  = false;
            
            // if date
            if (sortBy == "alpha" || sortBy == 'alpha') {
                currentEntry = entries[entryNum].getElementsByClassName("title")[0].innerHTML;
                nextEntry = entries[entryNum + 1].getElementsByClassName("title")[0].innerHTML;
            }

            // if we're doing ascending order
            if (order == "asc") {
                if (currentEntry > nextEntry) {
                    // if this is true, means we need to to place the current one above the next one
                    shouldSwitch = true;
                    break;
                }
            }
            if (order == "desc") {
                if (currentEntry < nextEntry) {
                    // if this is true, means we need to to place the current one above the next one
                    shouldSwitch = true;
                    break;
                }
            }
        }

        if (shouldSwitch) {
            entries[entryNum].parentNode.insertBefore(entries[entryNum + 1], entries[entryNum]);
            switching = true;
        }
    }
}