from View import DoctorUsView
from Controller import DoctorUsController
from Model import DoctorUsModel

if __name__ == "__main__":
    # Create Interface with user
    view = DoctorUsView.DoctorUsView()

    # Create Model
    model = DoctorUsModel.DoctorUsModel()

    # Create Controller
    drUs = DoctorUsController.DoctorUsController(view, model)

    # Start program
    drUs.run()

