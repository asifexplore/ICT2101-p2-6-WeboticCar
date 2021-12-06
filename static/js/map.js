function cycleValue(id){
    console.log(id);
    switch(document.getElementById(id).className){
        case "obstacle":
            nextClass = "road";
            break;
        case "road":
            nextClass = "start";
            break;
        case "start":
            nextClass = "end";
            break;
        case "end":
            nextClass = "obstacle";
            break;
    }
    document.getElementById(id).className = nextClass;
    return;
}

function doSubmit(){
    let grid = ""
    grid += classToInt(document.getElementById("1"));
    grid += classToInt(document.getElementById("2"));
    grid += classToInt(document.getElementById("3"));
    grid += classToInt(document.getElementById("4"));
    grid += classToInt(document.getElementById("5"));
    grid += classToInt(document.getElementById("6"));
    grid += classToInt(document.getElementById("7"));
    grid += classToInt(document.getElementById("8"));
    grid += classToInt(document.getElementById("9"));
    grid += classToInt(document.getElementById("0"));
    document.getElementById("grid").value = grid
}

function classToInt(row){
    let int = ""
    for (var i = 0, col; col = row.cells[i]; i++){
        switch(col.className){
            case "obstacle":
                int = int + "0";
                break;
            case "road":
                int = int + "1";
                break;
            case "start":
                int = int + "2";
                break;
            case "end":
                int = int + "3";
                break;
        }
    }
    return int;
}

$(document).ready(function() {
    $("#createBtn").click(function() {
        doSubmit();
        $("#mapform").submit();
    });
<<<<<<< HEAD
});

=======
});
>>>>>>> Development-Integration-(Marven-and-Kok-Hwee)
