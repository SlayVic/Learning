var $ = function(id) {
  return document.getElementById(id);
};

var money = parseFloat(prompt("Сумма вкладу"));
var yearAdd = parseFloat(prompt("Кожен рік додавати"));
var persent = parseInt(prompt("Проценти"));
var years = parseInt(prompt("Кількість років"));

for (let i = 1; i <= years; i++) {
  money *= persent / 100 + 1;
  money += yearAdd;
  alert("Через " + i + " років у вас буде " + money);
}
