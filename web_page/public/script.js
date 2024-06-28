const url = new URL(window.location.href)
const ip = url.host.split(':')[0]

const ws = new WebSocket(`ws://${ip}:8765`);

ws.onmessage = (event) => {
  console.log(event)
}

setInterval(keep_alive, 1000)

function movement(ele, data) {
  ws.send(JSON.stringify({
    type: 'movement',
    data
  }))
  ele?.classList?.add("button-touched")

  const audio = document.createElement("audio");
  audio.src = "wooden_fish.mp3";
  audio.play();
  navigator.vibrate(20);
}

function movement_touchend(ele) {
  ws.send(JSON.stringify({
    type: 'movement',
    data: 'stop'
  }))
  ele.classList.remove("button-touched")
}

function keep_alive() {
  ws.send(JSON.stringify({
    type: 'ping'
  }))
}