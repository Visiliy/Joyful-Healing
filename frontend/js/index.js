const btn1 = document.getElementById("btn1"); // получаем кнопку по id
const btn2 = document.getElementById("btn2"); // получаем другую кнопку по id

const p = document.querySelector(".p"); // получаем текст по названию классса из main.css
const error = document.querySelector(".error"); // получаем текст по названию классса из main.css
p.className += " display_none"; // добавляем к елементу класс со стилями из main.css

let count1 = 0; // инициализируем счётчик для подсчёта количества нажатий.
let flag = false; // значение: можно ли запускать процедуру
let res = null; // сюда записываем значение выбранной процедуры

elements = [ // список с названиями процедур
    "name1",
    "name2",
    "name3",
    "name4",
    "name5",
    "name6",
    "name7",
    "name8",
];

function getRadioValue() { // функция для получения значения при выборе процедуры
    var radio = document.getElementsByName("name");// получаем круглые кнопки по названию имени
    for (i = 0; i < radio.length; i++) { // проходимся по ним циклом
        if (radio[i].checked) { // если кнопка выбрана
            flag = true; // можно запускать процедуру
            const div = document.querySelector(".menu"); // получаем форму с круглыми кнопками по названию класса из main.css
            res = radio[i].value; // записываем название процедуры
            div.remove(); // закрываем форму
            count1++;
            p.className = "p"; // тексту меняем класс из main.css
            error.className += " display_none"; // скрываем текст с ошибкой
        }
    }
}

btn1.addEventListener("click", () => { // функция, которая срабатывает при нажатии на кнопку "Выбрать процедуру"
    if (count1 % 2 == 0) {
        const div = document.createElement("div"); // создаём форму для круглых кнопок
        div.className = "menu"; // подключаем класс из main.css
        for (let i = 0; i < elements.length; i++) { // циклом идём по списку процедур
            const div2 = document.createElement("div"); // создаём блок
            const label = document.createElement("label"); // создаём текст
            const radio = document.createElement("input"); // создаём круглую кнопку

            radio.type = "radio"; // кнопке даём тип
            radio.name = "name"; // кнопке даём имя группы
            radio.value = elements[i]; // кнопке присваиваем значение
            radio.className = "radio"; // кнопке даём класс из main.css
            label.innerText = elements[i]; // наполняем элемент текстом
            label.className = "label"; // даём класс из main.css
            div2.className = "block"; // даём класс из main.css

            div2.appendChild(radio); // в блок помещаем круглую кнопку
            div2.appendChild(label); // в блок помещаем текст
            div.appendChild(div2); // в форму помещаем блок
        }
        const btn3 = document.createElement("button"); // создаём кнопку
        btn3.className = "btn t3"; // даём ей класс из main.css
        btn3.id = "btn3"; // даём ей id
        btn3.innerText = "Выбрать"; // устанавливаем ей текст
        div.append(btn3); // в форму добавляем кнопку
        document.querySelector(".main").appendChild(div); // форму добавляем на страницу
        btn3.addEventListener("click", getRadioValue); // при нажатии на кнопку вызываем функцию getRadioValue
    } else {
        const div = document.querySelector(".menu"); // получаем форму по классу
        div.remove(); // удаляем форму
    }
    count1++;
    
});

btn2.addEventListener("click", () => { // функция, которая срабатывает при нажатии на кнопку "Приступить"
    if (!flag) { // знак ! эквивалентен not в python
        error.className = "error"; // елементу устанавливаем класс
    } else {
        error.className += " display_none"; // елементу добавляем класс
        eel.hello(res); // вызываем функцию hello в python
    }
});
