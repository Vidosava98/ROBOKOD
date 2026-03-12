function proveriRodjendan() {
    let input = document.getElementById("birthday").value;
    let rezultat = document.getElementById("rezultat");

    if (input === "") {
        rezultat.innerText = "Molimo unesite datum rođendana.";
        return;
    }

    let danas = new Date();
    let rodjendan = new Date(input);

    let danasDan = danas.getDate();
    let danasMesec = danas.getMonth();

    let rodjDan = rodjendan.getDate();
    let rodjMesec = rodjendan.getMonth();

    if (danasDan === rodjDan && danasMesec === rodjMesec) {
        rezultat.innerText = "Čestitamo! Danas ti je rođendan!";
    } else {
        let sledeciRodjendan = new Date(
            danas.getFullYear(),
            rodjMesec,
            rodjDan
        );

        if (sledeciRodjendan < danas) {
            sledeciRodjendan.setFullYear(danas.getFullYear() + 1);
        }

        let razlika = sledeciRodjendan - danas;
        let brojDana = Math.ceil(razlika / (1000 * 60 * 60 * 24));

        rezultat.innerText = "Tvoj rođendan je za " + brojDana + " dana";
    }
}