"use strict";
// function logAMessage(message){
//   console.log(message)
// }
exports.__esModule = true;
// // var message = 'hello world!'
// // log(message)
// function doSomethingHerePlease(){
//   for (var i = 0; i < 10; i++){
//     logAMessage(i)
//   }
//   console.log('finally', i)
// }
// // doSomething()
// // var count = 5
// // count = 'a'
// var a: number;
// a = 12
// enum Color {Red, Green, Blue};
// var backgroundColor = Color.Red
// var message;
// message = 'abc';
// var endsWithC = message.endsWith('c')
// console.log(endsWithC)
// // now passing a point can be passed
// let drawPoint = (point: Point) => { }
// let getDistance = (pointA: Point, pointB: Point) => {  }
// drawPoint({
//   x: 1,
//   y: 2
// })
// let point = new Point();
// point.x = 1
// point.y = 2
// point.draw()
var point_1 = require("./point");
var point = new point_1.Point(1, 2);
point.draw();
point.x = 10;
console.log(point.x);
