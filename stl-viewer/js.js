function loadSTL(){

    // loads the stl viewer
    stl_viewer = new StlViewer(document.getElementById("stl_cont"), {models: [ {id:0, filename:"/stlfile.stl"} ] });

    setTimeout(function () {

        // removes the loading text
        var stlDiv = document.getElementById('loading')
        stlDiv.style.display = 'none'

        // rotate to make it normal
        stl_viewer.rotate(0, -1.5, 0, 0);

        // animate with rotating
        // msec is speed
        stl_viewer.animate_model(0, {delta:{rotationz:1.2, msec:1500, loop:true}} );
    }, 1000);
}

// pausing the rotation
function togglePause(){
    if (pause == false){
        stl_viewer.animate_model(0, {delta:{rotationz:0, msec:1500, loop:true}} );
        pause = true
    }
    else{
        stl_viewer.animate_model(0, {delta:{rotationz:1.2, msec:1500, loop:true}} );
        pause = false
    }
}

var pause = false