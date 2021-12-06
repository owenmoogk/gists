var i = 0

var interval = setInterval(() => {
    i += 1
    console.log(i)
    if (i == 10){
        clearInterval(interval)
        interval = undefined
    }
}, 100)



function checkInterval(){
    console.log("interval", interval)
}