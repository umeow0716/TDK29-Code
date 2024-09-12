document.addEventListener('contextmenu', event => event.preventDefault()); // no 右鍵

const url = new URL(window.location.href)
const ip = url.host.split(':')[0]

let ws = null;

function websocketConnect() {
  let dotElement = document.querySelector("#dot")
  dotElement.classList.remove("status-ready")
  dotElement.classList.remove("status-stopped")
  dotElement.classList.add("status-waiting")
  
  ws = new WebSocket(`ws://${ip}:8765`)

  ws.addEventListener("open", (_event) => {
    dotElement.classList.remove("status-waiting")
    dotElement.classList.remove("status-stopped")
    dotElement.classList.add("status-ready")
  })

  ws.addEventListener("message", (event) => {
    if(event.data === "using joystick!")
      alert("不能同時使用 搖桿 與 網頁 操作！")
  })
  
  ws.addEventListener("close", (_event) => {
    dotElement.classList.remove("status-waiting")
    dotElement.classList.remove("status-ready")
    dotElement.classList.add("status-stopped")
  
    setTimeout(websocketConnect, 1000);
  })
}

addEventListener("DOMContentLoaded", websocketConnect);
setInterval(keep_alive, 10000)

function commandSend(ele, event) {
  if(ele.tagName === "BUTTON") ele?.classList?.add("button-touched")

  const commandType = ele.getAttribute("command-type")
  const commandData = ele.getAttribute("command-data")

  if(!commandType || !commandData) return;

  if(ele.tagName === "BUTTON") {
    try {
      ws.send(JSON.stringify({
        type: commandType,
        data: commandData
      }))
    } catch(err) {
      console.error(err)
    }
    typeEmit(commandType, ele, event);
  } else if(commandType === "ball_door") {
    const realData = ele.checked ? "open" : "close"
    try {
      ws.send(JSON.stringify({
        type: commandType,
        data: realData
      }))
    } catch(err) {
      console.error(err)
    }
  }
}

function typeEmit(commandType, ele, event) {
  if(commandType === "movement") {
    if(!ele.ontouchend) ele.ontouchend = () => { defaultTouchEnd(ele) };
    if(!ele.ontouchcancel) ele.ontouchcancel = () => { defaultTouchEnd(ele) };

    movement(ele, event)
  } else {
    if(ele.tagName === "BUTTON" && !ele.ontouchend) ele.ontouchend = () => { defaultTouchEnd(ele) };
    if(ele.tagName === "BUTTON" && !ele.ontouchcancel) ele.ontouchcancel = () => { defaultTouchEnd(ele) };

    defaultTouchStart(ele, event)
  }
}

function movement(ele, event) {
  const commandData = ele.getAttribute("command-data")

  const audio = document.createElement("audio")
  audio.src = `${commandData}.mp3`
  audio.play()
  plusOne(event)
  window.navigator.vibrate(20)
}

function defaultTouchStart(_ele, event) {
  const audio = document.createElement("audio")
  audio.src = "forward.mp3"
  audio.play()
  plusOne(event)
  window.navigator.vibrate(20)
}

function defaultTouchEnd(ele) {
  const commandType = ele.getAttribute("command-type")

  try {
    ws.send(JSON.stringify({
      type: commandType,
      data: "stop"
    }))
  } catch(err) {
    console.error(err)
  }

  ele.classList.remove("button-touched")
}

function plusOne(event) {
  console.log(event)
  let x = event.targetTouches[0].clientX + 10;
  let y = event.targetTouches[0].clientY - 30;

  let element = document.createElement('span')
  element.innerHTML = '功德 +1'
  element.setAttribute("style", `position: fixed;top: ${y}px;left: ${x}px;`)
  document.body.appendChild(element)
  element.setAttribute("class", "plus-one")

  setTimeout(() => {
    element.remove()
  }, 900)
}

function keep_alive() {
  try{
    ws.send(JSON.stringify({
      type: 'ping'
    }))
  } catch(err) {
    ws = new WebSocket(`ws://${ip}:8765`);
  }
}