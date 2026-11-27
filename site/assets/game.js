(function () {
  "use strict";

  var KEY = "veilig_deadline";
  var DURATION_MS = 75 * 60 * 1000;
  var timerEl = document.getElementById("timer");
  var startBtn = document.getElementById("start-clock");
  var resetBtn = document.getElementById("reset-clock");

  function fmt(totalSeconds) {
    var m = Math.floor(totalSeconds / 60);
    var s = totalSeconds % 60;
    return m + ":" + (s < 10 ? "0" : "") + s;
  }

  function tick() {
    var deadline = Number(localStorage.getItem(KEY) || 0);
    if (!deadline) {
      timerEl.textContent = "75:00";
      timerEl.classList.remove("danger");
      return;
    }
    var remaining = Math.max(0, Math.floor((deadline - Date.now()) / 1000));
    if (remaining === 0) {
      timerEl.textContent = "KRAAI WINT";
    } else {
      timerEl.textContent = fmt(remaining);
    }
    timerEl.classList.toggle("danger", remaining < 5 * 60);
  }

  function start() {
    localStorage.setItem(KEY, String(Date.now() + DURATION_MS));
    if (startBtn) startBtn.hidden = true;
    if (resetBtn) resetBtn.hidden = false;
    tick();
  }

  function reset() {
    localStorage.removeItem(KEY);
    if (startBtn) startBtn.hidden = false;
    if (resetBtn) resetBtn.hidden = true;
    tick();
  }

  if (startBtn) startBtn.addEventListener("click", start);
  if (resetBtn) resetBtn.addEventListener("click", reset);

  if (localStorage.getItem(KEY)) {
    if (startBtn) startBtn.hidden = true;
    if (resetBtn) resetBtn.hidden = false;
  }

  setInterval(tick, 1000);
  tick();

  var slots = Array.prototype.slice.call(document.querySelectorAll(".slots input"));
  if (!slots.length) return;

  var taunts = [
    "Nee. Probeer het nog eens, incidentteam.",
    "Dichtbij? Nee. Ik kan jullie gedachten lezen, en er staat niets in.",
    "Zes letters. Jullie zaten de hele avond mee in de les.",
    "Tik maar. Ik heb alle tijd. Hmm, nee: 75 minuten.",
    "Jullie hebben het hele spel gezien. Het antwoord sprak jullie toe."
  ];

  function check() {
    var word = slots.map(function (s) { return s.value.toUpperCase(); }).join("");
    if (word.length < slots.length) return;
    if (word === "VEILIG") {
      document.getElementById("victory").style.display = "block";
      document.getElementById("console-msg").textContent = "";
      slots.forEach(function (s) { s.classList.remove("err"); });
      localStorage.removeItem(KEY);
    } else {
      document.getElementById("console-msg").textContent =
        taunts[Math.floor(Math.random() * taunts.length)];
      slots.forEach(function (s) { s.classList.add("err"); });
      setTimeout(function () {
        slots.forEach(function (s) { s.classList.remove("err"); s.value = ""; });
        slots[0].focus();
      }, 900);
    }
  }

  slots.forEach(function (slot, i) {
    slot.addEventListener("input", function () {
      slot.value = slot.value.toUpperCase().replace(/[^A-Z]/g, "");
      if (slot.value && i < slots.length - 1) slots[i + 1].focus();
      check();
    });
    slot.addEventListener("keydown", function (e) {
      if (e.key === "Backspace" && !slot.value && i > 0) slots[i - 1].focus();
    });
  });
})();
