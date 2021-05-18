window.onload = function(){
    canvas = document.getElementById('sky')
    ctx = canvas.getContext('2d')

    width = window.innerWidth
    height = window.innerHeight

    canvas.width = width
    canvas.height = height

    maxFlakes = 100;
    let flakes = []

    console.log(width, height)

    for(let i = 0; i < maxFlakes; i++){
        flakes.push(
            {
                x: Math.random() * width,
                y: Math.random() * height,
                r: Math.random() * 5 + 2,
                d: Math.random() + 1
            }
        )
    }

    console.log(flakes)
    
    function drawFlakes(){
        console.log("here")
        ctx.clearRect(0,0,width,height)
        ctx.fillStyle = "white";
        ctx.beginPath()

        for(let i = 0; i < maxFlakes; i++){
            let flake = flakes[i]
            ctx.moveTo(flake.x, flake.y)
            ctx.arc(flake.x, flake.y, 0, Math.PI*2, true)
        }
        ctx.fill()
        moveFlakes()
    }

    angle = 0

    function moveFlakes(){
        angle += 0.01
        for (let i = 0; i < maxFlakes; i++){
            flake = flakes[i]
            
            flake.y = Math.pow(flake.d, 2) + 1
            flake.x = Math.sin(angle) * 2
            
            if (flake.y > height){
                flakes[i] = {
                    x: Math.random() * width,
                    y: 0,
                    r: flake.r,
                    d: flake.d,
                }
            }
        }
    }

    setInterval(drawFlakes,25);
}