window.addEventListener("DOMContentLoaded", (e) => {
    const status = document.querySelector("#stepper_id").dataset.stepperStatus;
    const step_span = document.querySelectorAll("#stepper_id span")

    const span_ = () => {

    }

    const index = () => {
        switch (status) {
            case "Confirmada":
                return "1";
            case "Em Revisão":
                return "2";
            case "Selecionada":
                return "3";
            case "Finalizada":
                return "4";
            default:
                return "4";
        }
    }

    step_span.forEach(step => {

        if (step.id <= index()) {
            step.classList.remove("bg-gray-100", "text-gray-500")
            step.classList.add("bg-green-200", "text-green-500")
        }

        if (step.id === index() && step.id !== "4") {
            step.classList.add("animate-bounce")
        }

    })

})