let tg = window.Telegram.WebApp; //получаем объект webapp телеграма

tg.expand(); //расширяем на все окно

tg.MainButton.text = "Changed Text"; //изменяем текст кнопки
tg.MainButton.setText("Changed Text1"); //изменяем текст кнопки иначе
tg.MainButton.textColor = "#F55353"; //изменяем цвет текста кнопки
tg.MainButton.color = "#143F6B"; //изменяем цвет бэкграунда кнопки
tg.MainButton.setParams({"color": "#143F6B"}); //так изменяются все параметры

//let btn = document.getElementById("btn"); //получаем кнопку активировать/деактивировать
btn.addEventListener('onclick', function(){ //вешаем событие на нажатие html-кнопки
    alert("Hello");
});


Telegram.WebApp.onEvent('mainButtonClicked', function(){
	tg.sendData("some string that we need to send");
	//при клике на основную кнопку отправляем данные в строковом виде
});