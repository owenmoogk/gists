"use strict";
exports.__esModule = true;
exports.Point = void 0;
// point is an object, with two numbers, x and y
var Point = /** @class */ (function () {
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
    function Point(_x, _y) {
        this._x = _x;
        this._y = _y;
    }
    // putting the sigature of the function
    Point.prototype.draw = function () {
        console.log(this._x, this._y);
    };
    Object.defineProperty(Point.prototype, "x", {
        // instead of getX
        // getter
        get: function () {
            return this._x;
        },
        // setter
        set: function (value) {
            if (value < 0)
                // uwu syntax
                throw new Error("value cannot be less than 0");
            this._x = value;
        },
        enumerable: false,
        configurable: true
    });
    return Point;
}());
exports.Point = Point;
