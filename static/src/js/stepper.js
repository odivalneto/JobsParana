window.addEventListener("DOMContentLoaded", () => {
    const status = document.querySelector("#stepper_id").dataset.stepperStatus;
    const step_span = document.querySelectorAll("#stepper_id span")
    const button = document.querySelector("#remove_application")

    const span_css = () => {
        return ("bg-green-100", "text-green-500")
    }

    const index = () => {
        switch (status) {
            case "Confirmada":
                return "step-1";
            case "Em Revisão":
                return "step-2";
            case "Selecionada":
                return "step-3";
            case "Finalizada":
                return "step-4";
            default:
                return "step-4";
        }
    }

    if (index() !== "step-1") {
        button.disabled = true;
        button.classList.remove("btn-primary");
        button.classList.add("btn-disabled");
    }

    step_span.forEach(step => {

        if (step.id <= index()) {
            step.classList.remove("bg-gray-100", "text-gray-500")
            step.classList.add("bg-green-100", "text-green-500")
        }

        if (step.id === index() && step.id !== "step-4") {
            step.classList.add("animate-bounce")
        }

    })

})