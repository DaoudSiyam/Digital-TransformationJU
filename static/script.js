let form = document.getElementById("eval");
form.addEventListener('submit',getData);

function getData(e) {

    e.preventDefault(); //preventing refresh after submission
    
    let answers = {};

    for (let i = 1; i <= 11; i++) {
        answers[`q${i}`]=e.target[`q${i}`].value;
        if(answers[`q${i}`] == ""){
            answers[`q${i}`] = 0;
        }  
    }
    
    console.log(answers); //logging answers 

    window.alert("Evaluation Submitted, Thank you") //alert

    form.reset(); //clearing the form after submission

}