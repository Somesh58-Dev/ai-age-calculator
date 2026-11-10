const $ = (id) => document.getElementById(id);

$("dob").max = new Date().toISOString().split("T")[0];

// Dark mode (remembered in the browser)
if (localStorage.getItem("theme") === "dark") document.body.classList.add("dark");
$("theme").addEventListener("click", () => {
  document.body.classList.toggle("dark");
  localStorage.setItem("theme", document.body.classList.contains("dark") ? "dark" : "light");
});

$("calc").addEventListener("click", async () => {
  $("error").textContent = "";
  const dob = $("dob").value;
  if (!dob) { $("error").textContent = "Please choose your date of birth."; return; }

  try {
    const res = await fetch("/api/age", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ dob }),
    });
    const data = await res.json();
    if (!res.ok) { $("error").textContent = data.error; $("result").hidden = true; return; }
    show(data);
  } catch (e) {
    $("error").textContent = "Server not reachable. Is app.py running?";
  }
});

function show(d) {
  $("years").textContent = d.age.years;
  $("months").textContent = d.age.months;
  $("days").textContent = d.age.days;
  $("born").textContent = d.born_on;
  $("total").textContent = d.age.total_days.toLocaleString();
  $("next").textContent = d.next_birthday.days_left;
  $("nextday").textContent = d.next_birthday.weekday;
  $("zodiac").textContent = d.zodiac;
  $("gen").textContent = d.generation;
  $("remaining").textContent = d.ml.remaining_years + " years";
  $("progress").textContent = d.ml.life_progress_percent + "% of estimated life lived";
  $("result").hidden = false;
  $("fill").style.width = "0";
  requestAnimationFrame(() => { $("fill").style.width = d.ml.life_progress_percent + "%"; });
}
