function getStateData() {
    _removeAllChildren();

    let state = document.getElementById('selectState').value;
    axios.get(`/api/covid_19/states/?state=${state}`).then(function (response) {
        for (const [key, value] of Object.entries(response.data[0])) {
            let node = document.createElement("li");
            var textnode = document.createTextNode(`${key.toUpperCase()}: ${value}`);
            node.appendChild(textnode);
            document.getElementById("stateStatus").appendChild(node);
        }
    });
}

function _removeAllChildren() {
    let list = document.getElementById('stateStatus');
    let first = list.firstElementChild;
    while (first) {
        list.removeChild(first);
        first = list.firstElementChild;
    }
}