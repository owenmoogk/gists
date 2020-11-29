
function tester(){
    var string = 'i went to the mall mall mall today today fam!'
    var exitLoop = false
    while (exitLoop == false){
        string = string.replace('mall','~~')
        var i = string.search('mall')
        if (i == -1){
            exitLoop = true
        }
    }
    console.log(string)
    
}
