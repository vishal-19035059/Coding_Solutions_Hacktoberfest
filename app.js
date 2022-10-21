function list_task() {
  $.ajax({
    url: "https://devza.com/tests/tasks/list",
    headers: { AuthToken: "UrM4YHgb1FcqEf1tuKwmAMMX5MxFZ12a" },
  }).done((p) => {
    tasks = p["tasks"];
    employ_table = $("#employee");
  });
}

