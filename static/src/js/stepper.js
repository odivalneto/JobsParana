window.addEventListener("DOMContentLoaded", () => {
    const status = document.querySelector("#stepper_id").dataset.stepperStatus;
    const steps = document.querySelectorAll("#stepper_id span")
    const button = document.querySelector("#remove_application")

    const index = () => {
        switch (status) {
            case "Confirmada":
                return "step-1";
            case "Em Revisão":
                return "step-2";
            case "Entrevista":
                return "step-3";
            case "Selecionada":
                return "step-4";
            default:
                return "step-null";
        }
    }

    if (index() === "step-1") {
        button.disabled = false;
        button.classList.remove("btn-disabled");
        button.classList.add("btn-primary");
    }

    steps.forEach(step => {

        if (step.id <= index()) {
            step.classList.remove("stepper__item-default")
            step.classList.add("stepper__item-success");
        }

    })

})