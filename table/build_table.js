let items = [
    {name: "W3Schools", link: "youtube.com", category: "Coding"},
    {name: "Repl.it", link: "firstinspires.org", category: "Coding"},
    {name: "Github", link: "youtube.com", category: "Coding"},
    {name: "Thingiverse", link: "firstinspires.org", category: "Design"},
    {name: "Minecraft Gamepedia", link: "youtube.com", category: "Games"},
    {name: "Spotify", link: "firstinspires.org", category: "Music"},
    {name: "Slides Template", link: "youtube.com", category: "Presentation"},
    {name: "Bitly", link: "firstinspires.org", category: "Presentation"},
    {name: "Citation Machine", link: "youtube.com", category: "Presentation"},
    {name: "SpaceX Time Machine", link: "firstinspires.org", category: "Hobby"},
]

function addRow(table, data){
    for (let element of data){
        let row = table.insertRow();
        for (key in element){
            let cell = row.insertCell();
            let text = document.createTextNode(element[key]);
            cell.appendChild(text)
        }
    }
}

function getSortedList(sortBy){
    return items.sort((a, b)=>{
      let x = a[sortBy] > b[sortBy]
      if(x)
        return 1;
      else
        return -1;
    })
}

function generateTableHead(table, data) {
    let thead = table.createTHead();
    let row = thead.insertRow();
    for (let key of data){
        let th = document.createElement("th");
        let text = document.createTextNode(key);
        th.appendChild(text);
        row.appendChild(th);
    }
}

function generateTableBody(table, data){
    for (let element of data){
        let row = table.insertRow();
        for (key in element){
            let cell = row.insertCell();
            let text = document.createTextNode(element[key]);
            cell.appendChild(text);
        }
    }
}
let firstTime = 1;

function buttonClick(organizer){
    sortedList = getSortedList(organizer);
    let table = document.querySelector("table.jstable");
    let data = Object.keys(sortedList[0]);
    generateTableHead(table, data);
    generateTableBody(table, sortedList);
}

buttonClick("name");