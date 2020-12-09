function loadSTL(){
    stl_viewer = new StlViewer(document.getElementById("stl_cont"), {models: [ {id:0, filename:"/stlfile.stl"} ] });

    setTimeout(function () {
        stl_viewer.rotate(0, -1.5, 0, 0);
        stl_viewer.animate_model(0, {delta:{rotationz:1.2, msec:1500, loop:true}} );
    }, 1000);
}

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