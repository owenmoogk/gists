// for (statement 1; statement 2; statement 3){ code }

//statement 1 is run once before the code is run [ex. var i = 0]
// statement 2 defines the range ed [i < 5]
//statement 3 is executed everytime after the block has been run [i++]

for (var i = 1; i < 11; i++){
    console.log(i);
}

//statement 1 is optional, not needed if the variable is already defined.

var person = [fname = 'owen', lname = 'moogk', age = 43, urmom = 'hi', 'yeet', 43];
console.log(person);

var text = '';
for (x in person){
    text += x;
    console.log('x is '+x);
    console.log('text is '+text);
}

console.log(text)

console.log(person);

console.log('fname is '+person[fname])