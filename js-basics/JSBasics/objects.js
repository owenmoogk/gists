let person = {
    name: "owen",
    age: 20,
    personality: "tres cool",
};

console.log(person);

//dot notation

x = person.name;
console.log(x);
console.log(person.name);

person.name = "john";
console.log(person.name);

//bracket notation
person["name"] = 'mary' // useful when we do not know what we want to access until runtime, can include a variable