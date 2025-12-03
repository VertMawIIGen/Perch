// figure out how to make calculate the dailyBells and show the current class.
// Before that, I think we should figure out changed bells

function printEverything(dailyBells, studentTimetable, roomVariations, teacherVariations, bellData) {
    console.log(dailyBells);
    console.log(studentTimetable);
    console.log(roomVariations);
    console.log(teacherVariations);
    console.log(bellData)
}

function calculateTime(dailyBells, roomVariations, teacherVariations, bellData) {
    const now = new Date();
    const classDate = bellData.date;

    let len = dailyBells.length;
    let i = 0
    var foundNext = false
    while (i < len || foundNext === false) {
        var targetDate = new Date(``)
        timeRemaining = now - i++
    }
}

printEverything(dailyBells, studentTimetable, roomVariations, teacherVariations, bellData)

