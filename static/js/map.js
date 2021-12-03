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
    document.getElementById("one").value = classToInt(document.getElementById("1"));
    document.getElementById("two").value = classToInt(document.getElementById("2"));
    document.getElementById("three").value = classToInt(document.getElementById("3"));
    document.getElementById("four").value = classToInt(document.getElementById("4"));
    document.getElementById("five").value = classToInt(document.getElementById("5"));
    document.getElementById("six").value = classToInt(document.getElementById("6"));
    document.getElementById("seven").value = classToInt(document.getElementById("7"));
    document.getElementById("eight").value = classToInt(document.getElementById("8"));
    document.getElementById("nine").value = classToInt(document.getElementById("9"));
    document.getElementById("ten").value = classToInt(document.getElementById("0"));
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
});