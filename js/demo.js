/*
console.log("welcome to Javascript")
let myvar="JavaScript is amazing"
console.log(myvar);
console.log('C is fun\nPython is cool\nJavascript is amazing');

let a=10;
let b=20;
let add=0;
add = add + (a+b);
console.log(add);
add +=(a+b);
console.log(add);

for (const line of ['C is fun', 'Python is cool', 'Javascript is amazing']) {
  console.log(line);
}
*/

/*#!/usr/bin/node
const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
console.log(typeof (argv))
*/
/*#!/usr/bin/node
console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
*/
/*#!/usr/bin/node
console.log(process.argv[2] + ' is ' + process.argv[3]);*/
/*#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('No argument'); 
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
*/
/*

if (isNaN(parseInt(process.argv[2], 10))) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2], 10));
} 
*/
/*
//stars 
//let numberOfStars = 9;
//output = '';
for(let i = 1;i<= numberOfStars; i++){
    for(let j = 1;j <= i; j++){
        output += '*'; 
    }
    output += '\n';
}
console.log(output);
*/
/*
#!/usr/bin/node
exports.add = function (a, b) {
  a=10, b=20;
  return a + b;
};

const add = function (a, b) {
  console.log(parseInt(a) + parseInt(b))
}
add(process.argv[2] , process.argv[3]);

n=Number.parseInt(process.argv[2]);
if (n>0) {
  for(i=0;i<n;i++){
    console.log("C is fun")
  }
}
  else if(isNaN(n)){
  console.log("Missing number of occurrences")
}

//#!/usr/bin/node
function factorial (a) {
  const number = parseInt(a);
  if (isNaN(number)) {
    return 1;
  }
  if (a === 0) {
    return 1;
  }
  return a * factorial(number - 1);
}
console.log(factorial(process.argv[2]));
*/
//#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const mod = process.argv.slice(2);
  mod.sort((a, b) => b - a);
  console.log(mod[1]);
}
function myFunction(a) {
  console.log(a);
}

const person = {
  name: ["Bob", "Smith"],
  age: 32,
  bio: function () {
    console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
  },
  introduceSelf: function () {
    console.log(`Hi! I'm ${this.name[0]}.`);
  },
};

//#!/usr/bin/node
const myObject = {
  type: 'object', value: 12
};
console.log(myObject);
myObject.incr = function () {
  myObject.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);


    for(var i=0;i<5;i++){
       setTimeout(()=>{
           console.log(i);
       },5000); 
    }

    for(let i=0;i<5;i++){
       setTimeout(()=>{
           console.log(i);
       },5000); 
    }

    function init() {
      var name = "Mozilla"; // name is a local variable created by init
      function displayName() {
        // displayName() is the inner function, that forms the closure
        console.log(name); // use variable declared in the parent function
      }
      displayName();
    }
    init();
    if (Math.random() > 0.5) {
      const x = 1;
    } else {
      const x = 2;
    }
    //console.log(x); // ReferenceError: x is not defined
      
        
