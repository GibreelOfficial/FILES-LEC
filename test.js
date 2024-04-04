var hour = prompt("Enter hours");
var counter =0;

while (counter<5){

    counter+=1

    if (hour>18){
        greeting ="Good evening"

    }else{
        greeting="good day"
    }
}

console.log (greeting);