function filterReports() {
    let input = document.querySelector('.searchbar').value.toLowerCase();
    let reports = document.querySelectorAll('#report');

    reports.forEach(function(report) {
        let room = report.getAttribute('data-room');
        if (room.includes(input)) {
            report.classList.remove('hidden');
        } else {
            report.classList.add('hidden');
        }
    });
}
