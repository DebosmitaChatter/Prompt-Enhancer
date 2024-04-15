function printOutput() {
    var userInput = document.getElementById("userInput").value;
    var outputDiv = document.getElementById("output");
    outputDiv.innerHTML = "<p>You entered: " + userInput + "</p>";
}