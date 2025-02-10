const btn1 = document.getElementById("btn1");
const btn2 = document.getElementById("btn2");

const p = document.querySelector(".p");
const error = document.querySelector(".error");
p.className += " display_none";

let count1 = 0;
let flag = false;
let res = null;

elements = [
    "name1",
    "name2",
    "name3",
    "name4",
    "name5",
    "name6",
    "name7",
    "name8",
];

function getRadioValue() {
    var radio = document.getElementsByName("name");
    for (i = 0; i < radio.length; i++) {
        if (radio[i].checked) {
            flag = true;
            const div = document.querySelector(".menu");
            res = radio[i].value;
            div.remove();
            count1++;
            p.className = "p";
            error.className += " display_none";
        }
    }
}

btn1.addEventListener("click", () => {
    if (count1 % 2 == 0) {
        const div = document.createElement("div");
        div.className = "menu";
        for (let i = 0; i < elements.length; i++) {
            const div2 = document.createElement("div");
            const label = document.createElement("label");
            const radio = document.createElement("input");

            radio.type = "radio";
            radio.name = "name";
            radio.value = elements[i];
            radio.className = "radio";
            label.innerText = elements[i];
            label.className = "label";
            div2.className = "block";

            div2.appendChild(radio);
            div2.appendChild(label);
            div.appendChild(div2);
        }
        const btn3 = document.createElement("button");
        btn3.className = "btn t3";
        btn3.id = "btn3";
        btn3.innerText = "Выбрать";
        div.append(btn3);
        document.querySelector(".main").appendChild(div);
        btn3.addEventListener("click", getRadioValue);
    } else {
        const div = document.querySelector(".menu");
        div.remove();
    }
    count1++;
    
});

btn2.addEventListener("click", () => {
    if (!flag) {
        error.className = "error";
    } else {
        error.className += " display_none";
        eel.hello(res);
    }
});
