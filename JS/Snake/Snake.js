function $(id) {
   return document.getElementById(id);
}

var canvas = /** @type {HTMLCanvasElement} */ ($("canvas")),
   ctx = canvas.getContext("2d");

var res = 20;

var gameSpace = {
   x: 600 / res - 1,
   y: 500 / res - 1
};

class Snake {
   constructor() {
      this.snakeElements = [];
      this.snakeElements[0] = {
         x: 5,
         y: 5,
         xv: 0,
         yv: 0
      };
      this.food = {
         x: Math.floor(Math.random() * gameSpace.x),
         y: Math.floor(Math.random() * gameSpace.y)
         //  x:1,
         //  y:1
      };
   }

   MoveUp() {
      if (this.snakeElements[0].yv != 1) {
         this.snakeElements[0].xv = 0;
         this.snakeElements[0].yv = -1;
      }
   }
   MoveDown() {
      if (this.snakeElements[0].yv != -1) {
         this.snakeElements[0].xv = 0;
         this.snakeElements[0].yv = 1;
      }
   }
   MoveLeft() {
      if (this.snakeElements[0].xv != -1) {
         this.snakeElements[0].xv = 1;
         this.snakeElements[0].yv = 0;
      }
   }
   MoveRight() {
      if (this.snakeElements[0].xv != 1) {
         this.snakeElements[0].xv = -1;
         this.snakeElements[0].yv = 0;
      }
   }

   // update() {
   //    // if (
   //    //    this.snakeElements[0].x > gameSpace.x ||
   //    //    this.snakeElements[0].y > gameSpace.y ||
   //    //    this.snakeElements[0].y < 0 ||
   //    //    this.snakeElements[0].x < 0
   //    // ) {
   //    //    this.restart();
   //    // }
   //    for (let i = 1; i < this.snakeElements.length; i++) {
   //       this.snakeElements[i] = this.snakeElements[i - 1];
   //    }

   //    this.snakeElements[0].x += this.snakeElements[0].xv;
   //    this.snakeElements[0].y += this.snakeElements[0].yv;

   //    if (this.snakeElements[0].x > gameSpace.x) {
   //       this.snakeElements[0].x = 0;
   //    }
   //    if (this.snakeElements[0].x < 0) {
   //       this.snakeElements[0].x = gameSpace.x;
   //    }
   //    if (this.snakeElements[0].y > gameSpace.y) {
   //       this.snakeElements[0].y = 0;
   //    }
   //    if (this.snakeElements[0].y < 0) {
   //       this.snakeElements[0].y = gameSpace.y;
   //    }

   //    if (
   //       this.snakeElements[0].x == this.food.x &&
   //       this.snakeElements[0].y == this.food.y
   //    ) {
   //       this.snakeElements.push(this.snakeElements[0]);
   //       this.food = {
   //          x: Math.floor(Math.random() * gameSpace.x),
   //          y: Math.floor(Math.random() * gameSpace.y)
   //       };
   //    }
   // }

   update() {
      let head = {
         x: this.snakeElements[0].x + this.snakeElements[0].xv,
         y: this.snakeElements[0].y + this.snakeElements[0].yv,
         xv: this.snakeElements[0].xv,
         yv: this.snakeElements[0].yv
      };

      if (head.x > gameSpace.x) {
         head.x = 0;
      }
      if (head.x < 0) {
         head.x = gameSpace.x;
      }
      if (head.y > gameSpace.y) {
         head.y = 0;
      }
      if (head.y < 0) {
         head.y = gameSpace.y;
      }
      //let flag = false;
      if (
         this.snakeElements[0].x == this.food.x &&
         this.snakeElements[0].y == this.food.y
      ) {
         this.snakeElements.push(this.snakeElements[0]);
         // do {
         //    this.food = {
         //       x: Math.floor(Math.random() * gameSpace.x),
         //       y: Math.floor(Math.random() * gameSpace.y)
         //    };
         //    for (let i = 0; i < this.snakeElements.length; i++) {
         //       const element = this.snakeElements[i];
         //       if(flag !==true && (element.x == this.food.x && element.y == this.food.y))
         //       {
         //          flag=true;
         //       }
         //    }
         // } while (flag)

         this.food = {
            x: Math.floor(Math.random() * gameSpace.x),
            y: Math.floor(Math.random() * gameSpace.y)
         };
      }

      for (let i = 0; i < this.snakeElements.length - 1; i++) {
         const part = this.snakeElements[i];
         if (part.x == head.x && part.y == head.y) {
            this.restart();
         }
      }
      this.snakeElements.unshift(head);
      this.snakeElements.pop();
   }

   draw() {
      ctx.fillStyle = "#ffffff";
      for (let i = this.snakeElements.length; i > 0; i--) {
         if (i - 1 == 0) {
            ctx.fillStyle = "#dddddd";
         }
         ctx.fillRect(
            this.snakeElements[i - 1].x * res,
            this.snakeElements[i - 1].y * res,
            res,
            res
         );
         ctx.fillStyle = "#ffffff";
      }
      ctx.fillStyle = "#DD2244";
      ctx.fillRect(this.food.x * res, this.food.y * res, res, res);
   }

   restart() {
      this.snakeElements = null;
      this.snakeElements = [];
      this.snakeElements[0] = {
         x: 10,
         y: 10,
         xv: 0,
         yv: 0
      };
   }
}

var snake = new Snake();
document.onkeydown = function(event) {
   switch (event.keyCode) {
      case 37:
         snake.MoveRight();
         break;
      case 38:
         snake.MoveUp();
         break;
      case 39:
         snake.MoveLeft();
         break;
      case 40:
         snake.MoveDown();
         break;
   }
};

function draw() {
   ctx.fillStyle = "#222a33";
   ctx.fillRect(0, 0, canvas.width, canvas.height);
   // ctx.fill();
   snake.update();
   snake.draw();

   sleep(100);
   requestAnimationFrame(draw);
}

function sleep(milliseconds) {
   var start = new Date().getTime();
   for (var i = 0; i < 1e7; i++) {
      if (new Date().getTime() - start > milliseconds) {
         break;
      }
   }
}

draw();
