const serverDOM = document.createElement('div');
const serverInput = document.createElement('input');
const serverLabel = document.createElement('label');
const serverSubmit = document.createElement('button');

serverDOM.appendChild(serverLabel);
serverDOM.appendChild(serverInput);
serverDOM.appendChild(serverSubmit);

document.body.appendChild(serverDOM);

serverHost = '';

let ws = null

const chatInput = document.createElement('input');
const chatTrash = document.createElement('div');

serverLabel.append('server host')
serverInput.onchange = (e) => {
    serverHost = event.currentTarget.value;
};
serverSubmit.append('connect');
serverSubmit.onclick = () => {
    try {
        connection();
    } catch (e) {
        alert('error')
    }
};

function connection() {
    ws = new WebSocket(serverHost);

    alert('connected!');

    document.removeChild(serverDOM);
    document.appendChild(chatInput);
    document.appendChild(chatTrash);

    ws.onmessage = (res) => {
        let msg = document.createElement('div');
        msg.appendChild(res.data);
        chatTrash.appendChild(msg);
    }

    chatInput.onkeydown = () => {
        if (e.currentTarget.key === 'Enter') {
            ws.send(e.currentTarget.value);

            e.currentTarget.value = '';
        }
    };
}
