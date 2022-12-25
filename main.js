document.querySelector('.send').onclick = send;
document.querySelector('.clear').onclick = clear;



function clear() {
    document.querySelector('.input').value = "";
}

document.addEventListener('keydown', function(event) {
    if (event.code == 'Enter') {
        send()
    }
});



function send() {
    let list = document.querySelector('.input').value;
    let list_cut = []
    var summ = 0
    var answer = 0
    var temp = 0 

    for (var n in list) {
        list_cut.push(Number(list[n]))
    }
    summ = list_cut.reduce((partialSum, a) => partialSum + a, 0);
    answer = summ / list_cut.length
    answer = answer.toFixed(2)

    temp = list_cut.length
    var summ1 = summ
    while (Math.round(summ1 / temp) <=4.5 ) {
        summ1 += 5
        temp += 1
        var upFiveRatingFive = temp - list_cut.length
    }

    temp = list_cut.length
    var summ2 = summ
    while (Math.round(summ2 / temp) <=3.5 ) {
        summ2 += 5
        temp += 1
        var upFourRatingFive = temp - list_cut.length
    }

    temp = list_cut.length
    var summ3 = summ
    while (Math.round(summ3 / temp) <=3.5 ) {
        summ3 += 4
        temp += 1
        var upFourRatingFour = temp - list_cut.length
    }




    if (isNaN(answer)) {
        answer = 0
    }
    if (upFiveRatingFive == undefined) {
        upFiveRatingFive = 0
    }
    if (upFourRatingFive == undefined) {
        upFourRatingFive = 0
    }
    if (upFourRatingFour == undefined) {
        upFourRatingFour = 0
    }



    localStorage.setItem('val', list);

    document.querySelector('.upFive').innerHTML = 'До пятёрки: ' + upFiveRatingFive + ' \"5\"'
    document.querySelector('.aver').innerHTML = 'Ср. балл: ' + answer
    document.querySelector('.upFour').innerHTML = 'До четвёрки: ' + upFourRatingFive + ' \"5\" или ' + upFourRatingFour +' \"4\"'

}