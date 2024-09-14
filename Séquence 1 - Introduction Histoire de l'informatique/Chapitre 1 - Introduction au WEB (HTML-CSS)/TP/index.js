function isWeekend() {
  const today = new Date().getDay();
  return today === 0 || today === 6; // 0 is Sunday, 6 is Saturday
}

function isEvenWeek() {
  const now = new Date();
  const firstJanuary = new Date(now.getFullYear(), 0, 1);
  const daysPassed = Math.floor((now - firstJanuary) / (24 * 60 * 60 * 1000));
  const weekNumber = Math.ceil((daysPassed + firstJanuary.getDay() + 1) / 7);

  return weekNumber % 2 === 0;
}

function toggleWeekCourses() {
  let isEven = isEvenWeek();

  if (isWeekend()) {
    isEven = !isEven; // Invert the week if it's weekend
  }

  const weekAElements = document.querySelectorAll(".week-a");
  const weekBElements = document.querySelectorAll(".week-b");

  if (isEven) {
    weekAElements.forEach((el) => (el.style.display = "block"));
    weekBElements.forEach((el) => (el.style.display = "none"));
  } else {
    weekAElements.forEach((el) => (el.style.display = "none"));
    weekBElements.forEach((el) => (el.style.display = "block"));
  }
}

document.addEventListener("DOMContentLoaded", () => {
  toggleWeekCourses();
});
