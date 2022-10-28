listCounter = 1;
document.querySelector("button").addEventListener("click", function(){
    var x = document.createElement("INPUT");
    var y = document.createElement("div");
    x.setAttribute("type", "text");
    x.setAttribute("placeholder", "Type mark");
    x.setAttribute("id", "mark");
    document.querySelector(".grid-container").appendChild(y);
    document.querySelector(".grid-container div:nth-child(" + listCounter + ")").appendChild(x);
    listCounter++;
})

document.getElementById("mark").addEventListener("keypress", function(e){
    if (e.key === 'Enter') {
        var p = document.createElement("p");
        inputtext = document.querySelector(".grid-container div input").value;
        p.setAttribute("value", inputtext);
        document.querySelector(".grid-container div:nth-child(" + listCounter + ")").appendChild("p");
    }
})