// point is an object, with two numbers, x and y
export class Point {

  // // CONSTRUCTOR SETTING THESE
  // x: number;

  // // since y is private we cannot change it
  // private y: number;

  // // ? makes param optional
  // constructor(x?: number, y?: number) {
  //   this.x = x
  //   this.y = y
  // }

  // if you prefix a var with an access modifier it will automatically set variables within the class.
  constructor(private _x?: number, private _y?: number) {

  }

  // putting the sigature of the function
  draw() {
    console.log(this._x, this._y)
  }

  // instead of getX
  // getter
  get x() {
    return this._x
  }

  // setter
  set x(value){
    if (value < 0)
    // uwu syntax
      throw new Error("value cannot be less than 0")
    
    this._x = value
  }
}
