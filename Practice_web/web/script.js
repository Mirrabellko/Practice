
function check() {
    let answer1 = document.getElementById("answer1")
    let answer2 = document.getElementById("answer2")
    let answer3 = document.getElementById("answer3")

    let result1 = eel.send_message(answer1)()
    let result2 = eel.send_message(answer2)()
    let result3 = eel.send_message(answer3)()

    document.getElementById("res1").innerHTML = result1;
    document.getElementById("res2").innerHTML = result2;
    document.getElementById("res3").innerHTML = result3;

    document.getElementById("answer1") = ''
    document.getElementById("answer2") = ''
    document.getElementById("answer3") = ''
}

$('check').click(function(){
    check();
})
