function gotostats(que_id) {
    var radios = document.getElementsByName('group');
    for (var i = 0; i < radios.length; i++)
        if (radios[i].checked)
            document.location.href = "../../stats/" + que_id;
    alert("Выбери ответ");
}