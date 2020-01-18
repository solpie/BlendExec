export function dragElement(elmnt) {
  if (!elmnt) return;
  var dx = 0,
    dy = 0,
    lastX = 0,
    lastY = 0;
  // otherwise, move the DIV from anywhere inside the DIV:
  if (elmnt.onmousedown) {
    return;
  }
  elmnt.onmousedown = dragMouseDown;
  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    lastX = e.clientX;
    lastY = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
    //   timer = window.requestAnimationFrame(elementDrag)
  }
  function move_by_delta(style, prop, delta) {
    let a = Number(style[prop].replace("px", ""));
    style[prop] = a - delta + "px";
  }
  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    dx = lastX - e.clientX;
    dy = lastY - e.clientY;
    lastX = e.clientX;
    lastY = e.clientY;
    move_by_delta(elmnt.style, "top", dy);
    move_by_delta(elmnt.style, "left", dx);
    // console.log(-dx, -dy);
  }

  function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
  }
}
